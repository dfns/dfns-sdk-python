"""Types for the wallets domain."""

from typing import Any, Literal, NotRequired, Optional, TypedDict, Union

class ActivateWalletResponse(TypedDict, total=False):
    """activateWallet response."""

    id: str
    wallet_id: str
    network: Literal["Algorand", "AlgorandTestnet", "Aptos", "AptosTestnet", "ArbitrumOne", "ArbitrumSepolia", "ArcTestnet", "AvalancheC", "AvalancheCFuji", "BabylonGenesis", "BabylonTestnet5", "Base", "BaseSepolia", "Berachain", "BerachainBepolia", "Bitcoin", "BitcoinSignet", "BitcoinTestnet3", "BitcoinCash", "Bob", "BobSepolia", "Bsc", "BscTestnet", "Canton", "CantonTestnet", "Cardano", "CardanoPreprod", "Concordium", "ConcordiumTestnet", "Celo", "CeloAlfajores", "Codex", "CodexSepolia", "CosmosHub4", "CosmosIcsTestnet", "Dogecoin", "Ethereum", "EthereumClassic", "EthereumClassicMordor", "EthereumGoerli", "EthereumSepolia", "EthereumHolesky", "EthereumHoodi", "FantomOpera", "FantomTestnet", "FlareC", "FlareCCoston2", "FlowEvm", "FlowEvmTestnet", "Hedera", "HederaTestnet", "Ink", "InkSepolia", "InternetComputer", "Ion", "IonTestnet", "Iota", "IotaTestnet", "Kaspa", "Kusama", "KusamaAssetHub", "Litecoin", "Near", "NearTestnet", "Optimism", "OptimismSepolia", "Origyn", "Plasma", "PlasmaTestnet", "Plume", "PlumeSepolia", "Paseo", "PaseoAssetHub", "Polkadot", "PolkadotAssetHub", "Polygon", "PolygonAmoy", "Polymesh", "PolymeshTestnet", "Race", "RaceSepolia", "SeiAtlantic2", "SeiPacific1", "Solana", "SolanaDevnet", "Starknet", "StarknetSepolia", "Stellar", "StellarTestnet", "Sui", "SuiTestnet", "Tezos", "TezosGhostnet", "TempoAndantino", "Tsc", "TscTestnet1", "Ton", "TonTestnet", "Tron", "TronNile", "Westend", "WestendAssetHub", "XrpLedger", "XrpLedgerTestnet"]
    requester: TypedDict
    request_body: TypedDict
    status: Literal["Pending", "Executing", "Broadcasted", "Confirmed", "Failed", "Rejected"]
    reason: NotRequired[str]
    tx_hash: NotRequired[str]
    fee: NotRequired[str]
    approval_id: NotRequired[str]
    date_requested: str
    date_policy_resolved: NotRequired[str]
    date_broadcasted: NotRequired[str]
    date_confirmed: NotRequired[str]
    external_id: NotRequired[str]

class ListTransactionsResponse(TypedDict, total=False):
    """listTransactions response."""

    wallet_id: str
    items: list[TypedDict]
    next_page_token: NotRequired[str]

class ListTransactionsQuery(TypedDict, total=False):
    """listTransactions query parameters."""

    limit: NotRequired[str]
    pagination_token: NotRequired[str]

class SignAndBroadcastTransactionResponse(TypedDict, total=False):
    """signAndBroadcastTransaction response."""

    id: str
    wallet_id: str
    network: Literal["Algorand", "AlgorandTestnet", "Aptos", "AptosTestnet", "ArbitrumOne", "ArbitrumSepolia", "ArcTestnet", "AvalancheC", "AvalancheCFuji", "BabylonGenesis", "BabylonTestnet5", "Base", "BaseSepolia", "Berachain", "BerachainBepolia", "Bitcoin", "BitcoinSignet", "BitcoinTestnet3", "BitcoinCash", "Bob", "BobSepolia", "Bsc", "BscTestnet", "Canton", "CantonTestnet", "Cardano", "CardanoPreprod", "Concordium", "ConcordiumTestnet", "Celo", "CeloAlfajores", "Codex", "CodexSepolia", "CosmosHub4", "CosmosIcsTestnet", "Dogecoin", "Ethereum", "EthereumClassic", "EthereumClassicMordor", "EthereumGoerli", "EthereumSepolia", "EthereumHolesky", "EthereumHoodi", "FantomOpera", "FantomTestnet", "FlareC", "FlareCCoston2", "FlowEvm", "FlowEvmTestnet", "Hedera", "HederaTestnet", "Ink", "InkSepolia", "InternetComputer", "Ion", "IonTestnet", "Iota", "IotaTestnet", "Kaspa", "Kusama", "KusamaAssetHub", "Litecoin", "Near", "NearTestnet", "Optimism", "OptimismSepolia", "Origyn", "Plasma", "PlasmaTestnet", "Plume", "PlumeSepolia", "Paseo", "PaseoAssetHub", "Polkadot", "PolkadotAssetHub", "Polygon", "PolygonAmoy", "Polymesh", "PolymeshTestnet", "Race", "RaceSepolia", "SeiAtlantic2", "SeiPacific1", "Solana", "SolanaDevnet", "Starknet", "StarknetSepolia", "Stellar", "StellarTestnet", "Sui", "SuiTestnet", "Tezos", "TezosGhostnet", "TempoAndantino", "Tsc", "TscTestnet1", "Ton", "TonTestnet", "Tron", "TronNile", "Westend", "WestendAssetHub", "XrpLedger", "XrpLedgerTestnet"]
    requester: TypedDict
    request_body: TypedDict
    status: Literal["Pending", "Executing", "Broadcasted", "Confirmed", "Failed", "Rejected"]
    reason: NotRequired[str]
    tx_hash: NotRequired[str]
    fee: NotRequired[str]
    approval_id: NotRequired[str]
    date_requested: str
    date_policy_resolved: NotRequired[str]
    date_broadcasted: NotRequired[str]
    date_confirmed: NotRequired[str]
    external_id: NotRequired[str]

class CancelTransactionResponse(TypedDict, total=False):
    """cancelTransaction response."""

    id: str
    wallet_id: str
    network: Literal["Algorand", "AlgorandTestnet", "Aptos", "AptosTestnet", "ArbitrumOne", "ArbitrumSepolia", "ArcTestnet", "AvalancheC", "AvalancheCFuji", "BabylonGenesis", "BabylonTestnet5", "Base", "BaseSepolia", "Berachain", "BerachainBepolia", "Bitcoin", "BitcoinSignet", "BitcoinTestnet3", "BitcoinCash", "Bob", "BobSepolia", "Bsc", "BscTestnet", "Canton", "CantonTestnet", "Cardano", "CardanoPreprod", "Concordium", "ConcordiumTestnet", "Celo", "CeloAlfajores", "Codex", "CodexSepolia", "CosmosHub4", "CosmosIcsTestnet", "Dogecoin", "Ethereum", "EthereumClassic", "EthereumClassicMordor", "EthereumGoerli", "EthereumSepolia", "EthereumHolesky", "EthereumHoodi", "FantomOpera", "FantomTestnet", "FlareC", "FlareCCoston2", "FlowEvm", "FlowEvmTestnet", "Hedera", "HederaTestnet", "Ink", "InkSepolia", "InternetComputer", "Ion", "IonTestnet", "Iota", "IotaTestnet", "Kaspa", "Kusama", "KusamaAssetHub", "Litecoin", "Near", "NearTestnet", "Optimism", "OptimismSepolia", "Origyn", "Plasma", "PlasmaTestnet", "Plume", "PlumeSepolia", "Paseo", "PaseoAssetHub", "Polkadot", "PolkadotAssetHub", "Polygon", "PolygonAmoy", "Polymesh", "PolymeshTestnet", "Race", "RaceSepolia", "SeiAtlantic2", "SeiPacific1", "Solana", "SolanaDevnet", "Starknet", "StarknetSepolia", "Stellar", "StellarTestnet", "Sui", "SuiTestnet", "Tezos", "TezosGhostnet", "TempoAndantino", "Tsc", "TscTestnet1", "Ton", "TonTestnet", "Tron", "TronNile", "Westend", "WestendAssetHub", "XrpLedger", "XrpLedgerTestnet"]
    requester: TypedDict
    request_body: TypedDict
    status: Literal["Pending", "Executing", "Broadcasted", "Confirmed", "Failed", "Rejected"]
    reason: NotRequired[str]
    tx_hash: NotRequired[str]
    fee: NotRequired[str]
    approval_id: NotRequired[str]
    date_requested: str
    date_policy_resolved: NotRequired[str]
    date_broadcasted: NotRequired[str]
    date_confirmed: NotRequired[str]
    external_id: NotRequired[str]

