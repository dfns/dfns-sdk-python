"""Webhooks domain module."""

from .client import WebhooksClient
from .delegated_client import DelegatedWebhooksClient
from . import types

__all__ = ["WebhooksClient", "DelegatedWebhooksClient", "types"]
