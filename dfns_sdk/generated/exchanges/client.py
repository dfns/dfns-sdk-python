"""Client for the exchanges domain."""

from typing import Any, cast

from ..._internal import HttpClient
from . import types as T


class ExchangesClient:
    """Client for exchanges operations."""

    def __init__(self, http_client: HttpClient):
        self._http = http_client

    def get_exchange(self, exchange_id: str) -> T.GetExchangeResponse:
        """
        Get Exchange.

        Retrieve the details of a specific exchange integration configuration.

        Args:
            exchange_id: Path parameter.

        Returns:
            T.GetExchangeResponse: The API response.
        """  # noqa: E501
        response = self._http.request(
            method="GET",
            path="/exchanges/{exchangeId}",
            path_params={"exchangeId": exchange_id},
            query_params=None,
            body=None,
            requires_signature=False,
        )
        return cast(T.GetExchangeResponse, response)

    def delete_exchange(self, exchange_id: str) -> T.DeleteExchangeResponse:
        """
        Delete Exchange.

        Delete the exchange configuration from your organization.

        Args:
            exchange_id: Path parameter.

        Returns:
            T.DeleteExchangeResponse: The API response.
        """  # noqa: E501
        response = self._http.request(
            method="DELETE",
            path="/exchanges/{exchangeId}",
            path_params={"exchangeId": exchange_id},
            query_params=None,
            body=None,
            requires_signature=True,
        )
        return cast(T.DeleteExchangeResponse, response)

    def list_exchanges(self, query: T.ListExchangesQuery | None = None) -> T.ListExchangesResponse:
        """
        List Exchanges.

        List all configured exchange integrations.

        Args:
            query: Query parameters.

        Returns:
            T.ListExchangesResponse: The API response.
        """  # noqa: E501
        response = self._http.request(
            method="GET",
            path="/exchanges",
            path_params={},
            query_params=query,
            body=None,
            requires_signature=False,
        )
        return cast(T.ListExchangesResponse, response)

    def create_exchange(self, body: T.CreateExchangeRequest) -> T.CreateExchangeResponse:
        """
        Create Exchange.

        Link your organization with a cryptocurrency exchange.

        Args:
            body: Request body.

        Returns:
            T.CreateExchangeResponse: The API response.
        """  # noqa: E501
        response = self._http.request(
            method="POST",
            path="/exchanges",
            path_params={},
            query_params=None,
            body=body,
            requires_signature=True,
        )
        return cast(T.CreateExchangeResponse, response)

    def list_accounts(self, exchange_id: str, query: T.ListAccountsQuery | None = None) -> T.ListAccountsResponse:
        """
        List Accounts.

        Get a list of accounts for a specific exchange.

        Args:
            exchange_id: Path parameter.
            query: Query parameters.

        Returns:
            T.ListAccountsResponse: The API response.
        """  # noqa: E501
        response = self._http.request(
            method="GET",
            path="/exchanges/{exchangeId}/accounts",
            path_params={"exchangeId": exchange_id},
            query_params=query,
            body=None,
            requires_signature=False,
        )
        return cast(T.ListAccountsResponse, response)

    def list_account_assets(
        self, exchange_id: str, account_id: str, query: T.ListAccountAssetsQuery | None = None
    ) -> T.ListAccountAssetsResponse:
        """
        List Account Assets.

        Retrieve the list of assets for a specific account on a specific exchange.

        Args:
            exchange_id: Path parameter.
            account_id: Path parameter.
            query: Query parameters.

        Returns:
            T.ListAccountAssetsResponse: The API response.
        """  # noqa: E501
        response = self._http.request(
            method="GET",
            path="/exchanges/{exchangeId}/accounts/{accountId}/assets",
            path_params={"exchangeId": exchange_id, "accountId": account_id},
            query_params=query,
            body=None,
            requires_signature=False,
        )
        return cast(T.ListAccountAssetsResponse, response)

    def list_asset_withdrawal_networks(self, exchange_id: str, account_id: str, asset: str) -> list[dict[str, Any]]:
        """
        List Asset Withdrawal Networks.

        Args:
            exchange_id: Path parameter.
            account_id: Path parameter.
            asset: Path parameter.

        Returns:
            list[dict[str, Any]]: The API response.
        """  # noqa: E501
        response = self._http.request(
            method="GET",
            path="/exchanges/{exchangeId}/accounts/{accountId}/assets/{asset}/withdrawal-networks",
            path_params={"exchangeId": exchange_id, "accountId": account_id, "asset": asset},
            query_params=None,
            body=None,
            requires_signature=False,
        )
        return cast(list[dict[str, Any]], response)

    def create_exchange_deposit(
        self, exchange_id: str, account_id: str, body: dict[str, Any]
    ) -> T.CreateExchangeDepositResponse:
        """
        Create Exchange Deposit.

        Creates a new exchange deposit transaction.

        Args:
            exchange_id: The exchange id obtained from the Create Exchange endpoint. Ex: `ex-1f04s-lqc9q-xxxxxxxxxxxxxxxx`
            account_id: Unique identifier for the account like "spot"
            body: Request body.

        Returns:
            T.CreateExchangeDepositResponse: The API response.
        """  # noqa: E501
        response = self._http.request(
            method="POST",
            path="/exchanges/{exchangeId}/accounts/{accountId}/deposits",
            path_params={"exchangeId": exchange_id, "accountId": account_id},
            query_params=None,
            body=body,
            requires_signature=True,
        )
        return cast(T.CreateExchangeDepositResponse, response)

    def create_exchange_withdrawal(
        self, exchange_id: str, account_id: str, body: dict[str, Any]
    ) -> T.CreateExchangeWithdrawalResponse:
        """
        Create Exchange Withdrawal.

        Creates a new exchange withdrawal transaction.

        Args:
            exchange_id: The exchange id obtained from the Create Exchange endpoint. Ex: `ex-1f04s-lqc9q-xxxxxxxxxxxxxxxx`
            account_id: Unique identifier for the account like "spot"
            body: Request body.

        Returns:
            T.CreateExchangeWithdrawalResponse: The API response.
        """  # noqa: E501
        response = self._http.request(
            method="POST",
            path="/exchanges/{exchangeId}/accounts/{accountId}/withdrawals",
            path_params={"exchangeId": exchange_id, "accountId": account_id},
            query_params=None,
            body=body,
            requires_signature=True,
        )
        return cast(T.CreateExchangeWithdrawalResponse, response)
