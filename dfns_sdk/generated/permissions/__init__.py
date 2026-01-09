"""Permissions domain module."""

from .client import PermissionsClient
from .delegated_client import DelegatedPermissionsClient
from . import types

__all__ = ["PermissionsClient", "DelegatedPermissionsClient", "types"]
