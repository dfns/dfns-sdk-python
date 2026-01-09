"""Base types for the Dfns SDK."""

from dataclasses import dataclass, field
from typing import Any, Callable, Awaitable, Optional


@dataclass
class DfnsClientConfig:
    """Configuration for the Dfns client."""

    auth_token: str
    """Authentication token (JWT)."""

    base_url: str = "https://api.dfns.io"
    """Base URL for the Dfns API."""

    signer: Optional["Signer"] = None
    """Signer for user action requests."""

    headers: dict[str, str] = field(default_factory=dict)
    """Additional headers to include in requests."""


@dataclass
class DfnsDelegatedClientConfig:
    """
    Configuration for the delegated Dfns client.

    Delegated clients are used when signing is handled externally,
    separating the challenge init from the completion phase.
    """

    auth_token: str
    """Authentication token (JWT) for the service account."""

    base_url: str = "https://api.dfns.io"
    """Base URL for the Dfns API."""

    headers: dict[str, str] = field(default_factory=dict)
    """Additional headers to include in requests."""


class DfnsError(Exception):
    """Exception raised by Dfns API errors."""

    def __init__(
        self,
        message: str,
        status_code: Optional[int] = None,
        error_code: Optional[str] = None,
        details: Optional[dict[str, Any]] = None,
    ):
        super().__init__(message)
        self.message = message
        self.status_code = status_code
        self.error_code = error_code
        self.details = details or {}

    def __str__(self) -> str:
        parts = [self.message]
        if self.status_code:
            parts.append(f"[{self.status_code}]")
        if self.error_code:
            parts.append(f"({self.error_code})")
        return " ".join(parts)

    def __repr__(self) -> str:
        return f"DfnsError({self.message!r}, status_code={self.status_code}, error_code={self.error_code!r})"


# Type alias for signer callback
Signer = Callable[[str], Awaitable[str]]
