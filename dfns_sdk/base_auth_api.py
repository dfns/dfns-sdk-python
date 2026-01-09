"""Base authentication API for delegated client operations."""

import json
from typing import Any, TypedDict, Optional

from ._internal import HttpClient


class AllowCredential(TypedDict):
    """Allowed credential for signing."""

    type: str
    id: str
    transports: list[str]


class SupportedCredentialKind(TypedDict):
    """Supported credential kind."""

    kind: str
    factor: str
    requiresSecondFactor: bool


class UserActionChallengeResponse(TypedDict):
    """Response from creating a user action challenge."""

    challengeIdentifier: str
    challenge: str
    allowCredentials: list[AllowCredential]
    supportedCredentialKinds: list[SupportedCredentialKind]
    userVerification: str
    rp: dict[str, str]
    externalAuthenticationUrl: str


class SignUserActionChallengeRequest(TypedDict, total=False):
    """Request to complete a user action challenge."""

    challengeIdentifier: str
    firstFactor: dict[str, Any]
    secondFactor: dict[str, Any]


class BaseAuthApi:
    """
    Helper class for delegated client user action signing.

    This class provides static methods for the two-phase user action signing flow:
    1. create_user_action_challenge() - Creates a challenge for external signing
    2. sign_user_action_challenge() - Completes signing with the signed challenge

    Example:
        >>> # Step 1: Create challenge
        >>> challenge = BaseAuthApi.create_user_action_challenge(
        ...     http_client,
        ...     user_action_http_method="POST",
        ...     user_action_http_path="/wallets",
        ...     user_action_payload='{"network":"EthereumSepolia"}',
        ... )
        >>>
        >>> # Step 2: Sign externally (your signing system)
        >>> signed = your_external_signer.sign(challenge)
        >>>
        >>> # Step 3: Complete with signed challenge
        >>> result = BaseAuthApi.sign_user_action_challenge(
        ...     http_client,
        ...     signed_challenge={
        ...         "challengeIdentifier": challenge["challengeIdentifier"],
        ...         "firstFactor": signed,
        ...     },
        ... )
    """

    @staticmethod
    def create_user_action_challenge(
        http_client: HttpClient,
        user_action_http_method: str,
        user_action_http_path: str,
        user_action_payload: str,
        user_action_server_kind: str = "Api",
    ) -> UserActionChallengeResponse:
        """
        Create a user action challenge for signing.

        Args:
            http_client: The HTTP client to use.
            user_action_http_method: The HTTP method of the action (GET, POST, etc.).
            user_action_http_path: The path of the action endpoint.
            user_action_payload: The JSON-serialized request body.
            user_action_server_kind: The server kind (default: "Api").

        Returns:
            The challenge response containing the challenge to sign.
        """
        return http_client.request(
            method="POST",
            path="/auth/action/init",
            body={
                "userActionHttpMethod": user_action_http_method,
                "userActionHttpPath": user_action_http_path,
                "userActionPayload": user_action_payload,
                "userActionServerKind": user_action_server_kind,
            },
            requires_signature=False,
        )

    @staticmethod
    def sign_user_action_challenge(
        http_client: HttpClient,
        signed_challenge: SignUserActionChallengeRequest,
    ) -> dict[str, Any]:
        """
        Complete user action signing with a signed challenge.

        Args:
            http_client: The HTTP client to use.
            signed_challenge: The signed challenge containing challengeIdentifier
                and firstFactor (and optional secondFactor).

        Returns:
            Dictionary containing the userAction token.
        """
        return http_client.request(
            method="POST",
            path="/auth/action",
            body=signed_challenge,
            requires_signature=False,
        )
