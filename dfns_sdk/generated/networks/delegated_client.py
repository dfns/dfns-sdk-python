"""Delegated client for the networks domain."""

import json
from typing import Any, Literal, TypedDict, cast
from typing_extensions import NotRequired, deprecated
from ..._internal import HttpClient
from ...base_auth_api import BaseAuthApi, SignUserActionChallengeRequest, UserActionChallengeResponse
from . import types as T


class DelegatedNetworksClient:
    """
    Delegated client for networks operations.

    This client separates user action signing into _init() and _complete() method pairs,
    allowing external systems to handle the signing process.
    """

    def __init__(self, http_client: HttpClient):
        self._http = http_client

    def estimate_fees(self, query: T.EstimateFeesQuery) -> dict[str, Any]:
        """
        Estimate Fees.

        Gets real-time fee details for a given network, allowing users to make decisions based on their preferences for transaction speed/priority. Three levels of priority will be displayed: `slow`, `standard`, `fast`.

        Args:
            query: Query parameters.

        Returns:
            dict[str, Any]: The API response.
        """  # noqa: E501
        response = self._http.request(
            method="GET",
            path="/networks/fees",
            path_params={},
            query_params=query,
            body=None,
            requires_signature=False,
        )
        return cast(dict[str, Any], response)

    def call_function(self, network: str, body: T.CallFunctionRequest) -> dict[str, Any]:
        """
        Call Function.

        Call a read-only function on a smart contract. In Solidity, these are functions with the state mutability set to `view`.

  <Note>
  Currently only works on EVM compatible chains.
  </Note>

        Args:
            network: Network name formatted in kebab case
            body: Request body.

        Returns:
            dict[str, Any]: The API response.
        """  # noqa: E501
        response = self._http.request(
            method="POST",
            path="/networks/{network}/call-function",
            path_params={"network": network},
            query_params=None,
            body=body,
            requires_signature=False,
        )
        return cast(dict[str, Any], response)

    def get_canton_validator(self, network: Literal["canton", "canton-devnet", "canton-testnet"], validator_id: str) -> T.GetCantonValidatorResponse:
        """
        Get Canton Validator.

        Return a configured Canton Validator in your organization.

        Args:
            network: Path parameter.
            validator_id: Path parameter.

        Returns:
            T.GetCantonValidatorResponse: The API response.
        """  # noqa: E501
        response = self._http.request(
            method="GET",
            path="/networks/{network}/validators/{validatorId}",
            path_params={"network": network, "validatorId": validator_id},
            query_params=None,
            body=None,
            requires_signature=False,
        )
        return cast(T.GetCantonValidatorResponse, response)

    def update_canton_validator_init(self, network: Literal["canton", "canton-devnet", "canton-testnet"], validator_id: str, body: T.UpdateCantonValidatorRequest) -> UserActionChallengeResponse:
        """
        Initialize Update Canton Validator.

        Creates a user action challenge for external signing.

        Args:
            network: Path parameter.
            validator_id: Path parameter.
            body: Request body.

        Returns:
            UserActionChallengeResponse: The challenge to sign externally.
        """  # noqa: E501
        path = "/networks/{network}/validators/{validatorId}"
        path = path.replace("{network}", str(network))
        path = path.replace("{validatorId}", str(validator_id))
        payload = json.dumps(body, separators=(",", ":")) if body else ""

        return BaseAuthApi.create_user_action_challenge(
            self._http,
            user_action_http_method="PUT",
            user_action_http_path=path,
            user_action_payload=payload,
        )

    def update_canton_validator_complete(self, network: Literal["canton", "canton-devnet", "canton-testnet"], validator_id: str, body: T.UpdateCantonValidatorRequest, signed_challenge: SignUserActionChallengeRequest) -> T.UpdateCantonValidatorResponse:
        """
        Complete Update Canton Validator.

        Submits the signed challenge and makes the API request.

        Args:
            network: Path parameter.
            validator_id: Path parameter.
            body: Request body.
            signed_challenge: The signed challenge from external signing.

        Returns:
            T.UpdateCantonValidatorResponse: The API response.
        """  # noqa: E501
        user_action_result = BaseAuthApi.sign_user_action_challenge(
            self._http, signed_challenge
        )
        user_action_token = user_action_result["userAction"]

        response = self._http.request_with_user_action(
            method="PUT",
            path="/networks/{network}/validators/{validatorId}",
            path_params={"network": network, "validatorId": validator_id},
            query_params=None,
            body=body,
            user_action=user_action_token,
        )
        return cast(T.UpdateCantonValidatorResponse, response)

    def delete_canton_validator_init(self, network: Literal["canton", "canton-devnet", "canton-testnet"], validator_id: str) -> UserActionChallengeResponse:
        """
        Initialize Delete Canton Validator.

        Creates a user action challenge for external signing.

        Args:
            network: Path parameter.
            validator_id: Path parameter.

        Returns:
            UserActionChallengeResponse: The challenge to sign externally.
        """  # noqa: E501
        path = "/networks/{network}/validators/{validatorId}"
        path = path.replace("{network}", str(network))
        path = path.replace("{validatorId}", str(validator_id))
        payload = ""

        return BaseAuthApi.create_user_action_challenge(
            self._http,
            user_action_http_method="DELETE",
            user_action_http_path=path,
            user_action_payload=payload,
        )

    def delete_canton_validator_complete(self, network: Literal["canton", "canton-devnet", "canton-testnet"], validator_id: str, signed_challenge: SignUserActionChallengeRequest) -> T.DeleteCantonValidatorResponse:
        """
        Complete Delete Canton Validator.

        Submits the signed challenge and makes the API request.

        Args:
            network: Path parameter.
            validator_id: Path parameter.
            signed_challenge: The signed challenge from external signing.

        Returns:
            T.DeleteCantonValidatorResponse: The API response.
        """  # noqa: E501
        user_action_result = BaseAuthApi.sign_user_action_challenge(
            self._http, signed_challenge
        )
        user_action_token = user_action_result["userAction"]

        response = self._http.request_with_user_action(
            method="DELETE",
            path="/networks/{network}/validators/{validatorId}",
            path_params={"network": network, "validatorId": validator_id},
            query_params=None,
            body=None,
            user_action=user_action_token,
        )
        return cast(T.DeleteCantonValidatorResponse, response)

    def list_canton_validators(self, network: Literal["canton", "canton-devnet", "canton-testnet"], query: T.ListCantonValidatorsQuery | None = None) -> T.ListCantonValidatorsResponse:
        """
        List Canton Validators.

        Retrieve the list of configured Canton Validators in your organization.

        Args:
            network: Path parameter.
            query: Query parameters.

        Returns:
            T.ListCantonValidatorsResponse: The API response.
        """  # noqa: E501
        response = self._http.request(
            method="GET",
            path="/networks/{network}/validators",
            path_params={"network": network},
            query_params=query,
            body=None,
            requires_signature=False,
        )
        return cast(T.ListCantonValidatorsResponse, response)

    def create_canton_validator_init(self, network: Literal["canton", "canton-devnet", "canton-testnet"], body: dict[str, Any]) -> UserActionChallengeResponse:
        """
        Initialize Create Canton Validator.

        Creates a user action challenge for external signing.

        Args:
            network: Path parameter.
            body: Request body.

        Returns:
            UserActionChallengeResponse: The challenge to sign externally.
        """  # noqa: E501
        path = "/networks/{network}/validators"
        path = path.replace("{network}", str(network))
        payload = json.dumps(body, separators=(",", ":")) if body else ""

        return BaseAuthApi.create_user_action_challenge(
            self._http,
            user_action_http_method="POST",
            user_action_http_path=path,
            user_action_payload=payload,
        )

    def create_canton_validator_complete(self, network: Literal["canton", "canton-devnet", "canton-testnet"], body: dict[str, Any], signed_challenge: SignUserActionChallengeRequest) -> T.CreateCantonValidatorResponse:
        """
        Complete Create Canton Validator.

        Submits the signed challenge and makes the API request.

        Args:
            network: Path parameter.
            body: Request body.
            signed_challenge: The signed challenge from external signing.

        Returns:
            T.CreateCantonValidatorResponse: The API response.
        """  # noqa: E501
        user_action_result = BaseAuthApi.sign_user_action_challenge(
            self._http, signed_challenge
        )
        user_action_token = user_action_result["userAction"]

        response = self._http.request_with_user_action(
            method="POST",
            path="/networks/{network}/validators",
            path_params={"network": network},
            query_params=None,
            body=body,
            user_action=user_action_token,
        )
        return cast(T.CreateCantonValidatorResponse, response)
