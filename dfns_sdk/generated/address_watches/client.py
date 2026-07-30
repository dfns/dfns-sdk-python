"""Client for the address_watches domain."""

from typing import cast

from ..._internal import HttpClient
from . import types as T


class AddressWatchesClient:
    """Client for address_watches operations."""

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

    def create_address_watch(self, body: T.CreateAddressWatchRequest) -> T.CreateAddressWatchResponse:
        """
                Create Address Watch.

                Registers an on chain address to watch. An address watch is not controlled by Dfns: it holds no key, it cannot sign or move funds. The indexer matches on chain activity touching the address and sends the corresponding webhooks.

        The address must already exist on chain and is normalized to the form the indexer matches on (lowercase for EVM networks). Only networks that support address watches are accepted. A given address can only be watched once per network within an organization while the watch is Active.

                Args:
                    body: Request body.

                Returns:
                    T.CreateAddressWatchResponse: The API response.
        """  # noqa: E501
        response = self._http.request(
            method="POST",
            path="/address-watches",
            path_params={},
            query_params=None,
            body=body,
            requires_signature=True,
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
