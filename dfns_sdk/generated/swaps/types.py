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

class CreateSwapRequest(TypedDict, total=False):
    """createSwap request body."""

    quote_id: str
    reference: NotRequired[str]
    provider: Literal["UniswapX", "UniswapClassic"]
    wallet_id: str
    target_wallet_id: NotRequired[str]
    slippage_bps: float
    source_asset: TypedDict
    target_asset: TypedDict

class CreateSwapResponse(TypedDict, total=False):
    """createSwap response."""

    id: str
    quote_id: str
    reference: Any
    wallet_id: str
    target_wallet_id: str
    status: Literal["PendingPolicyApproval", "InProgress", "Completed", "Failed", "Rejected"]
    provider: Literal["UniswapX", "UniswapClassic"]
    quoted_source_asset: TypedDict
    quoted_target_asset: TypedDict
    slippage_bps: float
    date_created: str
    request_body: TypedDict
    requester: TypedDict

class RequestSwapQuoteRequest(TypedDict, total=False):
    """requestSwapQuote request body."""

    provider: Literal["UniswapX", "UniswapClassic"]
    wallet_id: str
    target_wallet_id: NotRequired[str]
    source_asset: TypedDict
    target_asset: TypedDict
    slippage_bps: float

class RequestSwapQuoteResponse(TypedDict, total=False):
    """requestSwapQuote response."""

    id: str
    wallet_id: str
    target_wallet_id: NotRequired[str]
    provider: Literal["UniswapX", "UniswapClassic"]
    source_asset: TypedDict
    target_asset: TypedDict
    slippage_bps: float
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
    provider: Literal["UniswapX", "UniswapClassic"]
    quoted_source_asset: TypedDict
    quoted_target_asset: TypedDict
    slippage_bps: float
    date_created: str
    request_body: TypedDict
    requester: TypedDict

class GetSwapQuoteResponse(TypedDict, total=False):
    """getSwapQuote response."""

    id: str
    wallet_id: str
    target_wallet_id: NotRequired[str]
    provider: Literal["UniswapX", "UniswapClassic"]
    source_asset: TypedDict
    target_asset: TypedDict
    slippage_bps: float
    date_created: str
    request_body: TypedDict
    requester: TypedDict
