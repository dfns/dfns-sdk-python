"""Types for the signers domain."""

from typing import Any, Literal, NotRequired, Optional, TypedDict, Union

class CreateCloneInputRequest(TypedDict, total=False):
    """createCloneInput request body."""

    kind: Literal["Clone"]
    hsm_source_serial: str
    hsm_target_serial: str

class CreateCloneInputResponse(TypedDict, total=False):
    """createCloneInput response."""

    input_json: TypedDict

class CreateGenesisInputRequest(TypedDict, total=False):
    """createGenesisInput request body."""

    kind: Literal["Genesis"]
    num_provisioners: int
    num_secp256k1: NotRequired[int]
    num_ed25519: NotRequired[int]
    hsm_genesis_serial: str

class CreateGenesisInputResponse(TypedDict, total=False):
    """createGenesisInput response."""

    input_json: TypedDict

class ListKeyStoresResponse(TypedDict, total=False):
    """listKeyStores response."""

    items: list[TypedDict]

class ListSignersResponse(TypedDict, total=False):
    """listSigners response."""

    clusters: list[TypedDict]

class SubmitCloneOutputRequest(TypedDict, total=False):
    """submitCloneOutput request body."""

    file_checksum: str
    output_json: TypedDict

class SubmitCloneOutputResponse(TypedDict, total=False):
    """submitCloneOutput response."""

    pass

class SubmitGenesisOutputRequest(TypedDict, total=False):
    """submitGenesisOutput request body."""

    file_checksum: str
    output_json: TypedDict

class SubmitGenesisOutputResponse(TypedDict, total=False):
    """submitGenesisOutput response."""

    pass
