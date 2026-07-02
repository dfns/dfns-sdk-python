"""Client for the payouts domain."""

from typing import Any, cast

from ..._internal import HttpClient
from . import types as T


class PayoutsClient:
    """Client for payouts operations."""

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

    def create_payout(self, body: dict[str, Any]) -> dict[str, Any]:
        """
        Create Payout.

        Create a new payout to convert crypto assets to fiat currency.

        Args:
            body: Request body.

        Returns:
            dict[str, Any]: The API response.
        """  # noqa: E501
        response = self._http.request(
            method="POST",
            path="/payouts",
            path_params={},
            query_params=None,
            body=body,
            requires_signature=True,
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

    def create_payout_action(self, payout_id: str, body: dict[str, Any]) -> T.CreatePayoutActionResponse:
        """
        Create Payout Action.

        Perform an action on a payout, such as confirming or canceling.

        Args:
            payout_id: Payout id.
            body: Request body.

        Returns:
            T.CreatePayoutActionResponse: The API response.
        """  # noqa: E501
        response = self._http.request(
            method="POST",
            path="/payouts/{payoutId}/action",
            path_params={"payoutId": payout_id},
            query_params=None,
            body=body,
            requires_signature=True,
        )
        return cast(T.CreatePayoutActionResponse, response)
