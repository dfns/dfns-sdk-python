"""Delegated client for the keys domain."""

import json
from typing import Any, Literal, Optional, TypedDict, Union

from ..._internal import HttpClient
from ...base_auth_api import (
    BaseAuthApi,
    SignUserActionChallengeRequest,
    UserActionChallengeResponse,
)
from . import types as T


class DelegatedKeysClient:
    """
    Delegated client for keys operations.

    This client separates user action signing into _init() and _complete() method pairs,
    allowing external systems to handle the signing process.
    """

    def __init__(self, http_client: HttpClient):
        self._http = http_client

    def list_keys(self, query: Optional[T.ListKeysQuery] = None) -> T.ListKeysResponse:
        """
        List Keys.

        Retrieve all keys registered for your organization.

        Args:
        query: Query parameters.

        Returns:
            T.ListKeysResponse: The API response.
        """
        return self._http.request(
            method="GET",
            path="/keys",
            path_params={},
            query_params=query,
            body=None,
            requires_signature=False,
        )

    def create_key_init(self, body: T.CreateKeyRequest) -> UserActionChallengeResponse:
        """
        Initialize Create Key.

        Creates a user action challenge for external signing.

        Args:
        body: Request body.

        Returns:
            UserActionChallengeResponse: The challenge to sign externally.
        """
        path = "/keys"
        payload = json.dumps(body, separators=(",", ":")) if body else ""

        return BaseAuthApi.create_user_action_challenge(
            self._http,
            user_action_http_method="POST",
            user_action_http_path=path,
            user_action_payload=payload,
        )

    def create_key_complete(self, body: T.CreateKeyRequest, signed_challenge: SignUserActionChallengeRequest) -> T.CreateKeyResponse:
        """
        Complete Create Key.

        Submits the signed challenge and makes the API request.

        Args:
        body: Request body.
        signed_challenge: The signed challenge from external signing.

        Returns:
            T.CreateKeyResponse: The API response.
        """
        user_action_result = BaseAuthApi.sign_user_action_challenge(
            self._http, signed_challenge
        )
        user_action_token = user_action_result["userAction"]

        return self._http.request_with_user_action(
            method="POST",
            path="/keys",
            path_params={},
            query_params=None,
            body=body,
            user_action=user_action_token,
        )

    def delegate_key_init(self, key_id: str, body: T.DelegateKeyRequest) -> UserActionChallengeResponse:
        """
        Initialize Delegate Key.

        Creates a user action challenge for external signing.

        Args:
        key_id: Path parameter.
        body: Request body.

        Returns:
            UserActionChallengeResponse: The challenge to sign externally.
        """
        path = "/keys/{keyId}/delegate"
        path = path.replace("{keyId}", str(key_id))
        payload = json.dumps(body, separators=(",", ":")) if body else ""

        return BaseAuthApi.create_user_action_challenge(
            self._http,
            user_action_http_method="POST",
            user_action_http_path=path,
            user_action_payload=payload,
        )

    def delegate_key_complete(self, key_id: str, body: T.DelegateKeyRequest, signed_challenge: SignUserActionChallengeRequest) -> T.DelegateKeyResponse:
        """
        Complete Delegate Key.

        Submits the signed challenge and makes the API request.

        Args:
        key_id: Path parameter.
        body: Request body.
        signed_challenge: The signed challenge from external signing.

        Returns:
            T.DelegateKeyResponse: The API response.
        """
        user_action_result = BaseAuthApi.sign_user_action_challenge(
            self._http, signed_challenge
        )
        user_action_token = user_action_result["userAction"]

        return self._http.request_with_user_action(
            method="POST",
            path="/keys/{keyId}/delegate",
            path_params={"keyId": key_id},
            query_params=None,
            body=body,
            user_action=user_action_token,
        )

    def get_key(self, key_id: str) -> T.GetKeyResponse:
        """
        Get Key.

        Retrieves a key information by its ID.

        Args:
        key_id: Path parameter.

        Returns:
            T.GetKeyResponse: The API response.
        """
        return self._http.request(
            method="GET",
            path="/keys/{keyId}",
            path_params={"keyId": key_id},
            query_params=None,
            body=None,
            requires_signature=False,
        )

    def update_key_init(self, key_id: str, body: T.UpdateKeyRequest) -> UserActionChallengeResponse:
        """
        Initialize Update Key.

        Creates a user action challenge for external signing.

        Args:
        key_id: Path parameter.
        body: Request body.

        Returns:
            UserActionChallengeResponse: The challenge to sign externally.
        """
        path = "/keys/{keyId}"
        path = path.replace("{keyId}", str(key_id))
        payload = json.dumps(body, separators=(",", ":")) if body else ""

        return BaseAuthApi.create_user_action_challenge(
            self._http,
            user_action_http_method="PUT",
            user_action_http_path=path,
            user_action_payload=payload,
        )

    def update_key_complete(self, key_id: str, body: T.UpdateKeyRequest, signed_challenge: SignUserActionChallengeRequest) -> T.UpdateKeyResponse:
        """
        Complete Update Key.

        Submits the signed challenge and makes the API request.

        Args:
        key_id: Path parameter.
        body: Request body.
        signed_challenge: The signed challenge from external signing.

        Returns:
            T.UpdateKeyResponse: The API response.
        """
        user_action_result = BaseAuthApi.sign_user_action_challenge(
            self._http, signed_challenge
        )
        user_action_token = user_action_result["userAction"]

        return self._http.request_with_user_action(
            method="PUT",
            path="/keys/{keyId}",
            path_params={"keyId": key_id},
            query_params=None,
            body=body,
            user_action=user_action_token,
        )

    def delete_key_init(self, key_id: str) -> UserActionChallengeResponse:
        """
        Initialize Delete Key.

        Creates a user action challenge for external signing.

        Args:
        key_id: Path parameter.

        Returns:
            UserActionChallengeResponse: The challenge to sign externally.
        """
        path = "/keys/{keyId}"
        path = path.replace("{keyId}", str(key_id))
        payload = ""

        return BaseAuthApi.create_user_action_challenge(
            self._http,
            user_action_http_method="DELETE",
            user_action_http_path=path,
            user_action_payload=payload,
        )

    def delete_key_complete(self, key_id: str, signed_challenge: SignUserActionChallengeRequest) -> T.DeleteKeyResponse:
        """
        Complete Delete Key.

        Submits the signed challenge and makes the API request.

        Args:
        key_id: Path parameter.
        signed_challenge: The signed challenge from external signing.

        Returns:
            T.DeleteKeyResponse: The API response.
        """
        user_action_result = BaseAuthApi.sign_user_action_challenge(
            self._http, signed_challenge
        )
        user_action_token = user_action_result["userAction"]

        return self._http.request_with_user_action(
            method="DELETE",
            path="/keys/{keyId}",
            path_params={"keyId": key_id},
            query_params=None,
            body=None,
            user_action=user_action_token,
        )

    def derive_key_init(self, key_id: str, body: T.DeriveKeyRequest) -> UserActionChallengeResponse:
        """
        Initialize Derive Key.

        Creates a user action challenge for external signing.

        Args:
        key_id: Path parameter.
        body: Request body.

        Returns:
            UserActionChallengeResponse: The challenge to sign externally.
        """
        path = "/keys/{keyId}/derive"
        path = path.replace("{keyId}", str(key_id))
        payload = json.dumps(body, separators=(",", ":")) if body else ""

        return BaseAuthApi.create_user_action_challenge(
            self._http,
            user_action_http_method="POST",
            user_action_http_path=path,
            user_action_payload=payload,
        )

    def derive_key_complete(self, key_id: str, body: T.DeriveKeyRequest, signed_challenge: SignUserActionChallengeRequest) -> T.DeriveKeyResponse:
        """
        Complete Derive Key.

        Submits the signed challenge and makes the API request.

        Args:
        key_id: Path parameter.
        body: Request body.
        signed_challenge: The signed challenge from external signing.

        Returns:
            T.DeriveKeyResponse: The API response.
        """
        user_action_result = BaseAuthApi.sign_user_action_challenge(
            self._http, signed_challenge
        )
        user_action_token = user_action_result["userAction"]

        return self._http.request_with_user_action(
            method="POST",
            path="/keys/{keyId}/derive",
            path_params={"keyId": key_id},
            query_params=None,
            body=body,
            user_action=user_action_token,
        )

    def export_key_init(self, key_id: str, body: T.ExportKeyRequest) -> UserActionChallengeResponse:
        """
        Initialize Export Key.

        Creates a user action challenge for external signing.

        Args:
        key_id: Path parameter.
        body: Request body.

        Returns:
            UserActionChallengeResponse: The challenge to sign externally.
        """
        path = "/keys/{keyId}/export"
        path = path.replace("{keyId}", str(key_id))
        payload = json.dumps(body, separators=(",", ":")) if body else ""

        return BaseAuthApi.create_user_action_challenge(
            self._http,
            user_action_http_method="POST",
            user_action_http_path=path,
            user_action_payload=payload,
        )

    def export_key_complete(self, key_id: str, body: T.ExportKeyRequest, signed_challenge: SignUserActionChallengeRequest) -> T.ExportKeyResponse:
        """
        Complete Export Key.

        Submits the signed challenge and makes the API request.

        Args:
        key_id: Path parameter.
        body: Request body.
        signed_challenge: The signed challenge from external signing.

        Returns:
            T.ExportKeyResponse: The API response.
        """
        user_action_result = BaseAuthApi.sign_user_action_challenge(
            self._http, signed_challenge
        )
        user_action_token = user_action_result["userAction"]

        return self._http.request_with_user_action(
            method="POST",
            path="/keys/{keyId}/export",
            path_params={"keyId": key_id},
            query_params=None,
            body=body,
            user_action=user_action_token,
        )

    def list_signatures(self, key_id: str, query: Optional[T.ListSignaturesQuery] = None) -> T.ListSignaturesResponse:
        """
        List Signatures.

        List all signature requests for a key.

        Args:
        key_id: Path parameter.
        query: Query parameters.

        Returns:
            T.ListSignaturesResponse: The API response.
        """
        return self._http.request(
            method="GET",
            path="/keys/{keyId}/signatures",
            path_params={"keyId": key_id},
            query_params=query,
            body=None,
            requires_signature=False,
        )

    def generate_signature_init(self, key_id: str, body: dict[str, Any]) -> UserActionChallengeResponse:
        """
        Initialize Generate Signature.

        Creates a user action challenge for external signing.

        Args:
        key_id: Path parameter.
        body: Request body.

        Returns:
            UserActionChallengeResponse: The challenge to sign externally.
        """
        path = "/keys/{keyId}/signatures"
        path = path.replace("{keyId}", str(key_id))
        payload = json.dumps(body, separators=(",", ":")) if body else ""

        return BaseAuthApi.create_user_action_challenge(
            self._http,
            user_action_http_method="POST",
            user_action_http_path=path,
            user_action_payload=payload,
        )

    def generate_signature_complete(self, key_id: str, body: dict[str, Any], signed_challenge: SignUserActionChallengeRequest) -> T.GenerateSignatureResponse:
        """
        Complete Generate Signature.

        Submits the signed challenge and makes the API request.

        Args:
        key_id: Path parameter.
        body: Request body.
        signed_challenge: The signed challenge from external signing.

        Returns:
            T.GenerateSignatureResponse: The API response.
        """
        user_action_result = BaseAuthApi.sign_user_action_challenge(
            self._http, signed_challenge
        )
        user_action_token = user_action_result["userAction"]

        return self._http.request_with_user_action(
            method="POST",
            path="/keys/{keyId}/signatures",
            path_params={"keyId": key_id},
            query_params=None,
            body=body,
            user_action=user_action_token,
        )

    def get_signature(self, key_id: str, signature_id: str) -> T.GetSignatureResponse:
        """
        Get Signature.

        Retrieve a signature request details.

        Args:
        key_id: Path parameter.
        signature_id: Path parameter.

        Returns:
            T.GetSignatureResponse: The API response.
        """
        return self._http.request(
            method="GET",
            path="/keys/{keyId}/signatures/{signatureId}",
            path_params={"keyId": key_id, "signatureId": signature_id},
            query_params=None,
            body=None,
            requires_signature=False,
        )

    def import_key_init(self, body: T.ImportKeyRequest) -> UserActionChallengeResponse:
        """
        Initialize Import Key.

        Creates a user action challenge for external signing.

        Args:
        body: Request body.

        Returns:
            UserActionChallengeResponse: The challenge to sign externally.
        """
        path = "/keys/import"
        payload = json.dumps(body, separators=(",", ":")) if body else ""

        return BaseAuthApi.create_user_action_challenge(
            self._http,
            user_action_http_method="POST",
            user_action_http_path=path,
            user_action_payload=payload,
        )

    def import_key_complete(self, body: T.ImportKeyRequest, signed_challenge: SignUserActionChallengeRequest) -> T.ImportKeyResponse:
        """
        Complete Import Key.

        Submits the signed challenge and makes the API request.

        Args:
        body: Request body.
        signed_challenge: The signed challenge from external signing.

        Returns:
            T.ImportKeyResponse: The API response.
        """
        user_action_result = BaseAuthApi.sign_user_action_challenge(
            self._http, signed_challenge
        )
        user_action_token = user_action_result["userAction"]

        return self._http.request_with_user_action(
            method="POST",
            path="/keys/import",
            path_params={},
            query_params=None,
            body=body,
            user_action=user_action_token,
        )
