"""Authentication utilities for the Dfns SDK."""

import base64
import hashlib
import json
from typing import Any, Optional, Protocol, TypedDict

from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import ec, ed25519, padding


class UserActionChallenge(TypedDict):
    """Challenge returned by the server for user action signing."""

    challenge: str
    challengeIdentifier: str
    supportedCredentialKinds: list[dict[str, Any]]
    allowCredentials: dict[str, Any]
    rp: dict[str, str]
    externalAuthenticationUrl: str


class CredentialAssertion(TypedDict):
    """Credential assertion for signing."""

    kind: str
    credentialAssertion: dict[str, str]


class Signer(Protocol):
    """Protocol for signing user action challenges."""

    def sign(self, challenge: UserActionChallenge) -> CredentialAssertion:
        """
        Sign a user action challenge.

        Args:
            challenge: The challenge from the server.

        Returns:
            The credential assertion to submit to the server.
        """
        ...


def base64url_encode(data: bytes) -> str:
    """Encode bytes to base64url string without padding."""
    return base64.urlsafe_b64encode(data).rstrip(b"=").decode("ascii")


def base64url_decode(data: str) -> bytes:
    """Decode base64url string to bytes."""
    padding = 4 - len(data) % 4
    if padding != 4:
        data += "=" * padding
    return base64.urlsafe_b64decode(data)


class KeySigner:
    """
    Signer implementation using a private key credential.

    Supports Ed25519, ECDSA (secp256k1, P-256), and RSA keys.

    Example:
        >>> from dfns_sdk.auth import KeySigner
        >>> signer = KeySigner(
        ...     credential_id="cr-xxx-xxx",
        ...     private_key=open("private_key.pem").read(),
        ...     app_origin="https://app.dfns.io",
        ... )
    """

    def __init__(
        self,
        credential_id: str,
        private_key: str,
        app_origin: str = "https://app.dfns.io",
    ):
        """
        Initialize the key signer.

        Args:
            credential_id: The credential ID (cr-xxx-xxx format).
            private_key: The private key in PEM format.
            app_origin: The application origin for the client data.
        """
        self.credential_id = credential_id
        self.app_origin = app_origin
        self._private_key = serialization.load_pem_private_key(
            private_key.encode() if isinstance(private_key, str) else private_key,
            password=None,
        )

    def sign(self, challenge: UserActionChallenge) -> CredentialAssertion:
        """
        Sign a user action challenge.

        Args:
            challenge: The challenge from the server.

        Returns:
            The credential assertion to submit to the server.
        """
        client_data = {
            "type": "key.get",
            "challenge": challenge["challenge"],
            "origin": self.app_origin,
            "crossOrigin": False,
        }
        client_data_json = json.dumps(client_data, separators=(",", ":"))
        client_data_bytes = client_data_json.encode("utf-8")

        signature = self._sign_bytes(client_data_bytes)

        return {
            "kind": "Key",
            "credentialAssertion": {
                "credId": self.credential_id,
                "clientData": base64url_encode(client_data_bytes),
                "signature": base64url_encode(signature),
            },
        }

    def _sign_bytes(self, data: bytes) -> bytes:
        """Sign bytes with the private key."""
        if isinstance(self._private_key, ed25519.Ed25519PrivateKey):
            return self._private_key.sign(data)
        elif isinstance(self._private_key, ec.EllipticCurvePrivateKey):
            return self._private_key.sign(data, ec.ECDSA(hashes.SHA256()))
        else:
            # RSA
            return self._private_key.sign(
                data,
                padding.PKCS1v15(),
                hashes.SHA256(),
            )
