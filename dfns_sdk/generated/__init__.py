"""Generated domain clients."""

from .auth import AuthClient, DelegatedAuthClient
from .exchanges import ExchangesClient, DelegatedExchangesClient
from .fee_sponsors import FeeSponsorsClient, DelegatedFeeSponsorsClient
from .keys import KeysClient, DelegatedKeysClient
from .networks import NetworksClient, DelegatedNetworksClient
from .permissions import PermissionsClient, DelegatedPermissionsClient
from .policies import PoliciesClient, DelegatedPoliciesClient
from .signers import SignersClient, DelegatedSignersClient
from .staking import StakingClient, DelegatedStakingClient
from .wallets import WalletsClient, DelegatedWalletsClient
from .webhooks import WebhooksClient, DelegatedWebhooksClient
from .swaps import SwapsClient, DelegatedSwapsClient
from .agreements import AgreementsClient, DelegatedAgreementsClient
from .allocations import AllocationsClient, DelegatedAllocationsClient

__all__ = [
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
    "PermissionsClient",
    "DelegatedPermissionsClient",
    "PoliciesClient",
    "DelegatedPoliciesClient",
    "SignersClient",
    "DelegatedSignersClient",
    "StakingClient",
    "DelegatedStakingClient",
    "WalletsClient",
    "DelegatedWalletsClient",
    "WebhooksClient",
    "DelegatedWebhooksClient",
    "SwapsClient",
    "DelegatedSwapsClient",
    "AgreementsClient",
    "DelegatedAgreementsClient",
    "AllocationsClient",
    "DelegatedAllocationsClient",
]
