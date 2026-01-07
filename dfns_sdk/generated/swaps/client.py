"""Client for the swaps domain."""

from typing import Any, Literal, Optional, TypedDict, Union

from ..._internal import HttpClient
from . import types as T


class SwapsClient:
    """Client for swaps operations."""

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

    def create_swap(self, body: T.CreateSwapRequest) -> T.CreateSwapResponse:
        """
        Create Swap.

        Create a new swap based on an existing quote. This is the second step of the [Swap flow](https://docs.dfns.co/api-reference/swaps#flow-overview).

        Args:
        body: Request body.

        Returns:
            T.CreateSwapResponse: The API response.
        """
        return self._http.request(
            method="POST",
            path="/swaps",
            path_params={},
            query_params=None,
            body=body,
            requires_signature=True,
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
