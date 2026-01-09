"""Delegated Dfns client for external signing orchestration."""

from .types import DfnsDelegatedClientConfig
from ._internal import HttpClient
from .generated.auth import DelegatedAuthClient
from .generated.exchanges import DelegatedExchangesClient
from .generated.fee_sponsors import DelegatedFeeSponsorsClient
from .generated.keys import DelegatedKeysClient
from .generated.networks import DelegatedNetworksClient
from .generated.permissions import DelegatedPermissionsClient
from .generated.policies import DelegatedPoliciesClient
from .generated.signers import DelegatedSignersClient
from .generated.staking import DelegatedStakingClient
from .generated.wallets import DelegatedWalletsClient
from .generated.webhooks import DelegatedWebhooksClient
from .generated.swaps import DelegatedSwapsClient
from .generated.agreements import DelegatedAgreementsClient
from .generated.allocations import DelegatedAllocationsClient


class DfnsDelegatedClient:
    """
    Delegated client for the Dfns API.

    This client is designed for service accounts that orchestrate signing externally.
    Operations requiring user action signing are split into *_init() and *_complete()
    method pairs, allowing external systems to handle the signing process.

    Example:
        >>> from dfns_sdk import DfnsDelegatedClient, DfnsDelegatedClientConfig
        >>> config = DfnsDelegatedClientConfig(auth_token="service-account-token")
        >>> client = DfnsDelegatedClient(config)
        >>>
        >>> # Step 1: Initialize action (get challenge)
        >>> challenge = client.wallets.create_wallet_init(body={"network": "EthereumSepolia"})
        >>>
        >>> # Step 2: Sign externally (your signing system)
        >>> signed = your_external_signer.sign(challenge)
        >>>
        >>> # Step 3: Complete action with signed challenge
        >>> wallet = client.wallets.create_wallet_complete(
        ...     body={"network": "EthereumSepolia"},
        ...     signed_challenge={
        ...         "challengeIdentifier": challenge["challengeIdentifier"],
        ...         "firstFactor": signed,
        ...     },
        ... )
    """

    auth: DelegatedAuthClient
    exchanges: DelegatedExchangesClient
    fee_sponsors: DelegatedFeeSponsorsClient
    keys: DelegatedKeysClient
    networks: DelegatedNetworksClient
    permissions: DelegatedPermissionsClient
    policies: DelegatedPoliciesClient
    signers: DelegatedSignersClient
    staking: DelegatedStakingClient
    wallets: DelegatedWalletsClient
    webhooks: DelegatedWebhooksClient
    swaps: DelegatedSwapsClient
    agreements: DelegatedAgreementsClient
    allocations: DelegatedAllocationsClient

    def __init__(self, config: DfnsDelegatedClientConfig):
        """
        Initialize the delegated Dfns client.

        Args:
            config: Client configuration (no signer required).
        """
        self._config = config
        self._http = HttpClient(config)
        self.auth = DelegatedAuthClient(self._http)
        self.exchanges = DelegatedExchangesClient(self._http)
        self.fee_sponsors = DelegatedFeeSponsorsClient(self._http)
        self.keys = DelegatedKeysClient(self._http)
        self.networks = DelegatedNetworksClient(self._http)
        self.permissions = DelegatedPermissionsClient(self._http)
        self.policies = DelegatedPoliciesClient(self._http)
        self.signers = DelegatedSignersClient(self._http)
        self.staking = DelegatedStakingClient(self._http)
        self.wallets = DelegatedWalletsClient(self._http)
        self.webhooks = DelegatedWebhooksClient(self._http)
        self.swaps = DelegatedSwapsClient(self._http)
        self.agreements = DelegatedAgreementsClient(self._http)
        self.allocations = DelegatedAllocationsClient(self._http)

    def close(self) -> None:
        """Close the client and release resources."""
        self._http.close()

    def __enter__(self) -> "DfnsDelegatedClient":
        return self

    def __exit__(self, *args) -> None:
        self.close()
