"""Client for the wallets domain."""

from typing import Any, Literal, Optional, TypedDict, Union

from ..._internal import HttpClient
from . import types as T


class WalletsClient:
    """Client for wallets operations."""

    def __init__(self, http_client: HttpClient):
        self._http = http_client

    def abort_transaction(self, wallet_id: str, transaction_id: str) -> T.AbortTransactionResponse:
        """
        Abort Transaction.

        Aborts a transaction that is currently in 'Executing' status and has not yet been signed. Sets the transaction status to 'Failed' and removes it from the retry queue.

  This is useful when a transaction is stuck in the execution pipeline (e.g., during construct or sign phase) and you want to abort it without waiting for it to fail on its own.

  Unlike cancel, which creates a replacement on-chain transaction, abort simply marks the transaction as failed without any blockchain interaction.

        Args:
        wallet_id: Wallet id.
        transaction_id: Transaction id.

        Returns:
            T.AbortTransactionResponse: The API response.
        """
        return self._http.request(
            method="PUT",
            path="/wallets/{walletId}/transactions/{transactionId}/abort",
            path_params={"walletId": wallet_id, "transactionId": transaction_id},
            query_params=None,
            body=None,
            requires_signature=True,
        )

    def abort_transfer(self, wallet_id: str, transfer_id: str) -> T.AbortTransferResponse:
        """
        Abort Transfer.

        Aborts a transfer that is currently in 'Executing' status and has not yet been signed. Sets the transfer status to 'Failed' and removes it from the retry queue.

  This is useful when a transfer is stuck in the execution pipeline (e.g., during construct or sign phase) and you want to abort it without waiting for it to fail on its own.

  Unlike cancel, which creates a replacement on-chain transaction, abort simply marks the transfer as failed without any blockchain interaction.

        Args:
        wallet_id: Wallet id.
        transfer_id: Transfer id.

        Returns:
            T.AbortTransferResponse: The API response.
        """
        return self._http.request(
            method="PUT",
            path="/wallets/{walletId}/transfers/{transferId}/abort",
            path_params={"walletId": wallet_id, "transferId": transfer_id},
            query_params=None,
            body=None,
            requires_signature=True,
        )

    def activate_wallet(self, wallet_id: str, body: dict[str, Any]) -> T.ActivateWalletResponse:
        """
        Activate Wallet.

        Activates a wallet by deploying the account contract on-chain, making it ready for transactions.

    This operation is required for wallets on networks where you need to explicitly activate your account on-chain
    before it can be used for transactions.

    - **Starknet**: Deploys the account contract using the wallet's public key to initialize the account on the blockchain. No additional parameters required.
    - **Concordium**: Deploys the account using credential deployment information and cryptographic randomness returned by the IDApp.
    - **Canton**: Registers the wallet on a validator. You must specify the `validatorId` to activate the wallet. Before activation, the wallet cannot be used and its address will not have a prefix.

        Args:
        wallet_id: Wallet id.
        body: Request body.

        Returns:
            T.ActivateWalletResponse: The API response.
        """
        return self._http.request(
            method="POST",
            path="/wallets/{walletId}/activate",
            path_params={"walletId": wallet_id},
            query_params=None,
            body=body,
            requires_signature=True,
        )

    def list_transactions(self, wallet_id: str, query: Optional[T.ListTransactionsQuery] = None) -> T.ListTransactionsResponse:
        """
        List Transactions.

        Retrieves a list of transactions requests for the specified wallet.

        Args:
        wallet_id: Wallet id.
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

    def sign_and_broadcast_transaction(self, wallet_id: str, body: dict[str, Any]) -> T.SignAndBroadcastTransactionResponse:
        """
        Sign and Broadcast Transaction.

        Sign & Broadcast transaction enables communication with any arbitrary smart contract of the target blockchain. You can construct a transaction that performs a complex task and this endpoint will sign the transaction, add the signature and broadcast it to chain. It can be used to call smart contract functions like mint tokens and even deploy new smart contracts.

