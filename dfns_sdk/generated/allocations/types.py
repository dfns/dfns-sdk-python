"""Types for the allocations domain."""

from typing import Any, Literal, NotRequired, Optional, TypedDict, Union

class ListAllocationsResponse(TypedDict, total=False):
    """listAllocations response."""

    items: list[TypedDict]
    next_page_token: NotRequired[str]

class ListAllocationsQuery(TypedDict, total=False):
    """listAllocations query parameters."""

    limit: NotRequired[int]
    pagination_token: NotRequired[str]

class CreateAllocationResponse(TypedDict, total=False):
    """createAllocation response."""

    id: str
    wallet_id: str
    protocol: Literal["0fns"]
    amount: TypedDict
    rewards: TypedDict
    date_created: str
    actions: list[TypedDict]

class ListAllocationActionsResponse(TypedDict, total=False):
    """listAllocationActions response."""

    items: list[TypedDict]
    next_page_token: NotRequired[str]

class ListAllocationActionsQuery(TypedDict, total=False):
    """listAllocationActions query parameters."""

    limit: NotRequired[int]
    pagination_token: NotRequired[str]

class CreateAllocationActionRequest(TypedDict, total=False):
    """createAllocationAction request body."""

    kind: Literal["Deposit", "Withdraw"]
    external_id: NotRequired[str]
    source_asset: TypedDict
    target_asset: TypedDict
    slippage_bps: float

class CreateAllocationActionResponse(TypedDict, total=False):
    """createAllocationAction response."""

    id: str
    wallet_id: str
    protocol: Literal["0fns"]
    amount: TypedDict
    rewards: TypedDict
    date_created: str
    actions: list[TypedDict]

class GetAllocationResponse(TypedDict, total=False):
    """getAllocation response."""

    id: str
    wallet_id: str
    protocol: Literal["0fns"]
    amount: TypedDict
    rewards: TypedDict
    date_created: str
    actions: list[TypedDict]
