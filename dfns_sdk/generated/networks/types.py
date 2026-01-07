"""Types for the networks domain."""

from typing import Any, Literal, NotRequired, Optional, TypedDict, Union

class EstimateFeesQuery(TypedDict, total=False):
    """estimateFees query parameters."""

    network: Literal["Bitcoin", "BitcoinSignet", "BitcoinTestnet3", "Adi", "AdiTestnet", "AdiTestnetAb", "ArbitrumOne", "ArbitrumGoerli", "ArbitrumSepolia", "ArcTestnet", "AvalancheC", "AvalancheCFuji", "Base", "BaseGoerli", "BaseSepolia", "Bob", "BobSepolia", "Bsc", "BscTestnet", "Berachain", "BerachainBArtio", "BerachainBepolia", "Celo", "CeloAlfajores", "Codex", "CodexSepolia", "Ethereum", "EthereumClassic", "EthereumClassicMordor", "EthereumGoerli", "EthereumSepolia", "EthereumHolesky", "EthereumHoodi", "FantomOpera", "FantomTestnet", "FlareC", "FlareCCoston2", "FlowEvm", "FlowEvmTestnet", "Ink", "InkSepolia", "Optimism", "OptimismGoerli", "OptimismSepolia", "Plasma", "PlasmaTestnet", "Plume", "PlumeSepolia", "Polygon", "PolygonAmoy", "PolygonMumbai", "Race", "RaceSepolia", "Sonic", "SonicTestnet", "TempoAndantino", "Tsc", "TscTestnet1"]

class ReadContractResponse(TypedDict, total=False):
    """readContract response."""

    kind: Literal["Evm"]
    data: str

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
    validator: NotRequired[TypedDict]
    ledger: NotRequired[TypedDict]

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

    items: list[TypedDict]
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
