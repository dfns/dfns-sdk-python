"""Types for the policies domain."""

from typing import Any, Literal, TypedDict, cast
from typing_extensions import NotRequired, deprecated


class GetPolicyResponse(TypedDict, total=False):
    """getPolicy response."""

    pending_change_request: NotRequired[dict[str, Any]]

class CreateApprovalDecisionRequest(TypedDict, total=False):
    """createApprovalDecision request body."""

    value: Literal["Approved", "Denied"]
    reason: NotRequired[str]

class CreateApprovalDecisionResponse(TypedDict, total=False):
    """createApprovalDecision response."""

    id: str
    initiator_id: str
    activity: dict[str, Any]
    status: Literal["Pending", "Approved", "Denied", "Expired"]
    expiration_date: NotRequired[str]
    date_created: NotRequired[str]
    date_updated: str
    date_resolved: NotRequired[str]
    policy_evaluations: list[dict[str, Any]]
    decisions: list[dict[str, Any]]

class ListPoliciesResponse(TypedDict, total=False):
    """listPolicies response."""

    items: list[dict[str, Any]]
    next_page_token: NotRequired[str]

class ListPoliciesQuery(TypedDict, total=False):
    """listPolicies query parameters."""

    limit: NotRequired[str]
    pagination_token: NotRequired[str]
    status: NotRequired[Literal["Active", "Archived"]]

class GetApprovalResponse(TypedDict, total=False):
    """getApproval response."""

    id: str
    initiator_id: str
    activity: dict[str, Any]
    status: Literal["Pending", "Approved", "Denied", "Expired"]
    expiration_date: NotRequired[str]
    date_created: NotRequired[str]
    date_updated: str
    date_resolved: NotRequired[str]
    policy_evaluations: list[dict[str, Any]]
    decisions: list[dict[str, Any]]

class ListApprovalsResponse(TypedDict, total=False):
    """listApprovals response."""

    items: list[dict[str, Any]]
    next_page_token: NotRequired[str]

class ListApprovalsQuery(TypedDict, total=False):
    """listApprovals query parameters."""

    limit: NotRequired[str]
    pagination_token: NotRequired[str]
    status: NotRequired[Literal["Pending", "Approved", "Denied", "Expired"]]
    initiator_id: NotRequired[str]
    approver_id: NotRequired[str]
