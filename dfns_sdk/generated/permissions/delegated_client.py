"""Delegated client for the permissions domain."""

import json
from typing import Any, Literal, Optional, TypedDict, Union

from ..._internal import HttpClient
from ...base_auth_api import (
    BaseAuthApi,
    SignUserActionChallengeRequest,
    UserActionChallengeResponse,
)
from . import types as T


class DelegatedPermissionsClient:
    """
    Delegated client for permissions operations.

    This client separates user action signing into _init() and _complete() method pairs,
    allowing external systems to handle the signing process.
    """

    def __init__(self, http_client: HttpClient):
        self._http = http_client

    def list_permission_assignments(self, permission_id: str) -> T.ListPermissionAssignmentsResponse:
        """
        List Permission Assignments.

        Retrieves a list of permission assignments (success) or gives a reason why it's not possible (failure).

        Args:
        permission_id: Path parameter.

        Returns:
            T.ListPermissionAssignmentsResponse: The API response.
        """
        return self._http.request(
            method="GET",
            path="/permissions/{permissionId}/assignments",
            path_params={"permissionId": permission_id},
            query_params=None,
            body=None,
            requires_signature=False,
        )

    def assign_permission_init(self, permission_id: str, body: T.AssignPermissionRequest) -> UserActionChallengeResponse:
        """
        Initialize Assign Permission.

        Creates a user action challenge for external signing.

        Args:
        permission_id: Path parameter.
        body: Request body.

        Returns:
            UserActionChallengeResponse: The challenge to sign externally.
        """
        path = "/permissions/{permissionId}/assignments"
        path = path.replace("{permissionId}", str(permission_id))
        payload = json.dumps(body, separators=(",", ":")) if body else ""

        return BaseAuthApi.create_user_action_challenge(
            self._http,
            user_action_http_method="POST",
            user_action_http_path=path,
            user_action_payload=payload,
        )

    def assign_permission_complete(self, permission_id: str, body: T.AssignPermissionRequest, signed_challenge: SignUserActionChallengeRequest) -> T.AssignPermissionResponse:
        """
        Complete Assign Permission.

        Submits the signed challenge and makes the API request.

        Args:
        permission_id: Path parameter.
        body: Request body.
        signed_challenge: The signed challenge from external signing.

        Returns:
            T.AssignPermissionResponse: The API response.
        """
        user_action_result = BaseAuthApi.sign_user_action_challenge(
            self._http, signed_challenge
        )
        user_action_token = user_action_result["userAction"]

        return self._http.request_with_user_action(
            method="POST",
            path="/permissions/{permissionId}/assignments",
            path_params={"permissionId": permission_id},
            query_params=None,
            body=body,
            user_action=user_action_token,
        )

    def revoke_permission_init(self, permission_id: str, assignment_id: str, query: Optional[T.RevokePermissionQuery] = None) -> UserActionChallengeResponse:
        """
        Initialize Revoke Permission.

        Creates a user action challenge for external signing.

        Args:
        permission_id: Path parameter.
        assignment_id: Path parameter.
        query: Query parameters.

        Returns:
            UserActionChallengeResponse: The challenge to sign externally.
        """
        path = "/permissions/{permissionId}/assignments/{assignmentId}"
        path = path.replace("{permissionId}", str(permission_id))
        path = path.replace("{assignmentId}", str(assignment_id))
        payload = ""

        return BaseAuthApi.create_user_action_challenge(
            self._http,
            user_action_http_method="DELETE",
            user_action_http_path=path,
            user_action_payload=payload,
        )

    def revoke_permission_complete(self, permission_id: str, assignment_id: str, signed_challenge: SignUserActionChallengeRequest, query: Optional[T.RevokePermissionQuery] = None) -> None:
        """
        Complete Revoke Permission.

        Submits the signed challenge and makes the API request.

        Args:
        permission_id: Path parameter.
        assignment_id: Path parameter.
        signed_challenge: The signed challenge from external signing.
        query: Query parameters.
        """
        user_action_result = BaseAuthApi.sign_user_action_challenge(
            self._http, signed_challenge
        )
        user_action_token = user_action_result["userAction"]

        return self._http.request_with_user_action(
            method="DELETE",
            path="/permissions/{permissionId}/assignments/{assignmentId}",
            path_params={"permissionId": permission_id, "assignmentId": assignment_id},
            query_params=query,
            body=None,
            user_action=user_action_token,
        )

    def delete_permission_init(self, permission_id: str, body: T.DeletePermissionRequest) -> UserActionChallengeResponse:
        """
        Initialize Delete Permission.

        Creates a user action challenge for external signing.

        Args:
        permission_id: Path parameter.
        body: Request body.

        Returns:
            UserActionChallengeResponse: The challenge to sign externally.
        """
        path = "/permissions/{permissionId}/archive"
        path = path.replace("{permissionId}", str(permission_id))
        payload = json.dumps(body, separators=(",", ":")) if body else ""

        return BaseAuthApi.create_user_action_challenge(
            self._http,
            user_action_http_method="PUT",
            user_action_http_path=path,
            user_action_payload=payload,
        )

    def delete_permission_complete(self, permission_id: str, body: T.DeletePermissionRequest, signed_challenge: SignUserActionChallengeRequest) -> T.DeletePermissionResponse:
        """
        Complete Delete Permission.

        Submits the signed challenge and makes the API request.

        Args:
        permission_id: Path parameter.
        body: Request body.
        signed_challenge: The signed challenge from external signing.

        Returns:
            T.DeletePermissionResponse: The API response.
        """
        user_action_result = BaseAuthApi.sign_user_action_challenge(
            self._http, signed_challenge
        )
        user_action_token = user_action_result["userAction"]

        return self._http.request_with_user_action(
            method="PUT",
            path="/permissions/{permissionId}/archive",
            path_params={"permissionId": permission_id},
            query_params=None,
            body=body,
            user_action=user_action_token,
        )

    def list_permissions(self, query: Optional[T.ListPermissionsQuery] = None) -> T.ListPermissionsResponse:
        """
        List Permissions.

        Retrieves a list of permissions (success) or gives a reason why it's not possible (failure).

        Args:
        query: Query parameters.

        Returns:
            T.ListPermissionsResponse: The API response.
        """
        return self._http.request(
            method="GET",
            path="/permissions",
            path_params={},
            query_params=query,
            body=None,
            requires_signature=False,
        )

    def create_permission_init(self, body: T.CreatePermissionRequest) -> UserActionChallengeResponse:
        """
        Initialize Create Permission.

        Creates a user action challenge for external signing.

        Args:
        body: Request body.

        Returns:
            UserActionChallengeResponse: The challenge to sign externally.
        """
        path = "/permissions"
        payload = json.dumps(body, separators=(",", ":")) if body else ""

        return BaseAuthApi.create_user_action_challenge(
            self._http,
            user_action_http_method="POST",
            user_action_http_path=path,
            user_action_payload=payload,
        )

    def create_permission_complete(self, body: T.CreatePermissionRequest, signed_challenge: SignUserActionChallengeRequest) -> T.CreatePermissionResponse:
        """
        Complete Create Permission.

        Submits the signed challenge and makes the API request.

        Args:
        body: Request body.
        signed_challenge: The signed challenge from external signing.

        Returns:
            T.CreatePermissionResponse: The API response.
        """
        user_action_result = BaseAuthApi.sign_user_action_challenge(
            self._http, signed_challenge
        )
        user_action_token = user_action_result["userAction"]

        return self._http.request_with_user_action(
            method="POST",
            path="/permissions",
            path_params={},
            query_params=None,
            body=body,
            user_action=user_action_token,
        )

    def get_permission(self, permission_id: str) -> T.GetPermissionResponse:
        """
        Get Permission.

        Retrieves a specific permission (success) or gives a reason why it's not possible (failure).

        Args:
        permission_id: Path parameter.

        Returns:
            T.GetPermissionResponse: The API response.
        """
        return self._http.request(
            method="GET",
            path="/permissions/{permissionId}",
            path_params={"permissionId": permission_id},
            query_params=None,
            body=None,
            requires_signature=False,
        )

    def update_permission_init(self, permission_id: str, body: T.UpdatePermissionRequest) -> UserActionChallengeResponse:
        """
        Initialize Update Permission.

        Creates a user action challenge for external signing.

        Args:
        permission_id: Path parameter.
        body: Request body.

        Returns:
            UserActionChallengeResponse: The challenge to sign externally.
        """
        path = "/permissions/{permissionId}"
        path = path.replace("{permissionId}", str(permission_id))
        payload = json.dumps(body, separators=(",", ":")) if body else ""

        return BaseAuthApi.create_user_action_challenge(
            self._http,
            user_action_http_method="PUT",
            user_action_http_path=path,
            user_action_payload=payload,
        )

    def update_permission_complete(self, permission_id: str, body: T.UpdatePermissionRequest, signed_challenge: SignUserActionChallengeRequest) -> T.UpdatePermissionResponse:
        """
        Complete Update Permission.

        Submits the signed challenge and makes the API request.

        Args:
        permission_id: Path parameter.
        body: Request body.
        signed_challenge: The signed challenge from external signing.

        Returns:
            T.UpdatePermissionResponse: The API response.
        """
        user_action_result = BaseAuthApi.sign_user_action_challenge(
            self._http, signed_challenge
        )
        user_action_token = user_action_result["userAction"]

        return self._http.request_with_user_action(
            method="PUT",
            path="/permissions/{permissionId}",
            path_params={"permissionId": permission_id},
            query_params=None,
            body=body,
            user_action=user_action_token,
        )