class CancelTransferResponse(TypedDict, total=False):
    """cancelTransfer response."""

    id: str
    wallet_id: str
    network: Literal["Algorand", "AlgorandTestnet", "Aptos", "AptosTestnet", "ArbitrumOne", "ArbitrumSepolia", "ArcTestnet", "AvalancheC", "AvalancheCFuji", "BabylonGenesis", "BabylonTestnet5", "Base", "BaseSepolia", "Berachain", "BerachainBepolia", "Bitcoin", "BitcoinSignet", "BitcoinTestnet3", "BitcoinCash", "Bob", "BobSepolia", "Bsc", "BscTestnet", "Canton", "CantonTestnet", "Cardano", "CardanoPreprod", "Concordium", "ConcordiumTestnet", "Celo", "CeloAlfajores", "Codex", "CodexSepolia", "CosmosHub4", "CosmosIcsTestnet", "Dogecoin", "Ethereum", "EthereumClassic", "EthereumClassicMordor", "EthereumGoerli", "EthereumSepolia", "EthereumHolesky", "EthereumHoodi", "FantomOpera", "FantomTestnet", "FlareC", "FlareCCoston2", "FlowEvm", "FlowEvmTestnet", "Hedera", "HederaTestnet", "Ink", "InkSepolia", "InternetComputer", "Ion", "IonTestnet", "Iota", "IotaTestnet", "Kaspa", "Kusama", "KusamaAssetHub", "Litecoin", "Near", "NearTestnet", "Optimism", "OptimismSepolia", "Origyn", "Plasma", "PlasmaTestnet", "Plume", "PlumeSepolia", "Paseo", "PaseoAssetHub", "Polkadot", "PolkadotAssetHub", "Polygon", "PolygonAmoy", "Polymesh", "PolymeshTestnet", "Race", "RaceSepolia", "SeiAtlantic2", "SeiPacific1", "Solana", "SolanaDevnet", "Starknet", "StarknetSepolia", "Stellar", "StellarTestnet", "Sui", "SuiTestnet", "Tezos", "TezosGhostnet", "TempoAndantino", "Tsc", "TscTestnet1", "Ton", "TonTestnet", "Tron", "TronNile", "Westend", "WestendAssetHub", "XrpLedger", "XrpLedgerTestnet"]
    requester: TypedDict
    request_body: TypedDict
    status: Literal["Pending", "Executing", "Broadcasted", "Confirmed", "Failed", "Rejected"]
    reason: NotRequired[str]
    tx_hash: NotRequired[str]
    fee: NotRequired[str]
    approval_id: NotRequired[str]
    date_requested: str
    date_policy_resolved: NotRequired[str]
    date_broadcasted: NotRequired[str]
    date_confirmed: NotRequired[str]
    external_id: NotRequired[str]

class SpeedUpTransactionResponse(TypedDict, total=False):
    """speedUpTransaction response."""

    id: str
    wallet_id: str
    network: Literal["Algorand", "AlgorandTestnet", "Aptos", "AptosTestnet", "ArbitrumOne", "ArbitrumSepolia", "ArcTestnet", "AvalancheC", "AvalancheCFuji", "BabylonGenesis", "BabylonTestnet5", "Base", "BaseSepolia", "Berachain", "BerachainBepolia", "Bitcoin", "BitcoinSignet", "BitcoinTestnet3", "BitcoinCash", "Bob", "BobSepolia", "Bsc", "BscTestnet", "Canton", "CantonTestnet", "Cardano", "CardanoPreprod", "Concordium", "ConcordiumTestnet", "Celo", "CeloAlfajores", "Codex", "CodexSepolia", "CosmosHub4", "CosmosIcsTestnet", "Dogecoin", "Ethereum", "EthereumClassic", "EthereumClassicMordor", "EthereumGoerli", "EthereumSepolia", "EthereumHolesky", "EthereumHoodi", "FantomOpera", "FantomTestnet", "FlareC", "FlareCCoston2", "FlowEvm", "FlowEvmTestnet", "Hedera", "HederaTestnet", "Ink", "InkSepolia", "InternetComputer", "Ion", "IonTestnet", "Iota", "IotaTestnet", "Kaspa", "Kusama", "KusamaAssetHub", "Litecoin", "Near", "NearTestnet", "Optimism", "OptimismSepolia", "Origyn", "Plasma", "PlasmaTestnet", "Plume", "PlumeSepolia", "Paseo", "PaseoAssetHub", "Polkadot", "PolkadotAssetHub", "Polygon", "PolygonAmoy", "Polymesh", "PolymeshTestnet", "Race", "RaceSepolia", "SeiAtlantic2", "SeiPacific1", "Solana", "SolanaDevnet", "Starknet", "StarknetSepolia", "Stellar", "StellarTestnet", "Sui", "SuiTestnet", "Tezos", "TezosGhostnet", "TempoAndantino", "Tsc", "TscTestnet1", "Ton", "TonTestnet", "Tron", "TronNile", "Westend", "WestendAssetHub", "XrpLedger", "XrpLedgerTestnet"]
    requester: TypedDict
    request_body: TypedDict
    status: Literal["Pending", "Executing", "Broadcasted", "Confirmed", "Failed", "Rejected"]
    reason: NotRequired[str]
    tx_hash: NotRequired[str]
    fee: NotRequired[str]
    approval_id: NotRequired[str]
    date_requested: str
    date_policy_resolved: NotRequired[str]
    date_broadcasted: NotRequired[str]
    date_confirmed: NotRequired[str]
    external_id: NotRequired[str]

class SpeedUpTransferResponse(TypedDict, total=False):
    """speedUpTransfer response."""

    id: str
    wallet_id: str
    network: Literal["Algorand", "AlgorandTestnet", "Aptos", "AptosTestnet", "ArbitrumOne", "ArbitrumSepolia", "ArcTestnet", "AvalancheC", "AvalancheCFuji", "BabylonGenesis", "BabylonTestnet5", "Base", "BaseSepolia", "Berachain", "BerachainBepolia", "Bitcoin", "BitcoinSignet", "BitcoinTestnet3", "BitcoinCash", "Bob", "BobSepolia", "Bsc", "BscTestnet", "Canton", "CantonTestnet", "Cardano", "CardanoPreprod", "Concordium", "ConcordiumTestnet", "Celo", "CeloAlfajores", "Codex", "CodexSepolia", "CosmosHub4", "CosmosIcsTestnet", "Dogecoin", "Ethereum", "EthereumClassic", "EthereumClassicMordor", "EthereumGoerli", "EthereumSepolia", "EthereumHolesky", "EthereumHoodi", "FantomOpera", "FantomTestnet", "FlareC", "FlareCCoston2", "FlowEvm", "FlowEvmTestnet", "Hedera", "HederaTestnet", "Ink", "InkSepolia", "InternetComputer", "Ion", "IonTestnet", "Iota", "IotaTestnet", "Kaspa", "Kusama", "KusamaAssetHub", "Litecoin", "Near", "NearTestnet", "Optimism", "OptimismSepolia", "Origyn", "Plasma", "PlasmaTestnet", "Plume", "PlumeSepolia", "Paseo", "PaseoAssetHub", "Polkadot", "PolkadotAssetHub", "Polygon", "PolygonAmoy", "Polymesh", "PolymeshTestnet", "Race", "RaceSepolia", "SeiAtlantic2", "SeiPacific1", "Solana", "SolanaDevnet", "Starknet", "StarknetSepolia", "Stellar", "StellarTestnet", "Sui", "SuiTestnet", "Tezos", "TezosGhostnet", "TempoAndantino", "Tsc", "TscTestnet1", "Ton", "TonTestnet", "Tron", "TronNile", "Westend", "WestendAssetHub", "XrpLedger", "XrpLedgerTestnet"]
    requester: TypedDict
    request_body: TypedDict
    status: Literal["Pending", "Executing", "Broadcasted", "Confirmed", "Failed", "Rejected"]
    reason: NotRequired[str]
    tx_hash: NotRequired[str]
    fee: NotRequired[str]
    approval_id: NotRequired[str]
    date_requested: str
    date_policy_resolved: NotRequired[str]
    date_broadcasted: NotRequired[str]
    date_confirmed: NotRequired[str]
    external_id: NotRequired[str]

