"""Types for the address_watches domain."""

from typing import Any, Literal, TypedDict

from typing_extensions import NotRequired


class ListAddressWatchesResponse(TypedDict, total=False):
    """listAddressWatches response."""

    items: list[dict[str, Any]]
    next_page_token: NotRequired[str]


class ListAddressWatchesQuery(TypedDict, total=False):
    """listAddressWatches query parameters."""

    limit: NotRequired[int]
    pagination_token: NotRequired[str]


class CreateAddressWatchRequest(TypedDict, total=False):
    """createAddressWatch request body."""

    network: dict[str, Any]
    address: str
    name: NotRequired[str]
    external_id: NotRequired[str]
    tags: NotRequired[list[str]]


class CreateAddressWatchResponse(TypedDict, total=False):
    """createAddressWatch response."""

    id: str
    network: Literal[
        "ArbitrumOne",
        "ArbitrumSepolia",
        "ArcTestnet",
        "AvalancheC",
        "AvalancheCFuji",
        "Base",
        "BaseSepolia",
        "Berachain",
        "BerachainBepolia",
        "Bob",
        "BobSepolia",
        "Bsc",
        "BscTestnet",
        "Celo",
        "CeloAlfajores",
        "Codex",
        "CodexSepolia",
        "Ethereum",
        "EthereumClassic",
        "EthereumClassicMordor",
        "EthereumSepolia",
        "EthereumHoodi",
        "FlareC",
        "FlareCCoston2",
        "FlowEvm",
        "FlowEvmTestnet",
        "Ink",
        "InkSepolia",
        "Optimism",
        "OptimismSepolia",
        "Plasma",
        "PlasmaTestnet",
        "Plume",
        "PlumeSepolia",
        "Polygon",
        "PolygonAmoy",
        "Race",
        "RaceSepolia",
        "Rayls",
        "RaylsTestnet",
        "Robinhood",
        "RobinhoodSepolia",
        "SeiAtlantic2",
        "SeiPacific1",
        "Solana",
        "SolanaDevnet",
        "Sonic",
        "SonicTestnet",
        "Tempo",
        "TempoModerato",
        "Tsc",
        "TscTestnet1",
        "Xdc",
        "XdcApothem",
        "XLayer",
        "XLayerSepolia",
    ]
    address: str
    name: NotRequired[str]
    external_id: NotRequired[str]
    tags: list[str]
    status: Literal["Active", "Archived"]
    date_created: str
    date_deleted: NotRequired[str]


class GetAddressWatchResponse(TypedDict, total=False):
    """getAddressWatch response."""

    id: str
    network: Literal[
        "ArbitrumOne",
        "ArbitrumSepolia",
        "ArcTestnet",
        "AvalancheC",
        "AvalancheCFuji",
        "Base",
        "BaseSepolia",
        "Berachain",
        "BerachainBepolia",
        "Bob",
        "BobSepolia",
        "Bsc",
        "BscTestnet",
        "Celo",
        "CeloAlfajores",
        "Codex",
        "CodexSepolia",
        "Ethereum",
        "EthereumClassic",
        "EthereumClassicMordor",
        "EthereumSepolia",
        "EthereumHoodi",
        "FlareC",
        "FlareCCoston2",
        "FlowEvm",
        "FlowEvmTestnet",
        "Ink",
        "InkSepolia",
        "Optimism",
        "OptimismSepolia",
        "Plasma",
        "PlasmaTestnet",
        "Plume",
        "PlumeSepolia",
        "Polygon",
        "PolygonAmoy",
        "Race",
        "RaceSepolia",
        "Rayls",
        "RaylsTestnet",
        "Robinhood",
        "RobinhoodSepolia",
        "SeiAtlantic2",
        "SeiPacific1",
        "Solana",
        "SolanaDevnet",
        "Sonic",
        "SonicTestnet",
        "Tempo",
        "TempoModerato",
        "Tsc",
        "TscTestnet1",
        "Xdc",
        "XdcApothem",
        "XLayer",
        "XLayerSepolia",
    ]
    address: str
    name: NotRequired[str]
    external_id: NotRequired[str]
    tags: list[str]
    status: Literal["Active", "Archived"]
    date_created: str
    date_deleted: NotRequired[str]


class GetAddressWatchAssetsResponse(TypedDict, total=False):
    """getAddressWatchAssets response."""

    address_watch_id: str
    network: Literal[
        "ArbitrumOne",
        "ArbitrumSepolia",
        "ArcTestnet",
        "AvalancheC",
        "AvalancheCFuji",
        "Base",
        "BaseSepolia",
        "Berachain",
        "BerachainBepolia",
        "Bob",
        "BobSepolia",
        "Bsc",
        "BscTestnet",
        "Celo",
        "CeloAlfajores",
        "Codex",
        "CodexSepolia",
        "Ethereum",
        "EthereumClassic",
        "EthereumClassicMordor",
        "EthereumSepolia",
        "EthereumHoodi",
        "FlareC",
        "FlareCCoston2",
        "FlowEvm",
        "FlowEvmTestnet",
        "Ink",
        "InkSepolia",
        "Optimism",
        "OptimismSepolia",
        "Plasma",
        "PlasmaTestnet",
        "Plume",
        "PlumeSepolia",
        "Polygon",
        "PolygonAmoy",
        "Race",
        "RaceSepolia",
        "Rayls",
        "RaylsTestnet",
        "Robinhood",
        "RobinhoodSepolia",
        "SeiAtlantic2",
        "SeiPacific1",
        "Solana",
        "SolanaDevnet",
        "Sonic",
        "SonicTestnet",
        "Tempo",
        "TempoModerato",
        "Tsc",
        "TscTestnet1",
        "Xdc",
        "XdcApothem",
        "XLayer",
        "XLayerSepolia",
    ]
    assets: list[dict[str, Any]]
    net_worth: NotRequired[dict[str, Any]]


