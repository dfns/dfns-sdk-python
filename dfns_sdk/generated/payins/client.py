"""Client for the payins domain."""

from typing import Any, cast

from ..._internal import HttpClient
from . import types as T


class PayinsClient:
    """Client for payins operations."""

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

    def create_payin(self, body: dict[str, Any]) -> dict[str, Any]:
        """
        Create Payin.

        Deliver stablecoin from the organisation's provider balance to a wallet on-chain.

        Args:
            body: Request body.

        Returns:
            dict[str, Any]: The API response.
        """  # noqa: E501
        response = self._http.request(
            method="POST",
            path="/payins",
            path_params={},
            query_params=None,
            body=body,
            requires_signature=True,
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

    def register_payin_recipient(self, body: dict[str, Any]) -> T.RegisterPayinRecipientResponse:
        """
            Register Payin Recipient.

            Register a wallet's address as an payin recipient with the provider. The registration then needs
        to be approved on the provider's side (for Circle Mint: by an administrator in the Mint Console)
        before payins to that wallet can be created.

            Args:
                body: Request body.

            Returns:
                T.RegisterPayinRecipientResponse: The API response.
        """  # noqa: E501
        response = self._http.request(
            method="POST",
            path="/payins/recipients",
            path_params={},
            query_params=None,
            body=body,
            requires_signature=True,
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
