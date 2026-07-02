"""Generated domain clients."""

from .agreements import AgreementsClient, DelegatedAgreementsClient
from .allocations import AllocationsClient, DelegatedAllocationsClient
from .auth import AuthClient, DelegatedAuthClient
from .exchanges import DelegatedExchangesClient, ExchangesClient
from .fee_sponsors import DelegatedFeeSponsorsClient, FeeSponsorsClient
from .keys import DelegatedKeysClient, KeysClient
from .networks import DelegatedNetworksClient, NetworksClient
from .payouts import DelegatedPayoutsClient, PayoutsClient
from .permissions import DelegatedPermissionsClient, PermissionsClient
from .policies import DelegatedPoliciesClient, PoliciesClient
from .signers import DelegatedSignersClient, SignersClient
from .staking import DelegatedStakingClient, StakingClient
from .swaps import DelegatedSwapsClient, SwapsClient
from .wallets import DelegatedWalletsClient, WalletsClient
from .webhooks import DelegatedWebhooksClient, WebhooksClient

__all__ = [
    "AgreementsClient",
    "DelegatedAgreementsClient",
    "AllocationsClient",
    "DelegatedAllocationsClient",
    "AuthClient",
    "DelegatedAuthClient",
    "ExchangesClient",
    "DelegatedExchangesClient",
    "FeeSponsorsClient",
    "DelegatedFeeSponsorsClient",
    "KeysClient",
    "DelegatedKeysClient",
    "NetworksClient",
    "DelegatedNetworksClient",
    "PayoutsClient",
    "DelegatedPayoutsClient",
    "PermissionsClient",
    "DelegatedPermissionsClient",
    "PoliciesClient",
    "DelegatedPoliciesClient",
    "SignersClient",
    "DelegatedSignersClient",
    "StakingClient",
    "DelegatedStakingClient",
    "SwapsClient",
    "DelegatedSwapsClient",
    "WalletsClient",
    "DelegatedWalletsClient",
    "WebhooksClient",
    "DelegatedWebhooksClient",
]
