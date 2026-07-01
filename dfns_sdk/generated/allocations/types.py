"""Types for the allocations domain."""

from typing import Any, Literal, TypedDict, cast
from typing_extensions import NotRequired, deprecated


class ListAllocationsResponse(TypedDict, total=False):
    """listAllocations response."""

    items: list[dict[str, Any]]
    next_page_token: NotRequired[str]

class ListAllocationsQuery(TypedDict, total=False):
    """listAllocations query parameters."""

    limit: NotRequired[int]
    pagination_token: NotRequired[str]

class CreateAllocationResponse(TypedDict, total=False):
    """createAllocation response."""

    id: str
    wallet_id: str
    protocol: Literal["0fns", "SkySusds", "GauntletUsdcPrime", "SteakhouseUsdt", "GauntletUsdcPrimeBase", "SteakhouseUsdcBase", "SentoraPyusdMain"]
    provider: NotRequired[Literal["M0", "Yield.xyz"]]
    amount: dict[str, Any]
    rewards: dict[str, Any]
    date_created: str
    actions: list[dict[str, Any]]

class ListAllocationActionsResponse(TypedDict, total=False):
    """listAllocationActions response."""

    items: list[dict[str, Any]]
    next_page_token: NotRequired[str]

class ListAllocationActionsQuery(TypedDict, total=False):
    """listAllocationActions query parameters."""

    limit: NotRequired[int]
    pagination_token: NotRequired[str]

class CreateAllocationActionResponse(TypedDict, total=False):
    """createAllocationAction response."""

    id: str
    wallet_id: str
    protocol: Literal["0fns", "SkySusds", "GauntletUsdcPrime", "SteakhouseUsdt", "GauntletUsdcPrimeBase", "SteakhouseUsdcBase", "SentoraPyusdMain"]
    provider: NotRequired[Literal["M0", "Yield.xyz"]]
    amount: dict[str, Any]
    rewards: dict[str, Any]
    date_created: str
    actions: list[dict[str, Any]]

class GetAllocationResponse(TypedDict, total=False):
    """getAllocation response."""

    id: str
    wallet_id: str
    protocol: Literal["0fns", "SkySusds", "GauntletUsdcPrime", "SteakhouseUsdt", "GauntletUsdcPrimeBase", "SteakhouseUsdcBase", "SentoraPyusdMain"]
    provider: NotRequired[Literal["M0", "Yield.xyz"]]
    amount: dict[str, Any]
    rewards: dict[str, Any]
    date_created: str
    actions: list[dict[str, Any]]
