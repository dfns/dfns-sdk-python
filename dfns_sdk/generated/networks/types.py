"""Types for the networks domain."""

from typing import Any, Literal, TypedDict, cast
from typing_extensions import NotRequired, deprecated


class EstimateFeesQuery(TypedDict, total=False):
    """estimateFees query parameters."""

    network: Literal["Bitcoin", "BitcoinSignet", "BitcoinTestnet4", "Litecoin", "LitecoinTestnet", "Dogecoin", "DogecoinTestnet", "ArbitrumOne", "ArbitrumSepolia", "ArcTestnet", "AvalancheC", "AvalancheCFuji", "Base", "BaseSepolia", "Bob", "BobSepolia", "Bsc", "BscTestnet", "Berachain", "BerachainBepolia", "Celo", "CeloAlfajores", "Codex", "CodexSepolia", "Ethereum", "EthereumClassic", "EthereumClassicMordor", "EthereumSepolia", "EthereumHoodi", "FlareC", "FlareCCoston2", "FlowEvm", "FlowEvmTestnet", "Ink", "InkSepolia", "Optimism", "OptimismSepolia", "Plasma", "PlasmaTestnet", "Plume", "PlumeSepolia", "Polygon", "PolygonAmoy", "Race", "RaceSepolia", "Robinhood", "RobinhoodSepolia", "Sonic", "SonicTestnet", "Tempo", "TempoModerato", "Tsc", "TscTestnet1", "Xdc", "XdcApothem", "XLayer", "XLayerSepolia", "Solana", "SolanaDevnet"]

class CallFunctionRequest(TypedDict, total=False):
    """callFunction request body."""

    contract: str
    abi: dict[str, Any]
    calldata: NotRequired[dict[str, Any]]

class GetCantonValidatorResponse(TypedDict, total=False):
    """getCantonValidator response."""

    id: str
    org_id: str
    network: Literal["Canton", "CantonDevnet", "CantonTestnet"]
    name: NotRequired[str]
    kind: Literal["Shared", "Custom"]
    date_created: str
    party_hint: str

class UpdateCantonValidatorRequest(TypedDict, total=False):
    """updateCantonValidator request body."""

    name: NotRequired[str]
    validator: NotRequired[dict[str, Any]]
    ledger: NotRequired[dict[str, Any]]

class UpdateCantonValidatorResponse(TypedDict, total=False):
    """updateCantonValidator response."""

    id: str
    org_id: str
    network: Literal["Canton", "CantonDevnet", "CantonTestnet"]
    name: NotRequired[str]
    kind: Literal["Shared", "Custom"]
    date_created: str
    party_hint: str

class DeleteCantonValidatorResponse(TypedDict, total=False):
    """deleteCantonValidator response."""

    id: str
    org_id: str
    network: Literal["Canton", "CantonDevnet", "CantonTestnet"]
    name: NotRequired[str]
    kind: Literal["Shared", "Custom"]
    date_created: str
    party_hint: str

class ListCantonValidatorsResponse(TypedDict, total=False):
    """listCantonValidators response."""

    items: list[dict[str, Any]]
    next_page_token: NotRequired[str]

class ListCantonValidatorsQuery(TypedDict, total=False):
    """listCantonValidators query parameters."""

    limit: NotRequired[int]
    pagination_token: NotRequired[str]

class CreateCantonValidatorResponse(TypedDict, total=False):
    """createCantonValidator response."""

    id: str
    org_id: str
    network: Literal["Canton", "CantonDevnet", "CantonTestnet"]
    name: NotRequired[str]
    kind: Literal["Shared", "Custom"]
    date_created: str
    party_hint: str