class ListWalletsResponse(TypedDict, total=False):
    """listWallets response."""

    items: list[TypedDict]
    next_page_token: NotRequired[str]

class ListWalletsQuery(TypedDict, total=False):
    """listWallets query parameters."""

    limit: NotRequired[str]
    pagination_token: NotRequired[str]
    owner: NotRequired[str]
    owner_id: NotRequired[str]
    owner_username: NotRequired[str]

class CreateWalletRequest(TypedDict, total=False):
    """createWallet request body."""

    network: Literal["Algorand", "AlgorandTestnet", "Aptos", "AptosTestnet", "ArbitrumOne", "ArbitrumSepolia", "ArcTestnet", "AvalancheC", "AvalancheCFuji", "BabylonGenesis", "BabylonTestnet5", "Base", "BaseSepolia", "Berachain", "BerachainBepolia", "Bitcoin", "BitcoinSignet", "BitcoinTestnet3", "BitcoinCash", "Bob", "BobSepolia", "Bsc", "BscTestnet", "Canton", "CantonTestnet", "Cardano", "CardanoPreprod", "Concordium", "ConcordiumTestnet", "Celo", "CeloAlfajores", "Codex", "CodexSepolia", "CosmosHub4", "CosmosIcsTestnet", "Dogecoin", "Ethereum", "EthereumClassic", "EthereumClassicMordor", "EthereumGoerli", "EthereumSepolia", "EthereumHolesky", "EthereumHoodi", "FantomOpera", "FantomTestnet", "FlareC", "FlareCCoston2", "FlowEvm", "FlowEvmTestnet", "Hedera", "HederaTestnet", "Ink", "InkSepolia", "InternetComputer", "Ion", "IonTestnet", "Iota", "IotaTestnet", "Kaspa", "Kusama", "KusamaAssetHub", "Litecoin", "Near", "NearTestnet", "Optimism", "OptimismSepolia", "Origyn", "Plasma", "PlasmaTestnet", "Plume", "PlumeSepolia", "Paseo", "PaseoAssetHub", "Polkadot", "PolkadotAssetHub", "Polygon", "PolygonAmoy", "Polymesh", "PolymeshTestnet", "Race", "RaceSepolia", "SeiAtlantic2", "SeiPacific1", "Solana", "SolanaDevnet", "Starknet", "StarknetSepolia", "Stellar", "StellarTestnet", "Sui", "SuiTestnet", "Tezos", "TezosGhostnet", "TempoAndantino", "Tsc", "TscTestnet1", "Ton", "TonTestnet", "Tron", "TronNile", "Westend", "WestendAssetHub", "XrpLedger", "XrpLedgerTestnet"]
    name: NotRequired[str]
    signing_key: NotRequired[TypedDict]
    delegate_to: NotRequired[str]
    delay_delegation: NotRequired[bool]
    external_id: NotRequired[str]
    tags: NotRequired[list[str]]
    validator_id: NotRequired[str]

class CreateWalletResponse(TypedDict, total=False):
    """createWallet response."""

    id: str
    network: Literal["Algorand", "AlgorandTestnet", "Aptos", "AptosTestnet", "ArbitrumOne", "ArbitrumSepolia", "ArcTestnet", "AvalancheC", "AvalancheCFuji", "BabylonGenesis", "BabylonTestnet5", "Base", "BaseSepolia", "Berachain", "BerachainBepolia", "Bitcoin", "BitcoinSignet", "BitcoinTestnet3", "BitcoinCash", "Bob", "BobSepolia", "Bsc", "BscTestnet", "Canton", "CantonTestnet", "Cardano", "CardanoPreprod", "Concordium", "ConcordiumTestnet", "Celo", "CeloAlfajores", "Codex", "CodexSepolia", "CosmosHub4", "CosmosIcsTestnet", "Dogecoin", "Ethereum", "EthereumClassic", "EthereumClassicMordor", "EthereumGoerli", "EthereumSepolia", "EthereumHolesky", "EthereumHoodi", "FantomOpera", "FantomTestnet", "FlareC", "FlareCCoston2", "FlowEvm", "FlowEvmTestnet", "Hedera", "HederaTestnet", "Ink", "InkSepolia", "InternetComputer", "Ion", "IonTestnet", "Iota", "IotaTestnet", "Kaspa", "Kusama", "KusamaAssetHub", "Litecoin", "Near", "NearTestnet", "Optimism", "OptimismSepolia", "Origyn", "Plasma", "PlasmaTestnet", "Plume", "PlumeSepolia", "Paseo", "PaseoAssetHub", "Polkadot", "PolkadotAssetHub", "Polygon", "PolygonAmoy", "Polymesh", "PolymeshTestnet", "Race", "RaceSepolia", "SeiAtlantic2", "SeiPacific1", "Solana", "SolanaDevnet", "Starknet", "StarknetSepolia", "Stellar", "StellarTestnet", "Sui", "SuiTestnet", "Tezos", "TezosGhostnet", "TempoAndantino", "Tsc", "TscTestnet1", "Ton", "TonTestnet", "Tron", "TronNile", "Westend", "WestendAssetHub", "XrpLedger", "XrpLedgerTestnet"]
    address: NotRequired[str]
    signing_key: TypedDict
    status: Literal["Active", "Inactive", "Archived"]
    date_created: str
    date_deleted: NotRequired[str]
    name: NotRequired[str]
    custodial: bool
    external_id: NotRequired[str]
    tags: list[str]
    validator_id: NotRequired[str]

class DelegateWalletRequest(TypedDict, total=False):
    """delegateWallet request body."""

    user_id: str

class DelegateWalletResponse(TypedDict, total=False):
    """delegateWallet response."""

    wallet_id: str
    status: Literal["Delegated"]

class ExportWalletRequest(TypedDict, total=False):
    """exportWallet request body."""

    encryption_key: str
    supported_schemes: list[TypedDict]

class ExportWalletResponse(TypedDict, total=False):
    """exportWallet response."""

    public_key: str
    protocol: Union[Literal["CGGMP24", "FROST", "FROST_BITCOIN", "GLOW20_DH", "KU23"], Literal["CGGMP21"]]
    curve: Literal["ed25519", "secp256k1", "stark"]
    min_signers: float
    encrypted_key_shares: list[TypedDict]

class ListSignaturesResponse(TypedDict, total=False):
    """listSignatures response."""

    key_id: str
    items: list[TypedDict]
    next_page_token: NotRequired[str]

class ListSignaturesQuery(TypedDict, total=False):
    """listSignatures query parameters."""

    limit: NotRequired[str]
    pagination_token: NotRequired[str]

