"""Types for the policies domain."""

from typing import Any, Literal, TypedDict

from typing_extensions import NotRequired


class GetPolicyResponse(TypedDict, total=False):
    """getPolicy response."""

    pending_change_request: NotRequired[dict[str, Any]]


class CreateApprovalDecisionRequest(TypedDict, total=False):
    """createApprovalDecision request body."""

    value: Literal["Approved", "Denied"]
    reason: NotRequired[str]


class CreateApprovalDecisionResponse(TypedDict, total=False):
    """createApprovalDecision response."""

    id: str
    initiator_id: str
    activity: dict[str, Any]
    status: Literal["Pending", "Approved", "Denied", "Expired"]
    expiration_date: NotRequired[str]
    date_created: NotRequired[str]
    date_updated: str
    date_resolved: NotRequired[str]
    policy_evaluations: list[dict[str, Any]]
    decisions: list[dict[str, Any]]


class ListPoliciesResponse(TypedDict, total=False):
    """listPolicies response."""

    items: list[dict[str, Any]]
    next_page_token: NotRequired[str]


class ListPoliciesQuery(TypedDict, total=False):
    """listPolicies query parameters."""

    limit: NotRequired[str]
    pagination_token: NotRequired[str]
    status: NotRequired[Literal["Active", "Archived"]]


class GetSumsubTravelRulePublicKeyResponse(TypedDict, total=False):
    """getSumsubTravelRulePublicKey response."""

    kty: Literal["RSA"]
    kid: str
    n: str
    e: str
    use: NotRequired[str]


class GetApprovalResponse(TypedDict, total=False):
    """getApproval response."""

    id: str
    initiator_id: str
    activity: dict[str, Any]
    status: Literal["Pending", "Approved", "Denied", "Expired"]
    expiration_date: NotRequired[str]
    date_created: NotRequired[str]
    date_updated: str
    date_resolved: NotRequired[str]
    policy_evaluations: list[dict[str, Any]]
    decisions: list[dict[str, Any]]


class ListApprovalsResponse(TypedDict, total=False):
    """listApprovals response."""

    items: list[dict[str, Any]]
    next_page_token: NotRequired[str]


class ListApprovalsQuery(TypedDict, total=False):
    """listApprovals query parameters."""

    limit: NotRequired[str]
    pagination_token: NotRequired[str]
    status: NotRequired[Literal["Pending", "Approved", "Denied", "Expired"]]
    initiator_id: NotRequired[str]
    approver_id: NotRequired[str]


class LookupSumsubTravelRuleVaspRequest(TypedDict, total=False):
    """lookupSumsubTravelRuleVasp request body."""

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
    wallet_address: str
