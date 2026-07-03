"""Delegated client for the staking domain."""

import json
from typing import Any, Literal, Optional, TypedDict, Union

from ..._internal import HttpClient
from ...base_auth_api import (
    BaseAuthApi,
    SignUserActionChallengeRequest,
    UserActionChallengeResponse,
)
from . import types as T


class DelegatedStakingClient:
    """
    Delegated client for staking operations.

    This client separates user action signing into _init() and _complete() method pairs,
    allowing external systems to handle the signing process.
    """

    def __init__(self, http_client: HttpClient):
        self._http = http_client

    def list_stakes(self, query: Optional[T.ListStakesQuery] = None) -> T.ListStakesResponse:
        """
        List Stakes.

        Retrieve the list of stakes.

        Args:
        query: Query parameters.

        Returns:
            T.ListStakesResponse: The API response.
        """
        return self._http.request(
            method="GET",
            path="/staking/stakes",
            path_params={},
            query_params=query,
            body=None,
            requires_signature=False,
        )

    def create_stake_init(self, body: T.CreateStakeRequest) -> UserActionChallengeResponse:
        """
        Initialize Create Stake.

        Creates a user action challenge for external signing.

        Args:
        body: Request body.

        Returns:
            UserActionChallengeResponse: The challenge to sign externally.
        """
        path = "/staking/stakes"
        payload = json.dumps(body, separators=(",", ":")) if body else ""

        return BaseAuthApi.create_user_action_challenge(
            self._http,
            user_action_http_method="POST",
            user_action_http_path=path,
            user_action_payload=payload,
        )

    def create_stake_complete(self, body: T.CreateStakeRequest, signed_challenge: SignUserActionChallengeRequest) -> T.CreateStakeResponse:
        """
        Complete Create Stake.

        Submits the signed challenge and makes the API request.

        Args:
        body: Request body.
        signed_challenge: The signed challenge from external signing.

        Returns:
            T.CreateStakeResponse: The API response.
        """
        user_action_result = BaseAuthApi.sign_user_action_challenge(
            self._http, signed_challenge
        )
        user_action_token = user_action_result["userAction"]

        return self._http.request_with_user_action(
            method="POST",
            path="/staking/stakes",
            path_params={},
            query_params=None,
            body=body,
            user_action=user_action_token,
        )

    def list_stake_actions(self, stake_id: str, query: Optional[T.ListStakeActionsQuery] = None) -> T.ListStakeActionsResponse:
        """
        List Stake Actions.

        Retrieve the list of actions for a specific stake.

        Args:
        stake_id: Path parameter.
        query: Query parameters.

        Returns:
            T.ListStakeActionsResponse: The API response.
        """
        return self._http.request(
            method="GET",
            path="/staking/stakes/{stakeId}/actions",
            path_params={"stakeId": stake_id},
            query_params=query,
            body=None,
            requires_signature=False,
        )

    def create_stake_action_init(self, stake_id: str, body: T.CreateStakeActionRequest) -> UserActionChallengeResponse:
        """
        Initialize Create Stake Action.

        Creates a user action challenge for external signing.

        Args:
        stake_id: Path parameter.
        body: Request body.

        Returns:
            UserActionChallengeResponse: The challenge to sign externally.
        """
        path = "/staking/stakes/{stakeId}/actions"
        path = path.replace("{stakeId}", str(stake_id))
        payload = json.dumps(body, separators=(",", ":")) if body else ""

        return BaseAuthApi.create_user_action_challenge(
            self._http,
            user_action_http_method="POST",
            user_action_http_path=path,
            user_action_payload=payload,
        )

    def create_stake_action_complete(self, stake_id: str, body: T.CreateStakeActionRequest, signed_challenge: SignUserActionChallengeRequest) -> T.CreateStakeActionResponse:
        """
        Complete Create Stake Action.

        Submits the signed challenge and makes the API request.

        Args:
        stake_id: Path parameter.
        body: Request body.
        signed_challenge: The signed challenge from external signing.

        Returns:
            T.CreateStakeActionResponse: The API response.
        """
        user_action_result = BaseAuthApi.sign_user_action_challenge(
            self._http, signed_challenge
        )
        user_action_token = user_action_result["userAction"]

        return self._http.request_with_user_action(
            method="POST",
            path="/staking/stakes/{stakeId}/actions",
            path_params={"stakeId": stake_id},
            query_params=None,
            body=body,
            user_action=user_action_token,
        )

    def get_stakes(self, stake_id: str, query: Optional[T.GetStakesQuery] = None) -> T.GetStakesResponse:
        """
        Get Stakes.

        Retrieve the details of a specific stake.

        Args:
        stake_id: Path parameter.
        query: Query parameters.

        Returns:
            T.GetStakesResponse: The API response.
        """
        return self._http.request(
            method="GET",
            path="/staking/stakes/{stakeId}",
            path_params={"stakeId": stake_id},
            query_params=query,
            body=None,
            requires_signature=False,
        )

    def get_stake_rewards(self, stake_id: str) -> T.GetStakeRewardsResponse:
        """
        Get Stake Rewards.

        Retrieves the rewards linked to a specific stake.

        Args:
        stake_id: Path parameter.

        Returns:
            T.GetStakeRewardsResponse: The API response.
        """
        return self._http.request(
            method="GET",
            path="/staking/stakes/{stakeId}/rewards",
            path_params={"stakeId": stake_id},
            query_params=None,
            body=None,
            requires_signature=False,
        )
