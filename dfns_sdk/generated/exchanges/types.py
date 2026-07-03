"""Types for the exchanges domain."""

from typing import Any, Literal, NotRequired, Optional, TypedDict, Union

class GetExchangeResponse(TypedDict, total=False):
    """getExchange response."""

    id: str
    name: NotRequired[str]
    kind: Literal["Binance", "Kraken", "CoinbaseApp", "CoinbasePrime"]
    date_created: str

class DeleteExchangeResponse(TypedDict, total=False):
    """deleteExchange response."""

    deleted: Literal[True]

class ListExchangesResponse(TypedDict, total=False):
    """listExchanges response."""

    items: list[TypedDict]
    next_page_token: NotRequired[str]

class ListExchangesQuery(TypedDict, total=False):
    """listExchanges query parameters."""

    limit: NotRequired[int]
    pagination_token: NotRequired[str]

class CreateExchangeRequest(TypedDict, total=False):
    """createExchange request body."""

    name: NotRequired[str]
    kind: Literal["Binance", "Kraken", "CoinbaseApp", "CoinbasePrime"]
    read_configuration: TypedDict
    write_configuration: TypedDict

class CreateExchangeResponse(TypedDict, total=False):
    """createExchange response."""

    id: str
    name: NotRequired[str]
    kind: Literal["Binance", "Kraken", "CoinbaseApp", "CoinbasePrime"]
    date_created: str

class ListAccountsResponse(TypedDict, total=False):
    """listAccounts response."""

    items: list[TypedDict]
    next_page_token: NotRequired[str]

class ListAccountsQuery(TypedDict, total=False):
    """listAccounts query parameters."""

    limit: NotRequired[int]
    pagination_token: NotRequired[str]

class ListAccountAssetsResponse(TypedDict, total=False):
    """listAccountAssets response."""

    items: list[TypedDict]
    next_page_token: NotRequired[str]

class ListAccountAssetsQuery(TypedDict, total=False):
    """listAccountAssets query parameters."""

    limit: NotRequired[int]
    pagination_token: NotRequired[str]

class CreateExchangeDepositResponse(TypedDict, total=False):
    """createExchangeDeposit response."""

    id: str
    exchange_id: str
    account_id: str
    transfer_id: NotRequired[str]
    exchange_reference: NotRequired[str]
    kind: Literal["Withdrawal", "Deposit"]
    wallet_id: str
    requester: TypedDict
    request_body: TypedDict
    date_created: str

class CreateExchangeWithdrawalResponse(TypedDict, total=False):
    """createExchangeWithdrawal response."""

    id: str
    exchange_id: str
    account_id: str
    transfer_id: NotRequired[str]
    exchange_reference: NotRequired[str]
    kind: Literal["Withdrawal", "Deposit"]
    wallet_id: str
    requester: TypedDict
    request_body: TypedDict
    date_created: str
