"""Types for the fee_sponsors domain."""

from typing import Any, Literal, NotRequired, Optional, TypedDict, Union

class ListFeeSponsorsResponse(TypedDict, total=False):
    """listFeeSponsors response."""

    items: list[TypedDict]
    next_page_token: NotRequired[str]

class ListFeeSponsorsQuery(TypedDict, total=False):
    """listFeeSponsors query parameters."""

    limit: NotRequired[str]
    pagination_token: NotRequired[str]

class CreateFeeSponsorRequest(TypedDict, total=False):
    """createFeeSponsor request body."""

    name: NotRequired[str]
    wallet_id: str
    allow_end_user: NotRequired[bool]

class CreateFeeSponsorResponse(TypedDict, total=False):
    """createFeeSponsor response."""

    id: str
    name: NotRequired[str]
    wallet_id: str
    network: TypedDict
    status: Literal["Active", "Deactivated", "Archived"]
    date_created: str
    allow_end_user: NotRequired[bool]

class GetFeeSponsorResponse(TypedDict, total=False):
    """getFeeSponsor response."""

    id: str
    name: NotRequired[str]
    wallet_id: str
    network: TypedDict
    status: Literal["Active", "Deactivated", "Archived"]
    date_created: str
    allow_end_user: NotRequired[bool]

class DeleteFeeSponsorResponse(TypedDict, total=False):
    """deleteFeeSponsor response."""

    id: str
    name: NotRequired[str]
    wallet_id: str
    network: TypedDict
    status: Literal["Active", "Deactivated", "Archived"]
    date_created: str
    allow_end_user: NotRequired[bool]

class DeactivateFeeSponsorResponse(TypedDict, total=False):
    """deactivateFeeSponsor response."""

    id: str
    name: NotRequired[str]
    wallet_id: str
    network: TypedDict
    status: Literal["Active", "Deactivated", "Archived"]
    date_created: str
    allow_end_user: NotRequired[bool]

class ActivateFeeSponsorResponse(TypedDict, total=False):
    """activateFeeSponsor response."""

    id: str
    name: NotRequired[str]
    wallet_id: str
    network: TypedDict
    status: Literal["Active", "Deactivated", "Archived"]
    date_created: str
    allow_end_user: NotRequired[bool]

class ListSponsoredFeesResponse(TypedDict, total=False):
    """listSponsoredFees response."""

    items: list[TypedDict]
    next_page_token: NotRequired[str]

class ListSponsoredFeesQuery(TypedDict, total=False):
    """listSponsoredFees query parameters."""

    limit: NotRequired[str]
    pagination_token: NotRequired[str]
