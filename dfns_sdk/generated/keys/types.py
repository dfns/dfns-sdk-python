"""Types for the keys domain."""

from typing import Any, Literal, TypedDict, cast
from typing_extensions import NotRequired, deprecated


class ListKeysResponse(TypedDict, total=False):
    """listKeys response."""

    items: list[dict[str, Any]]
    next_page_token: NotRequired[str]

class ListKeysQuery(TypedDict, total=False):
    """listKeys query parameters."""

    limit: NotRequired[int]
    pagination_token: NotRequired[str]
    owner: NotRequired[str]

class CreateKeyRequest(TypedDict, total=False):
    """createKey request body."""

    scheme: Literal["ECDSA", "EdDSA", "Schnorr"]
    curve: Literal["ed25519", "secp256k1", "stark"]
    name: NotRequired[str]
    master_key: NotRequired[bool]
    derive_from: NotRequired[dict[str, Any]]
    store_id: NotRequired[str]
    delegate_to: NotRequired[str]
    delay_delegation: NotRequired[bool]

class CreateKeyResponse(TypedDict, total=False):
    """createKey response."""

    id: str
    scheme: Literal["ECDSA", "EdDSA", "Schnorr"]
    curve: Literal["ed25519", "secp256k1", "stark"]
    public_key: str
    master_key: NotRequired[bool]
    derived_from: NotRequired[dict[str, Any]]
    name: NotRequired[str]
    status: Literal["Active", "Archived"]
    custodial: bool
    date_created: str
    imported: NotRequired[bool]
    exported: NotRequired[bool]
    date_exported: NotRequired[str]
    date_deleted: NotRequired[str]

class DelegateKeyRequest(TypedDict, total=False):
    """delegateKey request body."""

    delegate_to: str

class DelegateKeyResponse(TypedDict, total=False):
    """delegateKey response."""

    key_id: str
    status: Literal["Delegated"]

class GetKeyResponse(TypedDict, total=False):
    """getKey response."""

    id: str
    scheme: Literal["ECDSA", "EdDSA", "Schnorr"]
    curve: Literal["ed25519", "secp256k1", "stark"]
    public_key: str
    master_key: NotRequired[bool]
    derived_from: NotRequired[dict[str, Any]]
    name: NotRequired[str]
    status: Literal["Active", "Archived"]
    custodial: bool
    date_created: str
    imported: NotRequired[bool]
    exported: NotRequired[bool]
    date_exported: NotRequired[str]
    date_deleted: NotRequired[str]
    wallets: list[dict[str, Any]]
    store: dict[str, Any]

class UpdateKeyRequest(TypedDict, total=False):
    """updateKey request body."""

    name: Any

class UpdateKeyResponse(TypedDict, total=False):
    """updateKey response."""

    id: str
    scheme: Literal["ECDSA", "EdDSA", "Schnorr"]
    curve: Literal["ed25519", "secp256k1", "stark"]
    public_key: str
    master_key: NotRequired[bool]
    derived_from: NotRequired[dict[str, Any]]
    name: NotRequired[str]
    status: Literal["Active", "Archived"]
    custodial: bool
    date_created: str
    imported: NotRequired[bool]
    exported: NotRequired[bool]
    date_exported: NotRequired[str]
    date_deleted: NotRequired[str]

class DeleteKeyResponse(TypedDict, total=False):
    """deleteKey response."""

    id: str
    scheme: Literal["ECDSA", "EdDSA", "Schnorr"]
    curve: Literal["ed25519", "secp256k1", "stark"]
    public_key: str
    master_key: NotRequired[bool]
    derived_from: NotRequired[dict[str, Any]]
    name: NotRequired[str]
    status: Literal["Active", "Archived"]
    custodial: bool
    date_created: str
    imported: NotRequired[bool]
    exported: NotRequired[bool]
    date_exported: NotRequired[str]
    date_deleted: NotRequired[str]

class DeriveKeyRequest(TypedDict, total=False):
    """deriveKey request body."""

    domain: str
    seed: str

class DeriveKeyResponse(TypedDict, total=False):
    """deriveKey response."""

    output: str

