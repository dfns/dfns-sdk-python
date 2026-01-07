"""Types for the permissions domain."""

from typing import Any, Literal, NotRequired, Optional, TypedDict, Union

class ListPermissionAssignmentsResponse(TypedDict, total=False):
    """listPermissionAssignments response."""

    items: list[TypedDict]
    next_page_token: NotRequired[str]

class AssignPermissionRequest(TypedDict, total=False):
    """assignPermission request body."""

    identity_id: str

class AssignPermissionResponse(TypedDict, total=False):
    """assignPermission response."""

    id: str
    permission_id: str
    identity_id: str
    is_immutable: bool
    date_created: str
    date_updated: str

class RevokePermissionQuery(TypedDict, total=False):
    """revokePermission query parameters."""

    force: NotRequired[bool]

class DeletePermissionRequest(TypedDict, total=False):
    """deletePermission request body."""

    is_archived: bool

class DeletePermissionResponse(TypedDict, total=False):
    """deletePermission response."""

    id: str
    name: str
    operations: list[str]
    status: Literal["Active"]
    is_immutable: bool
    is_archived: bool
    date_created: str
    date_updated: str

class ListPermissionsResponse(TypedDict, total=False):
    """listPermissions response."""

    items: list[TypedDict]
    next_page_token: NotRequired[str]

class ListPermissionsQuery(TypedDict, total=False):
    """listPermissions query parameters."""

    limit: NotRequired[str]
    pagination_token: NotRequired[str]

class CreatePermissionRequest(TypedDict, total=False):
    """createPermission request body."""

    name: str
    operations: list[Union[Literal["Registry:Addresses:Create", "Registry:Addresses:Delete", "Registry:Addresses:Read", "Registry:Addresses:Update", "Registry:ContractSchemas:Create", "Registry:ContractSchemas:Delete", "Registry:ContractSchemas:Read", "Auth:Logs:Read", "Auth:Users:Create", "Auth:Users:Read", "Auth:Users:Update", "Auth:Users:Activate", "Auth:Users:Deactivate", "Auth:Users:Delete", "Auth:ServiceAccounts:Create", "Auth:ServiceAccounts:Read", "Auth:ServiceAccounts:Update", "Auth:ServiceAccounts:Deactivate", "Auth:ServiceAccounts:Activate", "Auth:ServiceAccounts:Delete", "Auth:Pats:Create", "Auth:Register:Delegated", "Auth:Login:Delegated", "Auth:Recover:Delegated", "Agreements:Acceptance:Create", "Agreements:Acceptance:Read", "Events:Read", "Exchanges:Create", "Exchanges:Read", "Exchanges:Delete", "Exchanges:Deposits:Create", "Exchanges:Withdrawals:Create", "FeeSponsors:Create", "FeeSponsors:Read", "FeeSponsors:Update", "FeeSponsors:Delete", "FeeSponsors:Use", "Orgs:Read", "Orgs:Update", "Orgs:Settings:Read", "Orgs:Settings:Update", "Permissions:Archive", "Permissions:Create", "Permissions:Read", "Permissions:Update", "Permissions:Assign", "Permissions:Revoke", "Permissions:Assignments:Read", "Policies:Archive", "Policies:Create", "Policies:Read", "Policies:Update", "Policies:Approvals:Read", "Policies:Approvals:Approve", "Signers:ListSigners", "Stakes:Create", "Stakes:Read", "Stakes:Update", "Swaps:Create", "Swaps:Read", "Allocations:Create", "Allocations:Update", "Allocations:Read", "Keys:Create", "Keys:Delete", "Keys:Read", "Keys:Update", "Keys:Reuse", "Keys:Delegate", "Keys:Import", "Keys:Export", "Keys:Derive", "Keys:ChildKeys:Create", "Keys:Signatures:Create", "Keys:Signatures:Read", "KeyStores:Read", "Networks:CantonValidators:Create", "Networks:CantonValidators:Read", "Networks:CantonValidators:Update", "Networks:CantonValidators:Delete", "Wallets:Create", "Wallets:Read", "Wallets:Update", "Wallets:Tags:Add", "Wallets:Tags:Delete", "Wallets:Transactions:Create", "Wallets:Transactions:Read", "Wallets:Transfers:Create", "Wallets:Transfers:Read", "Wallets:Offers:Read", "Wallets:Offers:Settle", "Webhooks:Create", "Webhooks:Read", "Webhooks:Update", "Webhooks:Delete", "Webhooks:Ping", "Webhooks:Events:Read", "Billing:Read", "Billing:Write", "Analytics:Read"], Literal["Alias:Create", "Alias:Delete", "Alias:Read", "Alias:Update", "Wallets:GenerateSignature", "Wallets:BroadcastTransaction", "Auth:Action:Sign", "Auth:Apps:Read", "Auth:Apps:Create", "Auth:Apps:Update", "Auth:Creds:Create", "Auth:Creds:Read", "Auth:Creds:Update", "Auth:Creds:Code:Create", "Auth:Types:Application", "Auth:Types:Employee", "Auth:Types:EndUser", "Auth:Types:Pat", "Auth:Types:ServiceAccount", "Internal:Auth:Types:Staff", "Auth:Users:Delegate", "PermissionAssignments:Create", "PermissionAssignments:Read", "PermissionAssignments:Revoke"]]]

