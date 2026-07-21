"""Delegated client for the payins domain."""

import json
from typing import Any, cast

from ..._internal import HttpClient
from ...base_auth_api import BaseAuthApi, SignUserActionChallengeRequest, UserActionChallengeResponse
from . import types as T


class DelegatedPayinsClient:
    """
    Delegated client for payins operations.

    This client separates user action signing into _init() and _complete() method pairs,
    allowing external systems to handle the signing process.
    """

    def __init__(self, http_client: HttpClient):
        self._http = http_client

    def list_payins(self, query: T.ListPayinsQuery | None = None) -> T.ListPayinsResponse:
        """
        List Payins.

        List payins with optional filtering and pagination.

        Args:
            query: Query parameters.

        Returns:
            T.ListPayinsResponse: The API response.
        """  # noqa: E501
        response = self._http.request(
            method="GET",
            path="/payins",
            path_params={},
            query_params=query,
            body=None,
            requires_signature=False,
        )
        return cast(T.ListPayinsResponse, response)

    def create_payin_init(self, body: dict[str, Any]) -> UserActionChallengeResponse:
        """
        Initialize Create Payin.

        Creates a user action challenge for external signing.

        Args:
            body: Request body.

        Returns:
            UserActionChallengeResponse: The challenge to sign externally.
        """  # noqa: E501
        path = "/payins"
        payload = json.dumps(body, separators=(",", ":")) if body else ""

        return BaseAuthApi.create_user_action_challenge(
            self._http,
            user_action_http_method="POST",
            user_action_http_path=path,
            user_action_payload=payload,
        )

    def create_payin_complete(
        self, body: dict[str, Any], signed_challenge: SignUserActionChallengeRequest
    ) -> dict[str, Any]:
        """
        Complete Create Payin.

        Submits the signed challenge and makes the API request.

        Args:
            body: Request body.
            signed_challenge: The signed challenge from external signing.

        Returns:
            dict[str, Any]: The API response.
        """  # noqa: E501
        user_action_result = BaseAuthApi.sign_user_action_challenge(self._http, signed_challenge)
        user_action_token = user_action_result["userAction"]

        response = self._http.request_with_user_action(
            method="POST",
            path="/payins",
            path_params={},
            query_params=None,
            body=body,
            user_action=user_action_token,
        )
        return cast(dict[str, Any], response)

    def get_payin_recipient(self, query: T.GetPayinRecipientQuery) -> T.GetPayinRecipientResponse:
        """
        Get Payin Recipient.

        Check whether a wallet's address is registered (and approved) as an payin recipient with the provider.

        Args:
            query: Query parameters.

        Returns:
            T.GetPayinRecipientResponse: The API response.
        """  # noqa: E501
        response = self._http.request(
            method="GET",
            path="/payins/recipients",
            path_params={},
            query_params=query,
            body=None,
            requires_signature=False,
        )
        return cast(T.GetPayinRecipientResponse, response)

    def register_payin_recipient_init(self, body: dict[str, Any]) -> UserActionChallengeResponse:
        """
        Initialize Register Payin Recipient.

        Creates a user action challenge for external signing.

        Args:
            body: Request body.

        Returns:
            UserActionChallengeResponse: The challenge to sign externally.
        """  # noqa: E501
        path = "/payins/recipients"
        payload = json.dumps(body, separators=(",", ":")) if body else ""

        return BaseAuthApi.create_user_action_challenge(
            self._http,
            user_action_http_method="POST",
            user_action_http_path=path,
            user_action_payload=payload,
        )

    def register_payin_recipient_complete(
        self, body: dict[str, Any], signed_challenge: SignUserActionChallengeRequest
    ) -> T.RegisterPayinRecipientResponse:
        """
        Complete Register Payin Recipient.

        Submits the signed challenge and makes the API request.

        Args:
            body: Request body.
            signed_challenge: The signed challenge from external signing.

        Returns:
            T.RegisterPayinRecipientResponse: The API response.
        """  # noqa: E501
        user_action_result = BaseAuthApi.sign_user_action_challenge(self._http, signed_challenge)
        user_action_token = user_action_result["userAction"]

        response = self._http.request_with_user_action(
            method="POST",
            path="/payins/recipients",
            path_params={},
            query_params=None,
            body=body,
            user_action=user_action_token,
        )
        return cast(T.RegisterPayinRecipientResponse, response)

    def get_payin_status(self, payin_id: str) -> dict[str, Any]:
        """
        Get Payin Status.

        Retrieve the current status of an payin by its ID.

        Args:
            payin_id: Payin id.

        Returns:
            dict[str, Any]: The API response.
        """  # noqa: E501
        response = self._http.request(
            method="GET",
            path="/payins/{payinId}",
            path_params={"payinId": payin_id},
            query_params=None,
            body=None,
            requires_signature=False,
        )
        return cast(dict[str, Any], response)

    def list_payin_balances(self, query: T.ListPayinBalancesQuery) -> T.ListPayinBalancesResponse:
        """
            List Payin Balances.

            The organisation's available balance at the payin provider, one entry per currency —
        the funds payins can deliver on-chain.

            Args:
                query: Query parameters.

            Returns:
                T.ListPayinBalancesResponse: The API response.
        """  # noqa: E501
        response = self._http.request(
            method="GET",
            path="/payins/balances",
            path_params={},
            query_params=query,
            body=None,
            requires_signature=False,
        )
        return cast(T.ListPayinBalancesResponse, response)
