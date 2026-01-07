"""Client for the agreements domain."""

from typing import Any, Literal, Optional, TypedDict, Union

from ..._internal import HttpClient
from . import types as T


class AgreementsClient:
    """Client for agreements operations."""

    def __init__(self, http_client: HttpClient):
        self._http = http_client

    def get_latest_unaccepted_agreement(self, query: T.GetLatestUnacceptedAgreementQuery) -> T.GetLatestUnacceptedAgreementResponse:
        """
        Get Latest Unaccepted Agreement.

        Get the latest unaccepted agreement for a specific agreement type

        Args:
        query: Query parameters.

        Returns:
            T.GetLatestUnacceptedAgreementResponse: The API response.
        """
        return self._http.request(
            method="GET",
            path="/agreements/latest-unaccepted",
            path_params={},
            query_params=query,
            body=None,
            requires_signature=False,
        )

    def record_agreement_acceptance(self, agreement_id: str) -> T.RecordAgreementAcceptanceResponse:
        """
        Record Agreement Acceptance.

        Record the acceptance of a specific agreement by its ID

        Args:
        agreement_id: Path parameter.

        Returns:
            T.RecordAgreementAcceptanceResponse: The API response.
        """
        return self._http.request(
            method="POST",
            path="/agreements/{agreementId}/accept",
            path_params={"agreementId": agreement_id},
            query_params=None,
            body=None,
            requires_signature=True,
        )
