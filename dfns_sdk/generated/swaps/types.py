"""Types for the swaps domain."""

from typing import Any, Literal, NotRequired, Optional, TypedDict, Union

class ListSwapsResponse(TypedDict, total=False):
    """listSwaps response."""

    items: list[TypedDict]
    next_page_token: NotRequired[str]

class ListSwapsQuery(TypedDict, total=False):
    """listSwaps query parameters."""

    limit: NotRequired[int]
    pagination_token: NotRequired[str]

class CreateSwapResponse(TypedDict, total=False):
    """createSwap response."""

    id: str
    quote_id: str
    reference: Any
    wallet_id: str
    target_wallet_id: str
    status: Literal["PendingPolicyApproval", "InProgress", "Completed", "Failed", "Rejected"]
    provider: Literal["UniswapX", "UniswapClassic", "CircleCctp"]
    quoted_source_asset: TypedDict
    quoted_target_asset: TypedDict
    slippage_bps: float
    date_created: str
    request_body: TypedDict
    requester: TypedDict
    failure_reason: NotRequired[str]
    protocol_status: NotRequired[str]

class RequestSwapQuoteResponse(TypedDict, total=False):
    """requestSwapQuote response."""

    id: str
    wallet_id: str
    target_wallet_id: NotRequired[str]
    provider: Literal["UniswapX", "UniswapClassic", "CircleCctp"]
    source_asset: TypedDict
    target_asset: TypedDict
    slippage_bps: int
    fee: NotRequired[str]
    date_created: str
    request_body: TypedDict
    requester: TypedDict

class GetSwapResponse(TypedDict, total=False):
    """getSwap response."""

    id: str
    quote_id: str
    reference: Any
    wallet_id: str
    target_wallet_id: str
    status: Literal["PendingPolicyApproval", "InProgress", "Completed", "Failed", "Rejected"]
    provider: Literal["UniswapX", "UniswapClassic", "CircleCctp"]
    quoted_source_asset: TypedDict
    quoted_target_asset: TypedDict
    slippage_bps: float
    date_created: str
    request_body: TypedDict
    requester: TypedDict
    failure_reason: NotRequired[str]
    protocol_status: NotRequired[str]

class GetSwapQuoteResponse(TypedDict, total=False):
    """getSwapQuote response."""

    id: str
    wallet_id: str
    target_wallet_id: NotRequired[str]
    provider: Literal["UniswapX", "UniswapClassic", "CircleCctp"]
    source_asset: TypedDict
    target_asset: TypedDict
    slippage_bps: int
    fee: NotRequired[str]
    date_created: str
    request_body: TypedDict
    requester: TypedDict
