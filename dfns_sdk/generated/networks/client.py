"""Client for the networks domain."""

from typing import Any, Literal, Optional, TypedDict, Union

from ..._internal import HttpClient
from . import types as T


class NetworksClient:
    """Client for networks operations."""

    def __init__(self, http_client: HttpClient):
        self._http = http_client

    def estimate_fees(self, query: T.EstimateFeesQuery) -> TypedDict:
        """
        Estimate Fees.

        Gets real-time fee details for a given network, allowing users to make decisions based on their preferences for transaction speed/priority. Three levels of priority will be displayed: `slow`, `standard`, `fast`.

        Args:
        query: Query parameters.

        Returns:
            TypedDict: The API response.
        """
        return self._http.request(
            method="GET",
            path="/networks/fees",
            path_params={},
            query_params=query,
            body=None,
            requires_signature=False,
        )

    def read_contract(self, body: dict[str, Any]) -> T.ReadContractResponse:
        """
        Read Contract.

        Call a read-only function on a smart contract. In Solidity, this use the `view` keyword.

  <Note>
  Currently only works on EVM compatible chains.
  </Note>

        Args:
        body: Request body.

        Returns:
            T.ReadContractResponse: The API response.
        """
        return self._http.request(
            method="POST",
            path="/networks/read-contract",
            path_params={},
            query_params=None,
            body=body,
            requires_signature=False,
        )

    def get_canton_validator(self, network: Literal["canton", "canton-devnet", "canton-testnet"], validator_id: str) -> T.GetCantonValidatorResponse:
        """
        Get Canton Validator.

        Return a configured Canton Validator in your organization.

        Args:
        network: Path parameter.
        validator_id: Path parameter.

        Returns:
            T.GetCantonValidatorResponse: The API response.
        """
        return self._http.request(
            method="GET",
            path="/networks/{network}/validators/{validatorId}",
            path_params={"network": network, "validatorId": validator_id},
            query_params=None,
            body=None,
            requires_signature=False,
        )

    def update_canton_validator(self, network: Literal["canton", "canton-devnet", "canton-testnet"], validator_id: str, body: T.UpdateCantonValidatorRequest) -> T.UpdateCantonValidatorResponse:
        """
        Update Canton Validator.

        Update an existing Canton Validator configuration.
  
  Read details about the process [here](https://docs.dfns.co/networks/canton-validators). 

        Args:
        network: Path parameter.
        validator_id: Path parameter.
        body: Request body.

        Returns:
            T.UpdateCantonValidatorResponse: The API response.
        """
        return self._http.request(
            method="PUT",
            path="/networks/{network}/validators/{validatorId}",
            path_params={"network": network, "validatorId": validator_id},
            query_params=None,
            body=body,
            requires_signature=True,
        )

    def delete_canton_validator(self, network: Literal["canton", "canton-devnet", "canton-testnet"], validator_id: str) -> T.DeleteCantonValidatorResponse:
        """
        Delete Canton Validator.

        Delete a specific Canton Validator configuration.

        Args:
        network: Path parameter.
        validator_id: Path parameter.

        Returns:
            T.DeleteCantonValidatorResponse: The API response.
        """
        return self._http.request(
            method="DELETE",
            path="/networks/{network}/validators/{validatorId}",
            path_params={"network": network, "validatorId": validator_id},
            query_params=None,
            body=None,
            requires_signature=True,
        )

    def list_canton_validators(self, network: Literal["canton", "canton-devnet", "canton-testnet"], query: Optional[T.ListCantonValidatorsQuery] = None) -> T.ListCantonValidatorsResponse:
        """
        List Canton Validators.

        Retrieve the list of configured Canton Validators in your organization.

        Args:
        network: Path parameter.
        query: Query parameters.

        Returns:
            T.ListCantonValidatorsResponse: The API response.
        """
        return self._http.request(
            method="GET",
            path="/networks/{network}/validators",
            path_params={"network": network},
            query_params=query,
            body=None,
            requires_signature=False,
        )

    def create_canton_validator(self, network: Literal["canton", "canton-devnet", "canton-testnet"], body: dict[str, Any]) -> T.CreateCantonValidatorResponse:
        """
        Create Canton Validator.

        Link a Canton Validator to your organization. This is required in order to create wallets or interact with the Canton network.

  The `Shared` option allows you to use a shared validator hosted by DFNS and get started in seconds, while the `Custom` option allows you to connect your own validator and ledger nodes using OAuth2 authentication.

  Read details about the process [here](https://docs.dfns.co/networks/canton-validators). 

        Args:
        network: Path parameter.
        body: Request body.

        Returns:
            T.CreateCantonValidatorResponse: The API response.
        """
        return self._http.request(
            method="POST",
            path="/networks/{network}/validators",
            path_params={"network": network},
            query_params=None,
            body=body,
            requires_signature=True,
        )
