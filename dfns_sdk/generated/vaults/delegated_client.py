"""Delegated client for the vaults domain."""

import json
from typing import cast

from ..._internal import HttpClient
from ...base_auth_api import BaseAuthApi, SignUserActionChallengeRequest, UserActionChallengeResponse
from . import types as T


class DelegatedVaultsClient:
    """
    Delegated client for vaults operations.

    This client separates user action signing into _init() and _complete() method pairs,
    allowing external systems to handle the signing process.
    """

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

    def create_vault_init(self, body: T.CreateVaultRequest) -> UserActionChallengeResponse:
        """
        Initialize Create Vault.

        Creates a user action challenge for external signing.

        Args:
            body: Request body.

        Returns:
            UserActionChallengeResponse: The challenge to sign externally.
        """  # noqa: E501
        path = "/vaults"
        payload = json.dumps(body, separators=(",", ":")) if body else ""

        return BaseAuthApi.create_user_action_challenge(
            self._http,
            user_action_http_method="POST",
            user_action_http_path=path,
            user_action_payload=payload,
        )

    def create_vault_complete(
        self, body: T.CreateVaultRequest, signed_challenge: SignUserActionChallengeRequest
    ) -> T.CreateVaultResponse:
        """
        Complete Create Vault.

        Submits the signed challenge and makes the API request.

        Args:
            body: Request body.
            signed_challenge: The signed challenge from external signing.

        Returns:
            T.CreateVaultResponse: The API response.
        """  # noqa: E501
        user_action_result = BaseAuthApi.sign_user_action_challenge(self._http, signed_challenge)
        user_action_token = user_action_result["userAction"]

        response = self._http.request_with_user_action(
            method="POST",
            path="/vaults",
            path_params={},
            query_params=None,
            body=body,
            user_action=user_action_token,
        )
        return cast(T.CreateVaultResponse, response)

    def create_vault_address_init(
        self, vault_id: str, body: T.CreateVaultAddressRequest
    ) -> UserActionChallengeResponse:
        """
        Initialize Create Vault Address.

        Creates a user action challenge for external signing.

        Args:
            vault_id: Vault id.
            body: Request body.

        Returns:
            UserActionChallengeResponse: The challenge to sign externally.
        """  # noqa: E501
        path = "/vaults/{vaultId}/addresses"
        path = path.replace("{vaultId}", str(vault_id))
        payload = json.dumps(body, separators=(",", ":")) if body else ""

        return BaseAuthApi.create_user_action_challenge(
            self._http,
            user_action_http_method="POST",
            user_action_http_path=path,
            user_action_payload=payload,
        )

    def create_vault_address_complete(
        self, vault_id: str, body: T.CreateVaultAddressRequest, signed_challenge: SignUserActionChallengeRequest
    ) -> T.CreateVaultAddressResponse:
        """
        Complete Create Vault Address.

        Submits the signed challenge and makes the API request.

        Args:
            vault_id: Vault id.
            body: Request body.
            signed_challenge: The signed challenge from external signing.

        Returns:
            T.CreateVaultAddressResponse: The API response.
        """  # noqa: E501
        user_action_result = BaseAuthApi.sign_user_action_challenge(self._http, signed_challenge)
        user_action_token = user_action_result["userAction"]

        response = self._http.request_with_user_action(
            method="POST",
            path="/vaults/{vaultId}/addresses",
            path_params={"vaultId": vault_id},
            query_params=None,
            body=body,
            user_action=user_action_token,
        )
        return cast(T.CreateVaultAddressResponse, response)

    def create_vault_transfer_init(
        self, vault_id: str, body: T.CreateVaultTransferRequest
    ) -> UserActionChallengeResponse:
        """
        Initialize Create Vault Transfer.

        Creates a user action challenge for external signing.

        Args:
            vault_id: Vault id.
            body: Request body.

        Returns:
            UserActionChallengeResponse: The challenge to sign externally.
        """  # noqa: E501
        path = "/vaults/{vaultId}/transfers"
        path = path.replace("{vaultId}", str(vault_id))
        payload = json.dumps(body, separators=(",", ":")) if body else ""

        return BaseAuthApi.create_user_action_challenge(
            self._http,
            user_action_http_method="POST",
            user_action_http_path=path,
            user_action_payload=payload,
        )

    def create_vault_transfer_complete(
        self, vault_id: str, body: T.CreateVaultTransferRequest, signed_challenge: SignUserActionChallengeRequest
    ) -> T.CreateVaultTransferResponse:
        """
        Complete Create Vault Transfer.

        Submits the signed challenge and makes the API request.

        Args:
            vault_id: Vault id.
            body: Request body.
            signed_challenge: The signed challenge from external signing.

        Returns:
            T.CreateVaultTransferResponse: The API response.
        """  # noqa: E501
        user_action_result = BaseAuthApi.sign_user_action_challenge(self._http, signed_challenge)
        user_action_token = user_action_result["userAction"]

        response = self._http.request_with_user_action(
            method="POST",
            path="/vaults/{vaultId}/transfers",
            path_params={"vaultId": vault_id},
            query_params=None,
            body=body,
            user_action=user_action_token,
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

    def update_vault_init(self, vault_id: str, body: T.UpdateVaultRequest) -> UserActionChallengeResponse:
        """
        Initialize Update Vault.

        Creates a user action challenge for external signing.

        Args:
            vault_id: Vault id.
            body: Request body.

        Returns:
            UserActionChallengeResponse: The challenge to sign externally.
        """  # noqa: E501
        path = "/vaults/{vaultId}"
        path = path.replace("{vaultId}", str(vault_id))
        payload = json.dumps(body, separators=(",", ":")) if body else ""

        return BaseAuthApi.create_user_action_challenge(
            self._http,
            user_action_http_method="PUT",
            user_action_http_path=path,
            user_action_payload=payload,
        )

    def update_vault_complete(
        self, vault_id: str, body: T.UpdateVaultRequest, signed_challenge: SignUserActionChallengeRequest
    ) -> T.UpdateVaultResponse:
        """
        Complete Update Vault.

        Submits the signed challenge and makes the API request.

        Args:
            vault_id: Vault id.
            body: Request body.
            signed_challenge: The signed challenge from external signing.

        Returns:
            T.UpdateVaultResponse: The API response.
        """  # noqa: E501
        user_action_result = BaseAuthApi.sign_user_action_challenge(self._http, signed_challenge)
        user_action_token = user_action_result["userAction"]

        response = self._http.request_with_user_action(
            method="PUT",
            path="/vaults/{vaultId}",
            path_params={"vaultId": vault_id},
            query_params=None,
            body=body,
            user_action=user_action_token,
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

    def tag_vault_init(self, vault_id: str, body: T.TagVaultRequest) -> UserActionChallengeResponse:
        """
        Initialize Tag Vault.

        Creates a user action challenge for external signing.

        Args:
            vault_id: Vault id.
            body: Request body.

        Returns:
            UserActionChallengeResponse: The challenge to sign externally.
        """  # noqa: E501
        path = "/vaults/{vaultId}/tags"
        path = path.replace("{vaultId}", str(vault_id))
        payload = json.dumps(body, separators=(",", ":")) if body else ""

        return BaseAuthApi.create_user_action_challenge(
            self._http,
            user_action_http_method="PUT",
            user_action_http_path=path,
            user_action_payload=payload,
        )

    def tag_vault_complete(
        self, vault_id: str, body: T.TagVaultRequest, signed_challenge: SignUserActionChallengeRequest
    ) -> T.TagVaultResponse:
        """
        Complete Tag Vault.

        Submits the signed challenge and makes the API request.

        Args:
            vault_id: Vault id.
            body: Request body.
            signed_challenge: The signed challenge from external signing.

        Returns:
            T.TagVaultResponse: The API response.
        """  # noqa: E501
        user_action_result = BaseAuthApi.sign_user_action_challenge(self._http, signed_challenge)
        user_action_token = user_action_result["userAction"]

        response = self._http.request_with_user_action(
            method="PUT",
            path="/vaults/{vaultId}/tags",
            path_params={"vaultId": vault_id},
            query_params=None,
            body=body,
            user_action=user_action_token,
        )
        return cast(T.TagVaultResponse, response)

    def untag_vault_init(self, vault_id: str, body: T.UntagVaultRequest) -> UserActionChallengeResponse:
        """
        Initialize Untag Vault.

        Creates a user action challenge for external signing.

        Args:
            vault_id: Vault id.
            body: Request body.

        Returns:
            UserActionChallengeResponse: The challenge to sign externally.
        """  # noqa: E501
        path = "/vaults/{vaultId}/tags"
        path = path.replace("{vaultId}", str(vault_id))
        payload = json.dumps(body, separators=(",", ":")) if body else ""

        return BaseAuthApi.create_user_action_challenge(
            self._http,
            user_action_http_method="DELETE",
            user_action_http_path=path,
            user_action_payload=payload,
        )

    def untag_vault_complete(
        self, vault_id: str, body: T.UntagVaultRequest, signed_challenge: SignUserActionChallengeRequest
    ) -> T.UntagVaultResponse:
        """
        Complete Untag Vault.

        Submits the signed challenge and makes the API request.

        Args:
            vault_id: Vault id.
            body: Request body.
            signed_challenge: The signed challenge from external signing.

        Returns:
            T.UntagVaultResponse: The API response.
        """  # noqa: E501
        user_action_result = BaseAuthApi.sign_user_action_challenge(self._http, signed_challenge)
        user_action_token = user_action_result["userAction"]

        response = self._http.request_with_user_action(
            method="DELETE",
            path="/vaults/{vaultId}/tags",
            path_params={"vaultId": vault_id},
            query_params=None,
            body=body,
            user_action=user_action_token,
        )
        return cast(T.UntagVaultResponse, response)

    def unquarantine_init(
        self, vault_id: str, quarantine_id: str, body: T.UnquarantineRequest
    ) -> UserActionChallengeResponse:
        """
        Initialize Unquarantine.

        Creates a user action challenge for external signing.

        Args:
            vault_id: Vault id.
            quarantine_id: Vault quarantine id.
            body: Request body.

        Returns:
            UserActionChallengeResponse: The challenge to sign externally.
        """  # noqa: E501
        path = "/vaults/{vaultId}/quarantines/{quarantineId}"
        path = path.replace("{vaultId}", str(vault_id))
        path = path.replace("{quarantineId}", str(quarantine_id))
        payload = json.dumps(body, separators=(",", ":")) if body else ""

        return BaseAuthApi.create_user_action_challenge(
            self._http,
            user_action_http_method="DELETE",
            user_action_http_path=path,
            user_action_payload=payload,
        )

    def unquarantine_complete(
        self,
        vault_id: str,
        quarantine_id: str,
        body: T.UnquarantineRequest,
        signed_challenge: SignUserActionChallengeRequest,
    ) -> T.UnquarantineResponse:
        """
        Complete Unquarantine.

        Submits the signed challenge and makes the API request.

        Args:
            vault_id: Vault id.
            quarantine_id: Vault quarantine id.
            body: Request body.
            signed_challenge: The signed challenge from external signing.

        Returns:
            T.UnquarantineResponse: The API response.
        """  # noqa: E501
        user_action_result = BaseAuthApi.sign_user_action_challenge(self._http, signed_challenge)
        user_action_token = user_action_result["userAction"]

        response = self._http.request_with_user_action(
            method="DELETE",
            path="/vaults/{vaultId}/quarantines/{quarantineId}",
            path_params={"vaultId": vault_id, "quarantineId": quarantine_id},
            query_params=None,
            body=body,
            user_action=user_action_token,
        )
        return cast(T.UnquarantineResponse, response)
