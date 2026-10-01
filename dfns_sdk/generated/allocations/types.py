"""Types for the allocations domain."""

from typing import Any, Literal, TypedDict

from typing_extensions import NotRequired


class CreateAllocationQuoteRequest(TypedDict, total=False):
    """createAllocationQuote request body."""

    wallet_id: str
    protocol: Literal["0fns"]
    kind: Literal["Deposit", "Withdraw"]
    source_asset: dict[str, Any]
    target_asset: dict[str, Any]


class CreateAllocationQuoteResponse(TypedDict, total=False):
    """createAllocationQuote response."""

    wallet_id: str
    protocol: Literal[
        "0fns",
        "SkySusds",
        "GauntletUsdcPrime",
        "SteakhouseUsdt",
        "GauntletUsdcPrimeBase",
        "SteakhouseUsdcBase",
        "SentoraPyusdMain",
    ]
    kind: Literal["Deposit", "Withdraw"]
    source_asset: dict[str, Any]
    target_asset: dict[str, Any]
    est_fill_time: int
    date_created: str


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
    protocol: Literal[
        "0fns",
        "SkySusds",
        "GauntletUsdcPrime",
        "SteakhouseUsdt",
        "GauntletUsdcPrimeBase",
        "SteakhouseUsdcBase",
        "SentoraPyusdMain",
    ]
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
    protocol: Literal[
        "0fns",
        "SkySusds",
        "GauntletUsdcPrime",
        "SteakhouseUsdt",
        "GauntletUsdcPrimeBase",
        "SteakhouseUsdcBase",
        "SentoraPyusdMain",
    ]
    provider: NotRequired[Literal["M0", "Yield.xyz"]]
    amount: dict[str, Any]
    rewards: dict[str, Any]
    date_created: str
    actions: list[dict[str, Any]]


class GetAllocationResponse(TypedDict, total=False):
    """getAllocation response."""

    id: str
    wallet_id: str
    protocol: Literal[
        "0fns",
        "SkySusds",
        "GauntletUsdcPrime",
        "SteakhouseUsdt",
        "GauntletUsdcPrimeBase",
        "SteakhouseUsdcBase",
        "SentoraPyusdMain",
    ]
    provider: NotRequired[Literal["M0", "Yield.xyz"]]
    amount: dict[str, Any]
    rewards: dict[str, Any]
    date_created: str
    actions: list[dict[str, Any]]


class GetAllocationsInfoResponse(TypedDict, total=False):
    """getAllocationsInfo response."""

    ofns: NotRequired[dict[str, Any]]
    sky_susds: NotRequired[dict[str, Any]]
    gauntlet_usdc_prime: NotRequired[dict[str, Any]]
    steakhouse_usdt: NotRequired[dict[str, Any]]
    gauntlet_usdc_prime_base: NotRequired[dict[str, Any]]
    steakhouse_usdc_base: NotRequired[dict[str, Any]]
    sentora_pyusd_main: NotRequired[dict[str, Any]]


class Cancel0fnsOrderPlacementRequest(TypedDict, total=False):
    """cancel0fnsOrderPlacement request body."""

    allocation_action_id: str
    external_id: NotRequired[str]
    fee_sponsor_id: NotRequired[str]


class Cancel0fnsOrderPlacementResponse(TypedDict, total=False):
    """cancel0fnsOrderPlacement response."""

    transaction_id: str
