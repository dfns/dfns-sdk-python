"""Delegated client for the address_watches domain."""

import json
from typing import cast

from ..._internal import HttpClient
from ...base_auth_api import BaseAuthApi, SignUserActionChallengeRequest, UserActionChallengeResponse
from . import types as T


class DelegatedAddressWatchesClient:
    """
    Delegated client for address_watches operations.

    This client separates user action signing into _init() and _complete() method pairs,
    allowing external systems to handle the signing process.
    """

    def __init__(self, http_client: HttpClient):
        self._http = http_client

    def list_address_watches(self, query: T.ListAddressWatchesQuery | None = None) -> T.ListAddressWatchesResponse:
        """
        List Address Watches.

        Retrieves the list of address watches in your organization. Pagination is supported via limit and paginationToken parameters.

        Args:
            query: Query parameters.

        Returns:
            T.ListAddressWatchesResponse: The API response.
        """  # noqa: E501
        response = self._http.request(
            method="GET",
            path="/address-watches",
            path_params={},
            query_params=query,
            body=None,
            requires_signature=False,
        )
        return cast(T.ListAddressWatchesResponse, response)

    def create_address_watch_init(self, body: T.CreateAddressWatchRequest) -> UserActionChallengeResponse:
        """
        Initialize Create Address Watch.

        Creates a user action challenge for external signing.

        Args:
            body: Request body.

        Returns:
            UserActionChallengeResponse: The challenge to sign externally.
        """  # noqa: E501
        path = "/address-watches"
        payload = json.dumps(body, separators=(",", ":")) if body else ""

        return BaseAuthApi.create_user_action_challenge(
            self._http,
            user_action_http_method="POST",
            user_action_http_path=path,
            user_action_payload=payload,
        )

    def create_address_watch_complete(
        self, body: T.CreateAddressWatchRequest, signed_challenge: SignUserActionChallengeRequest
    ) -> T.CreateAddressWatchResponse:
        """
        Complete Create Address Watch.

        Submits the signed challenge and makes the API request.

        Args:
            body: Request body.
            signed_challenge: The signed challenge from external signing.

        Returns:
            T.CreateAddressWatchResponse: The API response.
        """  # noqa: E501
        user_action_result = BaseAuthApi.sign_user_action_challenge(self._http, signed_challenge)
        user_action_token = user_action_result["userAction"]

        response = self._http.request_with_user_action(
            method="POST",
            path="/address-watches",
            path_params={},
            query_params=None,
            body=body,
            user_action=user_action_token,
        )
        return cast(T.CreateAddressWatchResponse, response)

    def get_address_watch(self, address_watch_id: str) -> T.GetAddressWatchResponse:
        """
        Get Address Watch.

        Retrieves an address watch by its ID.

        Args:
            address_watch_id: The address watch to retrieve.

        Returns:
            T.GetAddressWatchResponse: The API response.
        """  # noqa: E501
        response = self._http.request(
            method="GET",
            path="/address-watches/{addressWatchId}",
            path_params={"addressWatchId": address_watch_id},
            query_params=None,
            body=None,
            requires_signature=False,
        )
        return cast(T.GetAddressWatchResponse, response)

    def get_address_watch_assets(
        self, address_watch_id: str, query: T.GetAddressWatchAssetsQuery | None = None
    ) -> T.GetAddressWatchAssetsResponse:
        """
        Get Address Watch Assets.

        Retrieves the list of assets held by the address watch, as tracked by the indexer. Balances are tracked from the moment the watch is created.

        Args:
            address_watch_id: The address watch to retrieve the assets of.
            query: Query parameters.

        Returns:
            T.GetAddressWatchAssetsResponse: The API response.
        """  # noqa: E501
        response = self._http.request(
            method="GET",
            path="/address-watches/{addressWatchId}/assets",
            path_params={"addressWatchId": address_watch_id},
            query_params=query,
            body=None,
            requires_signature=False,
        )
        return cast(T.GetAddressWatchAssetsResponse, response)

    def get_address_watch_blockchain_events(
        self, address_watch_id: str, query: T.GetAddressWatchBlockchainEventsQuery | None = None
    ) -> T.GetAddressWatchBlockchainEventsResponse:
        """
                Get Address Watch Blockchain Events.

                Retrieves a list of decoded blockchain events indexed for the specified address watch.

        Blockchain events are not value transfers: asset and token transfers are listed by
        [Get Address Watch History](https://docs.dfns.co/api-reference/address-watches/get-address-watch-history) instead.
        Events from the same transaction share the same `txHash` across both lists.

        Items are sorted by descending block number; within one block the item order is not the on-chain
        order. `index` is the block scoped log index as a decimal string: sort by `blockNumber` and the
        numeric value of `index` to recover the on-chain order. Webhook delivery is at-least-once and
        unordered; use `id` to deduplicate.

                Args:
                    address_watch_id: Address watch you want to get the blockchain events from.
                    query: Query parameters.

                Returns:
                    T.GetAddressWatchBlockchainEventsResponse: The API response.
        """  # noqa: E501
        response = self._http.request(
            method="GET",
            path="/address-watches/{addressWatchId}/blockchain-events",
            path_params={"addressWatchId": address_watch_id},
            query_params=query,
            body=None,
            requires_signature=False,
        )
        return cast(T.GetAddressWatchBlockchainEventsResponse, response)

    def get_address_watch_history(
        self, address_watch_id: str, query: T.GetAddressWatchHistoryQuery | None = None
    ) -> T.GetAddressWatchHistoryResponse:
        """
                Get Address Watch History.

                Retrieves the list of indexed on chain activities for the specified address watch.

        The list reflects the indexed on chain activity from the moment the watch was created. Events from before the watch are not backfilled.

                Args:
                    address_watch_id: Address watch you want to get the history from.
                    query: Query parameters.

                Returns:
                    T.GetAddressWatchHistoryResponse: The API response.
        """  # noqa: E501
        response = self._http.request(
            method="GET",
            path="/address-watches/{addressWatchId}/history",
            path_params={"addressWatchId": address_watch_id},
            query_params=query,
            body=None,
            requires_signature=False,
        )
        return cast(T.GetAddressWatchHistoryResponse, response)
