"""Types for the permissions domain."""

from typing import Any, Literal, TypedDict

from typing_extensions import NotRequired


class ArchivePermissionRequest(TypedDict, total=False):
    """archivePermission request body."""

    is_archived: bool


class ArchivePermissionResponse(TypedDict, total=False):
    """archivePermission response."""

    id: str
    name: str
    operations: list[str]
    status: Literal["Active"]
    is_immutable: bool
    is_archived: bool
    date_created: str
    date_updated: str


class ListPermissionAssignmentsResponse(TypedDict, total=False):
    """listPermissionAssignments response."""

    items: list[dict[str, Any]]
    next_page_token: NotRequired[str]


class ListPermissionAssignmentsQuery(TypedDict, total=False):
    """listPermissionAssignments query parameters."""

    limit: NotRequired[int]
    pagination_token: NotRequired[str]


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


class ListPermissionsResponse(TypedDict, total=False):
    """listPermissions response."""

    items: list[dict[str, Any]]
    next_page_token: NotRequired[str]


class ListPermissionsQuery(TypedDict, total=False):
    """listPermissions query parameters."""

    limit: NotRequired[int]
    pagination_token: NotRequired[str]


class CreatePermissionRequest(TypedDict, total=False):
    """createPermission request body."""

    name: str
    operations: list[
        Literal[
            "Auth:Logs:Read",
            "Auth:Users:Create",
            "Auth:Users:Read",
            "Auth:Users:Update",
            "Auth:Users:Activate",
            "Auth:Users:Deactivate",
            "Auth:Users:Delete",
            "Auth:ServiceAccounts:Create",
            "Auth:ServiceAccounts:Read",
            "Auth:ServiceAccounts:Update",
            "Auth:ServiceAccounts:Activate",
            "Auth:ServiceAccounts:Deactivate",
            "Auth:ServiceAccounts:Delete",
            "Auth:Pats:Create",
            "Auth:Delegated:Register",
            "Auth:Delegated:Login",
            "Auth:Delegated:Recover",
            "Agreements:Read",
            "Agreements:Accept",
            "Exchanges:Create",
            "Exchanges:Read",
            "Exchanges:Delete",
            "Exchanges:Deposits:Create",
            "Exchanges:Withdrawals:Create",
            "FeeSponsors:Create",
            "FeeSponsors:Read",
            "FeeSponsors:Update",
            "FeeSponsors:Delete",
            "FeeSponsors:Use",
            "Orgs:Read",
            "Orgs:Update",
            "Orgs:Settings:Read",
            "Orgs:Settings:Update",
            "Permissions:Create",
            "Permissions:Read",
            "Permissions:Update",
            "Permissions:Assign",
            "Permissions:Revoke",
            "Permissions:Delete",
            "Permissions:Assignments:Read",
            "Policies:Create",
            "Policies:Read",
            "Policies:Update",
            "Policies:Delete",
            "Policies:Evaluations:Read",
            "Policies:Evaluations:Vote",
            "Registry:Addresses:Create",
            "Registry:Addresses:Read",
            "Registry:Addresses:Update",
            "Registry:Addresses:Delete",
            "Registry:ContractSchemas:Create",
            "Registry:ContractSchemas:Read",
            "Registry:ContractSchemas:Delete",
            "Stakes:Create",
            "Stakes:Read",
            "Stakes:Update",
            "Swaps:Create",
            "Swaps:Read",
            "Payouts:Create",
            "Payouts:Read",
            "Payouts:Update",
            "Payins:Create",
            "Payins:Read",
            "Allocations:Create",
            "Allocations:Update",
            "Allocations:Read",
            "Keys:Create",
            "Keys:Read",
            "Keys:Update",
            "Keys:Reuse",
            "Keys:Delegate",
            "Keys:Import",
            "Keys:Export",
            "Keys:Delete",
            "Keys:Vrf:Derive",
            "Keys:ChildKeys:Create",
            "Keys:Signatures:Create",
            "Keys:Signatures:Read",
            "KeyStores:Read",
            "KeyStores:Instructions:Cancel",
            "KeyStores:Instructions:Fleets:Create",
            "KeyStores:Instructions:Fleets:Clone",
            "KeyStores:Instructions:Fleets:Users:Add",
            "KeyStores:Instructions:Fleets:Keys:Harvest",
            "KeyStores:Instructions:Fleets:Provisioners:Add",
            "KeyStores:Instructions:Keys:ProveControl",
            "KeyStores:Instructions:Keys:Sign",
            "Networks:Canton:Validators:Create",
            "Networks:Canton:Validators:Read",
            "Networks:Canton:Validators:Update",
            "Networks:Canton:Validators:Delete",
            "Wallets:Create",
            "Wallets:Read",
            "Wallets:Update",
            "Wallets:Tags:Add",
            "Wallets:Tags:Remove",
            "Wallets:Transactions:Create",
            "Wallets:Transactions:Read",
            "Wallets:Transactions:Abort",
            "Wallets:Transfers:Create",
            "Wallets:Transfers:Read",
            "Wallets:Transfers:Abort",
            "Wallets:Offers:Read",
            "Wallets:Offers:Settle",
            "AddressWatches:Create",
            "AddressWatches:Read",
            "Vaults:Create",
            "Vaults:Read",
            "Vaults:Update",
            "Vaults:Tags:Add",
            "Vaults:Tags:Remove",
            "Vaults:Quarantines:Release",
            "Vaults:Locks:Create",
            "Vaults:Locks:Release",
            "Vaults:Transfers:Create",
            "Webhooks:Create",
            "Webhooks:Read",
            "Webhooks:Update",
            "Webhooks:Delete",
            "Webhooks:Ping",
            "Webhooks:Events:Read",
            "Billing:Read",
            "Billing:Manage",
            "Activities:Read",
            "Analytics:Read",
        ]
        | Literal[
            "Auth:Register:Delegated",
            "Auth:Login:Delegated",
            "Auth:Recover:Delegated",
            "Agreements:Acceptance:Create",
            "Agreements:Acceptance:Read",
            "Events:Read",
            "Permissions:Archive",
            "Policies:Archive",
            "Policies:Approvals:Read",
            "Policies:Approvals:Approve",
            "Signers:ListSigners",
            "Payouts:Write",
            "Keys:Derive",
            "Networks:CantonValidators:Create",
            "Networks:CantonValidators:Read",
            "Networks:CantonValidators:Update",
            "Networks:CantonValidators:Delete",
            "Wallets:Tags:Delete",
            "Vaults:Tags:Delete",
            "Vaults:Addresses:Create",
            "Vaults:Locks:Delete",
            "Billing:Write",
            "KeyStores:Fleets:Cancel",
            "KeyStores:Fleets:Create",
            "KeyStores:Fleets:Clone",
            "KeyStores:Fleets:AddMacUser",
            "KeyStores:Fleets:AddProvisioner",
            "KeyStores:Fleets:KeyHarvest",
            "KeyStores:ProofOfControl:Create",
            "KeyStores:OnchainSignatures:Create",
            "Tenant:Billing:Write",
            "Tenant:Settings:Write",
        ]
    ]


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


