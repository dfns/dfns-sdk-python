"""Delegated client for the policies domain."""

import json
from typing import Any, Literal, Optional, TypedDict, Union

from ..._internal import HttpClient
from ...base_auth_api import (
    BaseAuthApi,
    SignUserActionChallengeRequest,
    UserActionChallengeResponse,
)
from . import types as T


class DelegatedPoliciesClient:
    """
    Delegated client for policies operations.

    This client separates user action signing into _init() and _complete() method pairs,
    allowing external systems to handle the signing process.
    """

    def __init__(self, http_client: HttpClient):
        self._http = http_client

    def get_policy(self, policy_id: str) -> T.GetPolicyResponse:
        """
        Get Policy.

        Retrieve information about a specific policy.

        Args:
        policy_id: Path parameter.

        Returns:
            T.GetPolicyResponse: The API response.
        """
        return self._http.request(
            method="GET",
            path="/v2/policies/{policyId}",
            path_params={"policyId": policy_id},
            query_params=None,
            body=None,
            requires_signature=False,
        )

    def update_policy_init(self, policy_id: str, body: dict[str, Any]) -> UserActionChallengeResponse:
        """
        Initialize Update Policy.

        Creates a user action challenge for external signing.

        Args:
        policy_id: Path parameter.
        body: Request body.

        Returns:
            UserActionChallengeResponse: The challenge to sign externally.
        """
        path = "/v2/policies/{policyId}"
        path = path.replace("{policyId}", str(policy_id))
        payload = json.dumps(body, separators=(",", ":")) if body else ""

        return BaseAuthApi.create_user_action_challenge(
            self._http,
            user_action_http_method="PUT",
            user_action_http_path=path,
            user_action_payload=payload,
        )

    def update_policy_complete(self, policy_id: str, body: dict[str, Any], signed_challenge: SignUserActionChallengeRequest) -> TypedDict:
        """
        Complete Update Policy.

        Submits the signed challenge and makes the API request.

        Args:
        policy_id: Path parameter.
        body: Request body.
        signed_challenge: The signed challenge from external signing.

        Returns:
            TypedDict: The API response.
        """
        user_action_result = BaseAuthApi.sign_user_action_challenge(
            self._http, signed_challenge
        )
        user_action_token = user_action_result["userAction"]

        return self._http.request_with_user_action(
            method="PUT",
            path="/v2/policies/{policyId}",
            path_params={"policyId": policy_id},
            query_params=None,
            body=body,
            user_action=user_action_token,
        )

    def delete_policy_init(self, policy_id: str) -> UserActionChallengeResponse:
        """
        Initialize Delete Policy.

        Creates a user action challenge for external signing.

        Args:
        policy_id: Path parameter.

        Returns:
            UserActionChallengeResponse: The challenge to sign externally.
        """
        path = "/v2/policies/{policyId}"
        path = path.replace("{policyId}", str(policy_id))
        payload = ""

        return BaseAuthApi.create_user_action_challenge(
            self._http,
            user_action_http_method="DELETE",
            user_action_http_path=path,
            user_action_payload=payload,
        )

    def delete_policy_complete(self, policy_id: str, signed_challenge: SignUserActionChallengeRequest) -> TypedDict:
        """
        Complete Delete Policy.

        Submits the signed challenge and makes the API request.

        Args:
        policy_id: Path parameter.
        signed_challenge: The signed challenge from external signing.

        Returns:
            TypedDict: The API response.
        """
        user_action_result = BaseAuthApi.sign_user_action_challenge(
            self._http, signed_challenge
        )
        user_action_token = user_action_result["userAction"]

        return self._http.request_with_user_action(
            method="DELETE",
            path="/v2/policies/{policyId}",
            path_params={"policyId": policy_id},
            query_params=None,
            body=None,
            user_action=user_action_token,
        )

    def create_approval_decision_init(self, approval_id: str, body: T.CreateApprovalDecisionRequest) -> UserActionChallengeResponse:
        """
        Initialize Create Approval Decision.

        Creates a user action challenge for external signing.

        Args:
        approval_id: Path parameter.
        body: Request body.

        Returns:
            UserActionChallengeResponse: The challenge to sign externally.
        """
        path = "/v2/policy-approvals/{approvalId}/decisions"
        path = path.replace("{approvalId}", str(approval_id))
        payload = json.dumps(body, separators=(",", ":")) if body else ""

        return BaseAuthApi.create_user_action_challenge(
            self._http,
            user_action_http_method="POST",
            user_action_http_path=path,
            user_action_payload=payload,
        )

    def create_approval_decision_complete(self, approval_id: str, body: T.CreateApprovalDecisionRequest, signed_challenge: SignUserActionChallengeRequest) -> T.CreateApprovalDecisionResponse:
        """
        Complete Create Approval Decision.

        Submits the signed challenge and makes the API request.

        Args:
        approval_id: Path parameter.
        body: Request body.
        signed_challenge: The signed challenge from external signing.

        Returns:
            T.CreateApprovalDecisionResponse: The API response.
        """
        user_action_result = BaseAuthApi.sign_user_action_challenge(
            self._http, signed_challenge
        )
        user_action_token = user_action_result["userAction"]

        return self._http.request_with_user_action(
            method="POST",
            path="/v2/policy-approvals/{approvalId}/decisions",
            path_params={"approvalId": approval_id},
            query_params=None,
            body=body,
            user_action=user_action_token,
        )

    def list_policies(self, query: Optional[T.ListPoliciesQuery] = None) -> T.ListPoliciesResponse:
        """
        List Policies.

        Retrieve the list of policies on your organization.

        Args:
        query: Query parameters.

        Returns:
            T.ListPoliciesResponse: The API response.
        """
        return self._http.request(
            method="GET",
            path="/v2/policies",
            path_params={},
            query_params=query,
            body=None,
            requires_signature=False,
        )

    def create_policy_init(self, body: dict[str, Any]) -> UserActionChallengeResponse:
        """
        Initialize Create Policy.

        Creates a user action challenge for external signing.

        Args:
        body: Request body.

        Returns:
            UserActionChallengeResponse: The challenge to sign externally.
        """
        path = "/v2/policies"
        payload = json.dumps(body, separators=(",", ":")) if body else ""

        return BaseAuthApi.create_user_action_challenge(
            self._http,
            user_action_http_method="POST",
            user_action_http_path=path,
            user_action_payload=payload,
        )

    def create_policy_complete(self, body: dict[str, Any], signed_challenge: SignUserActionChallengeRequest) -> TypedDict:
        """
        Complete Create Policy.

        Submits the signed challenge and makes the API request.

        Args:
        body: Request body.
        signed_challenge: The signed challenge from external signing.

        Returns:
            TypedDict: The API response.
        """
        user_action_result = BaseAuthApi.sign_user_action_challenge(
            self._http, signed_challenge
        )
        user_action_token = user_action_result["userAction"]

        return self._http.request_with_user_action(
            method="POST",
            path="/v2/policies",
            path_params={},
            query_params=None,
            body=body,
            user_action=user_action_token,
        )

    def get_approval(self, approval_id: str) -> T.GetApprovalResponse:
        """
        Get Approval.

        Retrieve information about a specific approval request.

        Args:
        approval_id: Path parameter.

        Returns:
            T.GetApprovalResponse: The API response.
        """
        return self._http.request(
            method="GET",
            path="/v2/policy-approvals/{approvalId}",
            path_params={"approvalId": approval_id},
            query_params=None,
            body=None,
            requires_signature=False,
        )

    def list_approvals(self, query: Optional[T.ListApprovalsQuery] = None) -> T.ListApprovalsResponse:
        """
        List Approvals.

        Retrieve the list of pending approval requests.

        Args:
        query: Query parameters.

        Returns:
            T.ListApprovalsResponse: The API response.
        """
        return self._http.request(
            method="GET",
            path="/v2/policy-approvals",
            path_params={},
            query_params=query,
            body=None,
            requires_signature=False,
        )
