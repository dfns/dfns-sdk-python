"""Types for the webhooks domain."""

from typing import Any, Literal, NotRequired, Optional, TypedDict, Union

class ListWebhooksResponse(TypedDict, total=False):
    """listWebhooks response."""

    items: list[TypedDict]
    next_page_token: NotRequired[str]

class ListWebhooksQuery(TypedDict, total=False):
    """listWebhooks query parameters."""

    limit: NotRequired[int]
    pagination_token: NotRequired[str]

class CreateWebhookRequest(TypedDict, total=False):
    """createWebhook request body."""

    url: str
    status: NotRequired[Literal["Enabled", "Disabled"]]
    description: NotRequired[str]
    events: list[Union[Literal["policy.triggered", "policy.approval.pending", "policy.approval.resolved", "key.created", "key.deleted", "key.delegated", "key.exported", "wallet.blockchainevent.detected", "wallet.created", "wallet.activated", "wallet.delegated", "wallet.exported", "wallet.signature.failed", "wallet.signature.rejected", "wallet.signature.requested", "wallet.signature.signed", "wallet.transaction.broadcasted", "wallet.transaction.confirmed", "wallet.transaction.failed", "wallet.transaction.rejected", "wallet.transaction.requested", "wallet.transfer.broadcasted", "wallet.transfer.confirmed", "wallet.transfer.failed", "wallet.transfer.rejected", "wallet.transfer.requested", "wallet.offer.received", "wallet.offer.accepted", "wallet.offer.rejected", "wallet.tags.modified"], Literal["*"]]]

class CreateWebhookResponse(TypedDict, total=False):
    """createWebhook response."""

    id: str
    url: str
    events: list[Union[Literal["policy.triggered", "policy.approval.pending", "policy.approval.resolved", "key.created", "key.deleted", "key.delegated", "key.exported", "wallet.blockchainevent.detected", "wallet.created", "wallet.activated", "wallet.delegated", "wallet.exported", "wallet.signature.failed", "wallet.signature.rejected", "wallet.signature.requested", "wallet.signature.signed", "wallet.transaction.broadcasted", "wallet.transaction.confirmed", "wallet.transaction.failed", "wallet.transaction.rejected", "wallet.transaction.requested", "wallet.transfer.broadcasted", "wallet.transfer.confirmed", "wallet.transfer.failed", "wallet.transfer.rejected", "wallet.transfer.requested", "wallet.offer.received", "wallet.offer.accepted", "wallet.offer.rejected", "wallet.tags.modified"], Literal["*"]]]
    status: Literal["Enabled", "Disabled"]
    description: NotRequired[str]
    date_created: str
    date_updated: str
    secret: str

class GetWebhookResponse(TypedDict, total=False):
    """getWebhook response."""

    id: str
    url: str
    events: list[Union[Literal["policy.triggered", "policy.approval.pending", "policy.approval.resolved", "key.created", "key.deleted", "key.delegated", "key.exported", "wallet.blockchainevent.detected", "wallet.created", "wallet.activated", "wallet.delegated", "wallet.exported", "wallet.signature.failed", "wallet.signature.rejected", "wallet.signature.requested", "wallet.signature.signed", "wallet.transaction.broadcasted", "wallet.transaction.confirmed", "wallet.transaction.failed", "wallet.transaction.rejected", "wallet.transaction.requested", "wallet.transfer.broadcasted", "wallet.transfer.confirmed", "wallet.transfer.failed", "wallet.transfer.rejected", "wallet.transfer.requested", "wallet.offer.received", "wallet.offer.accepted", "wallet.offer.rejected", "wallet.tags.modified"], Literal["*"]]]
    status: Literal["Enabled", "Disabled"]
    description: NotRequired[str]
    date_created: str
    date_updated: str

