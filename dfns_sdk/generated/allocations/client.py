"""Client for the allocations domain."""

from typing import Any, cast

from ..._internal import HttpClient
from . import types as T


class AllocationsClient:
    """Client for allocations operations."""

    def __init__(self, http_client: HttpClient):
        self._http = http_client

    def list_allocations(self, query: T.ListAllocationsQuery | None = None) -> T.ListAllocationsResponse:
        """
        List Allocations.

        Lists the allocations of your organization.

        Args:
            query: Query parameters.

        Returns:
            T.ListAllocationsResponse: The API response.
        """  # noqa: E501
        response = self._http.request(
            method="GET",
            path="/allocations",
            path_params={},
            query_params=query,
            body=None,
            requires_signature=False,
        )
        return cast(T.ListAllocationsResponse, response)

    def create_allocation(self, body: dict[str, Any]) -> T.CreateAllocationResponse:
        """
                Create Allocation.

                Create a new allocation.

        An allocation deposits assets from one of your wallets into a rewards-earning protocol. Two providers are available:

        | Provider  | Description                                                                                                                   | Supported chains                   |
        |-----------|---------------------------------------------------------------------------------------------------------------------------------|------------------------------------|
        | M0        | Offers the `0fns` protocol, an extension to the M0 USD-based stablecoin $M. Trade USDC on Ethereum into 0fns to earn rewards. | Ethereum Mainnet, Ethereum Sepolia |
        | Yield.xyz | Offers a set of DeFi vault strategies, each with its own APY. Deposit the vault's underlying token; withdraw it at any time.    | Ethereum Mainnet, Base             |

        The `protocol` field selects the strategy:

        | `protocol`              | Provider  | Strategy                          | Deposit asset | Network  |
        |---------------------------|-----------|-----------------------------------|---------------|----------|
        | `0fns`                  | M0        | 0fns                              | USDC          | Ethereum |
        | `SkySusds`              | Yield.xyz | Sky Savings Rate (sUSDS)          | USDS          | Ethereum |
        | `GauntletUsdcPrime`     | Yield.xyz | Gauntlet USDC Prime (gtUSDC)      | USDC          | Ethereum |
        | `SteakhouseUsdt`        | Yield.xyz | Steakhouse USDT (steakUSDT)       | USDT          | Ethereum |
        | `GauntletUsdcPrimeBase` | Yield.xyz | Gauntlet USDC Prime (gtUSDCp)     | USDC          | Base     |
        | `SteakhouseUsdcBase`    | Yield.xyz | Steakhouse USDC (steakUSDC)       | USDC          | Base     |
        | `SentoraPyusdMain`      | Yield.xyz | Sentora PYUSD Main (senPYUSDMain) | PYUSD         | Ethereum |

        Yield.xyz vaults are available on mainnet networks only.

                Args:
                    body: Request body.

                Returns:
                    T.CreateAllocationResponse: The API response.
        """  # noqa: E501
        response = self._http.request(
            method="POST",
            path="/allocations",
            path_params={},
            query_params=None,
            body=body,
            requires_signature=True,
        )
        return cast(T.CreateAllocationResponse, response)

    def list_allocation_actions(
        self, allocation_id: str, query: T.ListAllocationActionsQuery | None = None
    ) -> T.ListAllocationActionsResponse:
        """
        List Allocation Actions.

        Retrieve the list of actions for a specific allocation.

        Args:
            allocation_id: Unique identifier for the allocation investment.
            query: Query parameters.

        Returns:
            T.ListAllocationActionsResponse: The API response.
        """  # noqa: E501
        response = self._http.request(
            method="GET",
            path="/allocations/{allocationId}/actions",
            path_params={"allocationId": allocation_id},
            query_params=query,
            body=None,
            requires_signature=False,
        )
        return cast(T.ListAllocationActionsResponse, response)

    def create_allocation_action(self, allocation_id: str, body: dict[str, Any]) -> T.CreateAllocationActionResponse:
        """
        Create Allocation Action.

        Create a new action for an existing allocation.

        Args:
            allocation_id: Unique identifier for the allocation investment.
            body: Request body.

        Returns:
            T.CreateAllocationActionResponse: The API response.
        """  # noqa: E501
        response = self._http.request(
            method="POST",
            path="/allocations/{allocationId}/actions",
            path_params={"allocationId": allocation_id},
            query_params=None,
            body=body,
            requires_signature=True,
        )
        return cast(T.CreateAllocationActionResponse, response)

    def get_allocation(self, allocation_id: str) -> T.GetAllocationResponse:
        """
        Get Allocation.

        Retrieve the details of a specific allocation.

        Args:
            allocation_id: Unique identifier for the allocation investment.

        Returns:
            T.GetAllocationResponse: The API response.
        """  # noqa: E501
        response = self._http.request(
            method="GET",
            path="/allocations/{allocationId}",
            path_params={"allocationId": allocation_id},
            query_params=None,
            body=None,
            requires_signature=False,
        )
        return cast(T.GetAllocationResponse, response)

    def get_allocations_info(self) -> T.GetAllocationsInfoResponse:
        """
        Get Allocations Info.

        Retrieve the current reward rate (APY) for each supported allocation protocol.

        Returns:
            T.GetAllocationsInfoResponse: The API response.
        """  # noqa: E501
        response = self._http.request(
            method="GET",
            path="/allocations/info",
            path_params={},
            query_params=None,
            body=None,
            requires_signature=False,
        )
        return cast(T.GetAllocationsInfoResponse, response)
