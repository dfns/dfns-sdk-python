"""Delegated client for the webhooks domain."""

import json
from typing import Any, Literal, Optional, TypedDict, Union

from ..._internal import HttpClient
from ...base_auth_api import (
    BaseAuthApi,
    SignUserActionChallengeRequest,
    UserActionChallengeResponse,
)
from . import types as T


class DelegatedWebhooksClient:
    """
    Delegated client for webhooks operations.

    This client separates user action signing into _init() and _complete() method pairs,
    allowing external systems to handle the signing process.
    """

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

    def create_webhook_init(self, body: T.CreateWebhookRequest) -> UserActionChallengeResponse:
        """
        Initialize Create Webhook.

        Creates a user action challenge for external signing.

        Args:
        body: Request body.

        Returns:
            UserActionChallengeResponse: The challenge to sign externally.
        """
        path = "/webhooks"
        payload = json.dumps(body, separators=(",", ":")) if body else ""

        return BaseAuthApi.create_user_action_challenge(
            self._http,
            user_action_http_method="POST",
            user_action_http_path=path,
            user_action_payload=payload,
        )

    def create_webhook_complete(self, body: T.CreateWebhookRequest, signed_challenge: SignUserActionChallengeRequest) -> T.CreateWebhookResponse:
        """
        Complete Create Webhook.

        Submits the signed challenge and makes the API request.

        Args:
        body: Request body.
        signed_challenge: The signed challenge from external signing.

        Returns:
            T.CreateWebhookResponse: The API response.
        """
        user_action_result = BaseAuthApi.sign_user_action_challenge(
            self._http, signed_challenge
        )
        user_action_token = user_action_result["userAction"]

        return self._http.request_with_user_action(
            method="POST",
            path="/webhooks",
            path_params={},
            query_params=None,
            body=body,
            user_action=user_action_token,
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

    def update_webhook_init(self, webhook_id: str, body: T.UpdateWebhookRequest) -> UserActionChallengeResponse:
        """
        Initialize Update Webhook.

        Creates a user action challenge for external signing.

        Args:
        webhook_id: Path parameter.
        body: Request body.

        Returns:
            UserActionChallengeResponse: The challenge to sign externally.
        """
        path = "/webhooks/{webhookId}"
        path = path.replace("{webhookId}", str(webhook_id))
        payload = json.dumps(body, separators=(",", ":")) if body else ""

        return BaseAuthApi.create_user_action_challenge(
            self._http,
            user_action_http_method="PUT",
            user_action_http_path=path,
            user_action_payload=payload,
        )

    def update_webhook_complete(self, webhook_id: str, body: T.UpdateWebhookRequest, signed_challenge: SignUserActionChallengeRequest) -> T.UpdateWebhookResponse:
        """
        Complete Update Webhook.

        Submits the signed challenge and makes the API request.

        Args:
        webhook_id: Path parameter.
        body: Request body.
        signed_challenge: The signed challenge from external signing.

        Returns:
            T.UpdateWebhookResponse: The API response.
        """
        user_action_result = BaseAuthApi.sign_user_action_challenge(
            self._http, signed_challenge
        )
        user_action_token = user_action_result["userAction"]

        return self._http.request_with_user_action(
            method="PUT",
            path="/webhooks/{webhookId}",
            path_params={"webhookId": webhook_id},
            query_params=None,
            body=body,
            user_action=user_action_token,
        )

    def delete_webhook_init(self, webhook_id: str) -> UserActionChallengeResponse:
        """
        Initialize Delete Webhook.

        Creates a user action challenge for external signing.

        Args:
        webhook_id: Path parameter.

        Returns:
            UserActionChallengeResponse: The challenge to sign externally.
        """
        path = "/webhooks/{webhookId}"
        path = path.replace("{webhookId}", str(webhook_id))
        payload = ""

        return BaseAuthApi.create_user_action_challenge(
            self._http,
            user_action_http_method="DELETE",
            user_action_http_path=path,
            user_action_payload=payload,
        )

    def delete_webhook_complete(self, webhook_id: str, signed_challenge: SignUserActionChallengeRequest) -> T.DeleteWebhookResponse:
        """
        Complete Delete Webhook.

        Submits the signed challenge and makes the API request.

        Args:
        webhook_id: Path parameter.
        signed_challenge: The signed challenge from external signing.

        Returns:
            T.DeleteWebhookResponse: The API response.
        """
        user_action_result = BaseAuthApi.sign_user_action_challenge(
            self._http, signed_challenge
        )
        user_action_token = user_action_result["userAction"]

        return self._http.request_with_user_action(
            method="DELETE",
            path="/webhooks/{webhookId}",
            path_params={"webhookId": webhook_id},
            query_params=None,
            body=None,
            user_action=user_action_token,
        )

    def ping_webhook_init(self, webhook_id: str) -> UserActionChallengeResponse:
        """
        Initialize Ping Webhook.

        Creates a user action challenge for external signing.

        Args:
        webhook_id: Path parameter.

        Returns:
            UserActionChallengeResponse: The challenge to sign externally.
        """
        path = "/webhooks/{webhookId}/ping"
        path = path.replace("{webhookId}", str(webhook_id))
        payload = ""

        return BaseAuthApi.create_user_action_challenge(
            self._http,
            user_action_http_method="POST",
            user_action_http_path=path,
            user_action_payload=payload,
        )

    def ping_webhook_complete(self, webhook_id: str, signed_challenge: SignUserActionChallengeRequest) -> T.PingWebhookResponse:
        """
        Complete Ping Webhook.

        Submits the signed challenge and makes the API request.

        Args:
        webhook_id: Path parameter.
        signed_challenge: The signed challenge from external signing.

        Returns:
            T.PingWebhookResponse: The API response.
        """
        user_action_result = BaseAuthApi.sign_user_action_challenge(
            self._http, signed_challenge
        )
        user_action_token = user_action_result["userAction"]

        return self._http.request_with_user_action(
            method="POST",
            path="/webhooks/{webhookId}/ping",
            path_params={"webhookId": webhook_id},
            query_params=None,
            body=None,
            user_action=user_action_token,
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
