"""AddressWatches domain module."""

from . import types
from .client import AddressWatchesClient
from .delegated_client import DelegatedAddressWatchesClient

__all__ = ["AddressWatchesClient", "DelegatedAddressWatchesClient", "types"]
