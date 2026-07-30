"""Types for the vaults domain."""

from typing import Any, Literal, TypedDict

from typing_extensions import NotRequired


class ListVaultsResponse(TypedDict, total=False):
    """listVaults response."""

    items: list[dict[str, Any]]
    next_page_token: NotRequired[str]


class ListVaultsQuery(TypedDict, total=False):
    """listVaults query parameters."""

    limit: NotRequired[int]
    pagination_token: NotRequired[str]


class CreateVaultRequest(TypedDict, total=False):
    """createVault request body."""

    name: NotRequired[str]
    tags: NotRequired[list[str]]
    external_id: NotRequired[str]


class CreateVaultResponse(TypedDict, total=False):
    """createVault response."""

    id: str
    org_id: str
    name: NotRequired[str]
    tags: list[str]
    external_id: NotRequired[str]
    date_created: str
    date_updated: str
    addresses: NotRequired[list[dict[str, Any]]]


class CreateVaultAddressRequest(TypedDict, total=False):
    """createVaultAddress request body."""

    network: (
        Literal[
            "ArbitrumOne",
            "ArbitrumSepolia",
            "ArcTestnet",
            "AvalancheC",
            "AvalancheCFuji",
            "Base",
            "BaseSepolia",
            "Bob",
            "BobSepolia",
            "Bsc",
            "BscTestnet",
            "Berachain",
            "BerachainBepolia",
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
            "SeiPacific1",
            "SeiAtlantic2",
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
        | Literal["Bitcoin", "BitcoinSignet", "BitcoinTestnet4"]
    )


class CreateVaultAddressResponse(TypedDict, total=False):
    """createVaultAddress response."""

    wallet_id: str
    network: str
    address: str


class CreateVaultTransferRequest(TypedDict, total=False):
    """createVaultTransfer request body."""

    network: (
        Literal[
            "ArbitrumOne",
            "ArbitrumSepolia",
            "ArcTestnet",
            "AvalancheC",
            "AvalancheCFuji",
            "Base",
            "BaseSepolia",
            "Bob",
            "BobSepolia",
            "Bsc",
            "BscTestnet",
            "Berachain",
            "BerachainBepolia",
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
            "SeiPacific1",
            "SeiAtlantic2",
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
        | Literal["Bitcoin", "BitcoinSignet", "BitcoinTestnet4"]
    )
    tid: str
    to: str
    amount: str
    external_id: NotRequired[str]


class CreateVaultTransferResponse(TypedDict, total=False):
    """createVaultTransfer response."""

    id: str
    wallet_id: str
    network: dict[str, Any]
    requester: dict[str, Any]
    request_body: dict[str, Any]
    metadata: dict[str, Any]
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
    replacement_id: NotRequired[str]
    details: NotRequired[dict[str, dict[str, Any]]]


class GetVaultResponse(TypedDict, total=False):
    """getVault response."""

    id: str
    org_id: str
    name: NotRequired[str]
    tags: list[str]
    external_id: NotRequired[str]
    date_created: str
    date_updated: str
    addresses: NotRequired[list[dict[str, Any]]]


class UpdateVaultRequest(TypedDict, total=False):
    """updateVault request body."""

    name: NotRequired[str]
    external_id: NotRequired[str]


class UpdateVaultResponse(TypedDict, total=False):
    """updateVault response."""

    id: str
    org_id: str
    name: NotRequired[str]
    tags: list[str]
    external_id: NotRequired[str]
    date_created: str
    date_updated: str
    addresses: NotRequired[list[dict[str, Any]]]


class ListVaultAssetsResponse(TypedDict, total=False):
    """listVaultAssets response."""

    items: list[dict[str, Any]]
    net_worth: dict[str, Any]


class ListVaultAssetsQuery(TypedDict, total=False):
    """listVaultAssets query parameters."""

    show_unverified: NotRequired[Any]
    network: NotRequired[str]


class ListVaultBalancesResponse(TypedDict, total=False):
    """listVaultBalances response."""

    items: list[dict[str, Any]]
    next_page_token: NotRequired[str]


class ListVaultBalancesQuery(TypedDict, total=False):
    """listVaultBalances query parameters."""

    limit: NotRequired[int]
    pagination_token: NotRequired[str]
    kind: NotRequired[Literal["Available", "Outgoing", "Fee", "Incoming", "Locked", "Quarantined"]]
    network: NotRequired[str]
    tid: NotRequired[str]


class ReleaseQuarantineRequest(TypedDict, total=False):
    """releaseQuarantine request body."""

    reason: NotRequired[str]


class ReleaseQuarantineResponse(TypedDict, total=False):
    """releaseQuarantine response."""

    status: Literal["OK"]


class TagVaultRequest(TypedDict, total=False):
    """tagVault request body."""

    tags: list[str]


class TagVaultResponse(TypedDict, total=False):
    """tagVault response."""

    pass


class UntagVaultRequest(TypedDict, total=False):
    """untagVault request body."""

    tags: list[str]


class UntagVaultResponse(TypedDict, total=False):
    """untagVault response."""

    pass
