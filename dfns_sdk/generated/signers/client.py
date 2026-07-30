"""Client for the signers domain."""

from typing import cast

from ..._internal import HttpClient
from . import types as T


class SignersClient:
    """Client for signers operations."""

    def __init__(self, http_client: HttpClient):
        self._http = http_client

    def cancel_fleet_operation(
        self, store_id: str, body: T.CancelFleetOperationRequest
    ) -> T.CancelFleetOperationResponse:
        """
        Cancel Fleet Operation.

        Args:
            store_id: Path parameter.
            body: Request body.

        Returns:
            T.CancelFleetOperationResponse: The API response.
        """  # noqa: E501
        response = self._http.request(
            method="POST",
            path="/key-stores/{storeId}/fleet-operations/cancel",
            path_params={"storeId": store_id},
            query_params=None,
            body=body,
            requires_signature=True,
        )
        return cast(T.CancelFleetOperationResponse, response)

    def create_add_mac_user_input(self, store_id: str, body: T.CreateAddMacUserInputRequest) -> None:
        """
        Create Add Mac User Input.

        Creates the input archive for an add-mac-user fleet operation, which registers a new Mac operator machine with an HSM in the key store's trust set.

        Args:
            store_id: Path parameter.
            body: Request body.
        """  # noqa: E501
        self._http.request(
            method="POST",
            path="/key-stores/{storeId}/add-mac-user/input",
            path_params={"storeId": store_id},
            query_params=None,
            body=body,
            requires_signature=True,
        )

    def create_add_provisioner_input(self, store_id: str, body: T.CreateAddProvisionerInputRequest) -> None:
        """
        Create Add Provisioner Input.

        Creates the input archive for an add-provisioner fleet operation, which registers a new provisioner YubiKey into the key store's governance set.

        Args:
            store_id: Path parameter.
            body: Request body.
        """  # noqa: E501
        self._http.request(
            method="POST",
            path="/key-stores/{storeId}/add-provisioner/input",
            path_params={"storeId": store_id},
            query_params=None,
            body=body,
            requires_signature=True,
        )

    def create_clone_input(self, store_id: str, body: T.CreateCloneInputRequest) -> None:
        """
        Create Clone Input.

        Creates the input archive for a clone fleet operation, which replicates a key store from a source HSM to a target HSM.

        Args:
            store_id: Path parameter.
            body: Request body.
        """  # noqa: E501
        self._http.request(
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

        Creates the input archive for a genesis fleet operation, which provisions a new offline signer fleet and generates the key store's initial signing keys.

        Args:
            store_id: Path parameter.
            body: Request body.
        """  # noqa: E501
        self._http.request(
            method="POST",
            path="/key-stores/{storeId}/genesis/input",
            path_params={"storeId": store_id},
            query_params=None,
            body=body,
            requires_signature=True,
        )

    def create_key_harvest_input(self, store_id: str, body: T.CreateKeyHarvestInputRequest) -> None:
        """
        Create Key Harvest Input.

        Args:
            store_id: Path parameter.
            body: Request body.
        """  # noqa: E501
        self._http.request(
            method="POST",
            path="/key-stores/{storeId}/key-harvest/input",
            path_params={"storeId": store_id},
            query_params=None,
            body=body,
            requires_signature=True,
        )

    def create_onchain_sign_input(self, store_id: str, body: T.CreateOnchainSignInputRequest) -> None:
        """
        Create Onchain Sign Input.

        Creates the input archive for an onchain-sign operation covering the key store's pending signature requests.

        Args:
            store_id: Path parameter.
            body: Request body.
        """  # noqa: E501
        self._http.request(
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

        Creates the input archive for a proof-of-control operation covering the keys of the specified wallets.

        Args:
            store_id: Path parameter.
            body: Request body.
        """  # noqa: E501
        self._http.request(
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

        Lists the key stores of your organization.

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

        Lists the signer clusters of your key store, including each signer's ID and encryption public key.

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

    def submit_add_mac_user_output(
        self, store_id: str, body: T.SubmitAddMacUserOutputRequest, file: bytes
    ) -> T.SubmitAddMacUserOutputResponse:
        """
        Submit Add Mac User Output.

        Submits the output archive produced by the offline signer fleet for an add-mac-user operation.

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

    def submit_add_provisioner_output(
        self, store_id: str, body: T.SubmitAddProvisionerOutputRequest, file: bytes
    ) -> T.SubmitAddProvisionerOutputResponse:
        """
        Submit Add Provisioner Output.

        Submits the output archive produced by the offline signer fleet for an add-provisioner operation.

        Args:
            store_id: Path parameter.
            body: Request body.
            file: The file bytes to upload.

        Returns:
            T.SubmitAddProvisionerOutputResponse: The API response.
        """  # noqa: E501
        response = self._http.request(
            method="POST",
            path="/key-stores/{storeId}/add-provisioner/output",
            path_params={"storeId": store_id},
            query_params=None,
            body=body,
            file=file,
            requires_signature=True,
        )
        return cast(T.SubmitAddProvisionerOutputResponse, response)

    def submit_clone_output(
        self, store_id: str, body: T.SubmitCloneOutputRequest, file: bytes
    ) -> T.SubmitCloneOutputResponse:
        """
        Submit Clone Output.

        Submits the output archive produced by the offline signer fleet for a clone operation.

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

    def submit_genesis_output(
        self, store_id: str, body: T.SubmitGenesisOutputRequest, file: bytes
    ) -> T.SubmitGenesisOutputResponse:
        """
        Submit Genesis Output.

        Submits the output archive produced by the offline signer fleet for a genesis operation.

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

    def submit_key_harvest_output(
        self, store_id: str, body: T.SubmitKeyHarvestOutputRequest, file: bytes
    ) -> T.SubmitKeyHarvestOutputResponse:
        """
        Submit Key Harvest Output.

        Args:
            store_id: Path parameter.
            body: Request body.
            file: The file bytes to upload.

        Returns:
            T.SubmitKeyHarvestOutputResponse: The API response.
        """  # noqa: E501
        response = self._http.request(
            method="POST",
            path="/key-stores/{storeId}/key-harvest/output",
            path_params={"storeId": store_id},
            query_params=None,
            body=body,
            file=file,
            requires_signature=True,
        )
        return cast(T.SubmitKeyHarvestOutputResponse, response)

    def submit_onchain_sign_output(
        self, store_id: str, body: T.SubmitOnchainSignOutputRequest, file: bytes
    ) -> T.SubmitOnchainSignOutputResponse:
        """
        Submit Onchain Sign Output.

        Submits the output archive produced by the offline signer fleet for an onchain-sign operation.

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

    def submit_proof_of_control_output(
        self, store_id: str, body: T.SubmitProofOfControlOutputRequest, file: bytes
    ) -> T.SubmitProofOfControlOutputResponse:
        """
        Submit Proof Of Control Output.

        Submits the output archive produced by the offline signer fleet for a proof-of-control operation.

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
