"""Client for the payins domain."""

from typing import Any, cast

from ..._internal import HttpClient
from . import types as T


class PayinsClient:
    """Client for payins operations."""

    def __init__(self, http_client: HttpClient):
        self._http = http_client

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
