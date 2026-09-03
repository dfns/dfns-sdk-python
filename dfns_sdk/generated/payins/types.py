"""Types for the payins domain."""

from typing import Any, Literal, TypedDict

from typing_extensions import NotRequired


class ListPayinsResponse(TypedDict, total=False):
    """listPayins response."""

    items: list[dict[str, Any]]
    next_page_token: NotRequired[str]


class ListPayinsQuery(TypedDict, total=False):
    """listPayins query parameters."""

    limit: NotRequired[int]
    pagination_token: NotRequired[str]
    wallet_id: NotRequired[str]
    status: NotRequired[list[Literal["Processing", "Completed", "Failed"]]]
    provider: NotRequired[list[Literal["CircleMint", "Borderless"]]]


class RequestPayinQuoteResponse(TypedDict, total=False):
    """requestPayinQuote response."""

    provider: Literal["CircleMint", "Borderless"]
    currency: Literal["USD", "EUR"]
    network: dict[str, Any]
    tid: str
    timestamp: str
    quotes: list[dict[str, Any]]


class GetPayinRecipientResponse(TypedDict, total=False):
    """getPayinRecipient response."""

    provider: Literal["CircleMint", "Borderless"]
    wallet_id: str
    currency: Literal["USD", "EUR"]
    status: Literal["NotRegistered", "PendingVerification", "Active"]
    recipient_address_id: NotRequired[str]


class GetPayinRecipientQuery(TypedDict, total=False):
    """getPayinRecipient query parameters."""

    provider: Literal["CircleMint", "Borderless"]
    wallet_id: str
    currency: Literal["USD", "EUR"]


class RegisterPayinRecipientResponse(TypedDict, total=False):
    """registerPayinRecipient response."""

    provider: Literal["CircleMint", "Borderless"]
    wallet_id: str
    currency: Literal["USD", "EUR"]
    status: Literal["NotRegistered", "PendingVerification", "Active"]
    recipient_address_id: NotRequired[str]


class ListPayinAccountsResponse(TypedDict, total=False):
    """listPayinAccounts response."""

    items: list[dict[str, Any]]


class ListPayinAccountsQuery(TypedDict, total=False):
    """listPayinAccounts query parameters."""

    provider: Literal["CircleMint", "Borderless"]


class ListPayinBalancesResponse(TypedDict, total=False):
    """listPayinBalances response."""

    items: list[dict[str, Any]]


class ListPayinBalancesQuery(TypedDict, total=False):
    """listPayinBalances query parameters."""

    provider: Literal["CircleMint", "Borderless"]


class ListPayinOptionsResponse(TypedDict, total=False):
    """listPayinOptions response."""

    assets: list[str]
    currencies: list[dict[str, Any]]


class ListPayinOptionsQuery(TypedDict, total=False):
    """listPayinOptions query parameters."""

    provider: Literal["CircleMint", "Borderless"]


class RegisterPayinAccountAssetResponse(TypedDict, total=False):
    """registerPayinAccountAsset response."""

    account_id: str
    name: NotRequired[str]
    assets: list[dict[str, Any]]
