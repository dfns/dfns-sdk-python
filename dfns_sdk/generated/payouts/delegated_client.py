"""Delegated client for the payouts domain."""

import json
from typing import Any, cast

from ..._internal import HttpClient
from ...base_auth_api import BaseAuthApi, SignUserActionChallengeRequest, UserActionChallengeResponse
from . import types as T


class DelegatedPayoutsClient:
    """
    Delegated client for payouts operations.

    This client separates user action signing into _init() and _complete() method pairs,
    allowing external systems to handle the signing process.
    """

    def __init__(self, http_client: HttpClient):
        self._http = http_client

    def list_payouts(self, query: T.ListPayoutsQuery | None = None) -> T.ListPayoutsResponse:
        """
        List Payouts.

        List payouts with optional filtering and pagination.

        Args:
            query: Query parameters.

        Returns:
            T.ListPayoutsResponse: The API response.
        """  # noqa: E501
        response = self._http.request(
            method="GET",
            path="/payouts",
            path_params={},
            query_params=query,
            body=None,
            requires_signature=False,
        )
        return cast(T.ListPayoutsResponse, response)

    def create_payout_init(self, body: dict[str, Any]) -> UserActionChallengeResponse:
        """
        Initialize Create Payout.

        Creates a user action challenge for external signing.

        Args:
            body: Request body.

        Returns:
            UserActionChallengeResponse: The challenge to sign externally.
        """  # noqa: E501
        path = "/payouts"
        payload = json.dumps(body, separators=(",", ":")) if body else ""

        return BaseAuthApi.create_user_action_challenge(
            self._http,
            user_action_http_method="POST",
            user_action_http_path=path,
            user_action_payload=payload,
        )

    def create_payout_complete(
        self, body: dict[str, Any], signed_challenge: SignUserActionChallengeRequest
    ) -> dict[str, Any]:
        """
        Complete Create Payout.

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
            path="/payouts",
            path_params={},
            query_params=None,
            body=body,
            user_action=user_action_token,
        )
        return cast(dict[str, Any], response)

    def request_payout_quote(self, body: dict[str, Any]) -> T.RequestPayoutQuoteResponse:
        """
        Request Payout Quote.

        Request a quote from a given provider for a payout. Returns estimated fiat amount and fees.

        Args:
            body: Request body.

        Returns:
            T.RequestPayoutQuoteResponse: The API response.
        """  # noqa: E501
        response = self._http.request(
            method="POST",
            path="/payouts/quote",
            path_params={},
            query_params=None,
            body=body,
            requires_signature=False,
        )
        return cast(T.RequestPayoutQuoteResponse, response)

    def get_payout_status(self, payout_id: str) -> dict[str, Any]:
        """
        Get Payout Status.

        Retrieve the current status of a payout by its ID.

        Args:
            payout_id: Payout id.

        Returns:
            dict[str, Any]: The API response.
        """  # noqa: E501
        response = self._http.request(
            method="GET",
            path="/payouts/{payoutId}",
            path_params={"payoutId": payout_id},
            query_params=None,
            body=None,
            requires_signature=False,
        )
        return cast(dict[str, Any], response)

    def create_payout_action_init(self, payout_id: str, body: dict[str, Any]) -> UserActionChallengeResponse:
        """
        Initialize Create Payout Action.

        Creates a user action challenge for external signing.

        Args:
            payout_id: Payout id.
            body: Request body.

        Returns:
            UserActionChallengeResponse: The challenge to sign externally.
        """  # noqa: E501
        path = "/payouts/{payoutId}/action"
        path = path.replace("{payoutId}", str(payout_id))
        payload = json.dumps(body, separators=(",", ":")) if body else ""

        return BaseAuthApi.create_user_action_challenge(
            self._http,
            user_action_http_method="POST",
            user_action_http_path=path,
            user_action_payload=payload,
        )

    def create_payout_action_complete(
        self, payout_id: str, body: dict[str, Any], signed_challenge: SignUserActionChallengeRequest
    ) -> T.CreatePayoutActionResponse:
        """
        Complete Create Payout Action.

        Submits the signed challenge and makes the API request.

        Args:
            payout_id: Payout id.
            body: Request body.
            signed_challenge: The signed challenge from external signing.

        Returns:
            T.CreatePayoutActionResponse: The API response.
        """  # noqa: E501
        user_action_result = BaseAuthApi.sign_user_action_challenge(self._http, signed_challenge)
        user_action_token = user_action_result["userAction"]

        response = self._http.request_with_user_action(
            method="POST",
            path="/payouts/{payoutId}/action",
            path_params={"payoutId": payout_id},
            query_params=None,
            body=body,
            user_action=user_action_token,
        )
        return cast(T.CreatePayoutActionResponse, response)