class ExportKeyRequest(TypedDict, total=False):
    """exportKey request body."""

    encryption_key: str
    supported_schemes: list[dict[str, Any]]

class ExportKeyResponse(TypedDict, total=False):
    """exportKey response."""

    public_key: str
    protocol: Literal["CGGMP24", "FROST", "FROST_BITCOIN", "GLOW20_DH", "KU23"] | Literal["CGGMP21"]
    curve: Literal["ed25519", "secp256k1", "stark"]
    min_signers: float
    encrypted_key_shares: list[dict[str, Any]]

class ListSignaturesResponse(TypedDict, total=False):
    """listSignatures response."""

    items: list[dict[str, Any]]
    next_page_token: NotRequired[str]
    key_id: str

class ListSignaturesQuery(TypedDict, total=False):
    """listSignatures query parameters."""

    limit: NotRequired[int]
    pagination_token: NotRequired[str]

class GenerateSignatureResponse(TypedDict, total=False):
    """generateSignature response."""

    id: str
    key_id: str
    requester: dict[str, Any]
    request_body: dict[str, Any]
    status: Literal["Pending", "Executing", "Signed", "Confirmed", "Failed", "Rejected"]
    reason: NotRequired[str]
    signature: NotRequired[dict[str, Any]]
    signatures: NotRequired[list[dict[str, Any]]]
    signed_data: NotRequired[str]
    network: NotRequired[Literal["Algorand", "AlgorandTestnet", "Aptos", "AptosTestnet", "ArbitrumOne", "ArbitrumSepolia", "ArcTestnet", "AvalancheC", "AvalancheCFuji", "BabylonGenesis", "BabylonTestnet5", "Base", "BaseSepolia", "Berachain", "BerachainBepolia", "Bitcoin", "BitcoinSignet", "BitcoinTestnet4", "BitcoinCash", "Bob", "BobSepolia", "Bsc", "BscTestnet", "Canton", "CantonTestnet", "Cardano", "CardanoPreprod", "Concordium", "ConcordiumTestnet", "Celo", "CeloAlfajores", "Codex", "CodexSepolia", "CosmosHub4", "CosmosIcsTestnet", "Dogecoin", "DogecoinTestnet", "Ethereum", "EthereumClassic", "EthereumClassicMordor", "EthereumSepolia", "EthereumHoodi", "FlareC", "FlareCCoston2", "FlowEvm", "FlowEvmTestnet", "Hedera", "HederaTestnet", "Ink", "InkSepolia", "InternetComputer", "Ion", "IonTestnet", "Iota", "IotaTestnet", "Kusama", "KusamaAssetHub", "Litecoin", "LitecoinTestnet", "Movement", "MovementTestnet", "Near", "NearTestnet", "Optimism", "OptimismSepolia", "Origyn", "Plasma", "PlasmaTestnet", "Plume", "PlumeSepolia", "Paseo", "PaseoAssetHub", "Polkadot", "PolkadotAssetHub", "Polygon", "PolygonAmoy", "Polymesh", "PolymeshTestnet", "Race", "RaceSepolia", "Robinhood", "RobinhoodSepolia", "SeiAtlantic2", "SeiPacific1", "Solana", "SolanaDevnet", "Sonic", "SonicTestnet", "Starknet", "StarknetSepolia", "Stellar", "StellarTestnet", "Sui", "SuiTestnet", "Tezos", "TezosGhostnet", "TezosShadownet", "Tempo", "TempoModerato", "Tsc", "TscTestnet1", "Ton", "TonTestnet", "Tron", "TronNile", "Westend", "WestendAssetHub", "Xdc", "XdcApothem", "XLayer", "XLayerSepolia", "XrpLedger", "XrpLedgerTestnet"]]
    tx_hash: NotRequired[str]
    fee: NotRequired[str]
    approval_id: NotRequired[str]
    date_requested: str
    date_policy_resolved: NotRequired[str]
    date_signed: NotRequired[str]
    date_confirmed: NotRequired[str]
    external_id: NotRequired[str]
    details: NotRequired[dict[str, dict[str, Any]]]

