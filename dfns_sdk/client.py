"""Main Dfns client."""

from .types import DfnsClientConfig
from ._internal import HttpClient
from .generated.auth import AuthClient
from .generated.exchanges import ExchangesClient
from .generated.fee_sponsors import FeeSponsorsClient
from .generated.keys import KeysClient
from .generated.networks import NetworksClient
from .generated.permissions import PermissionsClient
from .generated.policies import PoliciesClient
from .generated.signers import SignersClient
from .generated.staking import StakingClient
from .generated.wallets import WalletsClient
from .generated.webhooks import WebhooksClient
from .generated.swaps import SwapsClient
from .generated.agreements import AgreementsClient
from .generated.allocations import AllocationsClient


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

    auth: AuthClient
    exchanges: ExchangesClient
    fee_sponsors: FeeSponsorsClient
    keys: KeysClient
    networks: NetworksClient
    permissions: PermissionsClient
    policies: PoliciesClient
    signers: SignersClient
    staking: StakingClient
    wallets: WalletsClient
    webhooks: WebhooksClient
    swaps: SwapsClient
    agreements: AgreementsClient
    allocations: AllocationsClient

    def __init__(self, config: DfnsClientConfig):
        """
        Initialize the Dfns client.

        Args:
            config: Client configuration.
        """
        self._config = config
        self._http = HttpClient(config)
        self.auth = AuthClient(self._http)
        self.exchanges = ExchangesClient(self._http)
        self.fee_sponsors = FeeSponsorsClient(self._http)
        self.keys = KeysClient(self._http)
        self.networks = NetworksClient(self._http)
        self.permissions = PermissionsClient(self._http)
        self.policies = PoliciesClient(self._http)
        self.signers = SignersClient(self._http)
        self.staking = StakingClient(self._http)
        self.wallets = WalletsClient(self._http)
        self.webhooks = WebhooksClient(self._http)
        self.swaps = SwapsClient(self._http)
        self.agreements = AgreementsClient(self._http)
        self.allocations = AllocationsClient(self._http)

    def close(self) -> None:
        """Close the client and release resources."""
        self._http.close()

    def __enter__(self) -> "DfnsClient":
        return self

    def __exit__(self, *args) -> None:
        self.close()
