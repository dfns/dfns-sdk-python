"""Delegated client for the agreements domain."""

import json
from typing import Any, Literal, Optional, TypedDict, Union

from ..._internal import HttpClient
from ...base_auth_api import (
    BaseAuthApi,
    SignUserActionChallengeRequest,
    UserActionChallengeResponse,
)
from . import types as T


class DelegatedAgreementsClient:
    """
    Delegated client for agreements operations.

    This client separates user action signing into _init() and _complete() method pairs,
    allowing external systems to handle the signing process.
    """

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

    def record_agreement_acceptance_init(self, agreement_id: str) -> UserActionChallengeResponse:
        """
        Initialize Record Agreement Acceptance.

        Creates a user action challenge for external signing.

        Args:
        agreement_id: Path parameter.

        Returns:
            UserActionChallengeResponse: The challenge to sign externally.
        """
        path = "/agreements/{agreementId}/accept"
        path = path.replace("{agreementId}", str(agreement_id))
        payload = ""

        return BaseAuthApi.create_user_action_challenge(
            self._http,
            user_action_http_method="POST",
            user_action_http_path=path,
            user_action_payload=payload,
        )

    def record_agreement_acceptance_complete(self, agreement_id: str, signed_challenge: SignUserActionChallengeRequest) -> T.RecordAgreementAcceptanceResponse:
        """
        Complete Record Agreement Acceptance.

        Submits the signed challenge and makes the API request.

        Args:
        agreement_id: Path parameter.
        signed_challenge: The signed challenge from external signing.

        Returns:
            T.RecordAgreementAcceptanceResponse: The API response.
        """
        user_action_result = BaseAuthApi.sign_user_action_challenge(
            self._http, signed_challenge
        )
        user_action_token = user_action_result["userAction"]

        return self._http.request_with_user_action(
            method="POST",
            path="/agreements/{agreementId}/accept",
            path_params={"agreementId": agreement_id},
            query_params=None,
            body=None,
            user_action=user_action_token,
        )
