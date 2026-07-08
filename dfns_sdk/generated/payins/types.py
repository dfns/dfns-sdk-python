"""Types for the payins domain."""

from typing import Literal, TypedDict

from typing_extensions import NotRequired


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
