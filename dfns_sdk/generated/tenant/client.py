"""Client for the tenant domain."""

from typing import cast

from ..._internal import HttpClient
from . import types as T


class TenantClient:
    """Client for tenant operations."""

    def __init__(self, http_client: HttpClient):
        self._http = http_client

    def assign_tenant_permission(self, permission_id: str, body: T.AssignTenantPermissionRequest) -> None:
        """
              Assign Tenant Permission.

              Creates a permission that allows certain specified operations to be executed.

        Response is either the permission object itself (success) or a reason why it was not possible to create the permission (failure).

              Args:
                  permission_id: ID of the permission (also referred to as "role" in the dashboard).
                  body: Request body.
        """  # noqa: E501
        self._http.request(
            method="POST",
            path="/tenant/permissions/{permissionId}/assign",
            path_params={"permissionId": permission_id},
            query_params=None,
            body=body,
            requires_signature=True,
        )

    def revoke_tenant_permission(self, permission_id: str, body: T.RevokeTenantPermissionRequest) -> None:
        """
        Revoke Tenant Permission.

        Revokes a permission assignment (success) or gives reason why it's not possible (failure).

        Args:
            permission_id: ID of the permission (also referred to as "role" in the dashboard).
            body: Request body.
        """  # noqa: E501
        self._http.request(
            method="POST",
            path="/tenant/permissions/{permissionId}/revoke",
            path_params={"permissionId": permission_id},
            query_params=None,
            body=body,
            requires_signature=True,
        )

    def get_tenant_permission(self, permission_id: str) -> T.GetTenantPermissionResponse:
        """
        Get Tenant Permission.

        Retrieves a specific permission (success) or gives a reason why it's not possible (failure).

        Args:
            permission_id: ID of the permission (also referred to as "role" in the dashboard).

        Returns:
            T.GetTenantPermissionResponse: The API response.
        """  # noqa: E501
        response = self._http.request(
            method="GET",
            path="/tenant/permissions/{permissionId}",
            path_params={"permissionId": permission_id},
            query_params=None,
            body=None,
            requires_signature=False,
        )
        return cast(T.GetTenantPermissionResponse, response)

    def list_tenant_permissions(
        self, query: T.ListTenantPermissionsQuery | None = None
    ) -> T.ListTenantPermissionsResponse:
        """
        List Tenant Permissions.

        Retrieves a list of permissions (success) or gives a reason why it's not possible (failure).

        Args:
            query: Query parameters.

        Returns:
            T.ListTenantPermissionsResponse: The API response.
        """  # noqa: E501
        response = self._http.request(
            method="GET",
            path="/tenant/permissions",
            path_params={},
            query_params=query,
            body=None,
            requires_signature=False,
        )
        return cast(T.ListTenantPermissionsResponse, response)

    def list_tenant_users(self, query: T.ListTenantUsersQuery | None = None) -> T.ListTenantUsersResponse:
        """
        List Tenant Users.

        List all Users in your Tenant.

        Args:
            query: Query parameters.

        Returns:
            T.ListTenantUsersResponse: The API response.
        """  # noqa: E501
        response = self._http.request(
            method="GET",
            path="/tenant/users",
            path_params={},
            query_params=query,
            body=None,
            requires_signature=False,
        )
        return cast(T.ListTenantUsersResponse, response)

    def create_tenant_user(self, body: T.CreateTenantUserRequest) -> T.CreateTenantUserResponse:
        """
        Create Tenant User.

        Creates a new Tenant User. This creates the user and sends him an email with a registration code. The user is created without any permissions.

        Args:
            body: Request body.

        Returns:
            T.CreateTenantUserResponse: The API response.
        """  # noqa: E501
        response = self._http.request(
            method="POST",
            path="/tenant/users",
            path_params={},
            query_params=None,
            body=body,
            requires_signature=True,
        )
        return cast(T.CreateTenantUserResponse, response)

    def get_tenant_user(self, user_id: str) -> T.GetTenantUserResponse:
        """
        Get Tenant User.

        Get a Tenant User.

        Args:
            user_id: User id.

        Returns:
            T.GetTenantUserResponse: The API response.
        """  # noqa: E501
        response = self._http.request(
            method="GET",
            path="/tenant/users/{userId}",
            path_params={"userId": user_id},
            query_params=None,
            body=None,
            requires_signature=False,
        )
        return cast(T.GetTenantUserResponse, response)

    def update_tenant_user(self, user_id: str, body: T.UpdateTenantUserRequest) -> T.UpdateTenantUserResponse:
        """
        Update Tenant User.

        Updates a new Tenant User details.

        Args:
            user_id: User id.
            body: Request body.

        Returns:
            T.UpdateTenantUserResponse: The API response.
        """  # noqa: E501
        response = self._http.request(
            method="PUT",
            path="/tenant/users/{userId}",
            path_params={"userId": user_id},
            query_params=None,
            body=body,
            requires_signature=True,
        )
        return cast(T.UpdateTenantUserResponse, response)

    def delete_tenant_user(self, user_id: str) -> T.DeleteTenantUserResponse:
        """
        Delete Tenant User.

        Delete a specific Tenant User.

        Args:
            user_id: User id.

        Returns:
            T.DeleteTenantUserResponse: The API response.
        """  # noqa: E501
        response = self._http.request(
            method="DELETE",
            path="/tenant/users/{userId}",
            path_params={"userId": user_id},
            query_params=None,
            body=None,
            requires_signature=True,
        )
        return cast(T.DeleteTenantUserResponse, response)

    def list_orgs(self, query: T.ListOrgsQuery | None = None) -> T.ListOrgsResponse:
        """
                List Orgs.

                List all Orgs in your Tenant.
        By default, returns non-archived Orgs, unless specific status are passed

                Args:
                    query: Query parameters.

                Returns:
                    T.ListOrgsResponse: The API response.
        """  # noqa: E501
        response = self._http.request(
            method="GET",
            path="/tenant/orgs",
            path_params={},
            query_params=query,
            body=None,
            requires_signature=False,
        )
        return cast(T.ListOrgsResponse, response)

    def create_org(self, body: T.CreateOrgRequest) -> T.CreateOrgResponse:
        """
        Create Org.

        Create a new Org in your Tenant. The creator of the org will be granted access to the Org as the first Org Admin.

        Args:
            body: Request body.

        Returns:
            T.CreateOrgResponse: The API response.
        """  # noqa: E501
        response = self._http.request(
            method="POST",
            path="/tenant/orgs",
            path_params={},
            query_params=None,
            body=body,
            requires_signature=True,
        )
        return cast(T.CreateOrgResponse, response)

    def list_tenant_user_groups(
        self, query: T.ListTenantUserGroupsQuery | None = None
    ) -> T.ListTenantUserGroupsResponse:
        """
        List Tenant User Groups.

        List the user groups in the caller's tenant.

        Args:
            query: Query parameters.

        Returns:
            T.ListTenantUserGroupsResponse: The API response.
        """  # noqa: E501
        response = self._http.request(
            method="GET",
            path="/tenant/user-groups",
            path_params={},
            query_params=query,
            body=None,
            requires_signature=False,
        )
        return cast(T.ListTenantUserGroupsResponse, response)

    def create_tenant_user_group(self, body: T.CreateTenantUserGroupRequest) -> T.CreateTenantUserGroupResponse:
        """
        Create Tenant User Group.

        Create a user group in the caller's tenant. A group holds tenant permissions through the tenant permission assignment endpoint, and its members hold those permissions in addition to their own.

        Args:
            body: Request body.

        Returns:
            T.CreateTenantUserGroupResponse: The API response.
        """  # noqa: E501
        response = self._http.request(
            method="POST",
            path="/tenant/user-groups",
            path_params={},
            query_params=None,
            body=body,
            requires_signature=True,
        )
        return cast(T.CreateTenantUserGroupResponse, response)

    def get_tenant_user_group(self, user_group_id: str) -> T.GetTenantUserGroupResponse:
        """
        Get Tenant User Group.

        Get a specific user group of the caller's tenant.

        Args:
            user_group_id: User group id.

        Returns:
            T.GetTenantUserGroupResponse: The API response.
        """  # noqa: E501
        response = self._http.request(
            method="GET",
            path="/tenant/user-groups/{userGroupId}",
            path_params={"userGroupId": user_group_id},
            query_params=None,
            body=None,
            requires_signature=False,
        )
        return cast(T.GetTenantUserGroupResponse, response)

    def update_tenant_user_group(
        self, user_group_id: str, body: T.UpdateTenantUserGroupRequest
    ) -> T.UpdateTenantUserGroupResponse:
        """
        Update Tenant User Group.

        Rename a user group of the caller's tenant or change its description. Fields left out keep their value. Its permissions and members are unaffected.

        Args:
            user_group_id: User group id.
            body: Request body.

        Returns:
            T.UpdateTenantUserGroupResponse: The API response.
        """  # noqa: E501
        response = self._http.request(
            method="PUT",
            path="/tenant/user-groups/{userGroupId}",
            path_params={"userGroupId": user_group_id},
            query_params=None,
            body=body,
            requires_signature=True,
        )
        return cast(T.UpdateTenantUserGroupResponse, response)

    def delete_tenant_user_group(self, user_group_id: str) -> T.DeleteTenantUserGroupResponse:
        """
        Delete Tenant User Group.

        Delete a user group of the caller's tenant. Its tenant permission assignments are revoked and its members are removed. The name can be reused.

        Args:
            user_group_id: User group id.

        Returns:
            T.DeleteTenantUserGroupResponse: The API response.
        """  # noqa: E501
        response = self._http.request(
            method="DELETE",
            path="/tenant/user-groups/{userGroupId}",
            path_params={"userGroupId": user_group_id},
            query_params=None,
            body=None,
            requires_signature=True,
        )
        return cast(T.DeleteTenantUserGroupResponse, response)

    def list_tenant_user_group_members(
        self, user_group_id: str, query: T.ListTenantUserGroupMembersQuery | None = None
    ) -> T.ListTenantUserGroupMembersResponse:
        """
        List Tenant User Group Members.

        List the members of a user group of the caller's tenant.

        Args:
            user_group_id: User group id.
            query: Query parameters.

        Returns:
            T.ListTenantUserGroupMembersResponse: The API response.
        """  # noqa: E501
        response = self._http.request(
            method="GET",
            path="/tenant/user-groups/{userGroupId}/members",
            path_params={"userGroupId": user_group_id},
            query_params=query,
            body=None,
            requires_signature=False,
        )
        return cast(T.ListTenantUserGroupMembersResponse, response)

    def add_tenant_user_group_members(
        self, user_group_id: str, body: T.AddTenantUserGroupMembersRequest
    ) -> T.AddTenantUserGroupMembersResponse:
        """
        Add Tenant User Group Members.

        Add tenant users to a user group. Each member gains every tenant permission assigned to the group, in addition to their own.

        Args:
            user_group_id: User group id.
            body: Request body.

        Returns:
            T.AddTenantUserGroupMembersResponse: The API response.
        """  # noqa: E501
        response = self._http.request(
            method="POST",
            path="/tenant/user-groups/{userGroupId}/members",
            path_params={"userGroupId": user_group_id},
            query_params=None,
            body=body,
            requires_signature=True,
        )
        return cast(T.AddTenantUserGroupMembersResponse, response)

    def remove_tenant_user_group_members(
        self, user_group_id: str, body: T.RemoveTenantUserGroupMembersRequest
    ) -> T.RemoveTenantUserGroupMembersResponse:
        """
        Remove Tenant User Group Members.

        Remove tenant users from a user group. Each removed user immediately loses every tenant permission they held only through this group.

        Args:
            user_group_id: User group id.
            body: Request body.

        Returns:
            T.RemoveTenantUserGroupMembersResponse: The API response.
        """  # noqa: E501
        response = self._http.request(
            method="DELETE",
            path="/tenant/user-groups/{userGroupId}/members",
            path_params={"userGroupId": user_group_id},
            query_params=None,
            body=body,
            requires_signature=True,
        )
        return cast(T.RemoveTenantUserGroupMembersResponse, response)

    def get_org(self, org_id: str) -> T.GetOrgResponse:
        """
        Get Org.

        Get details on a single Org within your Tenant.

        Args:
            org_id: Organization id.

        Returns:
            T.GetOrgResponse: The API response.
        """  # noqa: E501
        response = self._http.request(
            method="GET",
            path="/tenant/orgs/{orgId}",
            path_params={"orgId": org_id},
            query_params=None,
            body=None,
            requires_signature=False,
        )
        return cast(T.GetOrgResponse, response)

    def update_org(self, org_id: str, body: T.UpdateOrgRequest) -> T.UpdateOrgResponse:
        """
        Update Org.

        Update the name of an Org within your Tenant.

        Args:
            org_id: Organization id.
            body: Request body.

        Returns:
            T.UpdateOrgResponse: The API response.
        """  # noqa: E501
        response = self._http.request(
            method="PUT",
            path="/tenant/orgs/{orgId}",
            path_params={"orgId": org_id},
            query_params=None,
            body=body,
            requires_signature=True,
        )
        return cast(T.UpdateOrgResponse, response)

    def update_org_status(self, org_id: str, body: T.UpdateOrgStatusRequest) -> T.UpdateOrgStatusResponse:
        """
        Update Org Status.

        Change the status of an Org within your Tenant.

        Args:
            org_id: Organization id.
            body: Request body.

        Returns:
            T.UpdateOrgStatusResponse: The API response.
        """  # noqa: E501
        response = self._http.request(
            method="PUT",
            path="/tenant/orgs/{orgId}/status",
            path_params={"orgId": org_id},
            query_params=None,
            body=body,
            requires_signature=True,
        )
        return cast(T.UpdateOrgStatusResponse, response)
