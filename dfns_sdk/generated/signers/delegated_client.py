"""Delegated client for the signers domain."""

import json
from typing import Any, Literal, TypedDict, cast
from typing_extensions import NotRequired, deprecated
from ..._internal import HttpClient
from ...base_auth_api import BaseAuthApi, SignUserActionChallengeRequest, UserActionChallengeResponse
from . import types as T


class DelegatedSignersClient:
    """
    Delegated client for signers operations.

    This client separates user action signing into _init() and _complete() method pairs,
    allowing external systems to handle the signing process.
    """

    def __init__(self, http_client: HttpClient):
        self._http = http_client

    def create_add_mac_user_input_init(self, store_id: str, body: T.CreateAddMacUserInputRequest) -> UserActionChallengeResponse:
        """
        Initialize Create Add Mac User Input.

        Creates a user action challenge for external signing.

        Args:
            store_id: Path parameter.
            body: Request body.

        Returns:
            UserActionChallengeResponse: The challenge to sign externally.
        """  # noqa: E501
        path = "/key-stores/{storeId}/add-mac-user/input"
        path = path.replace("{storeId}", str(store_id))
        payload = json.dumps(body, separators=(",", ":")) if body else ""

        return BaseAuthApi.create_user_action_challenge(
            self._http,
            user_action_http_method="POST",
            user_action_http_path=path,
            user_action_payload=payload,
        )

    def create_add_mac_user_input_complete(self, store_id: str, body: T.CreateAddMacUserInputRequest, signed_challenge: SignUserActionChallengeRequest) -> None:
        """
        Complete Create Add Mac User Input.

        Submits the signed challenge and makes the API request.

        Args:
            store_id: Path parameter.
            body: Request body.
            signed_challenge: The signed challenge from external signing.
        """  # noqa: E501
        user_action_result = BaseAuthApi.sign_user_action_challenge(
            self._http, signed_challenge
        )
        user_action_token = user_action_result["userAction"]

        self._http.request_with_user_action(
            method="POST",
            path="/key-stores/{storeId}/add-mac-user/input",
            path_params={"storeId": store_id},
            query_params=None,
            body=body,
            user_action=user_action_token,
        )

    def create_clone_input_init(self, store_id: str, body: T.CreateCloneInputRequest) -> UserActionChallengeResponse:
        """
        Initialize Create Clone Input.

        Creates a user action challenge for external signing.

        Args:
            store_id: Path parameter.
            body: Request body.

        Returns:
            UserActionChallengeResponse: The challenge to sign externally.
        """  # noqa: E501
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
        """  # noqa: E501
        user_action_result = BaseAuthApi.sign_user_action_challenge(
            self._http, signed_challenge
        )
        user_action_token = user_action_result["userAction"]

        self._http.request_with_user_action(
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
        """  # noqa: E501
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
        """  # noqa: E501
        user_action_result = BaseAuthApi.sign_user_action_challenge(
            self._http, signed_challenge
        )
        user_action_token = user_action_result["userAction"]

        self._http.request_with_user_action(
            method="POST",
            path="/key-stores/{storeId}/genesis/input",
            path_params={"storeId": store_id},
            query_params=None,
            body=body,
            user_action=user_action_token,
        )

    def create_onchain_sign_input_init(self, store_id: str, body: T.CreateOnchainSignInputRequest) -> UserActionChallengeResponse:
        """
        Initialize Create Onchain Sign Input.

        Creates a user action challenge for external signing.

        Args:
            store_id: Path parameter.
            body: Request body.

        Returns:
            UserActionChallengeResponse: The challenge to sign externally.
        """  # noqa: E501
        path = "/key-stores/{storeId}/onchain-sign/input"
        path = path.replace("{storeId}", str(store_id))
        payload = json.dumps(body, separators=(",", ":")) if body else ""

        return BaseAuthApi.create_user_action_challenge(
            self._http,
            user_action_http_method="POST",
            user_action_http_path=path,
            user_action_payload=payload,
        )

    def create_onchain_sign_input_complete(self, store_id: str, body: T.CreateOnchainSignInputRequest, signed_challenge: SignUserActionChallengeRequest) -> None:
        """
        Complete Create Onchain Sign Input.

        Submits the signed challenge and makes the API request.

        Args:
            store_id: Path parameter.
            body: Request body.
            signed_challenge: The signed challenge from external signing.
        """  # noqa: E501
        user_action_result = BaseAuthApi.sign_user_action_challenge(
            self._http, signed_challenge
        )
        user_action_token = user_action_result["userAction"]

        self._http.request_with_user_action(
            method="POST",
            path="/key-stores/{storeId}/onchain-sign/input",
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
        """  # noqa: E501
        path = "/key-stores/{storeId}/proof-of-control/input"
        path = path.replace("{storeId}", str(store_id))
        payload = json.dumps(body, separators=(",", ":")) if body else ""

        return BaseAuthApi.create_user_action_challenge(
            self._http,
            user_action_http_method="POST",
            user_action_http_path=path,
            user_action_payload=payload,
        )

    def create_proof_of_control_input_complete(self, store_id: str, body: T.CreateProofOfControlInputRequest, signed_challenge: SignUserActionChallengeRequest) -> None:
        """
        Complete Create Proof Of Control Input.

        Submits the signed challenge and makes the API request.

        Args:
            store_id: Path parameter.
            body: Request body.
            signed_challenge: The signed challenge from external signing.
        """  # noqa: E501
        user_action_result = BaseAuthApi.sign_user_action_challenge(
            self._http, signed_challenge
        )
        user_action_token = user_action_result["userAction"]

        self._http.request_with_user_action(
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
        """  # noqa: E501
        response = self._http.request(
            method="GET",
            path="/key-stores",
            path_params={},
            query_params=None,
            body=None,
            requires_signature=False,
        )
        return cast(T.ListKeyStoresResponse, response)

    def list_signers(self) -> T.ListSignersResponse:
        """
        List Signers.

        Returns:
            T.ListSignersResponse: The API response.
        """  # noqa: E501
        response = self._http.request(
            method="GET",
            path="/signers",
            path_params={},
            query_params=None,
            body=None,
            requires_signature=False,
        )
        return cast(T.ListSignersResponse, response)

    def submit_add_mac_user_output(self, store_id: str, body: T.SubmitAddMacUserOutputRequest, file: bytes) -> T.SubmitAddMacUserOutputResponse:
        """
        Submit Add Mac User Output.

        Args:
            store_id: Path parameter.
            body: Request body.
            file: The file bytes to upload.

        Returns:
            T.SubmitAddMacUserOutputResponse: The API response.
        """  # noqa: E501
        response = self._http.request(
            method="POST",
            path="/key-stores/{storeId}/add-mac-user/output",
            path_params={"storeId": store_id},
            query_params=None,
            body=body,
            file=file,
            requires_signature=True,
        )
        return cast(T.SubmitAddMacUserOutputResponse, response)

    def submit_clone_output(self, store_id: str, body: T.SubmitCloneOutputRequest, file: bytes) -> T.SubmitCloneOutputResponse:
        """
        Submit Clone Output.

        Args:
            store_id: Path parameter.
            body: Request body.
            file: The file bytes to upload.

        Returns:
            T.SubmitCloneOutputResponse: The API response.
        """  # noqa: E501
        response = self._http.request(
            method="POST",
            path="/key-stores/{storeId}/clone/output",
            path_params={"storeId": store_id},
            query_params=None,
            body=body,
            file=file,
            requires_signature=True,
        )
        return cast(T.SubmitCloneOutputResponse, response)

    def submit_genesis_output(self, store_id: str, body: T.SubmitGenesisOutputRequest, file: bytes) -> T.SubmitGenesisOutputResponse:
        """
        Submit Genesis Output.

        Args:
            store_id: Path parameter.
            body: Request body.
            file: The file bytes to upload.

        Returns:
            T.SubmitGenesisOutputResponse: The API response.
        """  # noqa: E501
        response = self._http.request(
            method="POST",
            path="/key-stores/{storeId}/genesis/output",
            path_params={"storeId": store_id},
            query_params=None,
            body=body,
            file=file,
            requires_signature=True,
        )
        return cast(T.SubmitGenesisOutputResponse, response)

    def submit_onchain_sign_output(self, store_id: str, body: T.SubmitOnchainSignOutputRequest, file: bytes) -> T.SubmitOnchainSignOutputResponse:
        """
        Submit Onchain Sign Output.

        Args:
            store_id: Path parameter.
            body: Request body.
            file: The file bytes to upload.

        Returns:
            T.SubmitOnchainSignOutputResponse: The API response.
        """  # noqa: E501
        response = self._http.request(
            method="POST",
            path="/key-stores/{storeId}/onchain-sign/output",
            path_params={"storeId": store_id},
            query_params=None,
            body=body,
            file=file,
            requires_signature=True,
        )
        return cast(T.SubmitOnchainSignOutputResponse, response)

    def submit_proof_of_control_output(self, store_id: str, body: T.SubmitProofOfControlOutputRequest, file: bytes) -> T.SubmitProofOfControlOutputResponse:
        """
        Submit Proof Of Control Output.

        Args:
            store_id: Path parameter.
            body: Request body.
            file: The file bytes to upload.

        Returns:
            T.SubmitProofOfControlOutputResponse: The API response.
        """  # noqa: E501
        response = self._http.request(
            method="POST",
            path="/key-stores/{storeId}/proof-of-control/output",
            path_params={"storeId": store_id},
            query_params=None,
            body=body,
            file=file,
            requires_signature=True,
        )
        return cast(T.SubmitProofOfControlOutputResponse, response)