class GetAddressWatchAssetsQuery(TypedDict, total=False):
    """getAddressWatchAssets query parameters."""

    net_worth: NotRequired[Literal["true"]]


class GetAddressWatchBlockchainEventsResponse(TypedDict, total=False):
    """getAddressWatchBlockchainEvents response."""

    items: list[dict[str, Any]]
    next_page_token: NotRequired[str]
    address_watch_id: str
    network: Literal[
        "ArbitrumOne",
        "ArbitrumSepolia",
        "ArcTestnet",
        "AvalancheC",
        "AvalancheCFuji",
        "Base",
        "BaseSepolia",
        "Berachain",
        "BerachainBepolia",
        "Bob",
        "BobSepolia",
        "Bsc",
        "BscTestnet",
        "Celo",
        "CeloAlfajores",
        "Codex",
        "CodexSepolia",
        "Ethereum",
        "EthereumClassic",
        "EthereumClassicMordor",
        "EthereumSepolia",
        "EthereumHoodi",
        "FlareC",
        "FlareCCoston2",
        "FlowEvm",
        "FlowEvmTestnet",
        "Ink",
        "InkSepolia",
        "Optimism",
        "OptimismSepolia",
        "Plasma",
        "PlasmaTestnet",
        "Plume",
        "PlumeSepolia",
        "Polygon",
        "PolygonAmoy",
        "Race",
        "RaceSepolia",
        "Rayls",
        "RaylsTestnet",
        "Robinhood",
        "RobinhoodSepolia",
        "SeiAtlantic2",
        "SeiPacific1",
        "Solana",
        "SolanaDevnet",
        "Sonic",
        "SonicTestnet",
        "Tempo",
        "TempoModerato",
        "Tsc",
        "TscTestnet1",
        "Xdc",
        "XdcApothem",
        "XLayer",
        "XLayerSepolia",
    ]


class GetAddressWatchBlockchainEventsQuery(TypedDict, total=False):
    """getAddressWatchBlockchainEvents query parameters."""

    limit: NotRequired[int]
    pagination_token: NotRequired[str]
    name: NotRequired[str]
    contract: NotRequired[str]
    tx_hash: NotRequired[str]


class GetAddressWatchHistoryResponse(TypedDict, total=False):
    """getAddressWatchHistory response."""

    items: list[dict[str, Any]]
    next_page_token: NotRequired[str]
    address_watch_id: str
    network: Literal[
        "ArbitrumOne",
        "ArbitrumSepolia",
        "ArcTestnet",
        "AvalancheC",
        "AvalancheCFuji",
        "Base",
        "BaseSepolia",
        "Berachain",
        "BerachainBepolia",
        "Bob",
        "BobSepolia",
        "Bsc",
        "BscTestnet",
        "Celo",
        "CeloAlfajores",
        "Codex",
        "CodexSepolia",
        "Ethereum",
        "EthereumClassic",
        "EthereumClassicMordor",
        "EthereumSepolia",
        "EthereumHoodi",
        "FlareC",
        "FlareCCoston2",
        "FlowEvm",
        "FlowEvmTestnet",
        "Ink",
        "InkSepolia",
        "Optimism",
        "OptimismSepolia",
        "Plasma",
        "PlasmaTestnet",
        "Plume",
        "PlumeSepolia",
        "Polygon",
        "PolygonAmoy",
        "Race",
        "RaceSepolia",
        "Rayls",
        "RaylsTestnet",
        "Robinhood",
        "RobinhoodSepolia",
        "SeiAtlantic2",
        "SeiPacific1",
        "Solana",
        "SolanaDevnet",
        "Sonic",
        "SonicTestnet",
        "Tempo",
        "TempoModerato",
        "Tsc",
        "TscTestnet1",
        "Xdc",
        "XdcApothem",
        "XLayer",
        "XLayerSepolia",
    ]


class GetAddressWatchHistoryQuery(TypedDict, total=False):
    """getAddressWatchHistory query parameters."""

    limit: NotRequired[int]
    pagination_token: NotRequired[str]
    direction: NotRequired[Literal["In", "Out"]]
    kind: NotRequired[
        Literal[
            "NativeTransfer",
            "Aip21Transfer",
            "AsaTransfer",
            "AssetTransfer",
            "Cip56Transfer",
            "Cis2Transfer",
            "Cis7Transfer",
            "CoinTransfer",
            "Erc20Transfer",
            "Erc721Transfer",
            "Erc7984Transfer",
            "HederaErc20Transfer",
            "HederaErc721Transfer",
            "Hip17Transfer",
            "HtsTransfer",
            "IouTransfer",
            "LockedCoinTransfer",
            "Sep41Transfer",
            "Snip2Transfer",
            "Snip3Transfer",
            "SplTransfer",
            "Spl2022Transfer",
            "Tep74Transfer",
            "Trc10Transfer",
            "Trc20Transfer",
            "Trc721Transfer",
            "UtxoTransfer",
            "Xls33Transfer",
        ]
    ]
    contract: NotRequired[str]