class UpdateWebhookRequest(TypedDict, total=False):
    """updateWebhook request body."""

    url: NotRequired[str]
    description: NotRequired[str]
    events: NotRequired[list[Union[Literal["policy.triggered", "policy.approval.pending", "policy.approval.resolved", "key.created", "key.deleted", "key.delegated", "key.exported", "wallet.blockchainevent.detected", "wallet.created", "wallet.activated", "wallet.delegated", "wallet.exported", "wallet.signature.failed", "wallet.signature.rejected", "wallet.signature.requested", "wallet.signature.signed", "wallet.transaction.broadcasted", "wallet.transaction.confirmed", "wallet.transaction.failed", "wallet.transaction.rejected", "wallet.transaction.requested", "wallet.transfer.broadcasted", "wallet.transfer.confirmed", "wallet.transfer.failed", "wallet.transfer.rejected", "wallet.transfer.requested", "wallet.offer.received", "wallet.offer.accepted", "wallet.offer.rejected", "wallet.tags.modified"], Literal["*"]]]]
    status: NotRequired[Literal["Enabled", "Disabled"]]

class UpdateWebhookResponse(TypedDict, total=False):
    """updateWebhook response."""

    id: str
    url: str
    events: list[Union[Literal["policy.triggered", "policy.approval.pending", "policy.approval.resolved", "key.created", "key.deleted", "key.delegated", "key.exported", "wallet.blockchainevent.detected", "wallet.created", "wallet.activated", "wallet.delegated", "wallet.exported", "wallet.signature.failed", "wallet.signature.rejected", "wallet.signature.requested", "wallet.signature.signed", "wallet.transaction.broadcasted", "wallet.transaction.confirmed", "wallet.transaction.failed", "wallet.transaction.rejected", "wallet.transaction.requested", "wallet.transfer.broadcasted", "wallet.transfer.confirmed", "wallet.transfer.failed", "wallet.transfer.rejected", "wallet.transfer.requested", "wallet.offer.received", "wallet.offer.accepted", "wallet.offer.rejected", "wallet.tags.modified"], Literal["*"]]]
    status: Literal["Enabled", "Disabled"]
    description: NotRequired[str]
    date_created: str
    date_updated: str

class DeleteWebhookResponse(TypedDict, total=False):
    """deleteWebhook response."""

    deleted: Literal[True]

class PingWebhookResponse(TypedDict, total=False):
    """pingWebhook response."""

    status: str
    error: NotRequired[str]

class GetWebhookEventResponse(TypedDict, total=False):
    """getWebhookEvent response."""

    id: str
    date: str
    kind: Literal["policy.triggered", "policy.approval.pending", "policy.approval.resolved", "key.created", "key.deleted", "key.delegated", "key.exported", "wallet.blockchainevent.detected", "wallet.created", "wallet.activated", "wallet.delegated", "wallet.exported", "wallet.signature.failed", "wallet.signature.rejected", "wallet.signature.requested", "wallet.signature.signed", "wallet.transaction.broadcasted", "wallet.transaction.confirmed", "wallet.transaction.failed", "wallet.transaction.rejected", "wallet.transaction.requested", "wallet.transfer.broadcasted", "wallet.transfer.confirmed", "wallet.transfer.failed", "wallet.transfer.rejected", "wallet.transfer.requested", "wallet.offer.received", "wallet.offer.accepted", "wallet.offer.rejected", "wallet.tags.modified"]
    data: dict[str, dict[str, Any]]
    status: str
    error: NotRequired[str]
    timestamp_sent: int

class ListWebhookEventsResponse(TypedDict, total=False):
    """listWebhookEvents response."""

    items: list[TypedDict]
    next_page_token: NotRequired[str]

class ListWebhookEventsQuery(TypedDict, total=False):
    """listWebhookEvents query parameters."""

    kind: NotRequired[Literal["policy.triggered", "policy.approval.pending", "policy.approval.resolved", "key.created", "key.deleted", "key.delegated", "key.exported", "wallet.blockchainevent.detected", "wallet.created", "wallet.activated", "wallet.delegated", "wallet.exported", "wallet.signature.failed", "wallet.signature.rejected", "wallet.signature.requested", "wallet.signature.signed", "wallet.transaction.broadcasted", "wallet.transaction.confirmed", "wallet.transaction.failed", "wallet.transaction.rejected", "wallet.transaction.requested", "wallet.transfer.broadcasted", "wallet.transfer.confirmed", "wallet.transfer.failed", "wallet.transfer.rejected", "wallet.transfer.requested", "wallet.offer.received", "wallet.offer.accepted", "wallet.offer.rejected", "wallet.tags.modified"]]
    delivery_failed: NotRequired[Literal["true", "false"]]
    limit: NotRequired[int]
    pagination_token: NotRequired[str]
