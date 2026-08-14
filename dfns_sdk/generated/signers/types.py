"""Types for the signers domain."""

from typing import Any, Literal, TypedDict

from typing_extensions import NotRequired


class CancelFleetOperationRequest(TypedDict, total=False):
    """cancelFleetOperation request body."""

    group_id: str
    reason: NotRequired[str]


class CancelFleetOperationResponse(TypedDict, total=False):
    """cancelFleetOperation response."""

    group_id: str
    store_id: str
    org_id: str
    status: Literal["Initialized", "InReview", "Rejected", "Approved", "Canceled"]
    created_by: str
    submitted_by: Any
    date_submitted: Any
    reviewed_by: Any
    date_reviewed: Any
    canceled_by: Any
    date_canceled: Any
    reason: Any
    date_created: str
    operations: list[dict[str, Any]]


class CreateAddMacUserInputRequest(TypedDict, total=False):
    """createAddMacUserInput request body."""

    kind: Literal["AddMacUser"]
    mac_target_serial: str
    hsm_target_serial: str


class CreateAddProvisionerInputRequest(TypedDict, total=False):
    """createAddProvisionerInput request body."""

    kind: Literal["AddProvisioner"]
    yubikey_serial: str
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
    num_operational: int
    num_secp256k1: int
    num_ed25519: int
    hsm_genesis_serial: str
    mac_genesis_serial: NotRequired[str]
    hsm_genesis_firmware_version: NotRequired[Literal["2.4"]]
    debug_options: NotRequired[dict[str, Any]]


class CreateKeyHarvestInputRequest(TypedDict, total=False):
    """createKeyHarvestInput request body."""

    kind: Literal["KeyHarvest"]
    hsm_target_serial: str
    mac_target_serial: str
    mac_target_username: str
    num_secp256k1: NotRequired[int]
    num_ed25519: NotRequired[int]


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


class SubmitAddProvisionerOutputRequest(TypedDict, total=False):
    """submitAddProvisionerOutput request body."""

    file_checksum: str
    output_json: dict[str, Any]


class SubmitAddProvisionerOutputResponse(TypedDict, total=False):
    """submitAddProvisionerOutput response."""

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


class SubmitKeyHarvestOutputRequest(TypedDict, total=False):
    """submitKeyHarvestOutput request body."""

    file_checksum: str
    output_json: dict[str, Any]


class SubmitKeyHarvestOutputResponse(TypedDict, total=False):
    """submitKeyHarvestOutput response."""

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
