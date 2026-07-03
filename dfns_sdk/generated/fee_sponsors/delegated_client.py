"""Delegated client for the fee_sponsors domain."""

import json
from typing import Any, Literal, Optional, TypedDict, Union

from ..._internal import HttpClient
from ...base_auth_api import (
    BaseAuthApi,
    SignUserActionChallengeRequest,
    UserActionChallengeResponse,
)
from . import types as T


class DelegatedFeeSponsorsClient:
    """
    Delegated client for fee_sponsors operations.

    This client separates user action signing into _init() and _complete() method pairs,
    allowing external systems to handle the signing process.
    """

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

    def create_fee_sponsor_init(self, body: T.CreateFeeSponsorRequest) -> UserActionChallengeResponse:
        """
        Initialize Create Fee Sponsor.

        Creates a user action challenge for external signing.

        Args:
        body: Request body.

        Returns:
            UserActionChallengeResponse: The challenge to sign externally.
        """
        path = "/fee-sponsors"
        payload = json.dumps(body, separators=(",", ":")) if body else ""

        return BaseAuthApi.create_user_action_challenge(
            self._http,
            user_action_http_method="POST",
            user_action_http_path=path,
            user_action_payload=payload,
        )

    def create_fee_sponsor_complete(self, body: T.CreateFeeSponsorRequest, signed_challenge: SignUserActionChallengeRequest) -> T.CreateFeeSponsorResponse:
        """
        Complete Create Fee Sponsor.

        Submits the signed challenge and makes the API request.

        Args:
        body: Request body.
        signed_challenge: The signed challenge from external signing.

        Returns:
            T.CreateFeeSponsorResponse: The API response.
        """
        user_action_result = BaseAuthApi.sign_user_action_challenge(
            self._http, signed_challenge
        )
        user_action_token = user_action_result["userAction"]

        return self._http.request_with_user_action(
            method="POST",
            path="/fee-sponsors",
            path_params={},
            query_params=None,
            body=body,
            user_action=user_action_token,
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

    def delete_fee_sponsor_init(self, fee_sponsor_id: str) -> UserActionChallengeResponse:
        """
        Initialize Delete Fee Sponsor.

        Creates a user action challenge for external signing.

        Args:
        fee_sponsor_id: Which Fee Sponsor you wish to delete.

        Returns:
            UserActionChallengeResponse: The challenge to sign externally.
        """
        path = "/fee-sponsors/{feeSponsorId}"
        path = path.replace("{feeSponsorId}", str(fee_sponsor_id))
        payload = ""

        return BaseAuthApi.create_user_action_challenge(
            self._http,
            user_action_http_method="DELETE",
            user_action_http_path=path,
            user_action_payload=payload,
        )

    def delete_fee_sponsor_complete(self, fee_sponsor_id: str, signed_challenge: SignUserActionChallengeRequest) -> T.DeleteFeeSponsorResponse:
        """
        Complete Delete Fee Sponsor.

        Submits the signed challenge and makes the API request.

        Args:
        fee_sponsor_id: Which Fee Sponsor you wish to delete.
        signed_challenge: The signed challenge from external signing.

        Returns:
            T.DeleteFeeSponsorResponse: The API response.
        """
        user_action_result = BaseAuthApi.sign_user_action_challenge(
            self._http, signed_challenge
        )
        user_action_token = user_action_result["userAction"]

        return self._http.request_with_user_action(
            method="DELETE",
            path="/fee-sponsors/{feeSponsorId}",
            path_params={"feeSponsorId": fee_sponsor_id},
            query_params=None,
            body=None,
            user_action=user_action_token,
        )

    def deactivate_fee_sponsor_init(self, fee_sponsor_id: str) -> UserActionChallengeResponse:
        """
        Initialize Deactivate Fee Sponsor.

        Creates a user action challenge for external signing.

        Args:
        fee_sponsor_id: Which Fee Sponsor you wish to deactivate.

        Returns:
            UserActionChallengeResponse: The challenge to sign externally.
        """
        path = "/fee-sponsors/{feeSponsorId}/deactivate"
        path = path.replace("{feeSponsorId}", str(fee_sponsor_id))
        payload = ""

        return BaseAuthApi.create_user_action_challenge(
            self._http,
            user_action_http_method="PUT",
            user_action_http_path=path,
            user_action_payload=payload,
        )

    def deactivate_fee_sponsor_complete(self, fee_sponsor_id: str, signed_challenge: SignUserActionChallengeRequest) -> T.DeactivateFeeSponsorResponse:
        """
        Complete Deactivate Fee Sponsor.

        Submits the signed challenge and makes the API request.

        Args:
        fee_sponsor_id: Which Fee Sponsor you wish to deactivate.
        signed_challenge: The signed challenge from external signing.

        Returns:
            T.DeactivateFeeSponsorResponse: The API response.
        """
        user_action_result = BaseAuthApi.sign_user_action_challenge(
            self._http, signed_challenge
        )
        user_action_token = user_action_result["userAction"]

        return self._http.request_with_user_action(
            method="PUT",
            path="/fee-sponsors/{feeSponsorId}/deactivate",
            path_params={"feeSponsorId": fee_sponsor_id},
            query_params=None,
            body=None,
            user_action=user_action_token,
        )

    def activate_fee_sponsor_init(self, fee_sponsor_id: str) -> UserActionChallengeResponse:
        """
        Initialize Activate Fee Sponsor.

        Creates a user action challenge for external signing.

        Args:
        fee_sponsor_id: Which Fee Sponsor you wish to activate.

        Returns:
            UserActionChallengeResponse: The challenge to sign externally.
        """
        path = "/fee-sponsors/{feeSponsorId}/activate"
        path = path.replace("{feeSponsorId}", str(fee_sponsor_id))
        payload = ""

        return BaseAuthApi.create_user_action_challenge(
            self._http,
            user_action_http_method="PUT",
            user_action_http_path=path,
            user_action_payload=payload,
        )

    def activate_fee_sponsor_complete(self, fee_sponsor_id: str, signed_challenge: SignUserActionChallengeRequest) -> T.ActivateFeeSponsorResponse:
        """
        Complete Activate Fee Sponsor.

        Submits the signed challenge and makes the API request.

        Args:
        fee_sponsor_id: Which Fee Sponsor you wish to activate.
        signed_challenge: The signed challenge from external signing.

        Returns:
            T.ActivateFeeSponsorResponse: The API response.
        """
        user_action_result = BaseAuthApi.sign_user_action_challenge(
            self._http, signed_challenge
        )
        user_action_token = user_action_result["userAction"]

        return self._http.request_with_user_action(
            method="PUT",
            path="/fee-sponsors/{feeSponsorId}/activate",
            path_params={"feeSponsorId": fee_sponsor_id},
            query_params=None,
            body=None,
            user_action=user_action_token,
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
