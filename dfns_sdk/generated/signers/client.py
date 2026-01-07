"""Client for the signers domain."""

from typing import Any, Literal, Optional, TypedDict, Union

from ..._internal import HttpClient
from . import types as T


class SignersClient:
    """Client for signers operations."""

    def __init__(self, http_client: HttpClient):
        self._http = http_client

    def list_key_stores(self) -> T.ListKeyStoresResponse:
        """
        List Key Stores.

        Returns:
            T.ListKeyStoresResponse: The API response.
        """
        return self._http.request(
            method="GET",
            path="/key-stores",
            path_params={},
            query_params=None,
            body=None,
            requires_signature=False,
        )

    def list_signers(self) -> T.ListSignersResponse:
        """
        List Signers.

        Returns:
            T.ListSignersResponse: The API response.
        """
        return self._http.request(
            method="GET",
            path="/signers",
            path_params={},
            query_params=None,
            body=None,
            requires_signature=False,
        )
