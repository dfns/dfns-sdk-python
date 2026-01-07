"""Generated domain clients."""

from .auth import AuthClient
from .exchanges import ExchangesClient
from .fee_sponsors import FeeSponsorsClient
from .keys import KeysClient
from .networks import NetworksClient
from .permissions import PermissionsClient
from .policies import PoliciesClient
from .signers import SignersClient
from .staking import StakingClient
from .wallets import WalletsClient
from .webhooks import WebhooksClient
from .swaps import SwapsClient
from .agreements import AgreementsClient
from .allocations import AllocationsClient

__all__ = [
    "AuthClient",
    "ExchangesClient",
    "FeeSponsorsClient",
    "KeysClient",
    "NetworksClient",
    "PermissionsClient",
    "PoliciesClient",
    "SignersClient",
    "StakingClient",
    "WalletsClient",
    "WebhooksClient",
    "SwapsClient",
    "AgreementsClient",
    "AllocationsClient",
]
