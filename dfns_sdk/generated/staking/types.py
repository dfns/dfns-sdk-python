"""Types for the staking domain."""

from typing import Any, Literal, NotRequired, Optional, TypedDict, Union

class ListStakesResponse(TypedDict, total=False):
    """listStakes response."""

    items: list[TypedDict]
    next_page_token: NotRequired[str]

class ListStakesQuery(TypedDict, total=False):
    """listStakes query parameters."""

    limit: NotRequired[int]
    pagination_token: NotRequired[str]

class CreateStakeRequest(TypedDict, total=False):
    """createStake request body."""

    external_id: NotRequired[str]

class CreateStakeResponse(TypedDict, total=False):
    """createStake response."""

    actions: list[TypedDict]

class ListStakeActionsResponse(TypedDict, total=False):
    """listStakeActions response."""

    items: list[TypedDict]
    next_page_token: NotRequired[str]

class ListStakeActionsQuery(TypedDict, total=False):
    """listStakeActions query parameters."""

    limit: NotRequired[int]
    pagination_token: NotRequired[str]

class CreateStakeActionRequest(TypedDict, total=False):
    """createStakeAction request body."""

    external_id: NotRequired[str]

class CreateStakeActionResponse(TypedDict, total=False):
    """createStakeAction response."""

    actions: list[TypedDict]

class GetStakesResponse(TypedDict, total=False):
    """getStakes response."""

    actions: list[TypedDict]

class GetStakesQuery(TypedDict, total=False):
    """getStakes query parameters."""

    limit: NotRequired[int]
    pagination_token: NotRequired[str]

class GetStakeRewardsResponse(TypedDict, total=False):
    """getStakeRewards response."""

    symbol: str
    balance: str
