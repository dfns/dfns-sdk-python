"""Client for the signers domain."""

from typing import Any, Literal, Optional, TypedDict, Union

from ..._internal import HttpClient
from . import types as T


class SignersClient:
    """Client for signers operations."""

    def __init__(self, http_client: HttpClient):
        self._http = http_client

    def create_add_mac_user_input(self, store_id: str, body: T.CreateAddMacUserInputRequest) -> None:
        """
        Create Add Mac User Input.

        Args:
        store_id: Path parameter.
        body: Request body.
        """
        return self._http.request(
            method="POST",
            path="/key-stores/{storeId}/add-mac-user/input",
            path_params={"storeId": store_id},
            query_params=None,
            body=body,
            requires_signature=True,
        )

    def create_clone_input(self, store_id: str, body: T.CreateCloneInputRequest) -> None:
        """
        Create Clone Input.

        Args:
        store_id: Path parameter.
        body: Request body.
        """
        return self._http.request(
            method="POST",
            path="/key-stores/{storeId}/clone/input",
            path_params={"storeId": store_id},
            query_params=None,
            body=body,
            requires_signature=True,
        )

    def create_genesis_input(self, store_id: str, body: T.CreateGenesisInputRequest) -> None:
        """
        Create Genesis Input.

        Args:
        store_id: Path parameter.
        body: Request body.
        """
        return self._http.request(
            method="POST",
            path="/key-stores/{storeId}/genesis/input",
            path_params={"storeId": store_id},
            query_params=None,
            body=body,
            requires_signature=True,
        )

    def create_onchain_sign_input(self, store_id: str, body: T.CreateOnchainSignInputRequest) -> None:
        """
        Create Onchain Sign Input.

        Args:
        store_id: Path parameter.
        body: Request body.
        """
        return self._http.request(
            method="POST",
            path="/key-stores/{storeId}/onchain-sign/input",
            path_params={"storeId": store_id},
            query_params=None,
            body=body,
            requires_signature=True,
        )

    def create_proof_of_control_input(self, store_id: str, body: T.CreateProofOfControlInputRequest) -> None:
        """
        Create Proof Of Control Input.

        Args:
        store_id: Path parameter.
        body: Request body.
        """
        return self._http.request(
            method="POST",
            path="/key-stores/{storeId}/proof-of-control/input",
            path_params={"storeId": store_id},
            query_params=None,
            body=body,
            requires_signature=True,
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

    def submit_add_mac_user_output(self, store_id: str, body: T.SubmitAddMacUserOutputRequest) -> T.SubmitAddMacUserOutputResponse:
        """
        Submit Add Mac User Output.

        Args:
        store_id: Path parameter.
        body: Request body.

        Returns:
            T.SubmitAddMacUserOutputResponse: The API response.
        """
        return self._http.request(
            method="POST",
            path="/key-stores/{storeId}/add-mac-user/output",
            path_params={"storeId": store_id},
            query_params=None,
            body=body,
            requires_signature=True,
        )

    def submit_clone_output(self, store_id: str, body: T.SubmitCloneOutputRequest) -> T.SubmitCloneOutputResponse:
        """
        Submit Clone Output.

        Args:
        store_id: Path parameter.
        body: Request body.

        Returns:
            T.SubmitCloneOutputResponse: The API response.
        """
        return self._http.request(
            method="POST",
            path="/key-stores/{storeId}/clone/output",
            path_params={"storeId": store_id},
            query_params=None,
            body=body,
            requires_signature=True,
        )

    def submit_genesis_output(self, store_id: str, body: T.SubmitGenesisOutputRequest) -> T.SubmitGenesisOutputResponse:
        """
        Submit Genesis Output.

        Args:
        store_id: Path parameter.
        body: Request body.

        Returns:
            T.SubmitGenesisOutputResponse: The API response.
        """
        return self._http.request(
            method="POST",
            path="/key-stores/{storeId}/genesis/output",
            path_params={"storeId": store_id},
            query_params=None,
            body=body,
            requires_signature=True,
        )

    def submit_onchain_sign_output(self, store_id: str, body: T.SubmitOnchainSignOutputRequest) -> T.SubmitOnchainSignOutputResponse:
        """
        Submit Onchain Sign Output.

        Args:
        store_id: Path parameter.
        body: Request body.

        Returns:
            T.SubmitOnchainSignOutputResponse: The API response.
        """
        return self._http.request(
            method="POST",
            path="/key-stores/{storeId}/onchain-sign/output",
            path_params={"storeId": store_id},
            query_params=None,
            body=body,
            requires_signature=True,
        )

    def submit_proof_of_control_output(self, store_id: str, body: T.SubmitProofOfControlOutputRequest) -> T.SubmitProofOfControlOutputResponse:
        """
        Submit Proof Of Control Output.

        Args:
        store_id: Path parameter.
        body: Request body.

        Returns:
            T.SubmitProofOfControlOutputResponse: The API response.
        """
        return self._http.request(
            method="POST",
            path="/key-stores/{storeId}/proof-of-control/output",
            path_params={"storeId": store_id},
            query_params=None,
            body=body,
            requires_signature=True,
        )
