"""Client for the fee_sponsors domain."""

from typing import Any, Literal, Optional, TypedDict, Union

from ..._internal import HttpClient
from . import types as T


class FeeSponsorsClient:
    """Client for fee_sponsors operations."""

    def __init__(self, http_client: HttpClient):
        self._http = http_client

    def list_fee_sponsors(self, query: Optional[T.ListFeeSponsorsQuery] = None) -> T.ListFeeSponsorsResponse:
        """
        List Fee Sponsors.

        Retrieves all Fee Sponsors configured in your organization.

        Args:
        query: Query parameters.

        Returns:
            T.ListFeeSponsorsResponse: The API response.
        """
        return self._http.request(
            method="GET",
            path="/fee-sponsors",
            path_params={},
            query_params=query,
            body=None,
            requires_signature=False,
        )

    def create_fee_sponsor(self, body: T.CreateFeeSponsorRequest) -> T.CreateFeeSponsorResponse:
        """
        Create Fee Sponsor.

        Creates a new `FeeSponsor` associated with a sponsor wallet. Returns a new fee sponsor entity with the `id` to be used when making a transfer.

        Args:
        body: Request body.

        Returns:
            T.CreateFeeSponsorResponse: The API response.
        """
        return self._http.request(
            method="POST",
            path="/fee-sponsors",
            path_params={},
            query_params=None,
            body=body,
            requires_signature=True,
        )

    def get_fee_sponsor(self, fee_sponsor_id: str) -> T.GetFeeSponsorResponse:
        """
        Get Fee Sponsor.

        Retrieve a Fee Sponsor information by ID.

        Args:
        fee_sponsor_id: Which Fee Sponsor you wish to retrieve.

        Returns:
            T.GetFeeSponsorResponse: The API response.
        """
        return self._http.request(
            method="GET",
            path="/fee-sponsors/{feeSponsorId}",
            path_params={"feeSponsorId": fee_sponsor_id},
            query_params=None,
            body=None,
            requires_signature=False,
        )

    def delete_fee_sponsor(self, fee_sponsor_id: str) -> T.DeleteFeeSponsorResponse:
        """
        Delete Fee Sponsor.

        Delete a Fee Sponsor. This action is irreversible. The fee sponsor won't be able to be used anymore when making a transfer.

        Args:
        fee_sponsor_id: Which Fee Sponsor you wish to delete.

        Returns:
            T.DeleteFeeSponsorResponse: The API response.
        """
        return self._http.request(
            method="DELETE",
            path="/fee-sponsors/{feeSponsorId}",
            path_params={"feeSponsorId": fee_sponsor_id},
            query_params=None,
            body=None,
            requires_signature=True,
        )

    def deactivate_fee_sponsor(self, fee_sponsor_id: str) -> T.DeactivateFeeSponsorResponse:
        """
        Deactivate Fee Sponsor.

        Deactivate a Fee Sponsor: The fee sponsor won't be able to be used anymore when making a transfer.

        Args:
        fee_sponsor_id: Which Fee Sponsor you wish to deactivate.

        Returns:
            T.DeactivateFeeSponsorResponse: The API response.
        """
        return self._http.request(
            method="PUT",
            path="/fee-sponsors/{feeSponsorId}/deactivate",
            path_params={"feeSponsorId": fee_sponsor_id},
            query_params=None,
            body=None,
            requires_signature=True,
        )

    def activate_fee_sponsor(self, fee_sponsor_id: str) -> T.ActivateFeeSponsorResponse:
        """
        Activate Fee Sponsor.

        Activate a Fee Sponsor: The fee sponsor can be used when making a transfer.

        Args:
        fee_sponsor_id: Which Fee Sponsor you wish to activate.

        Returns:
            T.ActivateFeeSponsorResponse: The API response.
        """
        return self._http.request(
            method="PUT",
            path="/fee-sponsors/{feeSponsorId}/activate",
            path_params={"feeSponsorId": fee_sponsor_id},
            query_params=None,
            body=None,
            requires_signature=True,
        )

    def list_sponsored_fees(self, fee_sponsor_id: str, query: Optional[T.ListSponsoredFeesQuery] = None) -> T.ListSponsoredFeesResponse:
        """
        List Sponsored Fees.

        Retrieves all fees paid by the specific Fee Sponsor.

        Args:
        fee_sponsor_id: Fee Sponsor to retrieve the fees from.
        query: Query parameters.

        Returns:
            T.ListSponsoredFeesResponse: The API response.
        """
        return self._http.request(
            method="GET",
            path="/fee-sponsors/{feeSponsorId}/fees",
            path_params={"feeSponsorId": fee_sponsor_id},
            query_params=query,
            body=None,
            requires_signature=False,
        )
