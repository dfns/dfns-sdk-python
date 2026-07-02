"""Wallets domain module."""

from . import types
from .client import WalletsClient
from .delegated_client import DelegatedWalletsClient

__all__ = ["WalletsClient", "DelegatedWalletsClient", "types"]
