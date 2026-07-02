"""Types for the payouts domain."""

from typing import Any, Literal, TypedDict

from typing_extensions import NotRequired


class ListPayoutsResponse(TypedDict, total=False):
    """listPayouts response."""

    items: list[dict[str, Any]]
    next_page_token: NotRequired[str]


class ListPayoutsQuery(TypedDict, total=False):
    """listPayouts query parameters."""

    limit: NotRequired[int]
    pagination_token: NotRequired[str]
    wallet_id: NotRequired[str]
    status: NotRequired[list[Literal["Processing", "Completed", "Failed", "Rejected", "Expired", "Canceled"]]]


class RequestPayoutQuoteResponse(TypedDict, total=False):
    """requestPayoutQuote response."""

    provider: Literal["Borderless"]
    asset: dict[str, Any]
    timestamp: str
    quotes: list[dict[str, Any]]


class CreatePayoutActionResponse(TypedDict, total=False):
    """createPayoutAction response."""

    pass
