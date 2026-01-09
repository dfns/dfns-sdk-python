"""Delegated client for the wallets domain."""

import json
from typing import Any, Literal, Optional, TypedDict, Union
from warnings import deprecated


from ..._internal import HttpClient
from ...base_auth_api import (
    BaseAuthApi,
    SignUserActionChallengeRequest,
    UserActionChallengeResponse,
)
from . import types as T


class DelegatedWalletsClient:
    """
    Delegated client for wallets operations.

    This client separates user action signing into _init() and _complete() method pairs,
    allowing external systems to handle the signing process.
    """

    def __init__(self, http_client: HttpClient):
        self._http = http_client

    def activate_wallet_init(self, wallet_id: str, body: dict[str, Any]) -> UserActionChallengeResponse:
        """
        Initialize Activate Wallet.

        Creates a user action challenge for external signing.

        Args:
        wallet_id: Wallet id.
        body: Request body.

        Returns:
            UserActionChallengeResponse: The challenge to sign externally.
        """
        path = "/wallets/{walletId}/activate"
        path = path.replace("{walletId}", str(wallet_id))
        payload = json.dumps(body, separators=(",", ":")) if body else ""

        return BaseAuthApi.create_user_action_challenge(
            self._http,
            user_action_http_method="POST",
            user_action_http_path=path,
            user_action_payload=payload,
        )

    def activate_wallet_complete(self, wallet_id: str, body: dict[str, Any], signed_challenge: SignUserActionChallengeRequest) -> T.ActivateWalletResponse:
        """
        Complete Activate Wallet.

        Submits the signed challenge and makes the API request.

        Args:
        wallet_id: Wallet id.
        body: Request body.
        signed_challenge: The signed challenge from external signing.

        Returns:
            T.ActivateWalletResponse: The API response.
        """
        user_action_result = BaseAuthApi.sign_user_action_challenge(
            self._http, signed_challenge
        )
        user_action_token = user_action_result["userAction"]

        return self._http.request_with_user_action(
            method="POST",
            path="/wallets/{walletId}/activate",
            path_params={"walletId": wallet_id},
            query_params=None,
            body=body,
            user_action=user_action_token,
        )

    def list_transactions(self, wallet_id: str, query: Optional[T.ListTransactionsQuery] = None) -> T.ListTransactionsResponse:
        """
        List Transactions.

        Retrieves a list of transactions requests for the specified wallet.

        Args:
        wallet_id: Path parameter.
        query: Query parameters.

        Returns:
            T.ListTransactionsResponse: The API response.
        """
        return self._http.request(
            method="GET",
            path="/wallets/{walletId}/transactions",
            path_params={"walletId": wallet_id},
            query_params=query,
            body=None,
            requires_signature=False,
        )

    def sign_and_broadcast_transaction_init(self, wallet_id: str, body: dict[str, Any]) -> UserActionChallengeResponse:
        """
        Initialize Sign and Broadcast Transaction.

        Creates a user action challenge for external signing.

        Args:
        wallet_id: Path parameter.
        body: Request body.

        Returns:
            UserActionChallengeResponse: The challenge to sign externally.
        """
        path = "/wallets/{walletId}/transactions"
        path = path.replace("{walletId}", str(wallet_id))
        payload = json.dumps(body, separators=(",", ":")) if body else ""

        return BaseAuthApi.create_user_action_challenge(
            self._http,
            user_action_http_method="POST",
            user_action_http_path=path,
            user_action_payload=payload,
        )

    def sign_and_broadcast_transaction_complete(self, wallet_id: str, body: dict[str, Any], signed_challenge: SignUserActionChallengeRequest) -> T.SignAndBroadcastTransactionResponse:
        """
        Complete Sign and Broadcast Transaction.

        Submits the signed challenge and makes the API request.

        Args:
        wallet_id: Path parameter.
        body: Request body.
        signed_challenge: The signed challenge from external signing.

        Returns:
            T.SignAndBroadcastTransactionResponse: The API response.
        """
        user_action_result = BaseAuthApi.sign_user_action_challenge(
            self._http, signed_challenge
        )
        user_action_token = user_action_result["userAction"]

        return self._http.request_with_user_action(
            method="POST",
            path="/wallets/{walletId}/transactions",
            path_params={"walletId": wallet_id},
            query_params=None,
            body=body,
            user_action=user_action_token,
        )

    def cancel_transaction_init(self, wallet_id: str, transaction_id: str) -> UserActionChallengeResponse:
        """
        Initialize Cancel Transaction.

        Creates a user action challenge for external signing.

        Args:
        wallet_id: Wallet id.
        transaction_id: Transaction id.

        Returns:
            UserActionChallengeResponse: The challenge to sign externally.
        """
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

    def cancel_transaction_complete(self, wallet_id: str, transaction_id: str, signed_challenge: SignUserActionChallengeRequest) -> T.CancelTransactionResponse:
        """
        Complete Cancel Transaction.

        Submits the signed challenge and makes the API request.

        Args:
        wallet_id: Wallet id.
        transaction_id: Transaction id.
        signed_challenge: The signed challenge from external signing.

        Returns:
            T.CancelTransactionResponse: The API response.
        """
        user_action_result = BaseAuthApi.sign_user_action_challenge(
            self._http, signed_challenge
        )
        user_action_token = user_action_result["userAction"]

        return self._http.request_with_user_action(
            method="POST",
            path="/wallets/{walletId}/transactions/{transactionId}/cancel",
            path_params={"walletId": wallet_id, "transactionId": transaction_id},
            query_params=None,
            body=None,
            user_action=user_action_token,
        )

    def cancel_transfer_init(self, wallet_id: str, transfer_id: str) -> UserActionChallengeResponse:
        """
        Initialize Cancel Transfer.

        Creates a user action challenge for external signing.

        Args:
        wallet_id: Wallet id.
        transfer_id: Transfer id.

        Returns:
            UserActionChallengeResponse: The challenge to sign externally.
        """
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

    def cancel_transfer_complete(self, wallet_id: str, transfer_id: str, signed_challenge: SignUserActionChallengeRequest) -> T.CancelTransferResponse:
        """
        Complete Cancel Transfer.

        Submits the signed challenge and makes the API request.

        Args:
        wallet_id: Wallet id.
        transfer_id: Transfer id.
        signed_challenge: The signed challenge from external signing.

        Returns:
            T.CancelTransferResponse: The API response.
        """
        user_action_result = BaseAuthApi.sign_user_action_challenge(
            self._http, signed_challenge
        )
        user_action_token = user_action_result["userAction"]

        return self._http.request_with_user_action(
            method="POST",
            path="/wallets/{walletId}/transfers/{transferId}/cancel",
            path_params={"walletId": wallet_id, "transferId": transfer_id},
            query_params=None,
            body=None,
            user_action=user_action_token,
        )

    def speed_up_transaction_init(self, wallet_id: str, transaction_id: str) -> UserActionChallengeResponse:
        """
        Initialize Speed Up Transaction.

        Creates a user action challenge for external signing.

        Args:
        wallet_id: Wallet id.
        transaction_id: Transaction id.

        Returns:
            UserActionChallengeResponse: The challenge to sign externally.
        """
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

    def speed_up_transaction_complete(self, wallet_id: str, transaction_id: str, signed_challenge: SignUserActionChallengeRequest) -> T.SpeedUpTransactionResponse:
        """
        Complete Speed Up Transaction.

        Submits the signed challenge and makes the API request.

        Args:
        wallet_id: Wallet id.
        transaction_id: Transaction id.
        signed_challenge: The signed challenge from external signing.

        Returns:
            T.SpeedUpTransactionResponse: The API response.
        """
        user_action_result = BaseAuthApi.sign_user_action_challenge(
            self._http, signed_challenge
        )
        user_action_token = user_action_result["userAction"]

        return self._http.request_with_user_action(
            method="POST",
            path="/wallets/{walletId}/transactions/{transactionId}/speed-up",
            path_params={"walletId": wallet_id, "transactionId": transaction_id},
            query_params=None,
            body=None,
            user_action=user_action_token,
        )

    def speed_up_transfer_init(self, wallet_id: str, transfer_id: str) -> UserActionChallengeResponse:
        """
        Initialize Speed Up Transfer.

        Creates a user action challenge for external signing.

        Args:
        wallet_id: Wallet id.
        transfer_id: Transfer id.

        Returns:
            UserActionChallengeResponse: The challenge to sign externally.
        """
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

    def speed_up_transfer_complete(self, wallet_id: str, transfer_id: str, signed_challenge: SignUserActionChallengeRequest) -> T.SpeedUpTransferResponse:
        """
        Complete Speed Up Transfer.

        Submits the signed challenge and makes the API request.

        Args:
        wallet_id: Wallet id.
        transfer_id: Transfer id.
        signed_challenge: The signed challenge from external signing.

        Returns:
            T.SpeedUpTransferResponse: The API response.
        """
        user_action_result = BaseAuthApi.sign_user_action_challenge(
            self._http, signed_challenge
        )
        user_action_token = user_action_result["userAction"]

        return self._http.request_with_user_action(
            method="POST",
            path="/wallets/{walletId}/transfers/{transferId}/speed-up",
            path_params={"walletId": wallet_id, "transferId": transfer_id},
            query_params=None,
            body=None,
            user_action=user_action_token,
        )

    def list_wallets(self, query: Optional[T.ListWalletsQuery] = None) -> T.ListWalletsResponse:
        """
        List Wallets.

        Retrieves the list of Wallets in your organization. You can filter the results by owner (either by owner id or owner username). Pagination is supported via limit and paginationToken parameters.

        Args:
        query: Query parameters.

        Returns:
            T.ListWalletsResponse: The API response.
        """
        return self._http.request(
            method="GET",
            path="/wallets",
            path_params={},
            query_params=query,
            body=None,
            requires_signature=False,
        )

    def create_wallet_init(self, body: T.CreateWalletRequest) -> UserActionChallengeResponse:
        """
        Initialize Create Wallet.

        Creates a user action challenge for external signing.

        Args:
        body: Request body.

        Returns:
            UserActionChallengeResponse: The challenge to sign externally.
        """
        path = "/wallets"
        payload = json.dumps(body, separators=(",", ":")) if body else ""

        return BaseAuthApi.create_user_action_challenge(
            self._http,
            user_action_http_method="POST",
            user_action_http_path=path,
            user_action_payload=payload,
        )

    def create_wallet_complete(self, body: T.CreateWalletRequest, signed_challenge: SignUserActionChallengeRequest) -> T.CreateWalletResponse:
        """
        Complete Create Wallet.

        Submits the signed challenge and makes the API request.

        Args:
        body: Request body.
        signed_challenge: The signed challenge from external signing.

        Returns:
            T.CreateWalletResponse: The API response.
        """
        user_action_result = BaseAuthApi.sign_user_action_challenge(
            self._http, signed_challenge
        )
        user_action_token = user_action_result["userAction"]

        return self._http.request_with_user_action(
            method="POST",
            path="/wallets",
            path_params={},
            query_params=None,
            body=body,
            user_action=user_action_token,
        )

    def delegate_wallet_init(self, wallet_id: str, body: T.DelegateWalletRequest) -> UserActionChallengeResponse:
        """
        Initialize Delegate Wallet.

        Creates a user action challenge for external signing.

        Args:
        wallet_id: Path parameter.
        body: Request body.

        Returns:
            UserActionChallengeResponse: The challenge to sign externally.
        """
        path = "/wallets/{walletId}/delegate"
        path = path.replace("{walletId}", str(wallet_id))
        payload = json.dumps(body, separators=(",", ":")) if body else ""

        return BaseAuthApi.create_user_action_challenge(
            self._http,
            user_action_http_method="POST",
            user_action_http_path=path,
            user_action_payload=payload,
        )

    def delegate_wallet_complete(self, wallet_id: str, body: T.DelegateWalletRequest, signed_challenge: SignUserActionChallengeRequest) -> T.DelegateWalletResponse:
        """
        Complete Delegate Wallet.

        Submits the signed challenge and makes the API request.

        Args:
        wallet_id: Path parameter.
        body: Request body.
        signed_challenge: The signed challenge from external signing.

        Returns:
            T.DelegateWalletResponse: The API response.
        """
        user_action_result = BaseAuthApi.sign_user_action_challenge(
            self._http, signed_challenge
        )
        user_action_token = user_action_result["userAction"]

        return self._http.request_with_user_action(
            method="POST",
            path="/wallets/{walletId}/delegate",
            path_params={"walletId": wallet_id},
            query_params=None,
            body=body,
            user_action=user_action_token,
        )

    def export_wallet_init(self, wallet_id: str, body: T.ExportWalletRequest) -> UserActionChallengeResponse:
        """
        Initialize Export Wallet.

        Creates a user action challenge for external signing.

        Args:
        wallet_id: Path parameter.
        body: Request body.

        Returns:
            UserActionChallengeResponse: The challenge to sign externally.
        """
        path = "/wallets/{walletId}/export"
        path = path.replace("{walletId}", str(wallet_id))
        payload = json.dumps(body, separators=(",", ":")) if body else ""

        return BaseAuthApi.create_user_action_challenge(
            self._http,
            user_action_http_method="POST",
            user_action_http_path=path,
            user_action_payload=payload,
        )

    def export_wallet_complete(self, wallet_id: str, body: T.ExportWalletRequest, signed_challenge: SignUserActionChallengeRequest) -> T.ExportWalletResponse:
        """
        Complete Export Wallet.

        Submits the signed challenge and makes the API request.

        Args:
        wallet_id: Path parameter.
        body: Request body.
        signed_challenge: The signed challenge from external signing.

        Returns:
            T.ExportWalletResponse: The API response.
        """
        user_action_result = BaseAuthApi.sign_user_action_challenge(
            self._http, signed_challenge
        )
        user_action_token = user_action_result["userAction"]

        return self._http.request_with_user_action(
            method="POST",
            path="/wallets/{walletId}/export",
            path_params={"walletId": wallet_id},
            query_params=None,
            body=body,
            user_action=user_action_token,
        )

    @deprecated("This endpoint is deprecated.")
    def list_signatures(self, wallet_id: str, query: Optional[T.ListSignaturesQuery] = None) -> T.ListSignaturesResponse:
        """
        List Signatures.

        List all signature requests for a specific wallet.
  
<Danger>
Generating Signatures from a Wallet is deprecated. Please use the [Keys](https://docs.dfns.co/api-reference/keys) endpoints instead.
</Danger>

        Args:
        wallet_id: Path parameter.
        query: Query parameters.

        Returns:
            T.ListSignaturesResponse: The API response.
        """
        return self._http.request(
            method="GET",
            path="/wallets/{walletId}/signatures",
            path_params={"walletId": wallet_id},
            query_params=query,
            body=None,
            requires_signature=False,
        )

    def generate_signature_init(self, wallet_id: str, body: dict[str, Any]) -> UserActionChallengeResponse:
        """
        Initialize Generate Signature.

        Creates a user action challenge for external signing.

        Args:
        wallet_id: Path parameter.
        body: Request body.

        Returns:
            UserActionChallengeResponse: The challenge to sign externally.
        """
        path = "/wallets/{walletId}/signatures"
        path = path.replace("{walletId}", str(wallet_id))
        payload = json.dumps(body, separators=(",", ":")) if body else ""

        return BaseAuthApi.create_user_action_challenge(
            self._http,
            user_action_http_method="POST",
            user_action_http_path=path,
            user_action_payload=payload,
        )

    def generate_signature_complete(self, wallet_id: str, body: dict[str, Any], signed_challenge: SignUserActionChallengeRequest) -> T.GenerateSignatureResponse:
        """
        Complete Generate Signature.

        Submits the signed challenge and makes the API request.

        Args:
        wallet_id: Path parameter.
        body: Request body.
        signed_challenge: The signed challenge from external signing.

        Returns:
            T.GenerateSignatureResponse: The API response.
        """
        user_action_result = BaseAuthApi.sign_user_action_challenge(
            self._http, signed_challenge
        )
        user_action_token = user_action_result["userAction"]

        return self._http.request_with_user_action(
            method="POST",
            path="/wallets/{walletId}/signatures",
            path_params={"walletId": wallet_id},
            query_params=None,
            body=body,
            user_action=user_action_token,
        )

    @deprecated("This endpoint is deprecated.")
    def get_signature(self, wallet_id: str, signature_id: str) -> T.GetSignatureResponse:
        """
        Get Signature.

        Retrieves a Transaction Request information by its ID.

<Danger>
Generating Signatures from a Wallet is deprecated. Please use the [Keys](https://docs.dfns.co/api-reference/keys) endpoints instead.
</Danger>

        Args:
        wallet_id: Path parameter.
        signature_id: Path parameter.

        Returns:
            T.GetSignatureResponse: The API response.
        """
        return self._http.request(
            method="GET",
            path="/wallets/{walletId}/signatures/{signatureId}",
            path_params={"walletId": wallet_id, "signatureId": signature_id},
            query_params=None,
            body=None,
            requires_signature=False,
        )

    def get_transaction(self, wallet_id: str, transaction_id: str) -> T.GetTransactionResponse:
        """
        Get Transaction.

        Retrieve information about a specific transaction.

        Args:
        wallet_id: Path parameter.
        transaction_id: Path parameter.

        Returns:
            T.GetTransactionResponse: The API response.
        """
        return self._http.request(
            method="GET",
            path="/wallets/{walletId}/transactions/{transactionId}",
            path_params={"walletId": wallet_id, "transactionId": transaction_id},
            query_params=None,
            body=None,
            requires_signature=False,
        )

    def get_transfer(self, wallet_id: str, transfer_id: str) -> T.GetTransferResponse:
        """
        Get Transfer.

        Retrieves a Wallet Transfer Request by its ID.

        Args:
        wallet_id: Path parameter.
        transfer_id: Path parameter.

        Returns:
            T.GetTransferResponse: The API response.
        """
        return self._http.request(
            method="GET",
            path="/wallets/{walletId}/transfers/{transferId}",
            path_params={"walletId": wallet_id, "transferId": transfer_id},
            query_params=None,
            body=None,
            requires_signature=False,
        )

    def get_wallet(self, wallet_id: str) -> T.GetWalletResponse:
        """
        Get Wallet.

        Retrieves a Wallet information by its ID.

        Args:
        wallet_id: Path parameter.

        Returns:
            T.GetWalletResponse: The API response.
        """
        return self._http.request(
            method="GET",
            path="/wallets/{walletId}",
            path_params={"walletId": wallet_id},
            query_params=None,
            body=None,
            requires_signature=False,
        )

    def update_wallet_init(self, wallet_id: str, body: T.UpdateWalletRequest) -> UserActionChallengeResponse:
        """
        Initialize Update Wallet.

        Creates a user action challenge for external signing.

        Args:
        wallet_id: Path parameter.
        body: Request body.

        Returns:
            UserActionChallengeResponse: The challenge to sign externally.
        """
        path = "/wallets/{walletId}"
        path = path.replace("{walletId}", str(wallet_id))
        payload = json.dumps(body, separators=(",", ":")) if body else ""

        return BaseAuthApi.create_user_action_challenge(
            self._http,
            user_action_http_method="PUT",
            user_action_http_path=path,
            user_action_payload=payload,
        )

    def update_wallet_complete(self, wallet_id: str, body: T.UpdateWalletRequest, signed_challenge: SignUserActionChallengeRequest) -> T.UpdateWalletResponse:
        """
        Complete Update Wallet.

        Submits the signed challenge and makes the API request.

        Args:
        wallet_id: Path parameter.
        body: Request body.
        signed_challenge: The signed challenge from external signing.

        Returns:
            T.UpdateWalletResponse: The API response.
        """
        user_action_result = BaseAuthApi.sign_user_action_challenge(
            self._http, signed_challenge
        )
        user_action_token = user_action_result["userAction"]

        return self._http.request_with_user_action(
            method="PUT",
            path="/wallets/{walletId}",
            path_params={"walletId": wallet_id},
            query_params=None,
            body=body,
            user_action=user_action_token,
        )

    def get_wallet_assets(self, wallet_id: str, query: Optional[T.GetWalletAssetsQuery] = None) -> T.GetWalletAssetsResponse:
        """
        Get Wallet Assets.

        Retrieves a list of assets owned by the specified wallet.  Return values vary by chain as shown below.

        Args:
        wallet_id: Path parameter.
        query: Query parameters.

        Returns:
            T.GetWalletAssetsResponse: The API response.
        """
        return self._http.request(
            method="GET",
            path="/wallets/{walletId}/assets",
            path_params={"walletId": wallet_id},
            query_params=query,
            body=None,
            requires_signature=False,
        )

    def get_wallet_history(self, wallet_id: str, query: Optional[T.GetWalletHistoryQuery] = None) -> T.GetWalletHistoryResponse:
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
        """
        return self._http.request(
            method="GET",
            path="/wallets/{walletId}/history",
            path_params={"walletId": wallet_id},
            query_params=query,
            body=None,
            requires_signature=False,
        )

    def get_wallet_nfts(self, wallet_id: str) -> T.GetWalletNftsResponse:
        """
        Get Wallet Nfts.

        Retrieves a list of NFTs owned by the specified Wallet.

        Args:
        wallet_id: Path parameter.

        Returns:
            T.GetWalletNftsResponse: The API response.
        """
        return self._http.request(
            method="GET",
            path="/wallets/{walletId}/nfts",
            path_params={"walletId": wallet_id},
            query_params=None,
            body=None,
            requires_signature=False,
        )

    def import_wallet_init(self, body: T.ImportWalletRequest) -> UserActionChallengeResponse:
        """
        Initialize Import Wallet.

        Creates a user action challenge for external signing.

        Args:
        body: Request body.

        Returns:
            UserActionChallengeResponse: The challenge to sign externally.
        """
        path = "/wallets/import"
        payload = json.dumps(body, separators=(",", ":")) if body else ""

        return BaseAuthApi.create_user_action_challenge(
            self._http,
            user_action_http_method="POST",
            user_action_http_path=path,
            user_action_payload=payload,
        )

    def import_wallet_complete(self, body: T.ImportWalletRequest, signed_challenge: SignUserActionChallengeRequest) -> T.ImportWalletResponse:
        """
        Complete Import Wallet.

        Submits the signed challenge and makes the API request.

        Args:
        body: Request body.
        signed_challenge: The signed challenge from external signing.

        Returns:
            T.ImportWalletResponse: The API response.
        """
        user_action_result = BaseAuthApi.sign_user_action_challenge(
            self._http, signed_challenge
        )
        user_action_token = user_action_result["userAction"]

        return self._http.request_with_user_action(
            method="POST",
            path="/wallets/import",
            path_params={},
            query_params=None,
            body=body,
            user_action=user_action_token,
        )

    def list_transfers(self, wallet_id: str, query: Optional[T.ListTransfersQuery] = None) -> T.ListTransfersResponse:
        """
        List Transfers.

        Retrieves a list of transfer requests for the specified wallet.

        Args:
        wallet_id: Path parameter.
        query: Query parameters.

        Returns:
            T.ListTransfersResponse: The API response.
        """
        return self._http.request(
            method="GET",
            path="/wallets/{walletId}/transfers",
            path_params={"walletId": wallet_id},
            query_params=query,
            body=None,
            requires_signature=False,
        )

    def transfer_asset_init(self, wallet_id: str, body: dict[str, Any]) -> UserActionChallengeResponse:
        """
        Initialize Transfer Asset.

        Creates a user action challenge for external signing.

        Args:
        wallet_id: The source wallet id (`wa-...`).
        body: Request body.

        Returns:
            UserActionChallengeResponse: The challenge to sign externally.
        """
        path = "/wallets/{walletId}/transfers"
        path = path.replace("{walletId}", str(wallet_id))
        payload = json.dumps(body, separators=(",", ":")) if body else ""

        return BaseAuthApi.create_user_action_challenge(
            self._http,
            user_action_http_method="POST",
            user_action_http_path=path,
            user_action_payload=payload,
        )

    def transfer_asset_complete(self, wallet_id: str, body: dict[str, Any], signed_challenge: SignUserActionChallengeRequest) -> T.TransferAssetResponse:
        """
        Complete Transfer Asset.

        Submits the signed challenge and makes the API request.

        Args:
        wallet_id: The source wallet id (`wa-...`).
        body: Request body.
        signed_challenge: The signed challenge from external signing.

        Returns:
            T.TransferAssetResponse: The API response.
        """
        user_action_result = BaseAuthApi.sign_user_action_challenge(
            self._http, signed_challenge
        )
        user_action_token = user_action_result["userAction"]

        return self._http.request_with_user_action(
            method="POST",
            path="/wallets/{walletId}/transfers",
            path_params={"walletId": wallet_id},
            query_params=None,
            body=body,
            user_action=user_action_token,
        )

    def tag_wallet_init(self, wallet_id: str, body: T.TagWalletRequest) -> UserActionChallengeResponse:
        """
        Initialize Tag Wallet.

        Creates a user action challenge for external signing.

        Args:
        wallet_id: Path parameter.
        body: Request body.

        Returns:
            UserActionChallengeResponse: The challenge to sign externally.
        """
        path = "/wallets/{walletId}/tags"
        path = path.replace("{walletId}", str(wallet_id))
        payload = json.dumps(body, separators=(",", ":")) if body else ""

        return BaseAuthApi.create_user_action_challenge(
            self._http,
            user_action_http_method="PUT",
            user_action_http_path=path,
            user_action_payload=payload,
        )

    def tag_wallet_complete(self, wallet_id: str, body: T.TagWalletRequest, signed_challenge: SignUserActionChallengeRequest) -> T.TagWalletResponse:
        """
        Complete Tag Wallet.

        Submits the signed challenge and makes the API request.

        Args:
        wallet_id: Path parameter.
        body: Request body.
        signed_challenge: The signed challenge from external signing.

        Returns:
            T.TagWalletResponse: The API response.
        """
        user_action_result = BaseAuthApi.sign_user_action_challenge(
            self._http, signed_challenge
        )
        user_action_token = user_action_result["userAction"]

        return self._http.request_with_user_action(
            method="PUT",
            path="/wallets/{walletId}/tags",
            path_params={"walletId": wallet_id},
            query_params=None,
            body=body,
            user_action=user_action_token,
        )

    def untag_wallet_init(self, wallet_id: str, body: T.UntagWalletRequest) -> UserActionChallengeResponse:
        """
        Initialize Untag Wallet.

        Creates a user action challenge for external signing.

        Args:
        wallet_id: Path parameter.
        body: Request body.

        Returns:
            UserActionChallengeResponse: The challenge to sign externally.
        """
        path = "/wallets/{walletId}/tags"
        path = path.replace("{walletId}", str(wallet_id))
        payload = json.dumps(body, separators=(",", ":")) if body else ""

        return BaseAuthApi.create_user_action_challenge(
            self._http,
            user_action_http_method="DELETE",
            user_action_http_path=path,
            user_action_payload=payload,
        )

    def untag_wallet_complete(self, wallet_id: str, body: T.UntagWalletRequest, signed_challenge: SignUserActionChallengeRequest) -> T.UntagWalletResponse:
        """
        Complete Untag Wallet.

        Submits the signed challenge and makes the API request.

        Args:
        wallet_id: Path parameter.
        body: Request body.
        signed_challenge: The signed challenge from external signing.

        Returns:
            T.UntagWalletResponse: The API response.
        """
        user_action_result = BaseAuthApi.sign_user_action_challenge(
            self._http, signed_challenge
        )
        user_action_token = user_action_result["userAction"]

        return self._http.request_with_user_action(
            method="DELETE",
            path="/wallets/{walletId}/tags",
            path_params={"walletId": wallet_id},
            query_params=None,
            body=body,
            user_action=user_action_token,
        )

    def get_offer(self, wallet_id: str, offer_id: str) -> T.GetOfferResponse:
        """
        Get Offer.

        Retrieve information about a specific offer received on your wallet.

        Args:
        wallet_id: Wallet id.
        offer_id: Offer id.

        Returns:
            T.GetOfferResponse: The API response.
        """
        return self._http.request(
            method="GET",
            path="/wallets/{walletId}/offers/{offerId}",
            path_params={"walletId": wallet_id, "offerId": offer_id},
            query_params=None,
            body=None,
            requires_signature=False,
        )

    def list_offers(self, wallet_id: str, query: Optional[T.ListOffersQuery] = None) -> T.ListOffersResponse:
        """
        List Offers.

        List all offers received on a specific wallet.

        Args:
        wallet_id: Wallet id.
        query: Query parameters.

        Returns:
            T.ListOffersResponse: The API response.
        """
        return self._http.request(
            method="GET",
            path="/wallets/{walletId}/offers",
            path_params={"walletId": wallet_id},
            query_params=query,
            body=None,
            requires_signature=False,
        )

    def accept_offer_init(self, wallet_id: str, offer_id: str) -> UserActionChallengeResponse:
        """
        Initialize Accept Offer.

        Creates a user action challenge for external signing.

        Args:
        wallet_id: Wallet id.
        offer_id: Offer id.

        Returns:
            UserActionChallengeResponse: The challenge to sign externally.
        """
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

    def accept_offer_complete(self, wallet_id: str, offer_id: str, signed_challenge: SignUserActionChallengeRequest) -> T.AcceptOfferResponse:
        """
        Complete Accept Offer.

        Submits the signed challenge and makes the API request.

        Args:
        wallet_id: Wallet id.
        offer_id: Offer id.
        signed_challenge: The signed challenge from external signing.

        Returns:
            T.AcceptOfferResponse: The API response.
        """
        user_action_result = BaseAuthApi.sign_user_action_challenge(
            self._http, signed_challenge
        )
        user_action_token = user_action_result["userAction"]

        return self._http.request_with_user_action(
            method="PUT",
            path="/wallets/{walletId}/offers/{offerId}/accept",
            path_params={"walletId": wallet_id, "offerId": offer_id},
            query_params=None,
            body=None,
            user_action=user_action_token,
        )

    def reject_offer_init(self, wallet_id: str, offer_id: str) -> UserActionChallengeResponse:
        """
        Initialize Reject Offer.

        Creates a user action challenge for external signing.

        Args:
        wallet_id: Wallet id.
        offer_id: Offer id.

        Returns:
            UserActionChallengeResponse: The challenge to sign externally.
        """
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

    def reject_offer_complete(self, wallet_id: str, offer_id: str, signed_challenge: SignUserActionChallengeRequest) -> T.RejectOfferResponse:
        """
        Complete Reject Offer.

        Submits the signed challenge and makes the API request.

        Args:
        wallet_id: Wallet id.
        offer_id: Offer id.
        signed_challenge: The signed challenge from external signing.

        Returns:
            T.RejectOfferResponse: The API response.
        """
        user_action_result = BaseAuthApi.sign_user_action_challenge(
            self._http, signed_challenge
        )
        user_action_token = user_action_result["userAction"]

        return self._http.request_with_user_action(
            method="PUT",
            path="/wallets/{walletId}/offers/{offerId}/reject",
            path_params={"walletId": wallet_id, "offerId": offer_id},
            query_params=None,
            body=None,
            user_action=user_action_token,
        )

    def list_org_wallet_history(self, query: T.ListOrgWalletHistoryQuery) -> Union[TypedDict, str]:
        """
        List Org Wallet History.

        Retrieve the transaction history across all wallets within a specified timeframe.

        Args:
        query: Query parameters.

        Returns:
            Union[TypedDict, str]: The API response.
        """
        return self._http.request(
            method="GET",
            path="/wallets/all/history",
            path_params={},
            query_params=query,
            body=None,
            requires_signature=False,
        )
