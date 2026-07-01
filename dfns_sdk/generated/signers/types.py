"""Types for the signers domain."""

from typing import Any, Literal, TypedDict, cast
from typing_extensions import NotRequired, deprecated


class CreateAddMacUserInputRequest(TypedDict, total=False):
    """createAddMacUserInput request body."""

    kind: Literal["AddMacUser"]
    mac_target_serial: str
    hsm_target_serial: str

class CreateCloneInputRequest(TypedDict, total=False):
    """createCloneInput request body."""

    kind: Literal["Clone"]
    hsm_source_serial: str
    hsm_target_serial: str
    mac_target_serial: NotRequired[str]

class CreateGenesisInputRequest(TypedDict, total=False):
    """createGenesisInput request body."""

    kind: Literal["Genesis"]
    num_provisioners: int
    num_secp256k1: int
    num_ed25519: int
    hsm_genesis_serial: str
    mac_genesis_serial: NotRequired[str]
    hsm_genesis_firmware_version: NotRequired[Literal["2.2", "2.4"]]

class CreateOnchainSignInputRequest(TypedDict, total=False):
    """createOnchainSignInput request body."""

    pass

class CreateProofOfControlInputRequest(TypedDict, total=False):
    """createProofOfControlInput request body."""

    wallet_ids: list[str]

class ListKeyStoresResponse(TypedDict, total=False):
    """listKeyStores response."""

    items: list[dict[str, Any]]

class ListSignersResponse(TypedDict, total=False):
    """listSigners response."""

    clusters: list[dict[str, Any]]

class SubmitAddMacUserOutputRequest(TypedDict, total=False):
    """submitAddMacUserOutput request body."""

    file_checksum: str
    output_json: dict[str, Any]

class SubmitAddMacUserOutputResponse(TypedDict, total=False):
    """submitAddMacUserOutput response."""

    message: str

class SubmitCloneOutputRequest(TypedDict, total=False):
    """submitCloneOutput request body."""

    file_checksum: str
    output_json: dict[str, Any]

class SubmitCloneOutputResponse(TypedDict, total=False):
    """submitCloneOutput response."""

    message: str

class SubmitGenesisOutputRequest(TypedDict, total=False):
    """submitGenesisOutput request body."""

    file_checksum: str
    output_json: dict[str, Any]

class SubmitGenesisOutputResponse(TypedDict, total=False):
    """submitGenesisOutput response."""

    message: str

class SubmitOnchainSignOutputRequest(TypedDict, total=False):
    """submitOnchainSignOutput request body."""

    file_checksum: str
    output_json: dict[str, Any]

class SubmitOnchainSignOutputResponse(TypedDict, total=False):
    """submitOnchainSignOutput response."""

    status: Literal["success", "partial"]

class SubmitProofOfControlOutputRequest(TypedDict, total=False):
    """submitProofOfControlOutput request body."""

    file_checksum: str
    output_json: dict[str, Any]

class SubmitProofOfControlOutputResponse(TypedDict, total=False):
    """submitProofOfControlOutput response."""

    status: Literal["success", "partial"]
