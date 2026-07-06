"""Client for the allocations domain."""

from typing import Any, Literal, Optional, TypedDict, Union

from ..._internal import HttpClient
from . import types as T


class AllocationsClient:
    """Client for allocations operations."""

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

    def create_allocation(self, body: dict[str, Any]) -> T.CreateAllocationResponse:
        """
        Create Allocation.

        Create a new allocation.

        Args:
        body: Request body.

        Returns:
            T.CreateAllocationResponse: The API response.
        """
        return self._http.request(
            method="POST",
            path="/allocations",
            path_params={},
            query_params=None,
            body=body,
            requires_signature=True,
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

    def create_allocation_action(self, allocation_id: str, body: T.CreateAllocationActionRequest) -> T.CreateAllocationActionResponse:
        """
        Create Allocation Action.

        Create a new action for an existing allocation.

        Args:
        allocation_id: Unique identifier for the allocation investment.
        body: Request body.

        Returns:
            T.CreateAllocationActionResponse: The API response.
        """
        return self._http.request(
            method="POST",
            path="/allocations/{allocationId}/actions",
            path_params={"allocationId": allocation_id},
            query_params=None,
            body=body,
            requires_signature=True,
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
