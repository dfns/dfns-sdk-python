"""Client for the keys domain."""

from typing import Any, Literal, Optional, TypedDict, Union

from ..._internal import HttpClient
from . import types as T


class KeysClient:
    """Client for keys operations."""

    def __init__(self, http_client: HttpClient):
        self._http = http_client

    def list_keys(self, query: Optional[T.ListKeysQuery] = None) -> T.ListKeysResponse:
        """
        List Keys.

        Retrieve all keys registered for your organization.

        Args:
        query: Query parameters.

        Returns:
            T.ListKeysResponse: The API response.
        """
        return self._http.request(
            method="GET",
            path="/keys",
            path_params={},
            query_params=query,
            body=None,
            requires_signature=False,
        )

    def create_key(self, body: T.CreateKeyRequest) -> T.CreateKeyResponse:
        """
        Create Key.

        Creates a key for the given scheme and curve. Returns the new key entity. 

        Args:
        body: Request body.

        Returns:
            T.CreateKeyResponse: The API response.
        """
        return self._http.request(
            method="POST",
            path="/keys",
            path_params={},
            query_params=None,
            body=body,
            requires_signature=True,
        )

    def delegate_key(self, key_id: str, body: T.DelegateKeyRequest) -> T.DelegateKeyResponse:
        """
        Delegate Key.

        <Warning>
Only keys created with "`delayDelegation: true`" can then be delegated to an end-user. It means you need to know ahead of time that you're creating a wallet meant to be delegated to an end-user later. This is a safety to prevent, for example, a treasury wallet from being unintentionally delegated to an end-user.
</Warning>

<Note>
When a key is delegated to an end user, all wallets using this key as the signing key are also automatically delegated to the same end user. Key and wallet ownerships are guaranteed to be always consistent.
</Note>

<Danger>
This operation is irreversible. The key ownership will be transferred to the end-user
</Danger>

In most cases, when you want to implement [Wallet Delegation](https://docs.dfns.co/developers/guides/wallet-delegation), simply create the wallet by directly delegating it to an end user, in which case it will the non-custodial from the start.  There are some rare cases, however, where the key or wallet must be created before the user has accessed to the system.  To accommodate this, we've added the ability to create a key or wallet in delay delegation mode, and then later delegate it (ie. transfer ownership of it) to an end user via this endpoint.


        Args:
        key_id: Path parameter.
        body: Request body.

        Returns:
            T.DelegateKeyResponse: The API response.
        """
        return self._http.request(
            method="POST",
            path="/keys/{keyId}/delegate",
            path_params={"keyId": key_id},
            query_params=None,
            body=body,
            requires_signature=True,
        )

    def get_key(self, key_id: str) -> T.GetKeyResponse:
        """
        Get Key.

        Retrieves a key information by its ID.

        Args:
        key_id: Path parameter.

        Returns:
            T.GetKeyResponse: The API response.
        """
        return self._http.request(
            method="GET",
            path="/keys/{keyId}",
            path_params={"keyId": key_id},
            query_params=None,
            body=None,
            requires_signature=False,
        )

    def update_key(self, key_id: str, body: T.UpdateKeyRequest) -> T.UpdateKeyResponse:
        """
        Update Key.

        Updates the name of an existing key.

        Args:
        key_id: Path parameter.
        body: Request body.

        Returns:
            T.UpdateKeyResponse: The API response.
        """
        return self._http.request(
            method="PUT",
            path="/keys/{keyId}",
            path_params={"keyId": key_id},
            query_params=None,
            body=body,
            requires_signature=True,
        )

    def delete_key(self, key_id: str) -> T.DeleteKeyResponse:
        """
        Delete Key.

        Deletes the key and all wallets using this key. Once deleted, keys (and wallets) are not usable anymore, and won't count in your overall organisation wallet count.

        Args:
        key_id: Path parameter.

        Returns:
            T.DeleteKeyResponse: The API response.
        """
        return self._http.request(
            method="DELETE",
            path="/keys/{keyId}",
            path_params={"keyId": key_id},
            query_params=None,
            body=None,
            requires_signature=True,
        )

    def derive_key(self, key_id: str, body: T.DeriveKeyRequest) -> T.DeriveKeyResponse:
        """
        Derive Key.

        Dfns decentralized key management network supports threshold Diffie-Hellman protocol based on [GLOW20 paper](https://eprint.iacr.org/2020/096). You can use the DH protocol to derive output from a domain separation tag and a seed value. The derivation process is deterministic, i.e. the same Diffie-Hellman key and seed will lead to the same derived output. To ensure reproducibility, we use hash to curve [RFC9380](https://www.rfc-editor.org/rfc/rfc9380.html) and standard ciphersuite `secp256k1_XMD:SHA-256_SSWU_RO_`.

<Tip>
The seed doesn’t need to be secret. Without access to the DH key, it is not possible to do the derivation, even if the seed is known. Moreover, if both seed and derived output are known, it’s also not possible to do the derivation for another seed without having access to the DH key.
</Tip>

This endpoint only supports Diffie-Hellman keys. Regular threshold signature keys, like `ECDSA` or `EdDSA`, will not work. You can create a Diffie-Hellman key with the [Create Key](https://docs.dfns.co/api-reference/keys/create-key) endpoint using `scheme=DH` and `curve=secp256k1`.

        Args:
        key_id: Path parameter.
        body: Request body.

        Returns:
            T.DeriveKeyResponse: The API response.
        """
        return self._http.request(
            method="POST",
            path="/keys/{keyId}/derive",
            path_params={"keyId": key_id},
            query_params=None,
            body=body,
            requires_signature=True,
        )

    def export_key(self, key_id: str, body: T.ExportKeyRequest) -> T.ExportKeyResponse:
        """
        Export Key.

        Dfns secures private keys by generating them as MPC key shares in our decentralized key management network.  Our goal is to eliminate all single points of failure (SPOFs) associated with blockchain private keys.

In certain circumstances, however, customers require Dfns to export a private key. In this case, Dfns exposes the following endpoint which can be used in conjunction with our [export SDK](https://github.com/dfns/dfns-sdk-ts/tree/m/examples/sdk/export-wallet).

<Danger>
Dfns can not guarantee the security of exported keys as we have no way to control blockchain transactions once the single point of failure has been reconstituted.  For this reason, this feature is restricted to customers who have signed a contractual addendum limiting our liability for exported keys.  Additionally, by default exported keys can no longer be used to sign within the Dfns platform. Please contact your sales representative for more information.
</Danger>

        Args:
        key_id: Path parameter.
        body: Request body.

        Returns:
            T.ExportKeyResponse: The API response.
        """
        return self._http.request(
            method="POST",
            path="/keys/{keyId}/export",
            path_params={"keyId": key_id},
            query_params=None,
            body=body,
            requires_signature=True,
        )

    def list_signatures(self, key_id: str, query: Optional[T.ListSignaturesQuery] = None) -> T.ListSignaturesResponse:
        """
        List Signatures.

        List all signature requests for a key.

        Args:
        key_id: Path parameter.
        query: Query parameters.

        Returns:
            T.ListSignaturesResponse: The API response.
        """
        return self._http.request(
            method="GET",
            path="/keys/{keyId}/signatures",
            path_params={"keyId": key_id},
            query_params=query,
            body=None,
            requires_signature=False,
        )

    def generate_signature(self, key_id: str, body: dict[str, Any]) -> T.GenerateSignatureResponse:
        """
        Generate Signature.

        Request to generate a signature with the key. **This process does not broadcast anything on-chain**, this is just an off-chain signature request.

Dfns is compatible with any blockchain that uses a supported [key format](https://docs.dfns.co/networks/supported-key-formats). If Dfns doesn't officially integrate with a blockchain, you can use hash signing to generate the signatures to interact with the chain.

<Note>
If you were using the deprecated `POST /wallets/{walletId}/signatures` endpoint, then you should now use this one. See the [deprecation notice](https://docs.dfns.co/developers/guides/keys-and-multichain-migration-guide) to get more information about how to change your code. TL,DR: from a wallet you can obtain the key as `wallet.signingKey.id`. 
</Note>


        Args:
        key_id: Path parameter.
        body: Request body.

        Returns:
            T.GenerateSignatureResponse: The API response.
        """
        return self._http.request(
            method="POST",
            path="/keys/{keyId}/signatures",
            path_params={"keyId": key_id},
            query_params=None,
            body=body,
            requires_signature=True,
        )

    def get_signature(self, key_id: str, signature_id: str) -> T.GetSignatureResponse:
        """
        Get Signature.

        Retrieve a signature request details.

        Args:
        key_id: Path parameter.
        signature_id: Path parameter.

        Returns:
            T.GetSignatureResponse: The API response.
        """
        return self._http.request(
            method="GET",
            path="/keys/{keyId}/signatures/{signatureId}",
            path_params={"keyId": key_id, "signatureId": signature_id},
            query_params=None,
            body=None,
            requires_signature=False,
        )

    def import_key(self, body: T.ImportKeyRequest) -> T.ImportKeyResponse:
        """
        Import Key.

        Dfns secures private keys by generating them as MPC key shares in our decentralized key management network.  This happens by default when you create a [key](https://docs.dfns.co/api-reference/keys/create-key) or [wallet](https://docs.dfns.co/api-reference/wallets/create-wallet).

In some circumstances, however, you may need to import an existing private key into Dfns infrastructure, instead of creating a brand new wallet with Dfns and transfer funds to it. As an example, you might want to keep an existing wallet if its address is tied to a smart contract which you don't want to re-deploy.

In such a case, Dfns exposes this key import API endpoint, which can be used in conjunction with our [import SDK](https://github.com/dfns/dfns-sdk-ts/tree/m/examples/sdk/import-wallet).   Note this is intended to be used only to migrate wallets when first onboarding onto the Dfns platform.

<Danger>
Dfns can not guarantee the security of imported wallets, as we have no way to control who had access to the private key prior to import.  For this reason, this feature is restricted to Enterprise customers who have signed a contractual addendum limiting our liability for imported keys.  Please contact your sales representative for more information.
</Danger>


        Args:
        body: Request body.

        Returns:
            T.ImportKeyResponse: The API response.
        """
        return self._http.request(
            method="POST",
            path="/keys/import",
            path_params={},
            query_params=None,
            body=body,
            requires_signature=True,
        )