class GenerateSignatureResponse(TypedDict, total=False):
    """generateSignature response."""

    id: str
    key_id: str
    requester: TypedDict
    request_body: TypedDict
    status: Literal["Pending", "Executing", "Signed", "Confirmed", "Failed", "Rejected"]
    reason: NotRequired[str]
    signature: NotRequired[TypedDict]
    signatures: NotRequired[list[TypedDict]]
    signed_data: NotRequired[str]
    network: Literal["Algorand", "AlgorandTestnet", "Aptos", "AptosTestnet", "ArbitrumOne", "ArbitrumSepolia", "ArcTestnet", "AvalancheC", "AvalancheCFuji", "BabylonGenesis", "BabylonTestnet5", "Base", "BaseSepolia", "Berachain", "BerachainBepolia", "Bitcoin", "BitcoinSignet", "BitcoinTestnet3", "BitcoinCash", "Bob", "BobSepolia", "Bsc", "BscTestnet", "Canton", "CantonTestnet", "Cardano", "CardanoPreprod", "Concordium", "ConcordiumTestnet", "Celo", "CeloAlfajores", "Codex", "CodexSepolia", "CosmosHub4", "CosmosIcsTestnet", "Dogecoin", "Ethereum", "EthereumClassic", "EthereumClassicMordor", "EthereumGoerli", "EthereumSepolia", "EthereumHolesky", "EthereumHoodi", "FantomOpera", "FantomTestnet", "FlareC", "FlareCCoston2", "FlowEvm", "FlowEvmTestnet", "Hedera", "HederaTestnet", "Ink", "InkSepolia", "InternetComputer", "Ion", "IonTestnet", "Iota", "IotaTestnet", "Kaspa", "Kusama", "KusamaAssetHub", "Litecoin", "Near", "NearTestnet", "Optimism", "OptimismSepolia", "Origyn", "Plasma", "PlasmaTestnet", "Plume", "PlumeSepolia", "Paseo", "PaseoAssetHub", "Polkadot", "PolkadotAssetHub", "Polygon", "PolygonAmoy", "Polymesh", "PolymeshTestnet", "Race", "RaceSepolia", "SeiAtlantic2", "SeiPacific1", "Solana", "SolanaDevnet", "Starknet", "StarknetSepolia", "Stellar", "StellarTestnet", "Sui", "SuiTestnet", "Tezos", "TezosGhostnet", "TempoAndantino", "Tsc", "TscTestnet1", "Ton", "TonTestnet", "Tron", "TronNile", "Westend", "WestendAssetHub", "XrpLedger", "XrpLedgerTestnet"]
    tx_hash: NotRequired[str]
    fee: NotRequired[str]
    approval_id: NotRequired[str]
    date_requested: str
    date_policy_resolved: NotRequired[str]
    date_signed: NotRequired[str]
    date_confirmed: NotRequired[str]
    external_id: NotRequired[str]
    wallet_id: str

class GetSignatureResponse(TypedDict, total=False):
    """getSignature response."""

    id: str
    key_id: str
    requester: TypedDict
    request_body: TypedDict
    status: Literal["Pending", "Executing", "Signed", "Confirmed", "Failed", "Rejected"]
    reason: NotRequired[str]
    signature: NotRequired[TypedDict]
    signatures: NotRequired[list[TypedDict]]
    signed_data: NotRequired[str]
    network: NotRequired[Literal["Algorand", "AlgorandTestnet", "Aptos", "AptosTestnet", "ArbitrumOne", "ArbitrumSepolia", "ArcTestnet", "AvalancheC", "AvalancheCFuji", "BabylonGenesis", "BabylonTestnet5", "Base", "BaseSepolia", "Berachain", "BerachainBepolia", "Bitcoin", "BitcoinSignet", "BitcoinTestnet3", "BitcoinCash", "Bob", "BobSepolia", "Bsc", "BscTestnet", "Canton", "CantonTestnet", "Cardano", "CardanoPreprod", "Concordium", "ConcordiumTestnet", "Celo", "CeloAlfajores", "Codex", "CodexSepolia", "CosmosHub4", "CosmosIcsTestnet", "Dogecoin", "Ethereum", "EthereumClassic", "EthereumClassicMordor", "EthereumGoerli", "EthereumSepolia", "EthereumHolesky", "EthereumHoodi", "FantomOpera", "FantomTestnet", "FlareC", "FlareCCoston2", "FlowEvm", "FlowEvmTestnet", "Hedera", "HederaTestnet", "Ink", "InkSepolia", "InternetComputer", "Ion", "IonTestnet", "Iota", "IotaTestnet", "Kaspa", "Kusama", "KusamaAssetHub", "Litecoin", "Near", "NearTestnet", "Optimism", "OptimismSepolia", "Origyn", "Plasma", "PlasmaTestnet", "Plume", "PlumeSepolia", "Paseo", "PaseoAssetHub", "Polkadot", "PolkadotAssetHub", "Polygon", "PolygonAmoy", "Polymesh", "PolymeshTestnet", "Race", "RaceSepolia", "SeiAtlantic2", "SeiPacific1", "Solana", "SolanaDevnet", "Starknet", "StarknetSepolia", "Stellar", "StellarTestnet", "Sui", "SuiTestnet", "Tezos", "TezosGhostnet", "TempoAndantino", "Tsc", "TscTestnet1", "Ton", "TonTestnet", "Tron", "TronNile", "Westend", "WestendAssetHub", "XrpLedger", "XrpLedgerTestnet"]]
    tx_hash: NotRequired[str]
    fee: NotRequired[str]
    approval_id: NotRequired[str]
    date_requested: str
    date_policy_resolved: NotRequired[str]
    date_signed: NotRequired[str]
    date_confirmed: NotRequired[str]
    external_id: NotRequired[str]

class GetTransactionResponse(TypedDict, total=False):
    """getTransaction response."""

    id: str
    wallet_id: str
    network: Literal["Algorand", "AlgorandTestnet", "Aptos", "AptosTestnet", "ArbitrumOne", "ArbitrumSepolia", "ArcTestnet", "AvalancheC", "AvalancheCFuji", "BabylonGenesis", "BabylonTestnet5", "Base", "BaseSepolia", "Berachain", "BerachainBepolia", "Bitcoin", "BitcoinSignet", "BitcoinTestnet3", "BitcoinCash", "Bob", "BobSepolia", "Bsc", "BscTestnet", "Canton", "CantonTestnet", "Cardano", "CardanoPreprod", "Concordium", "ConcordiumTestnet", "Celo", "CeloAlfajores", "Codex", "CodexSepolia", "CosmosHub4", "CosmosIcsTestnet", "Dogecoin", "Ethereum", "EthereumClassic", "EthereumClassicMordor", "EthereumGoerli", "EthereumSepolia", "EthereumHolesky", "EthereumHoodi", "FantomOpera", "FantomTestnet", "FlareC", "FlareCCoston2", "FlowEvm", "FlowEvmTestnet", "Hedera", "HederaTestnet", "Ink", "InkSepolia", "InternetComputer", "Ion", "IonTestnet", "Iota", "IotaTestnet", "Kaspa", "Kusama", "KusamaAssetHub", "Litecoin", "Near", "NearTestnet", "Optimism", "OptimismSepolia", "Origyn", "Plasma", "PlasmaTestnet", "Plume", "PlumeSepolia", "Paseo", "PaseoAssetHub", "Polkadot", "PolkadotAssetHub", "Polygon", "PolygonAmoy", "Polymesh", "PolymeshTestnet", "Race", "RaceSepolia", "SeiAtlantic2", "SeiPacific1", "Solana", "SolanaDevnet", "Starknet", "StarknetSepolia", "Stellar", "StellarTestnet", "Sui", "SuiTestnet", "Tezos", "TezosGhostnet", "TempoAndantino", "Tsc", "TscTestnet1", "Ton", "TonTestnet", "Tron", "TronNile", "Westend", "WestendAssetHub", "XrpLedger", "XrpLedgerTestnet"]
    requester: TypedDict
    request_body: TypedDict
    status: Literal["Pending", "Executing", "Broadcasted", "Confirmed", "Failed", "Rejected"]
    reason: NotRequired[str]
    tx_hash: NotRequired[str]
    fee: NotRequired[str]
    approval_id: NotRequired[str]
    date_requested: str
    date_policy_resolved: NotRequired[str]
    date_broadcasted: NotRequired[str]
    date_confirmed: NotRequired[str]
    external_id: NotRequired[str]

