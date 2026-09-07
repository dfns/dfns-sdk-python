"""Tests for the regular DfnsClient (read + user-action flows)."""

import httpx
import pytest
import respx

from dfns_sdk import DfnsClient
from dfns_sdk.types import DfnsClientConfig, DfnsError

BASE_URL = "https://api.test.dfns"


def make_client() -> DfnsClient:
    return DfnsClient(DfnsClientConfig(auth_token="test-token", base_url=BASE_URL))


@respx.mock
def test_list_wallets_parses_response() -> None:
    respx.get(f"{BASE_URL}/wallets").mock(
        return_value=httpx.Response(200, json={"items": [{"id": "wa-1"}], "nextPageToken": None})
    )

    client = make_client()
    result = client.wallets.list_wallets()

    assert result["items"][0]["id"] == "wa-1"


@respx.mock
def test_auth_header_is_sent() -> None:
    route = respx.get(f"{BASE_URL}/wallets").mock(return_value=httpx.Response(200, json={"items": []}))

    make_client().wallets.list_wallets()

    assert route.calls.last.request.headers["authorization"] == "Bearer test-token"


@respx.mock
def test_error_response_surfaces_message_and_details() -> None:
    # Dfns wraps errors as {"error": {"message", "details", ...}}.
    respx.get(f"{BASE_URL}/wallets").mock(
        return_value=httpx.Response(
            400,
            json={
                "error": {
                    "id": "trace-1",
                    "status": 400,
                    "message": "duplicate derivation path",
                    "details": {"keyId": "key-1", "derivationPath": "m/44/60/0/0/0"},
                }
            },
        )
    )

    with pytest.raises(DfnsError) as exc:
        make_client().wallets.list_wallets()

    assert exc.value.message == "duplicate derivation path"
    assert exc.value.status_code == 400
    assert exc.value.details == {"keyId": "key-1", "derivationPath": "m/44/60/0/0/0"}


@respx.mock
def test_error_response_without_envelope_falls_back() -> None:
    respx.get(f"{BASE_URL}/wallets").mock(return_value=httpx.Response(500, json={"message": "boom"}))

    with pytest.raises(DfnsError) as exc:
        make_client().wallets.list_wallets()

    assert exc.value.message == "boom"
    assert exc.value.status_code == 500


@respx.mock
def test_error_response_non_dict_body_does_not_crash() -> None:
    # A non-dict 4xx body must degrade to a clean DfnsError, not raise AttributeError.
    respx.get(f"{BASE_URL}/wallets").mock(return_value=httpx.Response(400, json=["unexpected"]))

    with pytest.raises(DfnsError) as exc:
        make_client().wallets.list_wallets()

    assert exc.value.status_code == 400
    assert exc.value.message == "Unknown error"
