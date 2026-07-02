"""Client for the staking domain."""

from typing import cast

from ..._internal import HttpClient
from . import types as T


class StakingClient:
    """Client for staking operations."""

    def __init__(self, http_client: HttpClient):
        self._http = http_client

    def list_stakes(self, query: T.ListStakesQuery | None = None) -> T.ListStakesResponse:
        """
        List Stakes.

        Retrieve the list of stakes.

        Args:
            query: Query parameters.

        Returns:
            T.ListStakesResponse: The API response.
        """  # noqa: E501
        response = self._http.request(
            method="GET",
            path="/staking/stakes",
            path_params={},
            query_params=query,
            body=None,
            requires_signature=False,
        )
        return cast(T.ListStakesResponse, response)

    def create_stake(self, body: T.CreateStakeRequest) -> T.CreateStakeResponse:
        """
        Create Stake.

        Create a new stake.

        Args:
            body: Request body.

        Returns:
            T.CreateStakeResponse: The API response.
        """  # noqa: E501
        response = self._http.request(
            method="POST",
            path="/staking/stakes",
            path_params={},
            query_params=None,
            body=body,
            requires_signature=True,
        )
        return cast(T.CreateStakeResponse, response)

    def list_stake_actions(
        self, stake_id: str, query: T.ListStakeActionsQuery | None = None
    ) -> T.ListStakeActionsResponse:
        """
        List Stake Actions.

        Retrieve the list of actions for a specific stake.

        Args:
            stake_id: Path parameter.
            query: Query parameters.

        Returns:
            T.ListStakeActionsResponse: The API response.
        """  # noqa: E501
        response = self._http.request(
            method="GET",
            path="/staking/stakes/{stakeId}/actions",
            path_params={"stakeId": stake_id},
            query_params=query,
            body=None,
            requires_signature=False,
        )
        return cast(T.ListStakeActionsResponse, response)

    def create_stake_action(self, stake_id: str, body: T.CreateStakeActionRequest) -> T.CreateStakeActionResponse:
        """
        Create Stake Action.

        Create a new action for an existing stake.

        Args:
            stake_id: Path parameter.
            body: Request body.

        Returns:
            T.CreateStakeActionResponse: The API response.
        """  # noqa: E501
        response = self._http.request(
            method="POST",
            path="/staking/stakes/{stakeId}/actions",
            path_params={"stakeId": stake_id},
            query_params=None,
            body=body,
            requires_signature=True,
        )
        return cast(T.CreateStakeActionResponse, response)

    def get_stakes(self, stake_id: str, query: T.GetStakesQuery | None = None) -> T.GetStakesResponse:
        """
        Get Stakes.

        Retrieve the details of a specific stake.

        Args:
            stake_id: Path parameter.
            query: Query parameters.

        Returns:
            T.GetStakesResponse: The API response.
        """  # noqa: E501
        response = self._http.request(
            method="GET",
            path="/staking/stakes/{stakeId}",
            path_params={"stakeId": stake_id},
            query_params=query,
            body=None,
            requires_signature=False,
        )
        return cast(T.GetStakesResponse, response)

    def get_stake_rewards(self, stake_id: str) -> T.GetStakeRewardsResponse:
        """
        Get Stake Rewards.

        Retrieves the rewards linked to a specific stake.

        Args:
            stake_id: Path parameter.

        Returns:
            T.GetStakeRewardsResponse: The API response.
        """  # noqa: E501
        response = self._http.request(
            method="GET",
            path="/staking/stakes/{stakeId}/rewards",
            path_params={"stakeId": stake_id},
            query_params=None,
            body=None,
            requires_signature=False,
        )
        return cast(T.GetStakeRewardsResponse, response)