class GetTransferResponse(TypedDict, total=False):
    """getTransfer response."""

    id: str
    wallet_id: str
    network: Literal["Algorand", "AlgorandTestnet", "Aptos", "AptosTestnet", "ArbitrumOne", "ArbitrumSepolia", "ArcTestnet", "AvalancheC", "AvalancheCFuji", "BabylonGenesis", "BabylonTestnet5", "Base", "BaseSepolia", "Berachain", "BerachainBepolia", "Bitcoin", "BitcoinSignet", "BitcoinTestnet3", "BitcoinCash", "Bob", "BobSepolia", "Bsc", "BscTestnet", "Canton", "CantonTestnet", "Cardano", "CardanoPreprod", "Concordium", "ConcordiumTestnet", "Celo", "CeloAlfajores", "Codex", "CodexSepolia", "CosmosHub4", "CosmosIcsTestnet", "Dogecoin", "Ethereum", "EthereumClassic", "EthereumClassicMordor", "EthereumGoerli", "EthereumSepolia", "EthereumHolesky", "EthereumHoodi", "FantomOpera", "FantomTestnet", "FlareC", "FlareCCoston2", "FlowEvm", "FlowEvmTestnet", "Hedera", "HederaTestnet", "Ink", "InkSepolia", "InternetComputer", "Ion", "IonTestnet", "Iota", "IotaTestnet", "Kaspa", "Kusama", "KusamaAssetHub", "Litecoin", "Near", "NearTestnet", "Optimism", "OptimismSepolia", "Origyn", "Plasma", "PlasmaTestnet", "Plume", "PlumeSepolia", "Paseo", "PaseoAssetHub", "Polkadot", "PolkadotAssetHub", "Polygon", "PolygonAmoy", "Polymesh", "PolymeshTestnet", "Race", "RaceSepolia", "SeiAtlantic2", "SeiPacific1", "Solana", "SolanaDevnet", "Starknet", "StarknetSepolia", "Stellar", "StellarTestnet", "Sui", "SuiTestnet", "Tezos", "TezosGhostnet", "TempoAndantino", "Tsc", "TscTestnet1", "Ton", "TonTestnet", "Tron", "TronNile", "Westend", "WestendAssetHub", "XrpLedger", "XrpLedgerTestnet"]
    requester: TypedDict
    request_body: TypedDict
    metadata: TypedDict
    status: Literal["Pending", "Executing", "Broadcasted", "Confirmed", "Failed", "Rejected"]
    reason: NotRequired[str]
    tx_hash: NotRequired[str]
    fee: NotRequired[str]
    date_requested: str
    date_policy_resolved: NotRequired[str]
    date_broadcasted: NotRequired[str]
    date_confirmed: NotRequired[str]
    approval_id: NotRequired[str]
    external_id: NotRequired[str]
    fee_sponsor_id: NotRequired[str]

class GetWalletResponse(TypedDict, total=False):
    """getWallet response."""

    id: str
    network: Literal["Algorand", "AlgorandTestnet", "Aptos", "AptosTestnet", "ArbitrumOne", "ArbitrumSepolia", "ArcTestnet", "AvalancheC", "AvalancheCFuji", "BabylonGenesis", "BabylonTestnet5", "Base", "BaseSepolia", "Berachain", "BerachainBepolia", "Bitcoin", "BitcoinSignet", "BitcoinTestnet3", "BitcoinCash", "Bob", "BobSepolia", "Bsc", "BscTestnet", "Canton", "CantonTestnet", "Cardano", "CardanoPreprod", "Concordium", "ConcordiumTestnet", "Celo", "CeloAlfajores", "Codex", "CodexSepolia", "CosmosHub4", "CosmosIcsTestnet", "Dogecoin", "Ethereum", "EthereumClassic", "EthereumClassicMordor", "EthereumGoerli", "EthereumSepolia", "EthereumHolesky", "EthereumHoodi", "FantomOpera", "FantomTestnet", "FlareC", "FlareCCoston2", "FlowEvm", "FlowEvmTestnet", "Hedera", "HederaTestnet", "Ink", "InkSepolia", "InternetComputer", "Ion", "IonTestnet", "Iota", "IotaTestnet", "Kaspa", "Kusama", "KusamaAssetHub", "Litecoin", "Near", "NearTestnet", "Optimism", "OptimismSepolia", "Origyn", "Plasma", "PlasmaTestnet", "Plume", "PlumeSepolia", "Paseo", "PaseoAssetHub", "Polkadot", "PolkadotAssetHub", "Polygon", "PolygonAmoy", "Polymesh", "PolymeshTestnet", "Race", "RaceSepolia", "SeiAtlantic2", "SeiPacific1", "Solana", "SolanaDevnet", "Starknet", "StarknetSepolia", "Stellar", "StellarTestnet", "Sui", "SuiTestnet", "Tezos", "TezosGhostnet", "TempoAndantino", "Tsc", "TscTestnet1", "Ton", "TonTestnet", "Tron", "TronNile", "Westend", "WestendAssetHub", "XrpLedger", "XrpLedgerTestnet"]
    address: NotRequired[str]
    signing_key: TypedDict
    status: Literal["Active", "Inactive", "Archived"]
    date_created: str
    date_deleted: NotRequired[str]
    name: NotRequired[str]
    custodial: bool
    external_id: NotRequired[str]
    tags: list[str]
    validator_id: NotRequired[str]

class UpdateWalletRequest(TypedDict, total=False):
    """updateWallet request body."""

    name: NotRequired[Any]
    external_id: NotRequired[Any]

class UpdateWalletResponse(TypedDict, total=False):
    """updateWallet response."""

    id: str
    network: Literal["Algorand", "AlgorandTestnet", "Aptos", "AptosTestnet", "ArbitrumOne", "ArbitrumSepolia", "ArcTestnet", "AvalancheC", "AvalancheCFuji", "BabylonGenesis", "BabylonTestnet5", "Base", "BaseSepolia", "Berachain", "BerachainBepolia", "Bitcoin", "BitcoinSignet", "BitcoinTestnet3", "BitcoinCash", "Bob", "BobSepolia", "Bsc", "BscTestnet", "Canton", "CantonTestnet", "Cardano", "CardanoPreprod", "Concordium", "ConcordiumTestnet", "Celo", "CeloAlfajores", "Codex", "CodexSepolia", "CosmosHub4", "CosmosIcsTestnet", "Dogecoin", "Ethereum", "EthereumClassic", "EthereumClassicMordor", "EthereumGoerli", "EthereumSepolia", "EthereumHolesky", "EthereumHoodi", "FantomOpera", "FantomTestnet", "FlareC", "FlareCCoston2", "FlowEvm", "FlowEvmTestnet", "Hedera", "HederaTestnet", "Ink", "InkSepolia", "InternetComputer", "Ion", "IonTestnet", "Iota", "IotaTestnet", "Kaspa", "Kusama", "KusamaAssetHub", "Litecoin", "Near", "NearTestnet", "Optimism", "OptimismSepolia", "Origyn", "Plasma", "PlasmaTestnet", "Plume", "PlumeSepolia", "Paseo", "PaseoAssetHub", "Polkadot", "PolkadotAssetHub", "Polygon", "PolygonAmoy", "Polymesh", "PolymeshTestnet", "Race", "RaceSepolia", "SeiAtlantic2", "SeiPacific1", "Solana", "SolanaDevnet", "Starknet", "StarknetSepolia", "Stellar", "StellarTestnet", "Sui", "SuiTestnet", "Tezos", "TezosGhostnet", "TempoAndantino", "Tsc", "TscTestnet1", "Ton", "TonTestnet", "Tron", "TronNile", "Westend", "WestendAssetHub", "XrpLedger", "XrpLedgerTestnet"]
    address: NotRequired[str]
    signing_key: TypedDict
    status: Literal["Active", "Inactive", "Archived"]
    date_created: str
    date_deleted: NotRequired[str]
    name: NotRequired[str]
    custodial: bool
    external_id: NotRequired[str]
    tags: list[str]
    validator_id: NotRequired[str]

class GetWalletAssetsResponse(TypedDict, total=False):
    """getWalletAssets response."""

    wallet_id: str
    network: Literal["Algorand", "AlgorandTestnet", "Aptos", "AptosTestnet", "ArbitrumOne", "ArbitrumSepolia", "ArcTestnet", "AvalancheC", "AvalancheCFuji", "BabylonGenesis", "BabylonTestnet5", "Base", "BaseSepolia", "Berachain", "BerachainBepolia", "Bitcoin", "BitcoinSignet", "BitcoinTestnet3", "BitcoinCash", "Bob", "BobSepolia", "Bsc", "BscTestnet", "Canton", "CantonTestnet", "Cardano", "CardanoPreprod", "Concordium", "ConcordiumTestnet", "Celo", "CeloAlfajores", "Codex", "CodexSepolia", "CosmosHub4", "CosmosIcsTestnet", "Dogecoin", "Ethereum", "EthereumClassic", "EthereumClassicMordor", "EthereumGoerli", "EthereumSepolia", "EthereumHolesky", "EthereumHoodi", "FantomOpera", "FantomTestnet", "FlareC", "FlareCCoston2", "FlowEvm", "FlowEvmTestnet", "Hedera", "HederaTestnet", "Ink", "InkSepolia", "InternetComputer", "Ion", "IonTestnet", "Iota", "IotaTestnet", "Kaspa", "Kusama", "KusamaAssetHub", "Litecoin", "Near", "NearTestnet", "Optimism", "OptimismSepolia", "Origyn", "Plasma", "PlasmaTestnet", "Plume", "PlumeSepolia", "Paseo", "PaseoAssetHub", "Polkadot", "PolkadotAssetHub", "Polygon", "PolygonAmoy", "Polymesh", "PolymeshTestnet", "Race", "RaceSepolia", "SeiAtlantic2", "SeiPacific1", "Solana", "SolanaDevnet", "Starknet", "StarknetSepolia", "Stellar", "StellarTestnet", "Sui", "SuiTestnet", "Tezos", "TezosGhostnet", "TempoAndantino", "Tsc", "TscTestnet1", "Ton", "TonTestnet", "Tron", "TronNile", "Westend", "WestendAssetHub", "XrpLedger", "XrpLedgerTestnet"]
    assets: list[TypedDict]
    net_worth: NotRequired[TypedDict]

