"""Client for the policies domain."""

from typing import Any, Literal, Optional, TypedDict, Union

from ..._internal import HttpClient
from . import types as T


class PoliciesClient:
    """Client for policies operations."""

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

    def update_policy(self, policy_id: str, body: dict[str, Any]) -> TypedDict:
        """
        Update Policy.

        Update an existing policy.

        Args:
        policy_id: Path parameter.
        body: Request body.

        Returns:
            TypedDict: The API response.
        """
        return self._http.request(
            method="PUT",
            path="/v2/policies/{policyId}",
            path_params={"policyId": policy_id},
            query_params=None,
            body=body,
            requires_signature=True,
        )

    def delete_policy(self, policy_id: str) -> TypedDict:
        """
        Delete Policy.

        Delete an existing policy.

        Args:
        policy_id: Path parameter.

        Returns:
            TypedDict: The API response.
        """
        return self._http.request(
            method="DELETE",
            path="/v2/policies/{policyId}",
            path_params={"policyId": policy_id},
            query_params=None,
            body=None,
            requires_signature=True,
        )

    def create_approval_decision(self, approval_id: str, body: T.CreateApprovalDecisionRequest) -> T.CreateApprovalDecisionResponse:
        """
        Create Approval Decision.

        Approve or Reject an Approval request.

        Args:
        approval_id: Path parameter.
        body: Request body.

        Returns:
            T.CreateApprovalDecisionResponse: The API response.
        """
        return self._http.request(
            method="POST",
            path="/v2/policy-approvals/{approvalId}/decisions",
            path_params={"approvalId": approval_id},
            query_params=None,
            body=body,
            requires_signature=True,
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

    def create_policy(self, body: dict[str, Any]) -> TypedDict:
        """
        Create Policy.

        Setup a new Policy for your organization.
  
  Every policy requires a rule to be specified. Upon policy evaluation, the configuration specified in the rule will be used to determine whether the policy should trigger or not for a given activity.
  
  By exposing controls on permissions and policies, Dfns enables the specification of an admin quorum to approve sensitive actions which could change system governance.   Note Dfns does not expose a separate "admin quorum" concept like some of our competitors - we simply enable this use case as another configuration of the policy engine itself.   This was chosen to promote flexibility as not every customer will have the same requirements around creating and managing admin quorums.

        Args:
        body: Request body.

        Returns:
            TypedDict: The API response.
        """
        return self._http.request(
            method="POST",
            path="/v2/policies",
            path_params={},
            query_params=None,
            body=body,
            requires_signature=True,
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
