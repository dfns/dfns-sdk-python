"""Delegated client for the exchanges domain."""

import json
from typing import Any, Literal, TypedDict, cast
from typing_extensions import NotRequired, deprecated
from ..._internal import HttpClient
from ...base_auth_api import BaseAuthApi, SignUserActionChallengeRequest, UserActionChallengeResponse
from . import types as T


class DelegatedExchangesClient:
    """
    Delegated client for exchanges operations.

    This client separates user action signing into _init() and _complete() method pairs,
    allowing external systems to handle the signing process.
    """

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

    def delete_exchange_init(self, exchange_id: str) -> UserActionChallengeResponse:
        """
        Initialize Delete Exchange.

        Creates a user action challenge for external signing.

        Args:
            exchange_id: Path parameter.

        Returns:
            UserActionChallengeResponse: The challenge to sign externally.
        """  # noqa: E501
        path = "/exchanges/{exchangeId}"
        path = path.replace("{exchangeId}", str(exchange_id))
        payload = ""

        return BaseAuthApi.create_user_action_challenge(
            self._http,
            user_action_http_method="DELETE",
            user_action_http_path=path,
            user_action_payload=payload,
        )

    def delete_exchange_complete(self, exchange_id: str, signed_challenge: SignUserActionChallengeRequest) -> T.DeleteExchangeResponse:
        """
        Complete Delete Exchange.

        Submits the signed challenge and makes the API request.

        Args:
            exchange_id: Path parameter.
            signed_challenge: The signed challenge from external signing.

        Returns:
            T.DeleteExchangeResponse: The API response.
        """  # noqa: E501
        user_action_result = BaseAuthApi.sign_user_action_challenge(
            self._http, signed_challenge
        )
        user_action_token = user_action_result["userAction"]

        response = self._http.request_with_user_action(
            method="DELETE",
            path="/exchanges/{exchangeId}",
            path_params={"exchangeId": exchange_id},
            query_params=None,
            body=None,
            user_action=user_action_token,
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

    def create_exchange_init(self, body: T.CreateExchangeRequest) -> UserActionChallengeResponse:
        """
        Initialize Create Exchange.

        Creates a user action challenge for external signing.

        Args:
            body: Request body.

        Returns:
            UserActionChallengeResponse: The challenge to sign externally.
        """  # noqa: E501
        path = "/exchanges"
        payload = json.dumps(body, separators=(",", ":")) if body else ""

        return BaseAuthApi.create_user_action_challenge(
            self._http,
            user_action_http_method="POST",
            user_action_http_path=path,
            user_action_payload=payload,
        )

    def create_exchange_complete(self, body: T.CreateExchangeRequest, signed_challenge: SignUserActionChallengeRequest) -> T.CreateExchangeResponse:
        """
        Complete Create Exchange.

        Submits the signed challenge and makes the API request.

        Args:
            body: Request body.
            signed_challenge: The signed challenge from external signing.

        Returns:
            T.CreateExchangeResponse: The API response.
        """  # noqa: E501
        user_action_result = BaseAuthApi.sign_user_action_challenge(
            self._http, signed_challenge
        )
        user_action_token = user_action_result["userAction"]

        response = self._http.request_with_user_action(
            method="POST",
            path="/exchanges",
            path_params={},
            query_params=None,
            body=body,
            user_action=user_action_token,
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

    def list_account_assets(self, exchange_id: str, account_id: str, query: T.ListAccountAssetsQuery | None = None) -> T.ListAccountAssetsResponse:
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

    def create_exchange_deposit_init(self, exchange_id: str, account_id: str, body: dict[str, Any]) -> UserActionChallengeResponse:
        """
        Initialize Create Exchange Deposit.

        Creates a user action challenge for external signing.

        Args:
            exchange_id: The exchange id obtained from the Create Exchange endpoint. Ex: `ex-1f04s-lqc9q-xxxxxxxxxxxxxxxx`
            account_id: Unique identifier for the account like "spot"
            body: Request body.

        Returns:
            UserActionChallengeResponse: The challenge to sign externally.
        """  # noqa: E501
        path = "/exchanges/{exchangeId}/accounts/{accountId}/deposits"
        path = path.replace("{exchangeId}", str(exchange_id))
        path = path.replace("{accountId}", str(account_id))
        payload = json.dumps(body, separators=(",", ":")) if body else ""

        return BaseAuthApi.create_user_action_challenge(
            self._http,
            user_action_http_method="POST",
            user_action_http_path=path,
            user_action_payload=payload,
        )

    def create_exchange_deposit_complete(self, exchange_id: str, account_id: str, body: dict[str, Any], signed_challenge: SignUserActionChallengeRequest) -> T.CreateExchangeDepositResponse:
        """
        Complete Create Exchange Deposit.

        Submits the signed challenge and makes the API request.

        Args:
            exchange_id: The exchange id obtained from the Create Exchange endpoint. Ex: `ex-1f04s-lqc9q-xxxxxxxxxxxxxxxx`
            account_id: Unique identifier for the account like "spot"
            body: Request body.
            signed_challenge: The signed challenge from external signing.

        Returns:
            T.CreateExchangeDepositResponse: The API response.
        """  # noqa: E501
        user_action_result = BaseAuthApi.sign_user_action_challenge(
            self._http, signed_challenge
        )
        user_action_token = user_action_result["userAction"]

        response = self._http.request_with_user_action(
            method="POST",
            path="/exchanges/{exchangeId}/accounts/{accountId}/deposits",
            path_params={"exchangeId": exchange_id, "accountId": account_id},
            query_params=None,
            body=body,
            user_action=user_action_token,
        )
        return cast(T.CreateExchangeDepositResponse, response)

    def create_exchange_withdrawal_init(self, exchange_id: str, account_id: str, body: dict[str, Any]) -> UserActionChallengeResponse:
        """
        Initialize Create Exchange Withdrawal.

        Creates a user action challenge for external signing.

        Args:
            exchange_id: The exchange id obtained from the Create Exchange endpoint. Ex: `ex-1f04s-lqc9q-xxxxxxxxxxxxxxxx`
            account_id: Unique identifier for the account like "spot"
            body: Request body.

        Returns:
            UserActionChallengeResponse: The challenge to sign externally.
        """  # noqa: E501
        path = "/exchanges/{exchangeId}/accounts/{accountId}/withdrawals"
        path = path.replace("{exchangeId}", str(exchange_id))
        path = path.replace("{accountId}", str(account_id))
        payload = json.dumps(body, separators=(",", ":")) if body else ""

        return BaseAuthApi.create_user_action_challenge(
            self._http,
            user_action_http_method="POST",
            user_action_http_path=path,
            user_action_payload=payload,
        )

    def create_exchange_withdrawal_complete(self, exchange_id: str, account_id: str, body: dict[str, Any], signed_challenge: SignUserActionChallengeRequest) -> T.CreateExchangeWithdrawalResponse:
        """
        Complete Create Exchange Withdrawal.

        Submits the signed challenge and makes the API request.

        Args:
            exchange_id: The exchange id obtained from the Create Exchange endpoint. Ex: `ex-1f04s-lqc9q-xxxxxxxxxxxxxxxx`
            account_id: Unique identifier for the account like "spot"
            body: Request body.
            signed_challenge: The signed challenge from external signing.

        Returns:
            T.CreateExchangeWithdrawalResponse: The API response.
        """  # noqa: E501
        user_action_result = BaseAuthApi.sign_user_action_challenge(
            self._http, signed_challenge
        )
        user_action_token = user_action_result["userAction"]

        response = self._http.request_with_user_action(
            method="POST",
            path="/exchanges/{exchangeId}/accounts/{accountId}/withdrawals",
            path_params={"exchangeId": exchange_id, "accountId": account_id},
            query_params=None,
            body=body,
            user_action=user_action_token,
        )
        return cast(T.CreateExchangeWithdrawalResponse, response)