class GetWalletAssetsQuery(TypedDict, total=False):
    """getWalletAssets query parameters."""

    net_worth: NotRequired[Literal["true"]]

class GetWalletHistoryResponse(TypedDict, total=False):
    """getWalletHistory response."""

    items: list[TypedDict]
    next_page_token: NotRequired[str]
    wallet_id: str
    network: Literal["Algorand", "AlgorandTestnet", "Aptos", "AptosTestnet", "ArbitrumOne", "ArbitrumSepolia", "ArcTestnet", "AvalancheC", "AvalancheCFuji", "BabylonGenesis", "BabylonTestnet5", "Base", "BaseSepolia", "Berachain", "BerachainBepolia", "Bitcoin", "BitcoinSignet", "BitcoinTestnet3", "BitcoinCash", "Bob", "BobSepolia", "Bsc", "BscTestnet", "Canton", "CantonTestnet", "Cardano", "CardanoPreprod", "Concordium", "ConcordiumTestnet", "Celo", "CeloAlfajores", "Codex", "CodexSepolia", "CosmosHub4", "CosmosIcsTestnet", "Dogecoin", "Ethereum", "EthereumClassic", "EthereumClassicMordor", "EthereumGoerli", "EthereumSepolia", "EthereumHolesky", "EthereumHoodi", "FantomOpera", "FantomTestnet", "FlareC", "FlareCCoston2", "FlowEvm", "FlowEvmTestnet", "Hedera", "HederaTestnet", "Ink", "InkSepolia", "InternetComputer", "Ion", "IonTestnet", "Iota", "IotaTestnet", "Kaspa", "Kusama", "KusamaAssetHub", "Litecoin", "Near", "NearTestnet", "Optimism", "OptimismSepolia", "Origyn", "Plasma", "PlasmaTestnet", "Plume", "PlumeSepolia", "Paseo", "PaseoAssetHub", "Polkadot", "PolkadotAssetHub", "Polygon", "PolygonAmoy", "Polymesh", "PolymeshTestnet", "Race", "RaceSepolia", "SeiAtlantic2", "SeiPacific1", "Solana", "SolanaDevnet", "Starknet", "StarknetSepolia", "Stellar", "StellarTestnet", "Sui", "SuiTestnet", "Tezos", "TezosGhostnet", "TempoAndantino", "Tsc", "TscTestnet1", "Ton", "TonTestnet", "Tron", "TronNile", "Westend", "WestendAssetHub", "XrpLedger", "XrpLedgerTestnet"]

class GetWalletHistoryQuery(TypedDict, total=False):
    """getWalletHistory query parameters."""

    limit: NotRequired[int]
    pagination_token: NotRequired[str]
    direction: NotRequired[Literal["In", "Out"]]
    kind: NotRequired[Literal["NativeTransfer", "Aip21Transfer", "AsaTransfer", "AssetTransfer", "Cip56Transfer", "Cis2Transfer", "CoinTransfer", "Erc20Transfer", "Erc721Transfer", "Hip17Transfer", "HtsTransfer", "LockedCoinTransfer", "Cis7Transfer", "Snip2Transfer", "Snip3Transfer", "Tep74Transfer", "Trc10Transfer", "Trc20Transfer", "Trc721Transfer", "Sep41Transfer", "SplTransfer", "Spl2022Transfer", "UtxoTransfer"]]
    contract: NotRequired[str]

class GetWalletNftsResponse(TypedDict, total=False):
    """getWalletNfts response."""

    wallet_id: str
    network: Literal["Algorand", "AlgorandTestnet", "Aptos", "AptosTestnet", "ArbitrumOne", "ArbitrumSepolia", "ArcTestnet", "AvalancheC", "AvalancheCFuji", "BabylonGenesis", "BabylonTestnet5", "Base", "BaseSepolia", "Berachain", "BerachainBepolia", "Bitcoin", "BitcoinSignet", "BitcoinTestnet3", "BitcoinCash", "Bob", "BobSepolia", "Bsc", "BscTestnet", "Canton", "CantonTestnet", "Cardano", "CardanoPreprod", "Concordium", "ConcordiumTestnet", "Celo", "CeloAlfajores", "Codex", "CodexSepolia", "CosmosHub4", "CosmosIcsTestnet", "Dogecoin", "Ethereum", "EthereumClassic", "EthereumClassicMordor", "EthereumGoerli", "EthereumSepolia", "EthereumHolesky", "EthereumHoodi", "FantomOpera", "FantomTestnet", "FlareC", "FlareCCoston2", "FlowEvm", "FlowEvmTestnet", "Hedera", "HederaTestnet", "Ink", "InkSepolia", "InternetComputer", "Ion", "IonTestnet", "Iota", "IotaTestnet", "Kaspa", "Kusama", "KusamaAssetHub", "Litecoin", "Near", "NearTestnet", "Optimism", "OptimismSepolia", "Origyn", "Plasma", "PlasmaTestnet", "Plume", "PlumeSepolia", "Paseo", "PaseoAssetHub", "Polkadot", "PolkadotAssetHub", "Polygon", "PolygonAmoy", "Polymesh", "PolymeshTestnet", "Race", "RaceSepolia", "SeiAtlantic2", "SeiPacific1", "Solana", "SolanaDevnet", "Starknet", "StarknetSepolia", "Stellar", "StellarTestnet", "Sui", "SuiTestnet", "Tezos", "TezosGhostnet", "TempoAndantino", "Tsc", "TscTestnet1", "Ton", "TonTestnet", "Tron", "TronNile", "Westend", "WestendAssetHub", "XrpLedger", "XrpLedgerTestnet"]
    nfts: list[TypedDict]

class ImportWalletRequest(TypedDict, total=False):
    """importWallet request body."""

    name: NotRequired[str]
    curve: Literal["ed25519", "secp256k1", "stark"]
    protocol: Union[Literal["CGGMP24", "FROST", "FROST_BITCOIN", "GLOW20_DH", "KU23"], Literal["CGGMP21"]]
    min_signers: int
    encrypted_key_shares: list[TypedDict]
    network: Literal["Algorand", "AlgorandTestnet", "Aptos", "AptosTestnet", "ArbitrumOne", "ArbitrumSepolia", "ArcTestnet", "AvalancheC", "AvalancheCFuji", "BabylonGenesis", "BabylonTestnet5", "Base", "BaseSepolia", "Berachain", "BerachainBepolia", "Bitcoin", "BitcoinSignet", "BitcoinTestnet3", "BitcoinCash", "Bob", "BobSepolia", "Bsc", "BscTestnet", "Canton", "CantonTestnet", "Cardano", "CardanoPreprod", "Concordium", "ConcordiumTestnet", "Celo", "CeloAlfajores", "Codex", "CodexSepolia", "CosmosHub4", "CosmosIcsTestnet", "Dogecoin", "Ethereum", "EthereumClassic", "EthereumClassicMordor", "EthereumGoerli", "EthereumSepolia", "EthereumHolesky", "EthereumHoodi", "FantomOpera", "FantomTestnet", "FlareC", "FlareCCoston2", "FlowEvm", "FlowEvmTestnet", "Hedera", "HederaTestnet", "Ink", "InkSepolia", "InternetComputer", "Ion", "IonTestnet", "Iota", "IotaTestnet", "Kaspa", "Kusama", "KusamaAssetHub", "Litecoin", "Near", "NearTestnet", "Optimism", "OptimismSepolia", "Origyn", "Plasma", "PlasmaTestnet", "Plume", "PlumeSepolia", "Paseo", "PaseoAssetHub", "Polkadot", "PolkadotAssetHub", "Polygon", "PolygonAmoy", "Polymesh", "PolymeshTestnet", "Race", "RaceSepolia", "SeiAtlantic2", "SeiPacific1", "Solana", "SolanaDevnet", "Starknet", "StarknetSepolia", "Stellar", "StellarTestnet", "Sui", "SuiTestnet", "Tezos", "TezosGhostnet", "TempoAndantino", "Tsc", "TscTestnet1", "Ton", "TonTestnet", "Tron", "TronNile", "Westend", "WestendAssetHub", "XrpLedger", "XrpLedgerTestnet"]
    external_id: NotRequired[str]
    validator_id: NotRequired[str]

