"""Types for the payouts domain."""

from typing import Any, Literal, NotRequired, Optional, TypedDict, Union

class ListPayoutsResponse(TypedDict, total=False):
    """listPayouts response."""

    items: list[TypedDict]
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
    asset: TypedDict
    timestamp: str
    quotes: list[TypedDict]

class CreatePayoutActionResponse(TypedDict, total=False):
    """createPayoutAction response."""

    pass
