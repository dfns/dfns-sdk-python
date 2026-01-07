"""Types for the signers domain."""

from typing import Any, Literal, NotRequired, Optional, TypedDict, Union

class ListKeyStoresResponse(TypedDict, total=False):
    """listKeyStores response."""

    items: list[TypedDict]

class ListSignersResponse(TypedDict, total=False):
    """listSigners response."""

    clusters: list[TypedDict]