class ImportWalletResponse(TypedDict, total=False):
    """importWallet response."""

    id: str
    network: Literal["Algorand", "AlgorandTestnet", "Aptos", "AptosTestnet", "ArbitrumOne", "ArbitrumSepolia", "ArcTestnet", "AvalancheC", "AvalancheCFuji", "BabylonGenesis", "BabylonTestnet5", "Base", "BaseSepolia", "Berachain", "BerachainBepolia", "Bitcoin", "BitcoinSignet", "BitcoinTestnet3", "BitcoinCash", "Bob", "BobSepolia", "Bsc", "BscTestnet", "Canton", "CantonTestnet", "Cardano", "CardanoPreprod", "Concordium", "ConcordiumTestnet", "Celo", "CeloAlfajores", "Codex", "CodexSepolia", "CosmosHub4", "CosmosIcsTestnet", "Dogecoin", "Ethereum", "EthereumClassic", "EthereumClassicMordor", "EthereumGoerli", "EthereumSepolia", "EthereumHolesky", "EthereumHoodi", "FantomOpera", "FantomTestnet", "FlareC", "FlareCCoston2", "FlowEvm", "FlowEvmTestnet", "Hedera", "HederaTestnet", "Ink", "InkSepolia", "InternetComputer", "Ion", "IonTestnet", "Iota", "IotaTestnet", "Kaspa", "Kusama", "KusamaAssetHub", "Litecoin", "Near", "NearTestnet", "Optimism", "OptimismSepolia", "Origyn", "Plasma", "PlasmaTestnet", "Plume", "PlumeSepolia", "Paseo", "PaseoAssetHub", "Polkadot", "PolkadotAssetHub", "Polygon", "PolygonAmoy", "Polymesh", "PolymeshTestnet", "Race", "RaceSepolia", "SeiAtlantic2", "SeiPacific1", "Solana", "SolanaDevnet", "Starknet", "StarknetSepolia", "Stellar", "StellarTestnet", "Sui", "SuiTestnet", "Tezos", "TezosGhostnet", "TempoAndantino", "Tsc", "TscTestnet1", "Ton", "TonTestnet", "Tron", "TronNile", "Westend", "WestendAssetHub", "XrpLedger", "XrpLedgerTestnet"]
    address: NotRequired[str]
    signing_key: TypedDict
    status: Literal["Active", "Inactive", "Archived"]
    date_created: str
    date_deleted: NotRequired[str]
    name: NotRequired[str]
    custodial: bool
    external_id: NotRequired[str]
    tags: list[str]
    validator_id: NotRequired[str]

class ListTransfersResponse(TypedDict, total=False):
    """listTransfers response."""

    wallet_id: str
    items: list[TypedDict]
    next_page_token: NotRequired[str]

class ListTransfersQuery(TypedDict, total=False):
    """listTransfers query parameters."""

    limit: NotRequired[str]
    pagination_token: NotRequired[str]

class TransferAssetResponse(TypedDict, total=False):
    """transferAsset response."""

    id: str
    wallet_id: str
    network: Literal["Algorand", "AlgorandTestnet", "Aptos", "AptosTestnet", "ArbitrumOne", "ArbitrumSepolia", "ArcTestnet", "AvalancheC", "AvalancheCFuji", "BabylonGenesis", "BabylonTestnet5", "Base", "BaseSepolia", "Berachain", "BerachainBepolia", "Bitcoin", "BitcoinSignet", "BitcoinTestnet3", "BitcoinCash", "Bob", "BobSepolia", "Bsc", "BscTestnet", "Canton", "CantonTestnet", "Cardano", "CardanoPreprod", "Concordium", "ConcordiumTestnet", "Celo", "CeloAlfajores", "Codex", "CodexSepolia", "CosmosHub4", "CosmosIcsTestnet", "Dogecoin", "Ethereum", "EthereumClassic", "EthereumClassicMordor", "EthereumGoerli", "EthereumSepolia", "EthereumHolesky", "EthereumHoodi", "FantomOpera", "FantomTestnet", "FlareC", "FlareCCoston2", "FlowEvm", "FlowEvmTestnet", "Hedera", "HederaTestnet", "Ink", "InkSepolia", "InternetComputer", "Ion", "IonTestnet", "Iota", "IotaTestnet", "Kaspa", "Kusama", "KusamaAssetHub", "Litecoin", "Near", "NearTestnet", "Optimism", "OptimismSepolia", "Origyn", "Plasma", "PlasmaTestnet", "Plume", "PlumeSepolia", "Paseo", "PaseoAssetHub", "Polkadot", "PolkadotAssetHub", "Polygon", "PolygonAmoy", "Polymesh", "PolymeshTestnet", "Race", "RaceSepolia", "SeiAtlantic2", "SeiPacific1", "Solana", "SolanaDevnet", "Starknet", "StarknetSepolia", "Stellar", "StellarTestnet", "Sui", "SuiTestnet", "Tezos", "TezosGhostnet", "TempoAndantino", "Tsc", "TscTestnet1", "Ton", "TonTestnet", "Tron", "TronNile", "Westend", "WestendAssetHub", "XrpLedger", "XrpLedgerTestnet"]
    requester: TypedDict
    request_body: TypedDict
    metadata: TypedDict
    status: Literal["Pending", "Executing", "Broadcasted", "Confirmed", "Failed", "Rejected"]
    reason: NotRequired[str]
    tx_hash: NotRequired[str]
    fee: NotRequired[str]
    date_requested: str
    date_policy_resolved: NotRequired[str]
    date_broadcasted: NotRequired[str]
    date_confirmed: NotRequired[str]
    approval_id: NotRequired[str]
    external_id: NotRequired[str]
    fee_sponsor_id: NotRequired[str]

class TagWalletRequest(TypedDict, total=False):
    """tagWallet request body."""

    tags: list[str]

class TagWalletResponse(TypedDict, total=False):
    """tagWallet response."""

    pass

class UntagWalletRequest(TypedDict, total=False):
    """untagWallet request body."""

    tags: list[str]

class UntagWalletResponse(TypedDict, total=False):
    """untagWallet response."""

    pass

