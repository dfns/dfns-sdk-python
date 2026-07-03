"""Wallets domain module."""

from .client import WalletsClient
from .delegated_client import DelegatedWalletsClient
from . import types

__all__ = ["WalletsClient", "DelegatedWalletsClient", "types"]