class GetSignatureResponse(TypedDict, total=False):
    """getSignature response."""

    id: str
    key_id: str
    requester: dict[str, Any]
    request_body: dict[str, Any]
    status: Literal["Pending", "Executing", "Signed", "Confirmed", "Failed", "Rejected"]
    reason: NotRequired[str]
    signature: NotRequired[dict[str, Any]]
    signatures: NotRequired[list[dict[str, Any]]]
    signed_data: NotRequired[str]
    network: NotRequired[Literal["Algorand", "AlgorandTestnet", "Aptos", "AptosTestnet", "ArbitrumOne", "ArbitrumSepolia", "ArcTestnet", "AvalancheC", "AvalancheCFuji", "BabylonGenesis", "BabylonTestnet5", "Base", "BaseSepolia", "Berachain", "BerachainBepolia", "Bitcoin", "BitcoinSignet", "BitcoinTestnet4", "BitcoinCash", "Bob", "BobSepolia", "Bsc", "BscTestnet", "Canton", "CantonTestnet", "Cardano", "CardanoPreprod", "Concordium", "ConcordiumTestnet", "Celo", "CeloAlfajores", "Codex", "CodexSepolia", "CosmosHub4", "CosmosIcsTestnet", "Dogecoin", "DogecoinTestnet", "Ethereum", "EthereumClassic", "EthereumClassicMordor", "EthereumSepolia", "EthereumHoodi", "FlareC", "FlareCCoston2", "FlowEvm", "FlowEvmTestnet", "Hedera", "HederaTestnet", "Ink", "InkSepolia", "InternetComputer", "Ion", "IonTestnet", "Iota", "IotaTestnet", "Kusama", "KusamaAssetHub", "Litecoin", "LitecoinTestnet", "Movement", "MovementTestnet", "Near", "NearTestnet", "Optimism", "OptimismSepolia", "Origyn", "Plasma", "PlasmaTestnet", "Plume", "PlumeSepolia", "Paseo", "PaseoAssetHub", "Polkadot", "PolkadotAssetHub", "Polygon", "PolygonAmoy", "Polymesh", "PolymeshTestnet", "Race", "RaceSepolia", "Robinhood", "RobinhoodSepolia", "SeiAtlantic2", "SeiPacific1", "Solana", "SolanaDevnet", "Sonic", "SonicTestnet", "Starknet", "StarknetSepolia", "Stellar", "StellarTestnet", "Sui", "SuiTestnet", "Tezos", "TezosGhostnet", "TezosShadownet", "Tempo", "TempoModerato", "Tsc", "TscTestnet1", "Ton", "TonTestnet", "Tron", "TronNile", "Westend", "WestendAssetHub", "Xdc", "XdcApothem", "XLayer", "XLayerSepolia", "XrpLedger", "XrpLedgerTestnet"]]
    tx_hash: NotRequired[str]
    fee: NotRequired[str]
    approval_id: NotRequired[str]
    date_requested: str
    date_policy_resolved: NotRequired[str]
    date_signed: NotRequired[str]
    date_confirmed: NotRequired[str]
    external_id: NotRequired[str]
    details: NotRequired[dict[str, dict[str, Any]]]

class ImportKeyRequest(TypedDict, total=False):
    """importKey request body."""

    name: NotRequired[str]
    curve: Literal["ed25519", "secp256k1", "stark"]
    protocol: Literal["CGGMP24", "FROST", "FROST_BITCOIN", "GLOW20_DH", "KU23"] | Literal["CGGMP21"]
    min_signers: int
    encrypted_key_shares: list[dict[str, Any]]
    master_key: NotRequired[bool]

class ImportKeyResponse(TypedDict, total=False):
    """importKey response."""

    id: str
    scheme: Literal["ECDSA", "EdDSA", "Schnorr"]
    curve: Literal["ed25519", "secp256k1", "stark"]
    public_key: str
    master_key: NotRequired[bool]
    derived_from: NotRequired[dict[str, Any]]
    name: NotRequired[str]
    status: Literal["Active", "Archived"]
    custodial: bool
    date_created: str
    imported: NotRequired[bool]
    exported: NotRequired[bool]
    date_exported: NotRequired[str]
    date_deleted: NotRequired[str]
