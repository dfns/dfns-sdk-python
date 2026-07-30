"""Client for the vaults domain."""

from typing import cast

from ..._internal import HttpClient
from . import types as T


class VaultsClient:
    """Client for vaults operations."""

    def __init__(self, http_client: HttpClient):
        self._http = http_client

    def list_vaults(self, query: T.ListVaultsQuery | None = None) -> T.ListVaultsResponse:
        """
        List Vaults.

        Retrieves the list of Vaults in your organization.

        Args:
            query: Query parameters.

        Returns:
            T.ListVaultsResponse: The API response.
        """  # noqa: E501
        response = self._http.request(
            method="GET",
            path="/vaults",
            path_params={},
            query_params=query,
            body=None,
            requires_signature=False,
        )
        return cast(T.ListVaultsResponse, response)

    def create_vault(self, body: T.CreateVaultRequest) -> T.CreateVaultResponse:
        """
        Create Vault.

        Creates a new Vault.

        Args:
            body: Request body.

        Returns:
            T.CreateVaultResponse: The API response.
        """  # noqa: E501
        response = self._http.request(
            method="POST",
            path="/vaults",
            path_params={},
            query_params=None,
            body=body,
            requires_signature=True,
        )
        return cast(T.CreateVaultResponse, response)

    def create_vault_address(self, vault_id: str, body: T.CreateVaultAddressRequest) -> T.CreateVaultAddressResponse:
        """
        Create Vault Address.

        Creates a vault address (managed wallet) on an EVM or Bitcoin network.

        Args:
            vault_id: Vault id.
            body: Request body.

        Returns:
            T.CreateVaultAddressResponse: The API response.
        """  # noqa: E501
        response = self._http.request(
            method="POST",
            path="/vaults/{vaultId}/addresses",
            path_params={"vaultId": vault_id},
            query_params=None,
            body=body,
            requires_signature=True,
        )
        return cast(T.CreateVaultAddressResponse, response)

    def create_vault_transfer(self, vault_id: str, body: T.CreateVaultTransferRequest) -> T.CreateVaultTransferResponse:
        """
        Create Vault Transfer.

        Creates a transfer out of a vault, reserving the amount and estimated fee from the vault's available balance.

        Args:
            vault_id: Vault id.
            body: Request body.

        Returns:
            T.CreateVaultTransferResponse: The API response.
        """  # noqa: E501
        response = self._http.request(
            method="POST",
            path="/vaults/{vaultId}/transfers",
            path_params={"vaultId": vault_id},
            query_params=None,
            body=body,
            requires_signature=True,
        )
        return cast(T.CreateVaultTransferResponse, response)

    def get_vault(self, vault_id: str) -> T.GetVaultResponse:
        """
        Get Vault.

        Retrieves a Vault by its ID.

        Args:
            vault_id: The vault to retrieve.

        Returns:
            T.GetVaultResponse: The API response.
        """  # noqa: E501
        response = self._http.request(
            method="GET",
            path="/vaults/{vaultId}",
            path_params={"vaultId": vault_id},
            query_params=None,
            body=None,
            requires_signature=False,
        )
        return cast(T.GetVaultResponse, response)

    def update_vault(self, vault_id: str, body: T.UpdateVaultRequest) -> T.UpdateVaultResponse:
        """
        Update Vault.

        Updates an existing Vault.

        Args:
            vault_id: Vault id.
            body: Request body.

        Returns:
            T.UpdateVaultResponse: The API response.
        """  # noqa: E501
        response = self._http.request(
            method="PUT",
            path="/vaults/{vaultId}",
            path_params={"vaultId": vault_id},
            query_params=None,
            body=body,
            requires_signature=True,
        )
        return cast(T.UpdateVaultResponse, response)

    def list_vault_assets(
        self, vault_id: str, query: T.ListVaultAssetsQuery | None = None
    ) -> T.ListVaultAssetsResponse:
        """
        List Vault Assets.

        Lists a vault's assets with balances (available/quarantined/locked) and USD valuation.

        Args:
            vault_id: Vault id.
            query: Query parameters.

        Returns:
            T.ListVaultAssetsResponse: The API response.
        """  # noqa: E501
        response = self._http.request(
            method="GET",
            path="/vaults/{vaultId}/assets",
            path_params={"vaultId": vault_id},
            query_params=query,
            body=None,
            requires_signature=False,
        )
        return cast(T.ListVaultAssetsResponse, response)

    def list_vault_balances(
        self, vault_id: str, query: T.ListVaultBalancesQuery | None = None
    ) -> T.ListVaultBalancesResponse:
        """
        List Vault Balances.

        Lists a vault's balance entries.

        Args:
            vault_id: Vault id.
            query: Query parameters.

        Returns:
            T.ListVaultBalancesResponse: The API response.
        """  # noqa: E501
        response = self._http.request(
            method="GET",
            path="/vaults/{vaultId}/balances",
            path_params={"vaultId": vault_id},
            query_params=query,
            body=None,
            requires_signature=False,
        )
        return cast(T.ListVaultBalancesResponse, response)

    def release_quarantine(
        self, vault_id: str, quarantine_id: str, body: T.ReleaseQuarantineRequest
    ) -> T.ReleaseQuarantineResponse:
        """
        Release Quarantine.

        Releases quarantined funds into the available balance.

        Args:
            vault_id: Vault id.
            quarantine_id: Vault quarantine id.
            body: Request body.

        Returns:
            T.ReleaseQuarantineResponse: The API response.
        """  # noqa: E501
        response = self._http.request(
            method="POST",
            path="/vaults/{vaultId}/quarantines/{quarantineId}/release",
            path_params={"vaultId": vault_id, "quarantineId": quarantine_id},
            query_params=None,
            body=body,
            requires_signature=True,
        )
        return cast(T.ReleaseQuarantineResponse, response)

    def tag_vault(self, vault_id: str, body: T.TagVaultRequest) -> T.TagVaultResponse:
        """
        Tag Vault.

        Add tags to a vault.

        Args:
            vault_id: Vault id.
            body: Request body.

        Returns:
            T.TagVaultResponse: The API response.
        """  # noqa: E501
        response = self._http.request(
            method="PUT",
            path="/vaults/{vaultId}/tags",
            path_params={"vaultId": vault_id},
            query_params=None,
            body=body,
            requires_signature=True,
        )
        return cast(T.TagVaultResponse, response)

    def untag_vault(self, vault_id: str, body: T.UntagVaultRequest) -> T.UntagVaultResponse:
        """
        Untag Vault.

        Removes the specified tags from a vault.

        Args:
            vault_id: Vault id.
            body: Request body.

        Returns:
            T.UntagVaultResponse: The API response.
        """  # noqa: E501
        response = self._http.request(
            method="DELETE",
            path="/vaults/{vaultId}/tags",
            path_params={"vaultId": vault_id},
            query_params=None,
            body=body,
            requires_signature=True,
        )
        return cast(T.UntagVaultResponse, response)
