"""Client for the permissions domain."""

from typing import Any, Literal, Optional, TypedDict, Union

from ..._internal import HttpClient
from . import types as T


class PermissionsClient:
    """Client for permissions operations."""

    def __init__(self, http_client: HttpClient):
        self._http = http_client

    def archive_permission(self, permission_id: str, body: T.ArchivePermissionRequest) -> T.ArchivePermissionResponse:
        """
        Archive Permission.

        Archives or unarchives a permission (role). Archived permissions are effectively soft-deleted.

        Args:
        permission_id: ID of the permission (also referred to as "role" in the dashboard).
        body: Request body.

        Returns:
            T.ArchivePermissionResponse: The API response.
        """
        return self._http.request(
            method="PUT",
            path="/permissions/{permissionId}/archive",
            path_params={"permissionId": permission_id},
            query_params=None,
            body=body,
            requires_signature=True,
        )

    def list_permission_assignments(self, permission_id: str, query: Optional[T.ListPermissionAssignmentsQuery] = None) -> T.ListPermissionAssignmentsResponse:
        """
        List Permission Assignments.

        Lists all permission (role) assignments for a given permission.

        Args:
        permission_id: ID of the permission (also referred to as "role" in the dashboard).
        query: Query parameters.

        Returns:
            T.ListPermissionAssignmentsResponse: The API response.
        """
        return self._http.request(
            method="GET",
            path="/permissions/{permissionId}/assignments",
            path_params={"permissionId": permission_id},
            query_params=query,
            body=None,
            requires_signature=False,
        )

    def assign_permission(self, permission_id: str, body: T.AssignPermissionRequest) -> T.AssignPermissionResponse:
        """
        Assign Permission.

        Assigns a permission (role) to an identity (user, PAT or service account), granting it access to the operations defined in the permission. Returns the assignment on success (200), or a pending change request if approval is required (202).

        Args:
        permission_id: ID of the permission (also referred to as "role" in the dashboard).
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

    def list_permissions(self, query: Optional[T.ListPermissionsQuery] = None) -> T.ListPermissionsResponse:
        """
        List Permissions.

        Lists all permissions (roles) in the organization.

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

        Creates a new permission (also referred to as "role" in the dashboard) that grants access to the specified API operations.

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

    def revoke_permission(self, permission_id: str, assignment_id: str, query: Optional[T.RevokePermissionQuery] = None) -> None:
        """
        Revoke Permission.

        Revokes a permission (role) assignment, removing the identity's access to the operations granted by the permission.

        Args:
        permission_id: ID of the permission (also referred to as "role" in the dashboard).
        assignment_id: ID of the permission assignment.
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

    def get_permission(self, permission_id: str) -> T.GetPermissionResponse:
        """
        Get Permission.

        Retrieves a permission (role) by ID, including any pending change request.

        Args:
        permission_id: ID of the permission (also referred to as "role" in the dashboard).

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

        Updates the name or operations of an existing permission (role).

        Args:
        permission_id: ID of the permission (also referred to as "role" in the dashboard).
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
