"""Delegated client for the allocations domain."""

import json
from typing import Any, Literal, Optional, TypedDict, Union

from ..._internal import HttpClient
from ...base_auth_api import (
    BaseAuthApi,
    SignUserActionChallengeRequest,
    UserActionChallengeResponse,
)
from . import types as T


class DelegatedAllocationsClient:
    """
    Delegated client for allocations operations.

    This client separates user action signing into _init() and _complete() method pairs,
    allowing external systems to handle the signing process.
    """

    def __init__(self, http_client: HttpClient):
        self._http = http_client

    def list_allocations(self, query: Optional[T.ListAllocationsQuery] = None) -> T.ListAllocationsResponse:
        """
        List Allocations.

        Args:
        query: Query parameters.

        Returns:
            T.ListAllocationsResponse: The API response.
        """
        return self._http.request(
            method="GET",
            path="/allocations",
            path_params={},
            query_params=query,
            body=None,
            requires_signature=False,
        )

    def create_allocation_init(self, body: dict[str, Any]) -> UserActionChallengeResponse:
        """
        Initialize Create Allocation.

        Creates a user action challenge for external signing.

        Args:
        body: Request body.

        Returns:
            UserActionChallengeResponse: The challenge to sign externally.
        """
        path = "/allocations"
        payload = json.dumps(body, separators=(",", ":")) if body else ""

        return BaseAuthApi.create_user_action_challenge(
            self._http,
            user_action_http_method="POST",
            user_action_http_path=path,
            user_action_payload=payload,
        )

    def create_allocation_complete(self, body: dict[str, Any], signed_challenge: SignUserActionChallengeRequest) -> T.CreateAllocationResponse:
        """
        Complete Create Allocation.

        Submits the signed challenge and makes the API request.

        Args:
        body: Request body.
        signed_challenge: The signed challenge from external signing.

        Returns:
            T.CreateAllocationResponse: The API response.
        """
        user_action_result = BaseAuthApi.sign_user_action_challenge(
            self._http, signed_challenge
        )
        user_action_token = user_action_result["userAction"]

        return self._http.request_with_user_action(
            method="POST",
            path="/allocations",
            path_params={},
            query_params=None,
            body=body,
            user_action=user_action_token,
        )

    def list_allocation_actions(self, allocation_id: str, query: Optional[T.ListAllocationActionsQuery] = None) -> T.ListAllocationActionsResponse:
        """
        List Allocation Actions.

        Retrieve the list of actions for a specific allocation.

        Args:
        allocation_id: Unique identifier for the allocation investment.
        query: Query parameters.

        Returns:
            T.ListAllocationActionsResponse: The API response.
        """
        return self._http.request(
            method="GET",
            path="/allocations/{allocationId}/actions",
            path_params={"allocationId": allocation_id},
            query_params=query,
            body=None,
            requires_signature=False,
        )

    def create_allocation_action_init(self, allocation_id: str, body: T.CreateAllocationActionRequest) -> UserActionChallengeResponse:
        """
        Initialize Create Allocation Action.

        Creates a user action challenge for external signing.

        Args:
        allocation_id: Unique identifier for the allocation investment.
        body: Request body.

        Returns:
            UserActionChallengeResponse: The challenge to sign externally.
        """
        path = "/allocations/{allocationId}/actions"
        path = path.replace("{allocationId}", str(allocation_id))
        payload = json.dumps(body, separators=(",", ":")) if body else ""

        return BaseAuthApi.create_user_action_challenge(
            self._http,
            user_action_http_method="POST",
            user_action_http_path=path,
            user_action_payload=payload,
        )

    def create_allocation_action_complete(self, allocation_id: str, body: T.CreateAllocationActionRequest, signed_challenge: SignUserActionChallengeRequest) -> T.CreateAllocationActionResponse:
        """
        Complete Create Allocation Action.

        Submits the signed challenge and makes the API request.

        Args:
        allocation_id: Unique identifier for the allocation investment.
        body: Request body.
        signed_challenge: The signed challenge from external signing.

        Returns:
            T.CreateAllocationActionResponse: The API response.
        """
        user_action_result = BaseAuthApi.sign_user_action_challenge(
            self._http, signed_challenge
        )
        user_action_token = user_action_result["userAction"]

        return self._http.request_with_user_action(
            method="POST",
            path="/allocations/{allocationId}/actions",
            path_params={"allocationId": allocation_id},
            query_params=None,
            body=body,
            user_action=user_action_token,
        )

    def get_allocation(self, allocation_id: str) -> T.GetAllocationResponse:
        """
        Get Allocation.

        Retrieve the details of a specific allocation.

        Args:
        allocation_id: Unique identifier for the allocation investment.

        Returns:
            T.GetAllocationResponse: The API response.
        """
        return self._http.request(
            method="GET",
            path="/allocations/{allocationId}",
            path_params={"allocationId": allocation_id},
            query_params=None,
            body=None,
            requires_signature=False,
        )
