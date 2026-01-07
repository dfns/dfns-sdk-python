"""Client for the permissions domain."""

from typing import Any, Literal, Optional, TypedDict, Union

from ..._internal import HttpClient
from . import types as T


class PermissionsClient:
    """Client for permissions operations."""

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

    def assign_permission(self, permission_id: str, body: T.AssignPermissionRequest) -> T.AssignPermissionResponse:
        """
        Assign Permission.

        Creates a permission that allows certain specified operations to be executed. 
  
  Response is either the permission object itself (success) or a reason why it was not possible to create the permission (failure).

        Args:
        permission_id: Path parameter.
        body: Request body.

        Returns:
            T.AssignPermissionResponse: The API response.
        """
        return self._http.request(
            method="POST",
            path="/permissions/{permissionId}/assignments",
            path_params={"permissionId": permission_id},
            query_params=None,
            body=body,
            requires_signature=True,
        )

    def revoke_permission(self, permission_id: str, assignment_id: str, query: Optional[T.RevokePermissionQuery] = None) -> None:
        """
        Revoke Permission.

        Revokes a permission assignment (success) or gives reason why it’s not possible (failure).

        Args:
        permission_id: Path parameter.
        assignment_id: Path parameter.
        query: Query parameters.
        """
        return self._http.request(
            method="DELETE",
            path="/permissions/{permissionId}/assignments/{assignmentId}",
            path_params={"permissionId": permission_id, "assignmentId": assignment_id},
            query_params=query,
            body=None,
            requires_signature=True,
        )

    def delete_permission(self, permission_id: str, body: T.DeletePermissionRequest) -> T.DeletePermissionResponse:
        """
        Delete Permission.

        Delete a specific Permission.

        Args:
        permission_id: Path parameter.
        body: Request body.

        Returns:
            T.DeletePermissionResponse: The API response.
        """
        return self._http.request(
            method="PUT",
            path="/permissions/{permissionId}/archive",
            path_params={"permissionId": permission_id},
            query_params=None,
            body=body,
            requires_signature=True,
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

    def create_permission(self, body: T.CreatePermissionRequest) -> T.CreatePermissionResponse:
        """
        Create Permission.

        Creates a permission that allows certain specified operations to be executed.

        Args:
        body: Request body.

        Returns:
            T.CreatePermissionResponse: The API response.
        """
        return self._http.request(
            method="POST",
            path="/permissions",
            path_params={},
            query_params=None,
            body=body,
            requires_signature=True,
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

    def update_permission(self, permission_id: str, body: T.UpdatePermissionRequest) -> T.UpdatePermissionResponse:
        """
        Update Permission.

        Updates an existing permission. Response either returns the updated permission (success) or the reason why it was not possible to update (failure).

        Args:
        permission_id: Path parameter.
        body: Request body.

        Returns:
            T.UpdatePermissionResponse: The API response.
        """
        return self._http.request(
            method="PUT",
            path="/permissions/{permissionId}",
            path_params={"permissionId": permission_id},
            query_params=None,
            body=body,
            requires_signature=True,
        )