class GetOfferResponse(TypedDict, total=False):
    """getOffer response."""

    id: str
    org_id: str
    wallet_id: str
    network: Literal["Algorand", "AlgorandTestnet", "Aptos", "AptosTestnet", "ArbitrumOne", "ArbitrumSepolia", "ArcTestnet", "AvalancheC", "AvalancheCFuji", "BabylonGenesis", "BabylonTestnet5", "Base", "BaseSepolia", "Berachain", "BerachainBepolia", "Bitcoin", "BitcoinSignet", "BitcoinTestnet3", "BitcoinCash", "Bob", "BobSepolia", "Bsc", "BscTestnet", "Canton", "CantonTestnet", "Cardano", "CardanoPreprod", "Concordium", "ConcordiumTestnet", "Celo", "CeloAlfajores", "Codex", "CodexSepolia", "CosmosHub4", "CosmosIcsTestnet", "Dogecoin", "Ethereum", "EthereumClassic", "EthereumClassicMordor", "EthereumGoerli", "EthereumSepolia", "EthereumHolesky", "EthereumHoodi", "FantomOpera", "FantomTestnet", "FlareC", "FlareCCoston2", "FlowEvm", "FlowEvmTestnet", "Hedera", "HederaTestnet", "Ink", "InkSepolia", "InternetComputer", "Ion", "IonTestnet", "Iota", "IotaTestnet", "Kaspa", "Kusama", "KusamaAssetHub", "Litecoin", "Near", "NearTestnet", "Optimism", "OptimismSepolia", "Origyn", "Plasma", "PlasmaTestnet", "Plume", "PlumeSepolia", "Paseo", "PaseoAssetHub", "Polkadot", "PolkadotAssetHub", "Polygon", "PolygonAmoy", "Polymesh", "PolymeshTestnet", "Race", "RaceSepolia", "SeiAtlantic2", "SeiPacific1", "Solana", "SolanaDevnet", "Starknet", "StarknetSepolia", "Stellar", "StellarTestnet", "Sui", "SuiTestnet", "Tezos", "TezosGhostnet", "TempoAndantino", "Tsc", "TscTestnet1", "Ton", "TonTestnet", "Tron", "TronNile", "Westend", "WestendAssetHub", "XrpLedger", "XrpLedgerTestnet"]
    kind: Literal["Native", "Aip21", "Asa", "Coin", "Cip56", "Erc20", "Erc721", "Asset", "Hip17", "Hts", "Sep41", "Spl", "Spl2022", "Snip2", "Snip3", "Tep74", "Trc10", "Trc20", "Trc721", "Cis7", "Cis2"]
    metadata: TypedDict
    tx_hash: str
    status: Literal["Pending", "Accepted", "Rejected", "Expired"]
    from_: str
    to: str
    value: str
    timestamp: str
    expires_at: NotRequired[str]
    memo: NotRequired[str]
    settlement_transaction_id: NotRequired[str]
    date_settled: NotRequired[str]

class ListOffersResponse(TypedDict, total=False):
    """listOffers response."""

    items: list[TypedDict]
    next_page_token: NotRequired[str]

class ListOffersQuery(TypedDict, total=False):
    """listOffers query parameters."""

    limit: NotRequired[int]
    pagination_token: NotRequired[str]

class AcceptOfferResponse(TypedDict, total=False):
    """acceptOffer response."""

    id: str
    org_id: str
    wallet_id: str
    network: Literal["Algorand", "AlgorandTestnet", "Aptos", "AptosTestnet", "ArbitrumOne", "ArbitrumSepolia", "ArcTestnet", "AvalancheC", "AvalancheCFuji", "BabylonGenesis", "BabylonTestnet5", "Base", "BaseSepolia", "Berachain", "BerachainBepolia", "Bitcoin", "BitcoinSignet", "BitcoinTestnet3", "BitcoinCash", "Bob", "BobSepolia", "Bsc", "BscTestnet", "Canton", "CantonTestnet", "Cardano", "CardanoPreprod", "Concordium", "ConcordiumTestnet", "Celo", "CeloAlfajores", "Codex", "CodexSepolia", "CosmosHub4", "CosmosIcsTestnet", "Dogecoin", "Ethereum", "EthereumClassic", "EthereumClassicMordor", "EthereumGoerli", "EthereumSepolia", "EthereumHolesky", "EthereumHoodi", "FantomOpera", "FantomTestnet", "FlareC", "FlareCCoston2", "FlowEvm", "FlowEvmTestnet", "Hedera", "HederaTestnet", "Ink", "InkSepolia", "InternetComputer", "Ion", "IonTestnet", "Iota", "IotaTestnet", "Kaspa", "Kusama", "KusamaAssetHub", "Litecoin", "Near", "NearTestnet", "Optimism", "OptimismSepolia", "Origyn", "Plasma", "PlasmaTestnet", "Plume", "PlumeSepolia", "Paseo", "PaseoAssetHub", "Polkadot", "PolkadotAssetHub", "Polygon", "PolygonAmoy", "Polymesh", "PolymeshTestnet", "Race", "RaceSepolia", "SeiAtlantic2", "SeiPacific1", "Solana", "SolanaDevnet", "Starknet", "StarknetSepolia", "Stellar", "StellarTestnet", "Sui", "SuiTestnet", "Tezos", "TezosGhostnet", "TempoAndantino", "Tsc", "TscTestnet1", "Ton", "TonTestnet", "Tron", "TronNile", "Westend", "WestendAssetHub", "XrpLedger", "XrpLedgerTestnet"]
    kind: Literal["Native", "Aip21", "Asa", "Coin", "Cip56", "Erc20", "Erc721", "Asset", "Hip17", "Hts", "Sep41", "Spl", "Spl2022", "Snip2", "Snip3", "Tep74", "Trc10", "Trc20", "Trc721", "Cis7", "Cis2"]
    metadata: TypedDict
    tx_hash: str
    status: Literal["Pending", "Accepted", "Rejected", "Expired"]
    from_: str
    to: str
    value: str
    timestamp: str
    expires_at: NotRequired[str]
    memo: NotRequired[str]
    settlement_transaction_id: NotRequired[str]
    date_settled: NotRequired[str]

class RejectOfferResponse(TypedDict, total=False):
    """rejectOffer response."""

    id: str
    org_id: str
    wallet_id: str
    network: Literal["Algorand", "AlgorandTestnet", "Aptos", "AptosTestnet", "ArbitrumOne", "ArbitrumSepolia", "ArcTestnet", "AvalancheC", "AvalancheCFuji", "BabylonGenesis", "BabylonTestnet5", "Base", "BaseSepolia", "Berachain", "BerachainBepolia", "Bitcoin", "BitcoinSignet", "BitcoinTestnet3", "BitcoinCash", "Bob", "BobSepolia", "Bsc", "BscTestnet", "Canton", "CantonTestnet", "Cardano", "CardanoPreprod", "Concordium", "ConcordiumTestnet", "Celo", "CeloAlfajores", "Codex", "CodexSepolia", "CosmosHub4", "CosmosIcsTestnet", "Dogecoin", "Ethereum", "EthereumClassic", "EthereumClassicMordor", "EthereumGoerli", "EthereumSepolia", "EthereumHolesky", "EthereumHoodi", "FantomOpera", "FantomTestnet", "FlareC", "FlareCCoston2", "FlowEvm", "FlowEvmTestnet", "Hedera", "HederaTestnet", "Ink", "InkSepolia", "InternetComputer", "Ion", "IonTestnet", "Iota", "IotaTestnet", "Kaspa", "Kusama", "KusamaAssetHub", "Litecoin", "Near", "NearTestnet", "Optimism", "OptimismSepolia", "Origyn", "Plasma", "PlasmaTestnet", "Plume", "PlumeSepolia", "Paseo", "PaseoAssetHub", "Polkadot", "PolkadotAssetHub", "Polygon", "PolygonAmoy", "Polymesh", "PolymeshTestnet", "Race", "RaceSepolia", "SeiAtlantic2", "SeiPacific1", "Solana", "SolanaDevnet", "Starknet", "StarknetSepolia", "Stellar", "StellarTestnet", "Sui", "SuiTestnet", "Tezos", "TezosGhostnet", "TempoAndantino", "Tsc", "TscTestnet1", "Ton", "TonTestnet", "Tron", "TronNile", "Westend", "WestendAssetHub", "XrpLedger", "XrpLedgerTestnet"]
    kind: Literal["Native", "Aip21", "Asa", "Coin", "Cip56", "Erc20", "Erc721", "Asset", "Hip17", "Hts", "Sep41", "Spl", "Spl2022", "Snip2", "Snip3", "Tep74", "Trc10", "Trc20", "Trc721", "Cis7", "Cis2"]
    metadata: TypedDict
    tx_hash: str
    status: Literal["Pending", "Accepted", "Rejected", "Expired"]
    from_: str
    to: str
    value: str
    timestamp: str
    expires_at: NotRequired[str]
    memo: NotRequired[str]
    settlement_transaction_id: NotRequired[str]
    date_settled: NotRequired[str]

class ListOrgWalletHistoryQuery(TypedDict, total=False):
    """listOrgWalletHistory query parameters."""

    start_time: str
    end_time: str
    limit: NotRequired[str]
    pagination_token: NotRequired[str]
