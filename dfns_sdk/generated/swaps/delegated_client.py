"""Delegated client for the swaps domain."""

import json
from typing import Any, Literal, Optional, TypedDict, Union

from ..._internal import HttpClient
from ...base_auth_api import (
    BaseAuthApi,
    SignUserActionChallengeRequest,
    UserActionChallengeResponse,
)
from . import types as T


class DelegatedSwapsClient:
    """
    Delegated client for swaps operations.

    This client separates user action signing into _init() and _complete() method pairs,
    allowing external systems to handle the signing process.
    """

    def __init__(self, http_client: HttpClient):
        self._http = http_client

    def list_swaps(self, query: Optional[T.ListSwapsQuery] = None) -> T.ListSwapsResponse:
        """
        List Swaps.

        List all swaps with pagination

        Args:
        query: Query parameters.

        Returns:
            T.ListSwapsResponse: The API response.
        """
        return self._http.request(
            method="GET",
            path="/swaps",
            path_params={},
            query_params=query,
            body=None,
            requires_signature=False,
        )

    def create_swap_init(self, body: T.CreateSwapRequest) -> UserActionChallengeResponse:
        """
        Initialize Create Swap.

        Creates a user action challenge for external signing.

        Args:
        body: Request body.

        Returns:
            UserActionChallengeResponse: The challenge to sign externally.
        """
        path = "/swaps"
        payload = json.dumps(body, separators=(",", ":")) if body else ""

        return BaseAuthApi.create_user_action_challenge(
            self._http,
            user_action_http_method="POST",
            user_action_http_path=path,
            user_action_payload=payload,
        )

    def create_swap_complete(self, body: T.CreateSwapRequest, signed_challenge: SignUserActionChallengeRequest) -> T.CreateSwapResponse:
        """
        Complete Create Swap.

        Submits the signed challenge and makes the API request.

        Args:
        body: Request body.
        signed_challenge: The signed challenge from external signing.

        Returns:
            T.CreateSwapResponse: The API response.
        """
        user_action_result = BaseAuthApi.sign_user_action_challenge(
            self._http, signed_challenge
        )
        user_action_token = user_action_result["userAction"]

        return self._http.request_with_user_action(
            method="POST",
            path="/swaps",
            path_params={},
            query_params=None,
            body=body,
            user_action=user_action_token,
        )

    def request_swap_quote(self, body: T.RequestSwapQuoteRequest) -> T.RequestSwapQuoteResponse:
        """
        Request Swap Quote.

        Request a quote from a given provider for swapping assets. This is the first step of the [Swap flow](https://docs.dfns.co/api-reference/swaps#flow-overview).

        Args:
        body: Request body.

        Returns:
            T.RequestSwapQuoteResponse: The API response.
        """
        return self._http.request(
            method="POST",
            path="/swaps/quotes",
            path_params={},
            query_params=None,
            body=body,
            requires_signature=False,
        )

    def get_swap(self, swap_id: str) -> T.GetSwapResponse:
        """
        Get Swap.

        Get details of a specific swap by its ID

        Args:
        swap_id: Id of the swap for which we want to get details.

        Returns:
            T.GetSwapResponse: The API response.
        """
        return self._http.request(
            method="GET",
            path="/swaps/{swapId}",
            path_params={"swapId": swap_id},
            query_params=None,
            body=None,
            requires_signature=False,
        )

    def get_swap_quote(self, quote_id: str) -> T.GetSwapQuoteResponse:
        """
        Get Swap Quote.

        Get details of a specific swap quote by its ID

        Args:
        quote_id: The ID of the Swap Quote.

        Returns:
            T.GetSwapQuoteResponse: The API response.
        """
        return self._http.request(
            method="GET",
            path="/swaps/quotes/{quoteId}",
            path_params={"quoteId": quote_id},
            query_params=None,
            body=None,
            requires_signature=False,
        )