| Status      | Definition                                                                                                                                      |
|-------------|-------------------------------------------------------------------------------------------------------------------------------------------------|
| Pending     | The request is pending approval due to a policy applied to the wallet.                                                                          |
| Executing   | The request is approved and is in the process of being executed. note this status is only set for a short time between pending and broadcasted. |
| Broadcasted | The transaction has been successfully written to the mempool.                                                                                   |
| Confirmed   | The transaction has been confirmed on-chain by our indexing pipeline.                                                                           |
| Failed      | Indicates either a system failure to complete the request or the transaction failed on chain.                                                   |
| Rejected    | The request has been rejected by a policy approval action.                                                                                      |


  <Info>
  for reading from a "view" function on EVM chains, please use [Read Contract](https://docs.dfns.co/api-reference/networks/read-contract) endpoint.
  </Info>

        Args:
        wallet_id: Wallet id.
        body: Request body.

        Returns:
            T.SignAndBroadcastTransactionResponse: The API response.
        """
        return self._http.request(
            method="POST",
            path="/wallets/{walletId}/transactions",
            path_params={"walletId": wallet_id},
            query_params=None,
            body=body,
            requires_signature=True,
        )

    def cancel_transaction(self, wallet_id: str, transaction_id: str) -> T.CancelTransactionResponse:
        """
        Cancel Transaction.

        Cancels an EVM transaction by creating a replacement transaction with the same nonce. The new transaction sends 0 value to the same address, effectively nullifying the original transaction.
  
  This endpoint works for:
  - EVM-compatible networks (Ethereum, Polygon, BSC, etc.)
  - Transactions that are in 'Broadcasted' status (pending inclusion in a block)
  - Transactions that are in 'Failed' status, but failed off-chain (before being broadcasted to the network)
  
  The cancellation works by:
  1. Extracting the nonce from the original transaction's signed data
  2. Creating a new transaction to the same wallet address with 0 amount
  3. Using the same nonce to either:
     - Replace the original transaction in the mempool (if it was broadcasted)
     - Consume the nonce that was reserved but not used (if the transaction failed off-chain)
  
  Note: For transactions that were broadcasted on-chain, success is not guaranteed as it depends on network conditions and whether the original transaction has already been mined.

        Args:
        wallet_id: Wallet id.
        transaction_id: Transaction id.

        Returns:
            T.CancelTransactionResponse: The API response.
        """
        return self._http.request(
            method="POST",
            path="/wallets/{walletId}/transactions/{transactionId}/cancel",
            path_params={"walletId": wallet_id, "transactionId": transaction_id},
            query_params=None,
            body=None,
            requires_signature=True,
        )

    def cancel_transfer(self, wallet_id: str, transfer_id: str) -> T.CancelTransferResponse:
        """
        Cancel Transfer.

        Cancels an EVM transfer by creating a replacement transaction with the same nonce. The new transaction sends 0 value to the same address, effectively nullifying the original transfer.
  
  This endpoint works for:
  - EVM-compatible networks (Ethereum, Polygon, BSC, etc.)
  - Transfers that are in 'Broadcasted' status (pending inclusion in a block)
  - Transfers that are in 'Failed' status, but failed off-chain (before being broadcasted to the network)
  
  The cancellation works by:
  1. Extracting the nonce from the original transfer's signed data
  2. Creating a new transaction to the same wallet address with 0 amount
  3. Using the same nonce to either:
     - Replace the original transaction in the mempool (if it was broadcasted)
     - Consume the nonce that was reserved but not used (if the transfer failed off-chain)
  
  Note: For transfers that were broadcasted on-chain, success is not guaranteed as it depends on network conditions and whether the original transaction has already been mined.

        Args:
        wallet_id: Wallet id.
        transfer_id: Transfer id.

        Returns:
            T.CancelTransferResponse: The API response.
        """
        return self._http.request(
            method="POST",
            path="/wallets/{walletId}/transfers/{transferId}/cancel",
            path_params={"walletId": wallet_id, "transferId": transfer_id},
            query_params=None,
            body=None,
            requires_signature=True,
        )

    def proxy_a_request_to_the_canton_ledger_api(self, wallet_id: str, body: T.ProxyARequestToTheCantonLedgerApiRequest) -> dict[str, Any]:
        """
        Proxy a request to the Canton Ledger API.

        Proxies a request to the Canton Ledger API associated with this wallet, using the validator's OAuth2 credentials. Restricted to a curated allow-list of read-style resources. Used to satisfy the Canton WalletConnect `canton_ledgerApi` method.

        Args:
        wallet_id: Wallet id.
        body: Request body.

        Returns:
            dict[str, Any]: The API response.
        """
        return self._http.request(
            method="POST",
            path="/wallets/{walletId}/canton/ledger-api",
            path_params={"walletId": wallet_id},
            query_params=None,
            body=body,
            requires_signature=False,
        )

    def speed_up_transaction(self, wallet_id: str, transaction_id: str) -> T.SpeedUpTransactionResponse:
        """
        Speed Up Transaction.

        Speeds up a transaction by creating a replacement transaction with the same parameters but higher gas fees.
  
  This endpoint only works for:
  - EVM-compatible networks (Ethereum, Polygon, BSC, etc.)
  - Transactions that are in 'Broadcasted' status (already submitted to blockchain, but not confirmed yet)
  
  The speed-up works by:
  1. Extracting the parameters from the original broadcasted transaction
  2. Creating a new transaction with the same nonce, recipient, value, and data
  3. Using higher gas fees (maximum between 10% bump or Fast network fees)
  4. Replacing the original transaction in the mempool
  
  Note: Success is not guaranteed as it depends on network conditions and whether the original transaction has already been mined.

        Args:
        wallet_id: Wallet id.
        transaction_id: Transaction id.

        Returns:
            T.SpeedUpTransactionResponse: The API response.
        """
        return self._http.request(
            method="POST",
            path="/wallets/{walletId}/transactions/{transactionId}/speed-up",
            path_params={"walletId": wallet_id, "transactionId": transaction_id},
            query_params=None,
            body=None,
            requires_signature=True,
        )

    def speed_up_transfer(self, wallet_id: str, transfer_id: str) -> T.SpeedUpTransferResponse:
        """
        Speed Up Transfer.

        Speeds up a transfer by creating a replacement transaction with the same parameters but higher gas fees.
  
  This endpoint only works for:
  - EVM-compatible networks (Ethereum, Polygon, BSC, etc.)
  - Transfers that are in 'Broadcasted' status (already submitted to blockchain, but not confirmed yet)
  
  The speed-up works by:
  1. Extracting the parameters from the original broadcasted transfer
  2. Creating a new transaction with the same nonce, recipient, value, and data
  3. Using higher gas fees (maximum between 10% bump or Fast network fees)
  4. Replacing the original transaction in the mempool
  
  Note: Success is not guaranteed as it depends on network conditions and whether the original transaction has already been mined.

        Args:
        wallet_id: Wallet id.
        transfer_id: Transfer id.

        Returns:
            T.SpeedUpTransferResponse: The API response.
        """
        return self._http.request(
            method="POST",
            path="/wallets/{walletId}/transfers/{transferId}/speed-up",
            path_params={"walletId": wallet_id, "transferId": transfer_id},
            query_params=None,
            body=None,
            requires_signature=True,
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

    def create_wallet(self, body: T.CreateWalletRequest) -> T.CreateWalletResponse:
        """
        Create Wallet.

        Creates a new Wallet associated with the given chain (such as Bitcoin or Ethereum ). Returns a new wallet entity.

        Args:
        body: Request body.

        Returns:
            T.CreateWalletResponse: The API response.
        """
        return self._http.request(
            method="POST",
            path="/wallets",
            path_params={},
            query_params=None,
            body=body,
            requires_signature=True,
        )

    def get_transaction(self, wallet_id: str, transaction_id: str) -> T.GetTransactionResponse:
        """
        Get Transaction.

        Retrieve information about a specific transaction.

        Args:
        wallet_id: Wallet id.
        transaction_id: Transaction id.

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
        wallet_id: Wallet id.
        transfer_id: Transfer id.

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
        wallet_id: The wallet to retrieve.

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

    def update_wallet(self, wallet_id: str, body: T.UpdateWalletRequest) -> T.UpdateWalletResponse:
        """
        Update Wallet.

        Updates the name of an existing wallet.

        Args:
        wallet_id: Path parameter.
        body: Request body.

        Returns:
            T.UpdateWalletResponse: The API response.
        """
        return self._http.request(
            method="PUT",
            path="/wallets/{walletId}",
            path_params={"walletId": wallet_id},
            query_params=None,
            body=body,
            requires_signature=True,
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

    def import_wallet(self, body: T.ImportWalletRequest) -> T.ImportWalletResponse:
        """
        Import Wallet.

        <Warning>
This endpoint is not enabled by default. [Contact Dfns](https://support.dfns.co) to have it activated.
</Warning>

Dfns secures private keys by generating them as MPC key shares in our decentralized key management network.  This happens by default when you [create a wallet](https://docs.dfns.co/api-reference/wallets/create-wallet).

In some circumstances, however, you may need to import an existing wallet (an existing private key) into Dfns infrastructure, instead of creating a brand new wallet with Dfns and transfer funds to it. As an example, you might want to keep an existing wallet if its address is tied to a smart contract which you don't want to re-deploy.

In such a case, Dfns exposes this wallet import API endpoint, which can be used in conjunction with our [import SDK](https://github.com/dfns/dfns-sdk-ts/tree/m/examples/sdk/import-wallet).   Note this is intended to be used only to migrate wallets when first onboarding onto the Dfns platform.

<Danger>
Dfns can not guarantee the security of imported wallets, as we have no way to control who had access to the private key prior to import.  For this reason, this feature is restricted to Enterprise customers who have signed a contractual addendum limiting our liability for imported keys.  Please contact your sales representative for more information.
</Danger>

        Args:
        body: Request body.

        Returns:
            T.ImportWalletResponse: The API response.
        """
        return self._http.request(
            method="POST",
            path="/wallets/import",
            path_params={},
            query_params=None,
            body=body,
            requires_signature=True,
        )

    def list_transfers(self, wallet_id: str, query: Optional[T.ListTransfersQuery] = None) -> T.ListTransfersResponse:
        """
        List Transfers.

        Retrieves a list of transfer requests for the specified wallet.

        Args:
        wallet_id: Wallet id.
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

    def transfer_asset(self, wallet_id: str, body: dict[str, Any]) -> T.TransferAssetResponse:
        """
        Transfer Asset.

        Transfer an asset out of the specified wallet to a destination address.
For all fungible token transfers, the transfer amount must be specified in the minimum denomination of that token.
For example, use the amount in Satoshi for a Bitcoin transfer, or the amount in Wei for an Ethereum transfer etc.

See the different options in the Body description below. You can also select your kind of transfers in the payload examples in the different languages.

<Tip>
Binance chains users can use ERC transfers for BEP tokens and Native transfers for BNB.
</Tip>

<Note>
Some blockchains may require additional steps before the transfer can be completed, such as creating a destination account (e.g., Stellar). Please refer to the specific blockchain documentation for any prerequisites or additional requirements.
</Note>

        Args:
        wallet_id: The source wallet id (`wa-...`).
        body: Request body.

        Returns:
            T.TransferAssetResponse: The API response.
        """
        return self._http.request(
            method="POST",
            path="/wallets/{walletId}/transfers",
            path_params={"walletId": wallet_id},
            query_params=None,
            body=body,
            requires_signature=True,
        )

    def tag_wallet(self, wallet_id: str, body: T.TagWalletRequest) -> T.TagWalletResponse:
        """
        Tag Wallet.

        Add a [Tag](https://docs.dfns.co/api-reference/wallets/tags) to a wallet.

        Args:
        wallet_id: Path parameter.
        body: Request body.

        Returns:
            T.TagWalletResponse: The API response.
        """
        return self._http.request(
            method="PUT",
            path="/wallets/{walletId}/tags",
            path_params={"walletId": wallet_id},
            query_params=None,
            body=body,
            requires_signature=True,
        )

    def untag_wallet(self, wallet_id: str, body: T.UntagWalletRequest) -> T.UntagWalletResponse:
        """
        Untag Wallet.

        Removes the specified tags from a wallet.

        Args:
        wallet_id: Path parameter.
        body: Request body.

        Returns:
            T.UntagWalletResponse: The API response.
        """
        return self._http.request(
            method="DELETE",
            path="/wallets/{walletId}/tags",
            path_params={"walletId": wallet_id},
            query_params=None,
            body=body,
            requires_signature=True,
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

    def accept_offer(self, wallet_id: str, offer_id: str) -> T.AcceptOfferResponse:
        """
        Accept Offer.

        Accept an offer received on your wallet.

        Args:
        wallet_id: Wallet id.
        offer_id: Offer id.

        Returns:
            T.AcceptOfferResponse: The API response.
        """
        return self._http.request(
            method="PUT",
            path="/wallets/{walletId}/offers/{offerId}/accept",
            path_params={"walletId": wallet_id, "offerId": offer_id},
            query_params=None,
            body=None,
            requires_signature=True,
        )

    def reject_offer(self, wallet_id: str, offer_id: str) -> T.RejectOfferResponse:
        """
        Reject Offer.

        Reject an offer received on your wallet.

        Args:
        wallet_id: Wallet id.
        offer_id: Offer id.

        Returns:
            T.RejectOfferResponse: The API response.
        """
        return self._http.request(
            method="PUT",
            path="/wallets/{walletId}/offers/{offerId}/reject",
            path_params={"walletId": wallet_id, "offerId": offer_id},
            query_params=None,
            body=None,
            requires_signature=True,
        )

    def list_org_wallet_history(self, query: T.ListOrgWalletHistoryQuery) -> Union[TypedDict, str]:
        """
        List Org Wallet History.

        Retrieve the transaction history across all wallets within a specified timeframe. The time range is unbounded, but the CSV export is capped at 100,000 rows.

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
