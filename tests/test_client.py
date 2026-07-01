"""Tests for the regular DfnsClient (read + user-action flows)."""

import httpx
import respx

from dfns_sdk import DfnsClient
from dfns_sdk.types import DfnsClientConfig

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
