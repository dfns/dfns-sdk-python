"""Types for the payins domain."""

from typing import Any, Literal, TypedDict

from typing_extensions import NotRequired


class ListPayinsResponse(TypedDict, total=False):
    """listPayins response."""

    items: list[dict[str, Any]]
    next_page_token: NotRequired[str]


class ListPayinsQuery(TypedDict, total=False):
    """listPayins query parameters."""

    limit: NotRequired[int]
    pagination_token: NotRequired[str]
    wallet_id: NotRequired[str]
    status: NotRequired[list[Literal["Processing", "Completed", "Failed"]]]
    provider: NotRequired[list[Literal["CircleMint", "Borderless"]]]


class CreatePayinQuoteResponse(TypedDict, total=False):
    """createPayinQuote response."""

    provider: Literal["CircleMint", "Borderless"]
    currency: Literal["USD", "EUR"]
    network: Literal[
        "Algorand",
        "AlgorandTestnet",
        "Aptos",
        "AptosTestnet",
        "ArbitrumOne",
        "ArbitrumSepolia",
        "Arc",
        "ArcTestnet",
        "Areum",
        "AvalancheC",
        "AvalancheCFuji",
        "Base",
        "BaseSepolia",
        "Berachain",
        "BerachainBepolia",
        "Bitcoin",
        "BitcoinSignet",
        "BitcoinTestnet4",
        "BitcoinCash",
        "Bob",
        "BobSepolia",
        "Bsc",
        "BscTestnet",
        "Canton",
        "CantonTestnet",
        "Cardano",
        "CardanoPreprod",
        "Concordium",
        "ConcordiumTestnet",
        "Celo",
        "CeloSepolia",
        "Codex",
        "CodexSepolia",
        "CosmosHub4",
        "CosmosIcsTestnet",
        "Dogecoin",
        "DogecoinTestnet",
        "Ethereum",
        "EthereumClassic",
        "EthereumClassicMordor",
        "EthereumSepolia",
        "EthereumHoodi",
        "FlareC",
        "FlareCCoston2",
        "FlowEvm",
        "FlowEvmTestnet",
        "Hedera",
        "HederaTestnet",
        "HyperEvm",
        "HyperEvmTestnet",
        "Ink",
        "InkSepolia",
        "InternetComputer",
        "Ion",
        "IonTestnet",
        "Iota",
        "IotaTestnet",
        "Kusama",
        "KusamaAssetHub",
        "Litecoin",
        "LitecoinTestnet",
        "Monad",
        "MonadTestnet",
        "Movement",
        "MovementTestnet",
        "Near",
        "NearTestnet",
        "Optimism",
        "OptimismSepolia",
        "Origyn",
        "Plasma",
        "PlasmaTestnet",
        "Plume",
        "PlumeSepolia",
        "Paseo",
        "PaseoAssetHub",
        "Polkadot",
        "PolkadotAssetHub",
        "Polygon",
        "PolygonAmoy",
        "Polymesh",
        "PolymeshTestnet",
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
        "Starknet",
        "StarknetSepolia",
        "Stellar",
        "StellarTestnet",
        "Sui",
        "SuiTestnet",
        "Tezos",
        "TezosShadownet",
        "Tempo",
        "TempoModerato",
        "Tsc",
        "TscTestnet1",
        "Ton",
        "TonTestnet",
        "Tron",
        "TronNile",
        "Westend",
        "WestendAssetHub",
        "Xdc",
        "XdcApothem",
        "XLayer",
        "XLayerSepolia",
        "XrpLedger",
        "XrpLedgerTestnet",
    ]
    tid: str
    timestamp: str
    quotes: list[dict[str, Any]]


class GetPayinRecipientResponse(TypedDict, total=False):
    """getPayinRecipient response."""

    provider: Literal["CircleMint", "Borderless"]
    wallet_id: str
    currency: Literal["USD", "EUR"]
    status: Literal["NotRegistered", "PendingVerification", "Active"]
    recipient_address_id: NotRequired[str]


class GetPayinRecipientQuery(TypedDict, total=False):
    """getPayinRecipient query parameters."""

    provider: Literal["CircleMint", "Borderless"]
    wallet_id: str
    currency: Literal["USD", "EUR"]


class CreatePayinRecipientResponse(TypedDict, total=False):
    """createPayinRecipient response."""

    provider: Literal["CircleMint", "Borderless"]
    wallet_id: str
    currency: Literal["USD", "EUR"]
    status: Literal["NotRegistered", "PendingVerification", "Active"]
    recipient_address_id: NotRequired[str]


class ListPayinAccountsResponse(TypedDict, total=False):
    """listPayinAccounts response."""

    items: list[dict[str, Any]]


class ListPayinAccountsQuery(TypedDict, total=False):
    """listPayinAccounts query parameters."""

    provider: Literal["CircleMint", "Borderless"]


class ListPayinBalancesResponse(TypedDict, total=False):
    """listPayinBalances response."""

    items: list[dict[str, Any]]


class ListPayinBalancesQuery(TypedDict, total=False):
    """listPayinBalances query parameters."""

    provider: Literal["CircleMint", "Borderless"]


class ListPayinOptionsResponse(TypedDict, total=False):
    """listPayinOptions response."""

    assets: list[str]
    currencies: list[dict[str, Any]]


class ListPayinOptionsQuery(TypedDict, total=False):
    """listPayinOptions query parameters."""

    provider: Literal["CircleMint", "Borderless"]


class RegisterPayinAccountAssetResponse(TypedDict, total=False):
    """registerPayinAccountAsset response."""

    account_id: str
    name: NotRequired[str]
    assets: list[dict[str, Any]]


# Deprecated: use CreatePayinQuoteResponse instead.
RequestPayinQuoteResponse = CreatePayinQuoteResponse

# Deprecated: use CreatePayinRecipientResponse instead.
RegisterPayinRecipientResponse = CreatePayinRecipientResponse
