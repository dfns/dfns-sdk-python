"""Vaults domain module."""

from . import types
from .client import VaultsClient
from .delegated_client import DelegatedVaultsClient

__all__ = ["VaultsClient", "DelegatedVaultsClient", "types"]
