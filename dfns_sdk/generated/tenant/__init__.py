"""Tenant domain module."""

from . import types
from .client import TenantClient
from .delegated_client import DelegatedTenantClient

__all__ = ["TenantClient", "DelegatedTenantClient", "types"]
