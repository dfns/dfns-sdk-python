"""Delegated client for the signers domain."""

import json
from typing import Any, Literal, Optional, TypedDict, Union

from ..._internal import HttpClient
from ...base_auth_api import (
    BaseAuthApi,
    SignUserActionChallengeRequest,
    UserActionChallengeResponse,
)
from . import types as T


class DelegatedSignersClient:
    """
    Delegated client for signers operations.

    This client separates user action signing into _init() and _complete() method pairs,
    allowing external systems to handle the signing process.
    """

    def __init__(self, http_client: HttpClient):
        self._http = http_client

    def create_clone_input_init(self, store_id: str, body: T.CreateCloneInputRequest) -> UserActionChallengeResponse:
        """
        Initialize Create Clone Input.

        Creates a user action challenge for external signing.

        Args:
        store_id: Path parameter.
        body: Request body.

        Returns:
            UserActionChallengeResponse: The challenge to sign externally.
        """
        path = "/key-stores/{storeId}/clone/input"
        path = path.replace("{storeId}", str(store_id))
        payload = json.dumps(body, separators=(",", ":")) if body else ""

        return BaseAuthApi.create_user_action_challenge(
            self._http,
            user_action_http_method="POST",
            user_action_http_path=path,
            user_action_payload=payload,
        )

    def create_clone_input_complete(self, store_id: str, body: T.CreateCloneInputRequest, signed_challenge: SignUserActionChallengeRequest) -> None:
        """
        Complete Create Clone Input.

        Submits the signed challenge and makes the API request.

        Args:
        store_id: Path parameter.
        body: Request body.
        signed_challenge: The signed challenge from external signing.
        """
        user_action_result = BaseAuthApi.sign_user_action_challenge(
            self._http, signed_challenge
        )
        user_action_token = user_action_result["userAction"]

        return self._http.request_with_user_action(
            method="POST",
            path="/key-stores/{storeId}/clone/input",
            path_params={"storeId": store_id},
            query_params=None,
            body=body,
            user_action=user_action_token,
        )

    def create_genesis_input_init(self, store_id: str, body: T.CreateGenesisInputRequest) -> UserActionChallengeResponse:
        """
        Initialize Create Genesis Input.

        Creates a user action challenge for external signing.

        Args:
        store_id: Path parameter.
        body: Request body.

        Returns:
            UserActionChallengeResponse: The challenge to sign externally.
        """
        path = "/key-stores/{storeId}/genesis/input"
        path = path.replace("{storeId}", str(store_id))
        payload = json.dumps(body, separators=(",", ":")) if body else ""

        return BaseAuthApi.create_user_action_challenge(
            self._http,
            user_action_http_method="POST",
            user_action_http_path=path,
            user_action_payload=payload,
        )

    def create_genesis_input_complete(self, store_id: str, body: T.CreateGenesisInputRequest, signed_challenge: SignUserActionChallengeRequest) -> None:
        """
        Complete Create Genesis Input.

        Submits the signed challenge and makes the API request.

        Args:
        store_id: Path parameter.
        body: Request body.
        signed_challenge: The signed challenge from external signing.
        """
        user_action_result = BaseAuthApi.sign_user_action_challenge(
            self._http, signed_challenge
        )
        user_action_token = user_action_result["userAction"]

        return self._http.request_with_user_action(
            method="POST",
            path="/key-stores/{storeId}/genesis/input",
            path_params={"storeId": store_id},
            query_params=None,
            body=body,
            user_action=user_action_token,
        )

    def create_proof_of_control_input_init(self, store_id: str, body: T.CreateProofOfControlInputRequest) -> UserActionChallengeResponse:
        """
        Initialize Create Proof Of Control Input.

        Creates a user action challenge for external signing.

        Args:
        store_id: Path parameter.
        body: Request body.

        Returns:
            UserActionChallengeResponse: The challenge to sign externally.
        """
        path = "/key-stores/{storeId}/proof-of-control/input"
        path = path.replace("{storeId}", str(store_id))
        payload = json.dumps(body, separators=(",", ":")) if body else ""

        return BaseAuthApi.create_user_action_challenge(
            self._http,
            user_action_http_method="POST",
            user_action_http_path=path,
            user_action_payload=payload,
        )

    def create_proof_of_control_input_complete(self, store_id: str, body: T.CreateProofOfControlInputRequest, signed_challenge: SignUserActionChallengeRequest) -> T.CreateProofOfControlInputResponse:
        """
        Complete Create Proof Of Control Input.

        Submits the signed challenge and makes the API request.

        Args:
        store_id: Path parameter.
        body: Request body.
        signed_challenge: The signed challenge from external signing.

        Returns:
            T.CreateProofOfControlInputResponse: The API response.
        """
        user_action_result = BaseAuthApi.sign_user_action_challenge(
            self._http, signed_challenge
        )
        user_action_token = user_action_result["userAction"]

        return self._http.request_with_user_action(
            method="POST",
            path="/key-stores/{storeId}/proof-of-control/input",
            path_params={"storeId": store_id},
            query_params=None,
            body=body,
            user_action=user_action_token,
        )

    def list_key_stores(self) -> T.ListKeyStoresResponse:
        """
        List Key Stores.

        Returns:
            T.ListKeyStoresResponse: The API response.
        """
        return self._http.request(
            method="GET",
            path="/key-stores",
            path_params={},
            query_params=None,
            body=None,
            requires_signature=False,
        )

    def list_signers(self) -> T.ListSignersResponse:
        """
        List Signers.

        Returns:
            T.ListSignersResponse: The API response.
        """
        return self._http.request(
            method="GET",
            path="/signers",
            path_params={},
            query_params=None,
            body=None,
            requires_signature=False,
        )

    def submit_clone_output_init(self, store_id: str, body: T.SubmitCloneOutputRequest) -> UserActionChallengeResponse:
        """
        Initialize Submit Clone Output.

        Creates a user action challenge for external signing.

        Args:
        store_id: Path parameter.
        body: Request body.

        Returns:
            UserActionChallengeResponse: The challenge to sign externally.
        """
        path = "/key-stores/{storeId}/clone/output"
        path = path.replace("{storeId}", str(store_id))
        payload = json.dumps(body, separators=(",", ":")) if body else ""

        return BaseAuthApi.create_user_action_challenge(
            self._http,
            user_action_http_method="POST",
            user_action_http_path=path,
            user_action_payload=payload,
        )

    def submit_clone_output_complete(self, store_id: str, body: T.SubmitCloneOutputRequest, signed_challenge: SignUserActionChallengeRequest) -> T.SubmitCloneOutputResponse:
        """
        Complete Submit Clone Output.

        Submits the signed challenge and makes the API request.

        Args:
        store_id: Path parameter.
        body: Request body.
        signed_challenge: The signed challenge from external signing.

        Returns:
            T.SubmitCloneOutputResponse: The API response.
        """
        user_action_result = BaseAuthApi.sign_user_action_challenge(
            self._http, signed_challenge
        )
        user_action_token = user_action_result["userAction"]

        return self._http.request_with_user_action(
            method="POST",
            path="/key-stores/{storeId}/clone/output",
            path_params={"storeId": store_id},
            query_params=None,
            body=body,
            user_action=user_action_token,
        )

    def submit_genesis_output_init(self, store_id: str, body: T.SubmitGenesisOutputRequest) -> UserActionChallengeResponse:
        """
        Initialize Submit Genesis Output.

        Creates a user action challenge for external signing.

        Args:
        store_id: Path parameter.
        body: Request body.

        Returns:
            UserActionChallengeResponse: The challenge to sign externally.
        """
        path = "/key-stores/{storeId}/genesis/output"
        path = path.replace("{storeId}", str(store_id))
        payload = json.dumps(body, separators=(",", ":")) if body else ""

        return BaseAuthApi.create_user_action_challenge(
            self._http,
            user_action_http_method="POST",
            user_action_http_path=path,
            user_action_payload=payload,
        )

    def submit_genesis_output_complete(self, store_id: str, body: T.SubmitGenesisOutputRequest, signed_challenge: SignUserActionChallengeRequest) -> T.SubmitGenesisOutputResponse:
        """
        Complete Submit Genesis Output.

        Submits the signed challenge and makes the API request.

        Args:
        store_id: Path parameter.
        body: Request body.
        signed_challenge: The signed challenge from external signing.

        Returns:
            T.SubmitGenesisOutputResponse: The API response.
        """
        user_action_result = BaseAuthApi.sign_user_action_challenge(
            self._http, signed_challenge
        )
        user_action_token = user_action_result["userAction"]

        return self._http.request_with_user_action(
            method="POST",
            path="/key-stores/{storeId}/genesis/output",
            path_params={"storeId": store_id},
            query_params=None,
            body=body,
            user_action=user_action_token,
        )

    def submit_proof_of_control_output_init(self, store_id: str, body: T.SubmitProofOfControlOutputRequest) -> UserActionChallengeResponse:
        """
        Initialize Submit Proof Of Control Output.

        Creates a user action challenge for external signing.

        Args:
        store_id: Path parameter.
        body: Request body.

        Returns:
            UserActionChallengeResponse: The challenge to sign externally.
        """
        path = "/key-stores/{storeId}/proof-of-control/output"
        path = path.replace("{storeId}", str(store_id))
        payload = json.dumps(body, separators=(",", ":")) if body else ""

        return BaseAuthApi.create_user_action_challenge(
            self._http,
            user_action_http_method="POST",
            user_action_http_path=path,
            user_action_payload=payload,
        )

    def submit_proof_of_control_output_complete(self, store_id: str, body: T.SubmitProofOfControlOutputRequest, signed_challenge: SignUserActionChallengeRequest) -> T.SubmitProofOfControlOutputResponse:
        """
        Complete Submit Proof Of Control Output.

        Submits the signed challenge and makes the API request.

        Args:
        store_id: Path parameter.
        body: Request body.
        signed_challenge: The signed challenge from external signing.

        Returns:
            T.SubmitProofOfControlOutputResponse: The API response.
        """
        user_action_result = BaseAuthApi.sign_user_action_challenge(
            self._http, signed_challenge
        )
        user_action_token = user_action_result["userAction"]

        return self._http.request_with_user_action(
            method="POST",
            path="/key-stores/{storeId}/proof-of-control/output",
            path_params={"storeId": store_id},
            query_params=None,
            body=body,
            user_action=user_action_token,
        )
