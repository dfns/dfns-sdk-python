"""Main Dfns client."""

from typing import Any

from ._internal import HttpClient
from .generated.address_watches import AddressWatchesClient
from .generated.agreements import AgreementsClient
from .generated.allocations import AllocationsClient
from .generated.auth import AuthClient
from .generated.exchanges import ExchangesClient
from .generated.fee_sponsors import FeeSponsorsClient
from .generated.keys import KeysClient
from .generated.networks import NetworksClient
from .generated.payins import PayinsClient
from .generated.payouts import PayoutsClient
from .generated.permissions import PermissionsClient
from .generated.policies import PoliciesClient
from .generated.signers import SignersClient
from .generated.staking import StakingClient
from .generated.swaps import SwapsClient
from .generated.vaults import VaultsClient
from .generated.wallets import WalletsClient
from .generated.webhooks import WebhooksClient
from .types import DfnsClientConfig


class DfnsClient:
    """
    Main client for the Dfns API.

    This client provides access to all Dfns API domains through typed sub-clients.

    Example:
        >>> from dfns_sdk import DfnsClient, DfnsClientConfig
        >>> config = DfnsClientConfig(auth_token="your-token")
        >>> client = DfnsClient(config)
        >>> wallets = client.wallets.list_wallets()
    """

    address_watches: AddressWatchesClient
    agreements: AgreementsClient
    allocations: AllocationsClient
    auth: AuthClient
    exchanges: ExchangesClient
    fee_sponsors: FeeSponsorsClient
    keys: KeysClient
    networks: NetworksClient
    payins: PayinsClient
    payouts: PayoutsClient
    permissions: PermissionsClient
    policies: PoliciesClient
    signers: SignersClient
    staking: StakingClient
    swaps: SwapsClient
    vaults: VaultsClient
    wallets: WalletsClient
    webhooks: WebhooksClient

    def __init__(self, config: DfnsClientConfig):
        """
        Initialize the Dfns client.

        Args:
            config: Client configuration.
        """
        self._config = config
        self._http = HttpClient(config)
        self.address_watches = AddressWatchesClient(self._http)
        self.agreements = AgreementsClient(self._http)
        self.allocations = AllocationsClient(self._http)
        self.auth = AuthClient(self._http)
        self.exchanges = ExchangesClient(self._http)
        self.fee_sponsors = FeeSponsorsClient(self._http)
        self.keys = KeysClient(self._http)
        self.networks = NetworksClient(self._http)
        self.payins = PayinsClient(self._http)
        self.payouts = PayoutsClient(self._http)
        self.permissions = PermissionsClient(self._http)
        self.policies = PoliciesClient(self._http)
        self.signers = SignersClient(self._http)
        self.staking = StakingClient(self._http)
        self.swaps = SwapsClient(self._http)
        self.vaults = VaultsClient(self._http)
        self.wallets = WalletsClient(self._http)
        self.webhooks = WebhooksClient(self._http)

    def close(self) -> None:
        """Close the client and release resources."""
        self._http.close()

    def __enter__(self) -> "DfnsClient":
        return self

    def __exit__(self, *args: Any) -> None:
        self.close()
