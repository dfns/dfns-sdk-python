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
    provider: NotRequired[list[Literal["CircleMint"]]]


class GetPayinRecipientResponse(TypedDict, total=False):
    """getPayinRecipient response."""

    provider: Literal["CircleMint"]
    wallet_id: str
    currency: Literal["USD", "EUR"]
    status: Literal["NotRegistered", "PendingVerification", "Active"]
    recipient_address_id: NotRequired[str]


class GetPayinRecipientQuery(TypedDict, total=False):
    """getPayinRecipient query parameters."""

    provider: Literal["CircleMint"]
    wallet_id: str
    currency: Literal["USD", "EUR"]


class RegisterPayinRecipientResponse(TypedDict, total=False):
    """registerPayinRecipient response."""

    provider: Literal["CircleMint"]
    wallet_id: str
    currency: Literal["USD", "EUR"]
    status: Literal["NotRegistered", "PendingVerification", "Active"]
    recipient_address_id: NotRequired[str]


class ListPayinBalancesResponse(TypedDict, total=False):
    """listPayinBalances response."""

    items: list[dict[str, Any]]


class ListPayinBalancesQuery(TypedDict, total=False):
    """listPayinBalances query parameters."""

    provider: Literal["CircleMint"]