class RevokePermissionQuery(TypedDict, total=False):
    """revokePermission query parameters."""

    force: NotRequired[bool]


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
    pending_change_request: NotRequired[dict[str, Any]]


class UpdatePermissionRequest(TypedDict, total=False):
    """updatePermission request body."""

    name: NotRequired[str]
    operations: NotRequired[
        list[
            Literal[
                "Auth:Logs:Read",
                "Auth:Users:Create",
                "Auth:Users:Read",
                "Auth:Users:Update",
                "Auth:Users:Activate",
                "Auth:Users:Deactivate",
                "Auth:Users:Delete",
                "Auth:ServiceAccounts:Create",
                "Auth:ServiceAccounts:Read",
                "Auth:ServiceAccounts:Update",
                "Auth:ServiceAccounts:Activate",
                "Auth:ServiceAccounts:Deactivate",
                "Auth:ServiceAccounts:Delete",
                "Auth:Pats:Create",
                "Auth:Delegated:Register",
                "Auth:Delegated:Login",
                "Auth:Delegated:Recover",
                "Agreements:Read",
                "Agreements:Accept",
                "Exchanges:Create",
                "Exchanges:Read",
                "Exchanges:Delete",
                "Exchanges:Deposits:Create",
                "Exchanges:Withdrawals:Create",
                "FeeSponsors:Create",
                "FeeSponsors:Read",
                "FeeSponsors:Update",
                "FeeSponsors:Delete",
                "FeeSponsors:Use",
                "Orgs:Read",
                "Orgs:Update",
                "Orgs:Settings:Read",
                "Orgs:Settings:Update",
                "Permissions:Create",
                "Permissions:Read",
                "Permissions:Update",
                "Permissions:Assign",
                "Permissions:Revoke",
                "Permissions:Delete",
                "Permissions:Assignments:Read",
                "Policies:Create",
                "Policies:Read",
                "Policies:Update",
                "Policies:Delete",
                "Policies:Evaluations:Read",
                "Policies:Evaluations:Vote",
                "Registry:Addresses:Create",
                "Registry:Addresses:Read",
                "Registry:Addresses:Update",
                "Registry:Addresses:Delete",
                "Registry:ContractSchemas:Create",
                "Registry:ContractSchemas:Read",
                "Registry:ContractSchemas:Delete",
                "Stakes:Create",
                "Stakes:Read",
                "Stakes:Update",
                "Swaps:Create",
                "Swaps:Read",
                "Payouts:Create",
                "Payouts:Read",
                "Payouts:Update",
                "Payins:Create",
                "Payins:Read",
                "Allocations:Create",
                "Allocations:Update",
                "Allocations:Read",
                "Keys:Create",
                "Keys:Read",
                "Keys:Update",
                "Keys:Reuse",
                "Keys:Delegate",
                "Keys:Import",
                "Keys:Export",
                "Keys:Delete",
                "Keys:Vrf:Derive",
                "Keys:ChildKeys:Create",
                "Keys:Signatures:Create",
                "Keys:Signatures:Read",
                "KeyStores:Read",
                "KeyStores:Instructions:Cancel",
                "KeyStores:Instructions:Fleets:Create",
                "KeyStores:Instructions:Fleets:Clone",
                "KeyStores:Instructions:Fleets:Users:Add",
                "KeyStores:Instructions:Fleets:Keys:Harvest",
                "KeyStores:Instructions:Fleets:Provisioners:Add",
                "KeyStores:Instructions:Keys:ProveControl",
                "KeyStores:Instructions:Keys:Sign",
                "Networks:Canton:Validators:Create",
                "Networks:Canton:Validators:Read",
                "Networks:Canton:Validators:Update",
                "Networks:Canton:Validators:Delete",
                "Wallets:Create",
                "Wallets:Read",
                "Wallets:Update",
                "Wallets:Tags:Add",
                "Wallets:Tags:Remove",
                "Wallets:Transactions:Create",
                "Wallets:Transactions:Read",
                "Wallets:Transactions:Abort",
                "Wallets:Transfers:Create",
                "Wallets:Transfers:Read",
                "Wallets:Transfers:Abort",
                "Wallets:Offers:Read",
                "Wallets:Offers:Settle",
                "AddressWatches:Create",
                "AddressWatches:Read",
                "Vaults:Create",
                "Vaults:Read",
                "Vaults:Update",
                "Vaults:Tags:Add",
                "Vaults:Tags:Remove",
                "Vaults:Quarantines:Release",
                "Vaults:Locks:Create",
                "Vaults:Locks:Release",
                "Vaults:Transfers:Create",
                "Webhooks:Create",
                "Webhooks:Read",
                "Webhooks:Update",
                "Webhooks:Delete",
                "Webhooks:Ping",
                "Webhooks:Events:Read",
                "Billing:Read",
                "Billing:Manage",
                "Activities:Read",
                "Analytics:Read",
            ]
            | Literal[
                "Auth:Register:Delegated",
                "Auth:Login:Delegated",
                "Auth:Recover:Delegated",
                "Agreements:Acceptance:Create",
                "Agreements:Acceptance:Read",
                "Events:Read",
                "Permissions:Archive",
                "Policies:Archive",
                "Policies:Approvals:Read",
                "Policies:Approvals:Approve",
                "Signers:ListSigners",
                "Payouts:Write",
                "Keys:Derive",
                "Networks:CantonValidators:Create",
                "Networks:CantonValidators:Read",
                "Networks:CantonValidators:Update",
                "Networks:CantonValidators:Delete",
                "Wallets:Tags:Delete",
                "Vaults:Tags:Delete",
                "Vaults:Addresses:Create",
                "Vaults:Locks:Delete",
                "Billing:Write",
                "KeyStores:Fleets:Cancel",
                "KeyStores:Fleets:Create",
                "KeyStores:Fleets:Clone",
                "KeyStores:Fleets:AddMacUser",
                "KeyStores:Fleets:AddProvisioner",
                "KeyStores:Fleets:KeyHarvest",
                "KeyStores:ProofOfControl:Create",
                "KeyStores:OnchainSignatures:Create",
                "Tenant:Billing:Write",
                "Tenant:Settings:Write",
            ]
        ]
    ]


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
