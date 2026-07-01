"""Tests for the KeySigner (user-action challenge signing with a private key)."""

import json

from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import ec, ed25519

from dfns_sdk.auth import KeySigner, base64url_decode

CHALLENGE = {
    "challenge": "dGVzdC1jaGFsbGVuZ2U",
    "challengeIdentifier": "ch-1",
    "supportedCredentialKinds": [],
    "allowCredentials": {},
    "rp": {},
    "externalAuthenticationUrl": "",
}


def _pem(private_key) -> str:
    return private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.PKCS8,
        encryption_algorithm=serialization.NoEncryption(),
    ).decode()


def test_ed25519_assertion_structure_and_signature() -> None:
    key = ed25519.Ed25519PrivateKey.generate()
    signer = KeySigner(credential_id="cr-ed25519", private_key=_pem(key))

    assertion = signer.sign(CHALLENGE)

    assert assertion["kind"] == "Key"
    ca = assertion["credentialAssertion"]
    assert ca["credId"] == "cr-ed25519"

    # clientData decodes to the WebAuthn-style JSON binding the challenge.
    client_data = json.loads(base64url_decode(ca["clientData"]))
    assert client_data["type"] == "key.get"
    assert client_data["challenge"] == CHALLENGE["challenge"]
    assert client_data["crossOrigin"] is False

    # Ed25519 signs the raw clientData; the signature verifies against the public key.
    key.public_key().verify(base64url_decode(ca["signature"]), base64url_decode(ca["clientData"]))


def test_ecdsa_p256_assertion_signature_verifies() -> None:
    key = ec.generate_private_key(ec.SECP256R1())
    signer = KeySigner(credential_id="cr-ec", private_key=_pem(key))

    ca = signer.sign(CHALLENGE)["credentialAssertion"]
    client_data_bytes = base64url_decode(ca["clientData"])

    # ECDSA signs SHA-256 of the clientData; verify with the matching public key.
    key.public_key().verify(
        base64url_decode(ca["signature"]),
        client_data_bytes,
        ec.ECDSA(hashes.SHA256()),
    )


def test_ed25519_signing_is_deterministic() -> None:
    key = ed25519.Ed25519PrivateKey.generate()
    signer = KeySigner(credential_id="cr-ed25519", private_key=_pem(key))

    first = signer.sign(CHALLENGE)["credentialAssertion"]["signature"]
    second = signer.sign(CHALLENGE)["credentialAssertion"]["signature"]
    assert first == second


def test_app_origin_flows_into_client_data() -> None:
    key = ed25519.Ed25519PrivateKey.generate()
    signer = KeySigner(credential_id="cr-ed25519", private_key=_pem(key), app_origin="https://custom.example")

    ca = signer.sign(CHALLENGE)["credentialAssertion"]
    client_data = json.loads(base64url_decode(ca["clientData"]))
    assert client_data["origin"] == "https://custom.example"