class CreatePermissionResponse(TypedDict, total=False):
    """createPermission response."""

    id: str
    name: str
    operations: list[str]
    status: Literal["Active"]
    is_immutable: bool
    is_archived: bool
    date_created: str
    date_updated: str

class GetPermissionResponse(TypedDict, total=False):
    """getPermission response."""

    id: str
    name: str
    operations: list[str]
    status: Literal["Active"]
    is_immutable: bool
    is_archived: bool
    date_created: str
    date_updated: str
    pending_change_request: NotRequired[TypedDict]

class UpdatePermissionRequest(TypedDict, total=False):
    """updatePermission request body."""

    name: NotRequired[str]
    operations: NotRequired[list[Union[Literal["Registry:Addresses:Create", "Registry:Addresses:Delete", "Registry:Addresses:Read", "Registry:Addresses:Update", "Registry:ContractSchemas:Create", "Registry:ContractSchemas:Delete", "Registry:ContractSchemas:Read", "Auth:Logs:Read", "Auth:Users:Create", "Auth:Users:Read", "Auth:Users:Update", "Auth:Users:Activate", "Auth:Users:Deactivate", "Auth:Users:Delete", "Auth:ServiceAccounts:Create", "Auth:ServiceAccounts:Read", "Auth:ServiceAccounts:Update", "Auth:ServiceAccounts:Deactivate", "Auth:ServiceAccounts:Activate", "Auth:ServiceAccounts:Delete", "Auth:Pats:Create", "Auth:Register:Delegated", "Auth:Login:Delegated", "Auth:Recover:Delegated", "Agreements:Acceptance:Create", "Agreements:Acceptance:Read", "Events:Read", "Exchanges:Create", "Exchanges:Read", "Exchanges:Delete", "Exchanges:Deposits:Create", "Exchanges:Withdrawals:Create", "FeeSponsors:Create", "FeeSponsors:Read", "FeeSponsors:Update", "FeeSponsors:Delete", "FeeSponsors:Use", "Orgs:Read", "Orgs:Update", "Orgs:Settings:Read", "Orgs:Settings:Update", "Permissions:Archive", "Permissions:Create", "Permissions:Read", "Permissions:Update", "Permissions:Assign", "Permissions:Revoke", "Permissions:Assignments:Read", "Policies:Archive", "Policies:Create", "Policies:Read", "Policies:Update", "Policies:Approvals:Read", "Policies:Approvals:Approve", "Signers:ListSigners", "Stakes:Create", "Stakes:Read", "Stakes:Update", "Swaps:Create", "Swaps:Read", "Allocations:Create", "Allocations:Update", "Allocations:Read", "Keys:Create", "Keys:Delete", "Keys:Read", "Keys:Update", "Keys:Reuse", "Keys:Delegate", "Keys:Import", "Keys:Export", "Keys:Derive", "Keys:ChildKeys:Create", "Keys:Signatures:Create", "Keys:Signatures:Read", "KeyStores:Read", "Networks:CantonValidators:Create", "Networks:CantonValidators:Read", "Networks:CantonValidators:Update", "Networks:CantonValidators:Delete", "Wallets:Create", "Wallets:Read", "Wallets:Update", "Wallets:Tags:Add", "Wallets:Tags:Delete", "Wallets:Transactions:Create", "Wallets:Transactions:Read", "Wallets:Transfers:Create", "Wallets:Transfers:Read", "Wallets:Offers:Read", "Wallets:Offers:Settle", "Webhooks:Create", "Webhooks:Read", "Webhooks:Update", "Webhooks:Delete", "Webhooks:Ping", "Webhooks:Events:Read", "Billing:Read", "Billing:Write", "Analytics:Read"], Literal["Alias:Create", "Alias:Delete", "Alias:Read", "Alias:Update", "Wallets:GenerateSignature", "Wallets:BroadcastTransaction", "Auth:Action:Sign", "Auth:Apps:Read", "Auth:Apps:Create", "Auth:Apps:Update", "Auth:Creds:Create", "Auth:Creds:Read", "Auth:Creds:Update", "Auth:Creds:Code:Create", "Auth:Types:Application", "Auth:Types:Employee", "Auth:Types:EndUser", "Auth:Types:Pat", "Auth:Types:ServiceAccount", "Internal:Auth:Types:Staff", "Auth:Users:Delegate", "PermissionAssignments:Create", "PermissionAssignments:Read", "PermissionAssignments:Revoke"]]]]

class UpdatePermissionResponse(TypedDict, total=False):
    """updatePermission response."""

    id: str
    name: str
    operations: list[str]
    status: Literal["Active"]
    is_immutable: bool
    is_archived: bool
    date_created: str
    date_updated: str
