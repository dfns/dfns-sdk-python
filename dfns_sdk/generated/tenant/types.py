"""Types for the tenant domain."""

from typing import Any, Literal, TypedDict

from typing_extensions import NotRequired


class AssignTenantPermissionRequest(TypedDict, total=False):
    """assignTenantPermission request body."""

    identity_id: str


class RevokeTenantPermissionRequest(TypedDict, total=False):
    """revokeTenantPermission request body."""

    identity_id: str


class GetTenantPermissionResponse(TypedDict, total=False):
    """getTenantPermission response."""

    id: str
    name: str
    operations: list[str]
    status: Literal["Active"]
    is_immutable: bool
    is_archived: bool
    date_created: str
    date_updated: str


class ListTenantPermissionsResponse(TypedDict, total=False):
    """listTenantPermissions response."""

    items: list[dict[str, Any]]
    next_page_token: NotRequired[str]


class ListTenantPermissionsQuery(TypedDict, total=False):
    """listTenantPermissions query parameters."""

    limit: NotRequired[int]
    pagination_token: NotRequired[str]


class ListTenantUsersResponse(TypedDict, total=False):
    """listTenantUsers response."""

    items: list[dict[str, Any]]
    next_page_token: NotRequired[str]


class ListTenantUsersQuery(TypedDict, total=False):
    """listTenantUsers query parameters."""

    limit: NotRequired[int]
    pagination_token: NotRequired[str]


class CreateTenantUserRequest(TypedDict, total=False):
    """createTenantUser request body."""

    email: str
    external_id: NotRequired[str]
    is_s_s_o_required: NotRequired[bool]


class CreateTenantUserResponse(TypedDict, total=False):
    """createTenantUser response."""

    id: str
    kind: Literal["TenantUser"]
    username: str
    is_registered: bool
    is_active: bool
    is_s_s_o_required: bool
    external_id: NotRequired[str]
    permissions: list[dict[str, Any]]
    orgs: list[dict[str, Any]]


class GetTenantUserResponse(TypedDict, total=False):
    """getTenantUser response."""

    id: str
    kind: Literal["TenantUser"]
    username: str
    is_registered: bool
    is_active: bool
    is_s_s_o_required: bool
    external_id: NotRequired[str]
    permissions: list[dict[str, Any]]
    orgs: list[dict[str, Any]]


class UpdateTenantUserRequest(TypedDict, total=False):
    """updateTenantUser request body."""

    is_s_s_o_required: bool


class UpdateTenantUserResponse(TypedDict, total=False):
    """updateTenantUser response."""

    pass


class DeleteTenantUserResponse(TypedDict, total=False):
    """deleteTenantUser response."""

    pass


class ListOrgsResponse(TypedDict, total=False):
    """listOrgs response."""

    items: list[dict[str, Any]]
    next_page_token: NotRequired[str]


class ListOrgsQuery(TypedDict, total=False):
    """listOrgs query parameters."""

    limit: NotRequired[int]
    pagination_token: NotRequired[str]
    status: NotRequired[Literal["Active", "Suspended", "Archived"] | list[Literal["Active", "Suspended", "Archived"]]]


class CreateOrgRequest(TypedDict, total=False):
    """createOrg request body."""

    name: str
    key_stores: list[dict[str, Any]]


class CreateOrgResponse(TypedDict, total=False):
    """createOrg response."""

    org: dict[str, Any]


class ListTenantUserGroupsResponse(TypedDict, total=False):
    """listTenantUserGroups response."""

    items: list[dict[str, Any]]
    next_page_token: NotRequired[str]


class ListTenantUserGroupsQuery(TypedDict, total=False):
    """listTenantUserGroups query parameters."""

    limit: NotRequired[int]
    pagination_token: NotRequired[str]


class CreateTenantUserGroupRequest(TypedDict, total=False):
    """createTenantUserGroup request body."""

    name: str
    description: NotRequired[str]


class CreateTenantUserGroupResponse(TypedDict, total=False):
    """createTenantUserGroup response."""

    id: str
    org_id: NotRequired[str]
    tenant_id: NotRequired[str]
    name: str
    description: NotRequired[str]
    member_count: int
    date_created: str
    date_updated: str


class GetTenantUserGroupResponse(TypedDict, total=False):
    """getTenantUserGroup response."""

    id: str
    org_id: NotRequired[str]
    tenant_id: NotRequired[str]
    name: str
    description: NotRequired[str]
    member_count: int
    date_created: str
    date_updated: str


class UpdateTenantUserGroupRequest(TypedDict, total=False):
    """updateTenantUserGroup request body."""

    name: NotRequired[str]
    description: NotRequired[Any]


class UpdateTenantUserGroupResponse(TypedDict, total=False):
    """updateTenantUserGroup response."""

    id: str
    org_id: NotRequired[str]
    tenant_id: NotRequired[str]
    name: str
    description: NotRequired[str]
    member_count: int
    date_created: str
    date_updated: str


class DeleteTenantUserGroupResponse(TypedDict, total=False):
    """deleteTenantUserGroup response."""

    pass


class ListTenantUserGroupMembersResponse(TypedDict, total=False):
    """listTenantUserGroupMembers response."""

    items: list[dict[str, Any]]
    next_page_token: NotRequired[str]


class ListTenantUserGroupMembersQuery(TypedDict, total=False):
    """listTenantUserGroupMembers query parameters."""

    limit: NotRequired[int]
    pagination_token: NotRequired[str]


class AddTenantUserGroupMembersRequest(TypedDict, total=False):
    """addTenantUserGroupMembers request body."""

    user_ids: list[str]


class AddTenantUserGroupMembersResponse(TypedDict, total=False):
    """addTenantUserGroupMembers response."""

    pass


class RemoveTenantUserGroupMembersRequest(TypedDict, total=False):
    """removeTenantUserGroupMembers request body."""

    user_ids: list[str]


class RemoveTenantUserGroupMembersResponse(TypedDict, total=False):
    """removeTenantUserGroupMembers response."""

    pass


class GetOrgResponse(TypedDict, total=False):
    """getOrg response."""

    org: dict[str, Any]


class UpdateOrgRequest(TypedDict, total=False):
    """updateOrg request body."""

    name: NotRequired[str]


class UpdateOrgResponse(TypedDict, total=False):
    """updateOrg response."""

    org: dict[str, Any]


class UpdateOrgStatusRequest(TypedDict, total=False):
    """updateOrgStatus request body."""

    status: Literal["Active", "Suspended", "Archived"]


class UpdateOrgStatusResponse(TypedDict, total=False):
    """updateOrgStatus response."""

    pass
