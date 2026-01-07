"""Client for the webhooks domain."""

from typing import Any, Literal, Optional, TypedDict, Union

from ..._internal import HttpClient
from . import types as T


class WebhooksClient:
    """Client for webhooks operations."""

    def __init__(self, http_client: HttpClient):
        self._http = http_client

    def list_webhooks(self, query: Optional[T.ListWebhooksQuery] = None) -> T.ListWebhooksResponse:
        """
        List Webhooks.

        List all webhooks for the authenticated user's organization. The results are paginated.

        Args:
        query: Query parameters.

        Returns:
            T.ListWebhooksResponse: The API response.
        """
        return self._http.request(
            method="GET",
            path="/webhooks",
            path_params={},
            query_params=query,
            body=None,
            requires_signature=False,
        )

    def create_webhook(self, body: T.CreateWebhookRequest) -> T.CreateWebhookResponse:
        """
        Create Webhook.

        Register a new webhook.

        Args:
        body: Request body.

        Returns:
            T.CreateWebhookResponse: The API response.
        """
        return self._http.request(
            method="POST",
            path="/webhooks",
            path_params={},
            query_params=None,
            body=body,
            requires_signature=True,
        )

    def get_webhook(self, webhook_id: str) -> T.GetWebhookResponse:
        """
        Get Webhook.

        Retrieve information about a specific webhook.

        Args:
        webhook_id: Path parameter.

        Returns:
            T.GetWebhookResponse: The API response.
        """
        return self._http.request(
            method="GET",
            path="/webhooks/{webhookId}",
            path_params={"webhookId": webhook_id},
            query_params=None,
            body=None,
            requires_signature=False,
        )

    def update_webhook(self, webhook_id: str, body: T.UpdateWebhookRequest) -> T.UpdateWebhookResponse:
        """
        Update Webhook.

        Update the definition of an existing webhook.

        Args:
        webhook_id: Path parameter.
        body: Request body.

        Returns:
            T.UpdateWebhookResponse: The API response.
        """
        return self._http.request(
            method="PUT",
            path="/webhooks/{webhookId}",
            path_params={"webhookId": webhook_id},
            query_params=None,
            body=body,
            requires_signature=True,
        )

    def delete_webhook(self, webhook_id: str) -> T.DeleteWebhookResponse:
        """
        Delete Webhook.

        Deletes an existing webhook registration.

        Args:
        webhook_id: Path parameter.

        Returns:
            T.DeleteWebhookResponse: The API response.
        """
        return self._http.request(
            method="DELETE",
            path="/webhooks/{webhookId}",
            path_params={"webhookId": webhook_id},
            query_params=None,
            body=None,
            requires_signature=True,
        )

    def ping_webhook(self, webhook_id: str) -> T.PingWebhookResponse:
        """
        Ping Webhook.

        This endpoint is meant for webhook setup and troubleshooting. Calling the endpoint will trigger a fake test event that will be pushed to the webhook url. The fake event will not be saved and not appear in further requests to Webhook Events.

        Args:
        webhook_id: Path parameter.

        Returns:
            T.PingWebhookResponse: The API response.
        """
        return self._http.request(
            method="POST",
            path="/webhooks/{webhookId}/ping",
            path_params={"webhookId": webhook_id},
            query_params=None,
            body=None,
            requires_signature=True,
        )

    def get_webhook_event(self, webhook_id: str, webhook_event_id: str) -> T.GetWebhookEventResponse:
        """
        Get Webhook Event.

        Retrieve a specific webhook event details by its ID.
  
<Warning>
We only keep a trace of those Webhook Events in our system for a **retention period of 31 days**. Past that, they are discarded, so you cannot see them using [List Webhook Events](https://docs.dfns.co/api-reference/webhooks/list-webhook-events) or [Get Webhook Event](https://docs.dfns.co/api-reference/webhooks/get-webhook-event) endpoints.
</Warning>

        Args:
        webhook_id: Path parameter.
        webhook_event_id: Path parameter.

        Returns:
            T.GetWebhookEventResponse: The API response.
        """
        return self._http.request(
            method="GET",
            path="/webhooks/{webhookId}/events/{webhookEventId}",
            path_params={"webhookId": webhook_id, "webhookEventId": webhook_event_id},
            query_params=None,
            body=None,
            requires_signature=False,
        )

    def list_webhook_events(self, webhook_id: str, query: Optional[T.ListWebhookEventsQuery] = None) -> T.ListWebhookEventsResponse:
        """
        List Webhook Events.

        Lists all events for a given webhook. 


<Warning>
We only keep a trace of those Webhook Events in our system for a **retention period of 31 days**. Past that, they are discarded, so you cannot see them using [List Webhook Events](https://docs.dfns.co/api-reference/webhooks/list-webhook-events) or [Get Webhook Event](https://docs.dfns.co/api-reference/webhooks/get-webhook-event) endpoints.
</Warning>

        Args:
        webhook_id: Path parameter.
        query: Query parameters.

        Returns:
            T.ListWebhookEventsResponse: The API response.
        """
        return self._http.request(
            method="GET",
            path="/webhooks/{webhookId}/events",
            path_params={"webhookId": webhook_id},
            query_params=query,
            body=None,
            requires_signature=False,
        )
