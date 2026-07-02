"""Tests for multipart/form-data file-upload endpoints."""

import hashlib

import httpx
import respx

from dfns_sdk import DfnsClient
from dfns_sdk.types import DfnsClientConfig

BASE_URL = "https://api.test.dfns"


class _FakeSigner:
    """Duck-typed Signer for the user-action flow these upload endpoints require."""

    def sign(self, challenge):  # type: ignore[no-untyped-def]
        return {"kind": "Key", "credentialAssertion": {"credId": "cr-1", "clientData": "x", "signature": "y"}}


@respx.mock
def test_submit_onchain_sign_output_sends_multipart() -> None:
    respx.post(f"{BASE_URL}/auth/action/init").mock(
        return_value=httpx.Response(200, json={"challengeIdentifier": "ch", "challenge": "Y2g"})
    )
    respx.post(f"{BASE_URL}/auth/action").mock(return_value=httpx.Response(200, json={"userAction": "ua"}))
    route = respx.post(f"{BASE_URL}/key-stores/ks-1/onchain-sign/output").mock(
        return_value=httpx.Response(200, json={})
    )

    client = DfnsClient(DfnsClientConfig(auth_token="t", base_url=BASE_URL, signer=_FakeSigner()))
    file_bytes = b"signed-output-bytes"
    client.signers.submit_onchain_sign_output("ks-1", body={"foo": "bar"}, file=file_bytes)

    req = route.calls.last.request
    # Multipart content type, a `data` part with the file checksum, and a `file` part.
    assert req.headers["content-type"].startswith("multipart/form-data")
    body = req.content
    assert hashlib.sha256(file_bytes).hexdigest().encode() in body
    assert b'name="data"' in body
    assert b'name="file"' in body
    assert file_bytes in body
