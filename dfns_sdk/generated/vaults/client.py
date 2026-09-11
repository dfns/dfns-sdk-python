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

        Creates a vault address (managed wallet) on a network that supports vaults — EVM networks, Bitcoin, and Solana (native SOL and SPL/Token-2022 tokens). Add one network per call.

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

    def list_vault_locks(self, vault_id: str, query: T.ListVaultLocksQuery | None = None) -> T.ListVaultLocksResponse:
        """
        List Vault Locks.

        Lists a vault's locks, active and released.

        Args:
            vault_id: Vault id.
            query: Query parameters.

        Returns:
            T.ListVaultLocksResponse: The API response.
        """  # noqa: E501
        response = self._http.request(
            method="GET",
            path="/vaults/{vaultId}/locks",
            path_params={"vaultId": vault_id},
            query_params=query,
            body=None,
            requires_signature=False,
        )
        return cast(T.ListVaultLocksResponse, response)

    def create_vault_lock(self, vault_id: str, body: T.CreateVaultLockRequest) -> T.CreateVaultLockResponse:
        """
        Create Vault Lock.

        Requests locking funds from the vault's available balance for off-chain settlement or escrow. Returns the created lock (200), or the pending lock request (202) when a policy requires approval.

        Args:
            vault_id: Vault id.
            body: Request body.

        Returns:
            T.CreateVaultLockResponse: The API response.
        """  # noqa: E501
        response = self._http.request(
            method="POST",
            path="/vaults/{vaultId}/locks",
            path_params={"vaultId": vault_id},
            query_params=None,
            body=body,
            requires_signature=True,
        )
        return cast(T.CreateVaultLockResponse, response)

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

    def get_vault_lock(self, vault_id: str, lock_id: str) -> T.GetVaultLockResponse:
        """
        Get Vault Lock.

        Retrieves a vault lock by its ID.

        Args:
            vault_id: Vault id.
            lock_id: The lock to retrieve.

        Returns:
            T.GetVaultLockResponse: The API response.
        """  # noqa: E501
        response = self._http.request(
            method="GET",
            path="/vaults/{vaultId}/locks/{lockId}",
            path_params={"vaultId": vault_id, "lockId": lock_id},
            query_params=None,
            body=None,
            requires_signature=False,
        )
        return cast(T.GetVaultLockResponse, response)

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

    def release_vault_lock(self, vault_id: str, lock_id: str) -> T.ReleaseVaultLockResponse:
        """
        Release Vault Lock.

        Releases a lock, returning the locked funds to the vault's available balance. Owner only.

        Args:
            vault_id: Vault id.
            lock_id: Vault lock id.

        Returns:
            T.ReleaseVaultLockResponse: The API response.
        """  # noqa: E501
        response = self._http.request(
            method="POST",
            path="/vaults/{vaultId}/locks/{lockId}/release",
            path_params={"vaultId": vault_id, "lockId": lock_id},
            query_params=None,
            body=None,
            requires_signature=True,
        )
        return cast(T.ReleaseVaultLockResponse, response)

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

    def replace_vault_lock(
        self, vault_id: str, lock_id: str, body: T.ReplaceVaultLockRequest
    ) -> T.ReplaceVaultLockResponse:
        """
        Replace Vault Lock.

        Requests replacing a lock with a new lock at a new total amount. Owner only. Executed immediately unless a policy requires approval. On execution the lock is released, a new lock is created at the new amount (carrying over the owner, externalId and reason), and the new lock is returned. If a policy requires approval, responds 202 with the pending replace request instead.

        Args:
            vault_id: Vault id.
            lock_id: Vault lock id.
            body: Request body.

        Returns:
            T.ReplaceVaultLockResponse: The API response.
        """  # noqa: E501
        response = self._http.request(
            method="POST",
            path="/vaults/{vaultId}/locks/{lockId}/replace",
            path_params={"vaultId": vault_id, "lockId": lock_id},
            query_params=None,
            body=body,
            requires_signature=True,
        )
        return cast(T.ReplaceVaultLockResponse, response)
