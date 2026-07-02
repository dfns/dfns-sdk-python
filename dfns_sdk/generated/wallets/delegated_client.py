"""Delegated client for the wallets domain."""

import json
from typing import Any, cast

from ..._internal import HttpClient
from ...base_auth_api import BaseAuthApi, SignUserActionChallengeRequest, UserActionChallengeResponse
from . import types as T


class DelegatedWalletsClient:
    """
    Delegated client for wallets operations.

    This client separates user action signing into _init() and _complete() method pairs,
    allowing external systems to handle the signing process.
    """

    def __init__(self, http_client: HttpClient):
        self._http = http_client

    def abort_transaction_init(self, wallet_id: str, transaction_id: str) -> UserActionChallengeResponse:
        """
        Initialize Abort Transaction.

        Creates a user action challenge for external signing.

        Args:
            wallet_id: Wallet id.
            transaction_id: Transaction id.

        Returns:
            UserActionChallengeResponse: The challenge to sign externally.
        """  # noqa: E501
        path = "/wallets/{walletId}/transactions/{transactionId}/abort"
        path = path.replace("{walletId}", str(wallet_id))
        path = path.replace("{transactionId}", str(transaction_id))
        payload = ""

        return BaseAuthApi.create_user_action_challenge(
            self._http,
            user_action_http_method="PUT",
            user_action_http_path=path,
            user_action_payload=payload,
        )

    def abort_transaction_complete(
        self, wallet_id: str, transaction_id: str, signed_challenge: SignUserActionChallengeRequest
    ) -> T.AbortTransactionResponse:
        """
        Complete Abort Transaction.

        Submits the signed challenge and makes the API request.

        Args:
            wallet_id: Wallet id.
            transaction_id: Transaction id.
            signed_challenge: The signed challenge from external signing.

        Returns:
            T.AbortTransactionResponse: The API response.
        """  # noqa: E501
        user_action_result = BaseAuthApi.sign_user_action_challenge(self._http, signed_challenge)
        user_action_token = user_action_result["userAction"]

        response = self._http.request_with_user_action(
            method="PUT",
            path="/wallets/{walletId}/transactions/{transactionId}/abort",
            path_params={"walletId": wallet_id, "transactionId": transaction_id},
            query_params=None,
            body=None,
            user_action=user_action_token,
        )
        return cast(T.AbortTransactionResponse, response)

    def abort_transfer_init(self, wallet_id: str, transfer_id: str) -> UserActionChallengeResponse:
        """
        Initialize Abort Transfer.

        Creates a user action challenge for external signing.

        Args:
            wallet_id: Wallet id.
            transfer_id: Transfer id.

        Returns:
            UserActionChallengeResponse: The challenge to sign externally.
        """  # noqa: E501
        path = "/wallets/{walletId}/transfers/{transferId}/abort"
        path = path.replace("{walletId}", str(wallet_id))
        path = path.replace("{transferId}", str(transfer_id))
        payload = ""

        return BaseAuthApi.create_user_action_challenge(
            self._http,
            user_action_http_method="PUT",
            user_action_http_path=path,
            user_action_payload=payload,
        )

    def abort_transfer_complete(
        self, wallet_id: str, transfer_id: str, signed_challenge: SignUserActionChallengeRequest
    ) -> T.AbortTransferResponse:
        """
        Complete Abort Transfer.

        Submits the signed challenge and makes the API request.

        Args:
            wallet_id: Wallet id.
            transfer_id: Transfer id.
            signed_challenge: The signed challenge from external signing.

        Returns:
            T.AbortTransferResponse: The API response.
        """  # noqa: E501
        user_action_result = BaseAuthApi.sign_user_action_challenge(self._http, signed_challenge)
        user_action_token = user_action_result["userAction"]

        response = self._http.request_with_user_action(
            method="PUT",
            path="/wallets/{walletId}/transfers/{transferId}/abort",
            path_params={"walletId": wallet_id, "transferId": transfer_id},
            query_params=None,
            body=None,
            user_action=user_action_token,
        )
        return cast(T.AbortTransferResponse, response)

    def activate_wallet_init(self, wallet_id: str, body: dict[str, Any]) -> UserActionChallengeResponse:
        """
        Initialize Activate Wallet.

        Creates a user action challenge for external signing.

        Args:
            wallet_id: Wallet id.
            body: Request body.

        Returns:
            UserActionChallengeResponse: The challenge to sign externally.
        """  # noqa: E501
        path = "/wallets/{walletId}/activate"
        path = path.replace("{walletId}", str(wallet_id))
        payload = json.dumps(body, separators=(",", ":")) if body else ""

        return BaseAuthApi.create_user_action_challenge(
            self._http,
            user_action_http_method="POST",
            user_action_http_path=path,
            user_action_payload=payload,
        )

    def activate_wallet_complete(
        self, wallet_id: str, body: dict[str, Any], signed_challenge: SignUserActionChallengeRequest
    ) -> T.ActivateWalletResponse:
        """
        Complete Activate Wallet.

        Submits the signed challenge and makes the API request.

        Args:
            wallet_id: Wallet id.
            body: Request body.
            signed_challenge: The signed challenge from external signing.

        Returns:
            T.ActivateWalletResponse: The API response.
        """  # noqa: E501
        user_action_result = BaseAuthApi.sign_user_action_challenge(self._http, signed_challenge)
        user_action_token = user_action_result["userAction"]

        response = self._http.request_with_user_action(
            method="POST",
            path="/wallets/{walletId}/activate",
            path_params={"walletId": wallet_id},
            query_params=None,
            body=body,
            user_action=user_action_token,
        )
        return cast(T.ActivateWalletResponse, response)

    def list_transactions(
        self, wallet_id: str, query: T.ListTransactionsQuery | None = None
    ) -> T.ListTransactionsResponse:
        """
        List Transactions.

        Retrieves a list of transactions requests for the specified wallet.

        Args:
            wallet_id: Wallet id.
            query: Query parameters.

        Returns:
            T.ListTransactionsResponse: The API response.
        """  # noqa: E501
        response = self._http.request(
            method="GET",
            path="/wallets/{walletId}/transactions",
            path_params={"walletId": wallet_id},
            query_params=query,
            body=None,
            requires_signature=False,
        )
        return cast(T.ListTransactionsResponse, response)

    def sign_and_broadcast_transaction_init(self, wallet_id: str, body: dict[str, Any]) -> UserActionChallengeResponse:
        """
        Initialize Sign and Broadcast Transaction.

        Creates a user action challenge for external signing.

        Args:
            wallet_id: Wallet id.
            body: Request body.

        Returns:
            UserActionChallengeResponse: The challenge to sign externally.
        """  # noqa: E501
        path = "/wallets/{walletId}/transactions"
        path = path.replace("{walletId}", str(wallet_id))
        payload = json.dumps(body, separators=(",", ":")) if body else ""

        return BaseAuthApi.create_user_action_challenge(
            self._http,
            user_action_http_method="POST",
            user_action_http_path=path,
            user_action_payload=payload,
        )

    def sign_and_broadcast_transaction_complete(
        self, wallet_id: str, body: dict[str, Any], signed_challenge: SignUserActionChallengeRequest
    ) -> T.SignAndBroadcastTransactionResponse:
        """
        Complete Sign and Broadcast Transaction.

        Submits the signed challenge and makes the API request.

        Args:
            wallet_id: Wallet id.
            body: Request body.
            signed_challenge: The signed challenge from external signing.

        Returns:
            T.SignAndBroadcastTransactionResponse: The API response.
        """  # noqa: E501
        user_action_result = BaseAuthApi.sign_user_action_challenge(self._http, signed_challenge)
        user_action_token = user_action_result["userAction"]

        response = self._http.request_with_user_action(
            method="POST",
            path="/wallets/{walletId}/transactions",
            path_params={"walletId": wallet_id},
            query_params=None,
            body=body,
            user_action=user_action_token,
        )
        return cast(T.SignAndBroadcastTransactionResponse, response)

    def cancel_transaction_init(self, wallet_id: str, transaction_id: str) -> UserActionChallengeResponse:
        """
        Initialize Cancel Transaction.

        Creates a user action challenge for external signing.

        Args:
            wallet_id: Wallet id.
            transaction_id: Transaction id.

        Returns:
            UserActionChallengeResponse: The challenge to sign externally.
        """  # noqa: E501
        path = "/wallets/{walletId}/transactions/{transactionId}/cancel"
        path = path.replace("{walletId}", str(wallet_id))
        path = path.replace("{transactionId}", str(transaction_id))
        payload = ""

        return BaseAuthApi.create_user_action_challenge(
            self._http,
            user_action_http_method="POST",
            user_action_http_path=path,
            user_action_payload=payload,
        )

    def cancel_transaction_complete(
        self, wallet_id: str, transaction_id: str, signed_challenge: SignUserActionChallengeRequest
    ) -> T.CancelTransactionResponse:
        """
        Complete Cancel Transaction.

        Submits the signed challenge and makes the API request.

        Args:
            wallet_id: Wallet id.
            transaction_id: Transaction id.
            signed_challenge: The signed challenge from external signing.

        Returns:
            T.CancelTransactionResponse: The API response.
        """  # noqa: E501
        user_action_result = BaseAuthApi.sign_user_action_challenge(self._http, signed_challenge)
        user_action_token = user_action_result["userAction"]

        response = self._http.request_with_user_action(
            method="POST",
            path="/wallets/{walletId}/transactions/{transactionId}/cancel",
            path_params={"walletId": wallet_id, "transactionId": transaction_id},
            query_params=None,
            body=None,
            user_action=user_action_token,
        )
        return cast(T.CancelTransactionResponse, response)

    def cancel_transfer_init(self, wallet_id: str, transfer_id: str) -> UserActionChallengeResponse:
        """
        Initialize Cancel Transfer.

        Creates a user action challenge for external signing.

        Args:
            wallet_id: Wallet id.
            transfer_id: Transfer id.

        Returns:
            UserActionChallengeResponse: The challenge to sign externally.
        """  # noqa: E501
        path = "/wallets/{walletId}/transfers/{transferId}/cancel"
        path = path.replace("{walletId}", str(wallet_id))
        path = path.replace("{transferId}", str(transfer_id))
        payload = ""

        return BaseAuthApi.create_user_action_challenge(
            self._http,
            user_action_http_method="POST",
            user_action_http_path=path,
            user_action_payload=payload,
        )

    def cancel_transfer_complete(
        self, wallet_id: str, transfer_id: str, signed_challenge: SignUserActionChallengeRequest
    ) -> T.CancelTransferResponse:
        """
        Complete Cancel Transfer.

        Submits the signed challenge and makes the API request.

        Args:
            wallet_id: Wallet id.
            transfer_id: Transfer id.
            signed_challenge: The signed challenge from external signing.

        Returns:
            T.CancelTransferResponse: The API response.
        """  # noqa: E501
        user_action_result = BaseAuthApi.sign_user_action_challenge(self._http, signed_challenge)
        user_action_token = user_action_result["userAction"]

        response = self._http.request_with_user_action(
            method="POST",
            path="/wallets/{walletId}/transfers/{transferId}/cancel",
            path_params={"walletId": wallet_id, "transferId": transfer_id},
            query_params=None,
            body=None,
            user_action=user_action_token,
        )
        return cast(T.CancelTransferResponse, response)

    def proxy_a_request_to_the_canton_ledger_api(
        self, wallet_id: str, body: T.ProxyARequestToTheCantonLedgerApiRequest
    ) -> dict[str, Any]:
        """
        Proxy a request to the Canton Ledger API.

        Proxies a request to the Canton Ledger API associated with this wallet, using the validator's OAuth2 credentials. Restricted to a curated allow-list of read-style resources. Used to satisfy the Canton WalletConnect `canton_ledgerApi` method.

        Args:
            wallet_id: Wallet id.
            body: Request body.

        Returns:
            dict[str, Any]: The API response.
        """  # noqa: E501
        response = self._http.request(
            method="POST",
            path="/wallets/{walletId}/canton/ledger-api",
            path_params={"walletId": wallet_id},
            query_params=None,
            body=body,
            requires_signature=False,
        )
        return cast(dict[str, Any], response)

    def speed_up_transaction_init(self, wallet_id: str, transaction_id: str) -> UserActionChallengeResponse:
        """
        Initialize Speed Up Transaction.

        Creates a user action challenge for external signing.

        Args:
            wallet_id: Wallet id.
            transaction_id: Transaction id.

        Returns:
            UserActionChallengeResponse: The challenge to sign externally.
        """  # noqa: E501
        path = "/wallets/{walletId}/transactions/{transactionId}/speed-up"
        path = path.replace("{walletId}", str(wallet_id))
        path = path.replace("{transactionId}", str(transaction_id))
        payload = ""

        return BaseAuthApi.create_user_action_challenge(
            self._http,
            user_action_http_method="POST",
            user_action_http_path=path,
            user_action_payload=payload,
        )

    def speed_up_transaction_complete(
        self, wallet_id: str, transaction_id: str, signed_challenge: SignUserActionChallengeRequest
    ) -> T.SpeedUpTransactionResponse:
        """
        Complete Speed Up Transaction.

        Submits the signed challenge and makes the API request.

        Args:
            wallet_id: Wallet id.
            transaction_id: Transaction id.
            signed_challenge: The signed challenge from external signing.

        Returns:
            T.SpeedUpTransactionResponse: The API response.
        """  # noqa: E501
        user_action_result = BaseAuthApi.sign_user_action_challenge(self._http, signed_challenge)
        user_action_token = user_action_result["userAction"]

        response = self._http.request_with_user_action(
            method="POST",
            path="/wallets/{walletId}/transactions/{transactionId}/speed-up",
            path_params={"walletId": wallet_id, "transactionId": transaction_id},
            query_params=None,
            body=None,
            user_action=user_action_token,
        )
        return cast(T.SpeedUpTransactionResponse, response)

    def speed_up_transfer_init(self, wallet_id: str, transfer_id: str) -> UserActionChallengeResponse:
        """
        Initialize Speed Up Transfer.

        Creates a user action challenge for external signing.

        Args:
            wallet_id: Wallet id.
            transfer_id: Transfer id.

        Returns:
            UserActionChallengeResponse: The challenge to sign externally.
        """  # noqa: E501
        path = "/wallets/{walletId}/transfers/{transferId}/speed-up"
        path = path.replace("{walletId}", str(wallet_id))
        path = path.replace("{transferId}", str(transfer_id))
        payload = ""

        return BaseAuthApi.create_user_action_challenge(
            self._http,
            user_action_http_method="POST",
            user_action_http_path=path,
            user_action_payload=payload,
        )

    def speed_up_transfer_complete(
        self, wallet_id: str, transfer_id: str, signed_challenge: SignUserActionChallengeRequest
    ) -> T.SpeedUpTransferResponse:
        """
        Complete Speed Up Transfer.

        Submits the signed challenge and makes the API request.

        Args:
            wallet_id: Wallet id.
            transfer_id: Transfer id.
            signed_challenge: The signed challenge from external signing.

        Returns:
            T.SpeedUpTransferResponse: The API response.
        """  # noqa: E501
        user_action_result = BaseAuthApi.sign_user_action_challenge(self._http, signed_challenge)
        user_action_token = user_action_result["userAction"]

        response = self._http.request_with_user_action(
            method="POST",
            path="/wallets/{walletId}/transfers/{transferId}/speed-up",
            path_params={"walletId": wallet_id, "transferId": transfer_id},
            query_params=None,
            body=None,
            user_action=user_action_token,
        )
        return cast(T.SpeedUpTransferResponse, response)

    def list_wallets(self, query: T.ListWalletsQuery | None = None) -> T.ListWalletsResponse:
        """
        List Wallets.

        Retrieves the list of Wallets in your organization. You can filter the results by owner (either by owner id or owner username). Pagination is supported via limit and paginationToken parameters.

        Args:
            query: Query parameters.

        Returns:
            T.ListWalletsResponse: The API response.
        """  # noqa: E501
        response = self._http.request(
            method="GET",
            path="/wallets",
            path_params={},
            query_params=query,
            body=None,
            requires_signature=False,
        )
        return cast(T.ListWalletsResponse, response)

    def create_wallet_init(self, body: T.CreateWalletRequest) -> UserActionChallengeResponse:
        """
        Initialize Create Wallet.

        Creates a user action challenge for external signing.

        Args:
            body: Request body.

        Returns:
            UserActionChallengeResponse: The challenge to sign externally.
        """  # noqa: E501
        path = "/wallets"
        payload = json.dumps(body, separators=(",", ":")) if body else ""

        return BaseAuthApi.create_user_action_challenge(
            self._http,
            user_action_http_method="POST",
            user_action_http_path=path,
            user_action_payload=payload,
        )

    def create_wallet_complete(
        self, body: T.CreateWalletRequest, signed_challenge: SignUserActionChallengeRequest
    ) -> T.CreateWalletResponse:
        """
        Complete Create Wallet.

        Submits the signed challenge and makes the API request.

        Args:
            body: Request body.
            signed_challenge: The signed challenge from external signing.

        Returns:
            T.CreateWalletResponse: The API response.
        """  # noqa: E501
        user_action_result = BaseAuthApi.sign_user_action_challenge(self._http, signed_challenge)
        user_action_token = user_action_result["userAction"]

        response = self._http.request_with_user_action(
            method="POST",
            path="/wallets",
            path_params={},
            query_params=None,
            body=body,
            user_action=user_action_token,
        )
        return cast(T.CreateWalletResponse, response)

    def get_transaction(self, wallet_id: str, transaction_id: str) -> T.GetTransactionResponse:
        """
        Get Transaction.

        Retrieve information about a specific transaction.

        Args:
            wallet_id: Wallet id.
            transaction_id: Transaction id.

        Returns:
            T.GetTransactionResponse: The API response.
        """  # noqa: E501
        response = self._http.request(
            method="GET",
            path="/wallets/{walletId}/transactions/{transactionId}",
            path_params={"walletId": wallet_id, "transactionId": transaction_id},
            query_params=None,
            body=None,
            requires_signature=False,
        )
        return cast(T.GetTransactionResponse, response)

    def get_transfer(self, wallet_id: str, transfer_id: str) -> T.GetTransferResponse:
        """
        Get Transfer.

        Retrieves a Wallet Transfer Request by its ID.

        Args:
            wallet_id: Wallet id.
            transfer_id: Transfer id.

        Returns:
            T.GetTransferResponse: The API response.
        """  # noqa: E501
        response = self._http.request(
            method="GET",
            path="/wallets/{walletId}/transfers/{transferId}",
            path_params={"walletId": wallet_id, "transferId": transfer_id},
            query_params=None,
            body=None,
            requires_signature=False,
        )
        return cast(T.GetTransferResponse, response)

    def get_wallet(self, wallet_id: str) -> T.GetWalletResponse:
        """
        Get Wallet.

        Retrieves a Wallet information by its ID.

        Args:
            wallet_id: The wallet to retrieve.

        Returns:
            T.GetWalletResponse: The API response.
        """  # noqa: E501
        response = self._http.request(
            method="GET",
            path="/wallets/{walletId}",
            path_params={"walletId": wallet_id},
            query_params=None,
            body=None,
            requires_signature=False,
        )
        return cast(T.GetWalletResponse, response)

    def update_wallet_init(self, wallet_id: str, body: T.UpdateWalletRequest) -> UserActionChallengeResponse:
        """
        Initialize Update Wallet.

        Creates a user action challenge for external signing.

        Args:
            wallet_id: Path parameter.
            body: Request body.

        Returns:
            UserActionChallengeResponse: The challenge to sign externally.
        """  # noqa: E501
        path = "/wallets/{walletId}"
        path = path.replace("{walletId}", str(wallet_id))
        payload = json.dumps(body, separators=(",", ":")) if body else ""

        return BaseAuthApi.create_user_action_challenge(
            self._http,
            user_action_http_method="PUT",
            user_action_http_path=path,
            user_action_payload=payload,
        )

    def update_wallet_complete(
        self, wallet_id: str, body: T.UpdateWalletRequest, signed_challenge: SignUserActionChallengeRequest
    ) -> T.UpdateWalletResponse:
        """
        Complete Update Wallet.

        Submits the signed challenge and makes the API request.

        Args:
            wallet_id: Path parameter.
            body: Request body.
            signed_challenge: The signed challenge from external signing.

        Returns:
            T.UpdateWalletResponse: The API response.
        """  # noqa: E501
        user_action_result = BaseAuthApi.sign_user_action_challenge(self._http, signed_challenge)
        user_action_token = user_action_result["userAction"]

        response = self._http.request_with_user_action(
            method="PUT",
            path="/wallets/{walletId}",
            path_params={"walletId": wallet_id},
            query_params=None,
            body=body,
            user_action=user_action_token,
        )
        return cast(T.UpdateWalletResponse, response)

    def get_wallet_assets(
        self, wallet_id: str, query: T.GetWalletAssetsQuery | None = None
    ) -> T.GetWalletAssetsResponse:
        """
        Get Wallet Assets.

        Retrieves a list of assets owned by the specified wallet.  Return values vary by chain as shown below.

        Args:
            wallet_id: Path parameter.
            query: Query parameters.

        Returns:
            T.GetWalletAssetsResponse: The API response.
        """  # noqa: E501
        response = self._http.request(
            method="GET",
            path="/wallets/{walletId}/assets",
            path_params={"walletId": wallet_id},
            query_params=query,
            body=None,
            requires_signature=False,
        )
        return cast(T.GetWalletAssetsResponse, response)

    def get_wallet_history(
        self, wallet_id: str, query: T.GetWalletHistoryQuery | None = None
    ) -> T.GetWalletHistoryResponse:
        """
                Get Wallet History.

                Retrieves a list of historical on chain activities for the specified wallet.

        The list reflects the indexed on-chain activity: it includes confirmed transactions only.

        If you need to list your on-going or failed transactions please use the related endpoints (
        [List Transfers](https://docs.dfns.co/api-reference/wallets/list-transfers) or
        [List Transactions](https://docs.dfns.co/api-reference/wallets/list-transactions)
        depending on the API you are using).

                Args:
                    wallet_id: Wallet you want to get the history from.
                    query: Query parameters.

                Returns:
                    T.GetWalletHistoryResponse: The API response.
        """  # noqa: E501
        response = self._http.request(
            method="GET",
            path="/wallets/{walletId}/history",
            path_params={"walletId": wallet_id},
            query_params=query,
            body=None,
            requires_signature=False,
        )
        return cast(T.GetWalletHistoryResponse, response)

    def get_wallet_nfts(self, wallet_id: str) -> T.GetWalletNftsResponse:
        """
        Get Wallet Nfts.

        Retrieves a list of NFTs owned by the specified Wallet.

        Args:
            wallet_id: Path parameter.

        Returns:
            T.GetWalletNftsResponse: The API response.
        """  # noqa: E501
        response = self._http.request(
            method="GET",
            path="/wallets/{walletId}/nfts",
            path_params={"walletId": wallet_id},
            query_params=None,
            body=None,
            requires_signature=False,
        )
        return cast(T.GetWalletNftsResponse, response)

    def import_wallet_init(self, body: T.ImportWalletRequest) -> UserActionChallengeResponse:
        """
        Initialize Import Wallet.

        Creates a user action challenge for external signing.

        Args:
            body: Request body.

        Returns:
            UserActionChallengeResponse: The challenge to sign externally.
        """  # noqa: E501
        path = "/wallets/import"
        payload = json.dumps(body, separators=(",", ":")) if body else ""

        return BaseAuthApi.create_user_action_challenge(
            self._http,
            user_action_http_method="POST",
            user_action_http_path=path,
            user_action_payload=payload,
        )

    def import_wallet_complete(
        self, body: T.ImportWalletRequest, signed_challenge: SignUserActionChallengeRequest
    ) -> T.ImportWalletResponse:
        """
        Complete Import Wallet.

        Submits the signed challenge and makes the API request.

        Args:
            body: Request body.
            signed_challenge: The signed challenge from external signing.

        Returns:
            T.ImportWalletResponse: The API response.
        """  # noqa: E501
        user_action_result = BaseAuthApi.sign_user_action_challenge(self._http, signed_challenge)
        user_action_token = user_action_result["userAction"]

        response = self._http.request_with_user_action(
            method="POST",
            path="/wallets/import",
            path_params={},
            query_params=None,
            body=body,
            user_action=user_action_token,
        )
        return cast(T.ImportWalletResponse, response)

    def list_transfers(self, wallet_id: str, query: T.ListTransfersQuery | None = None) -> T.ListTransfersResponse:
        """
        List Transfers.

        Retrieves a list of transfer requests for the specified wallet.

        Args:
            wallet_id: Wallet id.
            query: Query parameters.

        Returns:
            T.ListTransfersResponse: The API response.
        """  # noqa: E501
        response = self._http.request(
            method="GET",
            path="/wallets/{walletId}/transfers",
            path_params={"walletId": wallet_id},
            query_params=query,
            body=None,
            requires_signature=False,
        )
        return cast(T.ListTransfersResponse, response)

    def transfer_asset_init(self, wallet_id: str, body: dict[str, Any]) -> UserActionChallengeResponse:
        """
        Initialize Transfer Asset.

        Creates a user action challenge for external signing.

        Args:
            wallet_id: The source wallet id (`wa-...`).
            body: Request body.

        Returns:
            UserActionChallengeResponse: The challenge to sign externally.
        """  # noqa: E501
        path = "/wallets/{walletId}/transfers"
        path = path.replace("{walletId}", str(wallet_id))
        payload = json.dumps(body, separators=(",", ":")) if body else ""

        return BaseAuthApi.create_user_action_challenge(
            self._http,
            user_action_http_method="POST",
            user_action_http_path=path,
            user_action_payload=payload,
        )

    def transfer_asset_complete(
        self, wallet_id: str, body: dict[str, Any], signed_challenge: SignUserActionChallengeRequest
    ) -> T.TransferAssetResponse:
        """
        Complete Transfer Asset.

        Submits the signed challenge and makes the API request.

        Args:
            wallet_id: The source wallet id (`wa-...`).
            body: Request body.
            signed_challenge: The signed challenge from external signing.

        Returns:
            T.TransferAssetResponse: The API response.
        """  # noqa: E501
        user_action_result = BaseAuthApi.sign_user_action_challenge(self._http, signed_challenge)
        user_action_token = user_action_result["userAction"]

        response = self._http.request_with_user_action(
            method="POST",
            path="/wallets/{walletId}/transfers",
            path_params={"walletId": wallet_id},
            query_params=None,
            body=body,
            user_action=user_action_token,
        )
        return cast(T.TransferAssetResponse, response)

    def tag_wallet_init(self, wallet_id: str, body: T.TagWalletRequest) -> UserActionChallengeResponse:
        """
        Initialize Tag Wallet.

        Creates a user action challenge for external signing.

        Args:
            wallet_id: Path parameter.
            body: Request body.

        Returns:
            UserActionChallengeResponse: The challenge to sign externally.
        """  # noqa: E501
        path = "/wallets/{walletId}/tags"
        path = path.replace("{walletId}", str(wallet_id))
        payload = json.dumps(body, separators=(",", ":")) if body else ""

        return BaseAuthApi.create_user_action_challenge(
            self._http,
            user_action_http_method="PUT",
            user_action_http_path=path,
            user_action_payload=payload,
        )

    def tag_wallet_complete(
        self, wallet_id: str, body: T.TagWalletRequest, signed_challenge: SignUserActionChallengeRequest
    ) -> T.TagWalletResponse:
        """
        Complete Tag Wallet.

        Submits the signed challenge and makes the API request.

        Args:
            wallet_id: Path parameter.
            body: Request body.
            signed_challenge: The signed challenge from external signing.

        Returns:
            T.TagWalletResponse: The API response.
        """  # noqa: E501
        user_action_result = BaseAuthApi.sign_user_action_challenge(self._http, signed_challenge)
        user_action_token = user_action_result["userAction"]

        response = self._http.request_with_user_action(
            method="PUT",
            path="/wallets/{walletId}/tags",
            path_params={"walletId": wallet_id},
            query_params=None,
            body=body,
            user_action=user_action_token,
        )
        return cast(T.TagWalletResponse, response)

    def untag_wallet_init(self, wallet_id: str, body: T.UntagWalletRequest) -> UserActionChallengeResponse:
        """
        Initialize Untag Wallet.

        Creates a user action challenge for external signing.

        Args:
            wallet_id: Path parameter.
            body: Request body.

        Returns:
            UserActionChallengeResponse: The challenge to sign externally.
        """  # noqa: E501
        path = "/wallets/{walletId}/tags"
        path = path.replace("{walletId}", str(wallet_id))
        payload = json.dumps(body, separators=(",", ":")) if body else ""

        return BaseAuthApi.create_user_action_challenge(
            self._http,
            user_action_http_method="DELETE",
            user_action_http_path=path,
            user_action_payload=payload,
        )

    def untag_wallet_complete(
        self, wallet_id: str, body: T.UntagWalletRequest, signed_challenge: SignUserActionChallengeRequest
    ) -> T.UntagWalletResponse:
        """
        Complete Untag Wallet.

        Submits the signed challenge and makes the API request.

        Args:
            wallet_id: Path parameter.
            body: Request body.
            signed_challenge: The signed challenge from external signing.

        Returns:
            T.UntagWalletResponse: The API response.
        """  # noqa: E501
        user_action_result = BaseAuthApi.sign_user_action_challenge(self._http, signed_challenge)
        user_action_token = user_action_result["userAction"]

        response = self._http.request_with_user_action(
            method="DELETE",
            path="/wallets/{walletId}/tags",
            path_params={"walletId": wallet_id},
            query_params=None,
            body=body,
            user_action=user_action_token,
        )
        return cast(T.UntagWalletResponse, response)

    def get_offer(self, wallet_id: str, offer_id: str) -> T.GetOfferResponse:
        """
        Get Offer.

        Retrieve information about a specific offer received on your wallet.

        Args:
            wallet_id: Wallet id.
            offer_id: Offer id.

        Returns:
            T.GetOfferResponse: The API response.
        """  # noqa: E501
        response = self._http.request(
            method="GET",
            path="/wallets/{walletId}/offers/{offerId}",
            path_params={"walletId": wallet_id, "offerId": offer_id},
            query_params=None,
            body=None,
            requires_signature=False,
        )
        return cast(T.GetOfferResponse, response)

    def list_offers(self, wallet_id: str, query: T.ListOffersQuery | None = None) -> T.ListOffersResponse:
        """
        List Offers.

        List all offers received on a specific wallet.

        Args:
            wallet_id: Wallet id.
            query: Query parameters.

        Returns:
            T.ListOffersResponse: The API response.
        """  # noqa: E501
        response = self._http.request(
            method="GET",
            path="/wallets/{walletId}/offers",
            path_params={"walletId": wallet_id},
            query_params=query,
            body=None,
            requires_signature=False,
        )
        return cast(T.ListOffersResponse, response)

    def accept_offer_init(self, wallet_id: str, offer_id: str) -> UserActionChallengeResponse:
        """
        Initialize Accept Offer.

        Creates a user action challenge for external signing.

        Args:
            wallet_id: Wallet id.
            offer_id: Offer id.

        Returns:
            UserActionChallengeResponse: The challenge to sign externally.
        """  # noqa: E501
        path = "/wallets/{walletId}/offers/{offerId}/accept"
        path = path.replace("{walletId}", str(wallet_id))
        path = path.replace("{offerId}", str(offer_id))
        payload = ""

        return BaseAuthApi.create_user_action_challenge(
            self._http,
            user_action_http_method="PUT",
            user_action_http_path=path,
            user_action_payload=payload,
        )

    def accept_offer_complete(
        self, wallet_id: str, offer_id: str, signed_challenge: SignUserActionChallengeRequest
    ) -> T.AcceptOfferResponse:
        """
        Complete Accept Offer.

        Submits the signed challenge and makes the API request.

        Args:
            wallet_id: Wallet id.
            offer_id: Offer id.
            signed_challenge: The signed challenge from external signing.

        Returns:
            T.AcceptOfferResponse: The API response.
        """  # noqa: E501
        user_action_result = BaseAuthApi.sign_user_action_challenge(self._http, signed_challenge)
        user_action_token = user_action_result["userAction"]

        response = self._http.request_with_user_action(
            method="PUT",
            path="/wallets/{walletId}/offers/{offerId}/accept",
            path_params={"walletId": wallet_id, "offerId": offer_id},
            query_params=None,
            body=None,
            user_action=user_action_token,
        )
        return cast(T.AcceptOfferResponse, response)

    def reject_offer_init(self, wallet_id: str, offer_id: str) -> UserActionChallengeResponse:
        """
        Initialize Reject Offer.

        Creates a user action challenge for external signing.

        Args:
            wallet_id: Wallet id.
            offer_id: Offer id.

        Returns:
            UserActionChallengeResponse: The challenge to sign externally.
        """  # noqa: E501
        path = "/wallets/{walletId}/offers/{offerId}/reject"
        path = path.replace("{walletId}", str(wallet_id))
        path = path.replace("{offerId}", str(offer_id))
        payload = ""

        return BaseAuthApi.create_user_action_challenge(
            self._http,
            user_action_http_method="PUT",
            user_action_http_path=path,
            user_action_payload=payload,
        )

    def reject_offer_complete(
        self, wallet_id: str, offer_id: str, signed_challenge: SignUserActionChallengeRequest
    ) -> T.RejectOfferResponse:
        """
        Complete Reject Offer.

        Submits the signed challenge and makes the API request.

        Args:
            wallet_id: Wallet id.
            offer_id: Offer id.
            signed_challenge: The signed challenge from external signing.

        Returns:
            T.RejectOfferResponse: The API response.
        """  # noqa: E501
        user_action_result = BaseAuthApi.sign_user_action_challenge(self._http, signed_challenge)
        user_action_token = user_action_result["userAction"]

        response = self._http.request_with_user_action(
            method="PUT",
            path="/wallets/{walletId}/offers/{offerId}/reject",
            path_params={"walletId": wallet_id, "offerId": offer_id},
            query_params=None,
            body=None,
            user_action=user_action_token,
        )
        return cast(T.RejectOfferResponse, response)

    def list_org_wallet_history(self, query: T.ListOrgWalletHistoryQuery) -> dict[str, Any] | str:
        """
        List Org Wallet History.

        Retrieve the transaction history across all wallets within a specified timeframe. The time range is unbounded, but the CSV export is capped at 100,000 rows.

        Args:
            query: Query parameters.

        Returns:
            dict[str, Any] | str: The API response.
        """  # noqa: E501
        response = self._http.request(
            method="GET",
            path="/wallets/all/history",
            path_params={},
            query_params=query,
            body=None,
            requires_signature=False,
        )
        return cast(dict[str, Any] | str, response)
