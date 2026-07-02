"""Types for the agreements domain."""

from typing import Any, Literal, TypedDict


class GetLatestUnacceptedAgreementResponse(TypedDict, total=False):
    """getLatestUnacceptedAgreement response."""

    latest_agreement: Any


class GetLatestUnacceptedAgreementQuery(TypedDict, total=False):
    """getLatestUnacceptedAgreement query parameters."""

    agreement_type: Literal["PrivacyPolicy", "TermsAndConditions", "UniswapTermsOfService", "UniswapPrivacyPolicy"]


class RecordAgreementAcceptanceResponse(TypedDict, total=False):
    """recordAgreementAcceptance response."""

    agreement_id: str
    user_id: str
    date_accepted: str
