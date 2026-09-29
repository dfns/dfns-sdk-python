"""Tests for the operationId-rename compat layer.

The SDK generators emit, for renamed endpoints, a canonical method plus a
``@deprecated`` forwarding alias under the old name. These tests assert the
alias hits the *same* endpoint (method + path + body) as the canonical method,
so callers on the old name keep working after the rename.
"""

import warnings

import httpx
import pytest
import respx

from dfns_sdk import DfnsClient
from dfns_sdk.types import DfnsClientConfig

BASE_URL = "https://api.test.dfns"


class _FakeSigner:
    """Duck-typed Signer for the user-action flow write endpoints require."""

    def sign(self, challenge):  # type: ignore[no-untyped-def]
        return {"kind": "Key", "credentialAssertion": {"credId": "cr-1", "clientData": "x", "signature": "y"}}


def _make_client() -> DfnsClient:
    return DfnsClient(DfnsClientConfig(auth_token="t", base_url=BASE_URL, signer=_FakeSigner()))


def _mock_user_action_flow() -> None:
    respx.post(f"{BASE_URL}/auth/action/init").mock(
        return_value=httpx.Response(200, json={"challengeIdentifier": "ch", "challenge": "Y2g"})
    )
    respx.post(f"{BASE_URL}/auth/action").mock(return_value=httpx.Response(200, json={"userAction": "ua"}))


@respx.mock
def test_create_exchange_deposit_alias_forwards_to_canonical() -> None:
    """create_exchange_deposit (deprecated) must issue the same request as create_deposit."""
    _mock_user_action_flow()
    route = respx.post(f"{BASE_URL}/exchanges/ex-1/accounts/acc-1/deposits").mock(
        return_value=httpx.Response(
            200, json={"id": "dp-1", "exchangeId": "ex-1", "accountId": "acc-1", "kind": "Deposit", "walletId": "wa-1"}
        )
    )

    client = _make_client()
    body = {"asset": "USDC", "amount": "100", "kind": "Native"}

    # Canonical method.
    client.exchanges.create_deposit("ex-1", "acc-1", body=body)

    # Deprecated alias, same arguments (suppress the emitted DeprecationWarning here;
    # it is asserted separately below).
    with warnings.catch_warnings():
        warnings.simplefilter("ignore", DeprecationWarning)
        client.exchanges.create_exchange_deposit("ex-1", "acc-1", body=body)

    assert len(route.calls) == 2, "expected both canonical and alias to hit the deposit endpoint"

    canonical_req = route.calls[0].request
    alias_req = route.calls[1].request

    assert alias_req.method == canonical_req.method == "POST"
    assert alias_req.url.path == canonical_req.url.path == "/exchanges/ex-1/accounts/acc-1/deposits"
    assert alias_req.content == canonical_req.content


@respx.mock
def test_create_exchange_deposit_alias_emits_deprecation_warning() -> None:
    """The @deprecated marker should surface as a runtime DeprecationWarning."""
    _mock_user_action_flow()
    respx.post(f"{BASE_URL}/exchanges/ex-1/accounts/acc-1/deposits").mock(
        return_value=httpx.Response(
            200, json={"id": "dp-1", "exchangeId": "ex-1", "accountId": "acc-1", "kind": "Deposit", "walletId": "wa-1"}
        )
    )

    client = _make_client()

    with pytest.warns(DeprecationWarning, match="create_deposit"):
        client.exchanges.create_exchange_deposit("ex-1", "acc-1", body={"asset": "USDC", "amount": "100"})
