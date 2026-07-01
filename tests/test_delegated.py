"""Tests for the delegated (externally-signed) client: init/complete flow."""

import httpx
import respx

from dfns_sdk import DfnsDelegatedClient
from dfns_sdk.types import DfnsDelegatedClientConfig

BASE_URL = "https://api.test.dfns"


def make_delegated() -> DfnsDelegatedClient:
    return DfnsDelegatedClient(DfnsDelegatedClientConfig(auth_token="service-account-token", base_url=BASE_URL))


@respx.mock
def test_create_wallet_init_returns_challenge() -> None:
    init = respx.post(f"{BASE_URL}/auth/action/init").mock(
        return_value=httpx.Response(200, json={"challengeIdentifier": "ch-1", "challenge": "Y2g"})
    )

    challenge = make_delegated().wallets.create_wallet_init(body={"network": "EthereumSepolia"})

    assert challenge["challengeIdentifier"] == "ch-1"
    sent = init.calls.last.request
    assert b'"userActionHttpPath":"/wallets"' in sent.content
    assert b'"userActionHttpMethod":"POST"' in sent.content


@respx.mock
def test_create_wallet_complete_uses_user_action_token() -> None:
    respx.post(f"{BASE_URL}/auth/action").mock(return_value=httpx.Response(200, json={"userAction": "ua-token"}))
    wallet_route = respx.post(f"{BASE_URL}/wallets").mock(
        return_value=httpx.Response(200, json={"id": "wa-123", "network": "EthereumSepolia"})
    )

    wallet = make_delegated().wallets.create_wallet_complete(
        body={"network": "EthereumSepolia"},
        signed_challenge={"challengeIdentifier": "ch-1", "firstFactor": {"kind": "Key"}},
    )

    assert wallet["id"] == "wa-123"
    # The actual request must carry the pre-obtained user action token.
    assert wallet_route.calls.last.request.headers["x-dfns-useraction"] == "ua-token"
