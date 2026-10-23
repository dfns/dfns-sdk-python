"""Delegated client for the tenant domain."""

import json
from typing import cast

from ..._internal import HttpClient
from ...base_auth_api import BaseAuthApi, SignUserActionChallengeRequest, UserActionChallengeResponse
from . import types as T


class DelegatedTenantClient:
    """
    Delegated client for tenant operations.

    This client separates user action signing into _init() and _complete() method pairs,
    allowing external systems to handle the signing process.
    """

    def __init__(self, http_client: HttpClient):
        self._http = http_client

    def assign_tenant_permission_init(
        self, permission_id: str, body: T.AssignTenantPermissionRequest
    ) -> UserActionChallengeResponse:
        """
        Initialize Assign Tenant Permission.

        Creates a user action challenge for external signing.

        Args:
            permission_id: ID of the permission (also referred to as "role" in the dashboard).
            body: Request body.

        Returns:
            UserActionChallengeResponse: The challenge to sign externally.
        """  # noqa: E501
        path = "/tenant/permissions/{permissionId}/assign"
        path = path.replace("{permissionId}", str(permission_id))
        payload = json.dumps(body, separators=(",", ":")) if body else ""

        return BaseAuthApi.create_user_action_challenge(
            self._http,
            user_action_http_method="POST",
            user_action_http_path=path,
            user_action_payload=payload,
        )

    def assign_tenant_permission_complete(
        self,
        permission_id: str,
        body: T.AssignTenantPermissionRequest,
        signed_challenge: SignUserActionChallengeRequest,
    ) -> None:
        """
        Complete Assign Tenant Permission.

        Submits the signed challenge and makes the API request.

        Args:
            permission_id: ID of the permission (also referred to as "role" in the dashboard).
            body: Request body.
            signed_challenge: The signed challenge from external signing.
        """  # noqa: E501
        user_action_result = BaseAuthApi.sign_user_action_challenge(self._http, signed_challenge)
        user_action_token = user_action_result["userAction"]

        self._http.request_with_user_action(
            method="POST",
            path="/tenant/permissions/{permissionId}/assign",
            path_params={"permissionId": permission_id},
            query_params=None,
            body=body,
            user_action=user_action_token,
        )

    def revoke_tenant_permission_init(
        self, permission_id: str, body: T.RevokeTenantPermissionRequest
    ) -> UserActionChallengeResponse:
        """
        Initialize Revoke Tenant Permission.

        Creates a user action challenge for external signing.

        Args:
            permission_id: ID of the permission (also referred to as "role" in the dashboard).
            body: Request body.

        Returns:
            UserActionChallengeResponse: The challenge to sign externally.
        """  # noqa: E501
        path = "/tenant/permissions/{permissionId}/revoke"
        path = path.replace("{permissionId}", str(permission_id))
        payload = json.dumps(body, separators=(",", ":")) if body else ""

        return BaseAuthApi.create_user_action_challenge(
            self._http,
            user_action_http_method="POST",
            user_action_http_path=path,
            user_action_payload=payload,
        )

    def revoke_tenant_permission_complete(
        self,
        permission_id: str,
        body: T.RevokeTenantPermissionRequest,
        signed_challenge: SignUserActionChallengeRequest,
    ) -> None:
        """
        Complete Revoke Tenant Permission.

        Submits the signed challenge and makes the API request.

        Args:
            permission_id: ID of the permission (also referred to as "role" in the dashboard).
            body: Request body.
            signed_challenge: The signed challenge from external signing.
        """  # noqa: E501
        user_action_result = BaseAuthApi.sign_user_action_challenge(self._http, signed_challenge)
        user_action_token = user_action_result["userAction"]

        self._http.request_with_user_action(
            method="POST",
            path="/tenant/permissions/{permissionId}/revoke",
            path_params={"permissionId": permission_id},
            query_params=None,
            body=body,
            user_action=user_action_token,
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

    def create_tenant_user_init(self, body: T.CreateTenantUserRequest) -> UserActionChallengeResponse:
        """
        Initialize Create Tenant User.

        Creates a user action challenge for external signing.

        Args:
            body: Request body.

        Returns:
            UserActionChallengeResponse: The challenge to sign externally.
        """  # noqa: E501
        path = "/tenant/users"
        payload = json.dumps(body, separators=(",", ":")) if body else ""

        return BaseAuthApi.create_user_action_challenge(
            self._http,
            user_action_http_method="POST",
            user_action_http_path=path,
            user_action_payload=payload,
        )

    def create_tenant_user_complete(
        self, body: T.CreateTenantUserRequest, signed_challenge: SignUserActionChallengeRequest
    ) -> T.CreateTenantUserResponse:
        """
        Complete Create Tenant User.

        Submits the signed challenge and makes the API request.

        Args:
            body: Request body.
            signed_challenge: The signed challenge from external signing.

        Returns:
            T.CreateTenantUserResponse: The API response.
        """  # noqa: E501
        user_action_result = BaseAuthApi.sign_user_action_challenge(self._http, signed_challenge)
        user_action_token = user_action_result["userAction"]

        response = self._http.request_with_user_action(
            method="POST",
            path="/tenant/users",
            path_params={},
            query_params=None,
            body=body,
            user_action=user_action_token,
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

    def update_tenant_user_init(self, user_id: str, body: T.UpdateTenantUserRequest) -> UserActionChallengeResponse:
        """
        Initialize Update Tenant User.

        Creates a user action challenge for external signing.

        Args:
            user_id: User id.
            body: Request body.

        Returns:
            UserActionChallengeResponse: The challenge to sign externally.
        """  # noqa: E501
        path = "/tenant/users/{userId}"
        path = path.replace("{userId}", str(user_id))
        payload = json.dumps(body, separators=(",", ":")) if body else ""

        return BaseAuthApi.create_user_action_challenge(
            self._http,
            user_action_http_method="PUT",
            user_action_http_path=path,
            user_action_payload=payload,
        )

    def update_tenant_user_complete(
        self, user_id: str, body: T.UpdateTenantUserRequest, signed_challenge: SignUserActionChallengeRequest
    ) -> T.UpdateTenantUserResponse:
        """
        Complete Update Tenant User.

        Submits the signed challenge and makes the API request.

        Args:
            user_id: User id.
            body: Request body.
            signed_challenge: The signed challenge from external signing.

        Returns:
            T.UpdateTenantUserResponse: The API response.
        """  # noqa: E501
        user_action_result = BaseAuthApi.sign_user_action_challenge(self._http, signed_challenge)
        user_action_token = user_action_result["userAction"]

        response = self._http.request_with_user_action(
            method="PUT",
            path="/tenant/users/{userId}",
            path_params={"userId": user_id},
            query_params=None,
            body=body,
            user_action=user_action_token,
        )
        return cast(T.UpdateTenantUserResponse, response)

    def delete_tenant_user_init(self, user_id: str) -> UserActionChallengeResponse:
        """
        Initialize Delete Tenant User.

        Creates a user action challenge for external signing.

        Args:
            user_id: User id.

        Returns:
            UserActionChallengeResponse: The challenge to sign externally.
        """  # noqa: E501
        path = "/tenant/users/{userId}"
        path = path.replace("{userId}", str(user_id))
        payload = ""

        return BaseAuthApi.create_user_action_challenge(
            self._http,
            user_action_http_method="DELETE",
            user_action_http_path=path,
            user_action_payload=payload,
        )

    def delete_tenant_user_complete(
        self, user_id: str, signed_challenge: SignUserActionChallengeRequest
    ) -> T.DeleteTenantUserResponse:
        """
        Complete Delete Tenant User.

        Submits the signed challenge and makes the API request.

        Args:
            user_id: User id.
            signed_challenge: The signed challenge from external signing.

        Returns:
            T.DeleteTenantUserResponse: The API response.
        """  # noqa: E501
        user_action_result = BaseAuthApi.sign_user_action_challenge(self._http, signed_challenge)
        user_action_token = user_action_result["userAction"]

        response = self._http.request_with_user_action(
            method="DELETE",
            path="/tenant/users/{userId}",
            path_params={"userId": user_id},
            query_params=None,
            body=None,
            user_action=user_action_token,
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

    def create_org_init(self, body: T.CreateOrgRequest) -> UserActionChallengeResponse:
        """
        Initialize Create Org.

        Creates a user action challenge for external signing.

        Args:
            body: Request body.

        Returns:
            UserActionChallengeResponse: The challenge to sign externally.
        """  # noqa: E501
        path = "/tenant/orgs"
        payload = json.dumps(body, separators=(",", ":")) if body else ""

        return BaseAuthApi.create_user_action_challenge(
            self._http,
            user_action_http_method="POST",
            user_action_http_path=path,
            user_action_payload=payload,
        )

    def create_org_complete(
        self, body: T.CreateOrgRequest, signed_challenge: SignUserActionChallengeRequest
    ) -> T.CreateOrgResponse:
        """
        Complete Create Org.

        Submits the signed challenge and makes the API request.

        Args:
            body: Request body.
            signed_challenge: The signed challenge from external signing.

        Returns:
            T.CreateOrgResponse: The API response.
        """  # noqa: E501
        user_action_result = BaseAuthApi.sign_user_action_challenge(self._http, signed_challenge)
        user_action_token = user_action_result["userAction"]

        response = self._http.request_with_user_action(
            method="POST",
            path="/tenant/orgs",
            path_params={},
            query_params=None,
            body=body,
            user_action=user_action_token,
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

    def create_tenant_user_group_init(self, body: T.CreateTenantUserGroupRequest) -> UserActionChallengeResponse:
        """
        Initialize Create Tenant User Group.

        Creates a user action challenge for external signing.

        Args:
            body: Request body.

        Returns:
            UserActionChallengeResponse: The challenge to sign externally.
        """  # noqa: E501
        path = "/tenant/user-groups"
        payload = json.dumps(body, separators=(",", ":")) if body else ""

        return BaseAuthApi.create_user_action_challenge(
            self._http,
            user_action_http_method="POST",
            user_action_http_path=path,
            user_action_payload=payload,
        )

    def create_tenant_user_group_complete(
        self, body: T.CreateTenantUserGroupRequest, signed_challenge: SignUserActionChallengeRequest
    ) -> T.CreateTenantUserGroupResponse:
        """
        Complete Create Tenant User Group.

        Submits the signed challenge and makes the API request.

        Args:
            body: Request body.
            signed_challenge: The signed challenge from external signing.

        Returns:
            T.CreateTenantUserGroupResponse: The API response.
        """  # noqa: E501
        user_action_result = BaseAuthApi.sign_user_action_challenge(self._http, signed_challenge)
        user_action_token = user_action_result["userAction"]

        response = self._http.request_with_user_action(
            method="POST",
            path="/tenant/user-groups",
            path_params={},
            query_params=None,
            body=body,
            user_action=user_action_token,
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

    def update_tenant_user_group_init(
        self, user_group_id: str, body: T.UpdateTenantUserGroupRequest
    ) -> UserActionChallengeResponse:
        """
        Initialize Update Tenant User Group.

        Creates a user action challenge for external signing.

        Args:
            user_group_id: User group id.
            body: Request body.

        Returns:
            UserActionChallengeResponse: The challenge to sign externally.
        """  # noqa: E501
        path = "/tenant/user-groups/{userGroupId}"
        path = path.replace("{userGroupId}", str(user_group_id))
        payload = json.dumps(body, separators=(",", ":")) if body else ""

        return BaseAuthApi.create_user_action_challenge(
            self._http,
            user_action_http_method="PUT",
            user_action_http_path=path,
            user_action_payload=payload,
        )

    def update_tenant_user_group_complete(
        self, user_group_id: str, body: T.UpdateTenantUserGroupRequest, signed_challenge: SignUserActionChallengeRequest
    ) -> T.UpdateTenantUserGroupResponse:
        """
        Complete Update Tenant User Group.

        Submits the signed challenge and makes the API request.

        Args:
            user_group_id: User group id.
            body: Request body.
            signed_challenge: The signed challenge from external signing.

        Returns:
            T.UpdateTenantUserGroupResponse: The API response.
        """  # noqa: E501
        user_action_result = BaseAuthApi.sign_user_action_challenge(self._http, signed_challenge)
        user_action_token = user_action_result["userAction"]

        response = self._http.request_with_user_action(
            method="PUT",
            path="/tenant/user-groups/{userGroupId}",
            path_params={"userGroupId": user_group_id},
            query_params=None,
            body=body,
            user_action=user_action_token,
        )
        return cast(T.UpdateTenantUserGroupResponse, response)

    def delete_tenant_user_group_init(self, user_group_id: str) -> UserActionChallengeResponse:
        """
        Initialize Delete Tenant User Group.

        Creates a user action challenge for external signing.

        Args:
            user_group_id: User group id.

        Returns:
            UserActionChallengeResponse: The challenge to sign externally.
        """  # noqa: E501
        path = "/tenant/user-groups/{userGroupId}"
        path = path.replace("{userGroupId}", str(user_group_id))
        payload = ""

        return BaseAuthApi.create_user_action_challenge(
            self._http,
            user_action_http_method="DELETE",
            user_action_http_path=path,
            user_action_payload=payload,
        )

    def delete_tenant_user_group_complete(
        self, user_group_id: str, signed_challenge: SignUserActionChallengeRequest
    ) -> T.DeleteTenantUserGroupResponse:
        """
        Complete Delete Tenant User Group.

        Submits the signed challenge and makes the API request.

        Args:
            user_group_id: User group id.
            signed_challenge: The signed challenge from external signing.

        Returns:
            T.DeleteTenantUserGroupResponse: The API response.
        """  # noqa: E501
        user_action_result = BaseAuthApi.sign_user_action_challenge(self._http, signed_challenge)
        user_action_token = user_action_result["userAction"]

        response = self._http.request_with_user_action(
            method="DELETE",
            path="/tenant/user-groups/{userGroupId}",
            path_params={"userGroupId": user_group_id},
            query_params=None,
            body=None,
            user_action=user_action_token,
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

    def add_tenant_user_group_members_init(
        self, user_group_id: str, body: T.AddTenantUserGroupMembersRequest
    ) -> UserActionChallengeResponse:
        """
        Initialize Add Tenant User Group Members.

        Creates a user action challenge for external signing.

        Args:
            user_group_id: User group id.
            body: Request body.

        Returns:
            UserActionChallengeResponse: The challenge to sign externally.
        """  # noqa: E501
        path = "/tenant/user-groups/{userGroupId}/members"
        path = path.replace("{userGroupId}", str(user_group_id))
        payload = json.dumps(body, separators=(",", ":")) if body else ""

        return BaseAuthApi.create_user_action_challenge(
            self._http,
            user_action_http_method="POST",
            user_action_http_path=path,
            user_action_payload=payload,
        )

    def add_tenant_user_group_members_complete(
        self,
        user_group_id: str,
        body: T.AddTenantUserGroupMembersRequest,
        signed_challenge: SignUserActionChallengeRequest,
    ) -> T.AddTenantUserGroupMembersResponse:
        """
        Complete Add Tenant User Group Members.

        Submits the signed challenge and makes the API request.

        Args:
            user_group_id: User group id.
            body: Request body.
            signed_challenge: The signed challenge from external signing.

        Returns:
            T.AddTenantUserGroupMembersResponse: The API response.
        """  # noqa: E501
        user_action_result = BaseAuthApi.sign_user_action_challenge(self._http, signed_challenge)
        user_action_token = user_action_result["userAction"]

        response = self._http.request_with_user_action(
            method="POST",
            path="/tenant/user-groups/{userGroupId}/members",
            path_params={"userGroupId": user_group_id},
            query_params=None,
            body=body,
            user_action=user_action_token,
        )
        return cast(T.AddTenantUserGroupMembersResponse, response)

    def remove_tenant_user_group_members_init(
        self, user_group_id: str, body: T.RemoveTenantUserGroupMembersRequest
    ) -> UserActionChallengeResponse:
        """
        Initialize Remove Tenant User Group Members.

        Creates a user action challenge for external signing.

        Args:
            user_group_id: User group id.
            body: Request body.

        Returns:
            UserActionChallengeResponse: The challenge to sign externally.
        """  # noqa: E501
        path = "/tenant/user-groups/{userGroupId}/members"
        path = path.replace("{userGroupId}", str(user_group_id))
        payload = json.dumps(body, separators=(",", ":")) if body else ""

        return BaseAuthApi.create_user_action_challenge(
            self._http,
            user_action_http_method="DELETE",
            user_action_http_path=path,
            user_action_payload=payload,
        )

    def remove_tenant_user_group_members_complete(
        self,
        user_group_id: str,
        body: T.RemoveTenantUserGroupMembersRequest,
        signed_challenge: SignUserActionChallengeRequest,
    ) -> T.RemoveTenantUserGroupMembersResponse:
        """
        Complete Remove Tenant User Group Members.

        Submits the signed challenge and makes the API request.

        Args:
            user_group_id: User group id.
            body: Request body.
            signed_challenge: The signed challenge from external signing.

        Returns:
            T.RemoveTenantUserGroupMembersResponse: The API response.
        """  # noqa: E501
        user_action_result = BaseAuthApi.sign_user_action_challenge(self._http, signed_challenge)
        user_action_token = user_action_result["userAction"]

        response = self._http.request_with_user_action(
            method="DELETE",
            path="/tenant/user-groups/{userGroupId}/members",
            path_params={"userGroupId": user_group_id},
            query_params=None,
            body=body,
            user_action=user_action_token,
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

    def update_org_init(self, org_id: str, body: T.UpdateOrgRequest) -> UserActionChallengeResponse:
        """
        Initialize Update Org.

        Creates a user action challenge for external signing.

        Args:
            org_id: Organization id.
            body: Request body.

        Returns:
            UserActionChallengeResponse: The challenge to sign externally.
        """  # noqa: E501
        path = "/tenant/orgs/{orgId}"
        path = path.replace("{orgId}", str(org_id))
        payload = json.dumps(body, separators=(",", ":")) if body else ""

        return BaseAuthApi.create_user_action_challenge(
            self._http,
            user_action_http_method="PUT",
            user_action_http_path=path,
            user_action_payload=payload,
        )

    def update_org_complete(
        self, org_id: str, body: T.UpdateOrgRequest, signed_challenge: SignUserActionChallengeRequest
    ) -> T.UpdateOrgResponse:
        """
        Complete Update Org.

        Submits the signed challenge and makes the API request.

        Args:
            org_id: Organization id.
            body: Request body.
            signed_challenge: The signed challenge from external signing.

        Returns:
            T.UpdateOrgResponse: The API response.
        """  # noqa: E501
        user_action_result = BaseAuthApi.sign_user_action_challenge(self._http, signed_challenge)
        user_action_token = user_action_result["userAction"]

        response = self._http.request_with_user_action(
            method="PUT",
            path="/tenant/orgs/{orgId}",
            path_params={"orgId": org_id},
            query_params=None,
            body=body,
            user_action=user_action_token,
        )
        return cast(T.UpdateOrgResponse, response)

    def update_org_status_init(self, org_id: str, body: T.UpdateOrgStatusRequest) -> UserActionChallengeResponse:
        """
        Initialize Update Org Status.

        Creates a user action challenge for external signing.

        Args:
            org_id: Organization id.
            body: Request body.

        Returns:
            UserActionChallengeResponse: The challenge to sign externally.
        """  # noqa: E501
        path = "/tenant/orgs/{orgId}/status"
        path = path.replace("{orgId}", str(org_id))
        payload = json.dumps(body, separators=(",", ":")) if body else ""

        return BaseAuthApi.create_user_action_challenge(
            self._http,
            user_action_http_method="PUT",
            user_action_http_path=path,
            user_action_payload=payload,
        )

    def update_org_status_complete(
        self, org_id: str, body: T.UpdateOrgStatusRequest, signed_challenge: SignUserActionChallengeRequest
    ) -> T.UpdateOrgStatusResponse:
        """
        Complete Update Org Status.

        Submits the signed challenge and makes the API request.

        Args:
            org_id: Organization id.
            body: Request body.
            signed_challenge: The signed challenge from external signing.

        Returns:
            T.UpdateOrgStatusResponse: The API response.
        """  # noqa: E501
        user_action_result = BaseAuthApi.sign_user_action_challenge(self._http, signed_challenge)
        user_action_token = user_action_result["userAction"]

        response = self._http.request_with_user_action(
            method="PUT",
            path="/tenant/orgs/{orgId}/status",
            path_params={"orgId": org_id},
            query_params=None,
            body=body,
            user_action=user_action_token,
        )
        return cast(T.UpdateOrgStatusResponse, response)
