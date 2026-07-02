"""Webhooks domain module."""

from . import types
from .client import WebhooksClient
from .delegated_client import DelegatedWebhooksClient

__all__ = ["WebhooksClient", "DelegatedWebhooksClient", "types"]
