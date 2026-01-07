"""HTTP client for making API requests."""

import json
from typing import Any, Optional, TypeVar, TYPE_CHECKING
from urllib.parse import urlencode, urlparse

import httpx

from dfns_sdk.types import DfnsClientConfig, DfnsError

if TYPE_CHECKING:
    from dfns_sdk.auth import Signer

T = TypeVar("T")


class HttpClient:
    """HTTP client for Dfns API requests."""

    def __init__(self, config: DfnsClientConfig):
        self.config = config
        self._client = httpx.Client(
            base_url=config.base_url,
            timeout=30.0,
        )

    def _build_headers(self, user_action_token: Optional[str] = None) -> dict[str, str]:
        """Build request headers."""
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.config.auth_token}",
            **self.config.headers,
        }

        if user_action_token:
            headers["X-DFNS-USERACTION"] = user_action_token

        return headers

    def _build_url(
        self,
        path: str,
        path_params: Optional[dict[str, Any]] = None,
        query_params: Optional[dict[str, Any]] = None,
    ) -> str:
        """Build the full URL with path and query parameters."""
        url = path

        if path_params:
            for key, value in path_params.items():
                url = url.replace(f"{{{key}}}", str(value))

        if query_params:
            filtered_params = {k: v for k, v in query_params.items() if v is not None}
            if filtered_params:
                url = f"{url}?{urlencode(filtered_params)}"

        return url

    def _handle_response(self, response: httpx.Response) -> Any:
        """Handle API response and raise errors if needed."""
        if response.status_code >= 400:
            try:
                error_data = response.json()
                raise DfnsError(
                    message=error_data.get("message", "Unknown error"),
                    status_code=response.status_code,
                    error_code=error_data.get("error"),
                    details=error_data.get("details"),
                )
            except json.JSONDecodeError:
                raise DfnsError(
                    message=response.text or "Unknown error",
                    status_code=response.status_code,
                )

        if response.status_code == 204 or not response.content:
            return None

        return response.json()

    def _get_user_action_token(
        self,
        method: str,
        path: str,
        body: Optional[Any] = None,
    ) -> str:
        """
        Get a user action token by creating and signing a challenge.

        Args:
            method: HTTP method.
            path: Request path.
            body: Request body.

        Returns:
            The user action token to include in the request header.

        Raises:
            DfnsError: If no signer is configured or signing fails.
        """
        if not self.config.signer:
            raise DfnsError(
                message="Signer required for this operation. Configure a signer in DfnsClientConfig.",
                status_code=None,
                error_code="SIGNER_REQUIRED",
            )

        # Step 1: Create user action challenge
        challenge_body = {
            "userActionPayload": json.dumps(body, separators=(",", ":")) if body else "",
            "userActionHttpMethod": method,
            "userActionHttpPath": path,
            "userActionServerKind": "Api",
        }

        challenge_response = self._client.request(
            method="POST",
            url="/auth/action/init",
            headers=self._build_headers(),
            json=challenge_body,
        )
        challenge = self._handle_response(challenge_response)

        # Step 2: Sign the challenge
        assertion = self.config.signer.sign(challenge)

        # Step 3: Submit signed challenge to get user action token
        signature_body = {
            "challengeIdentifier": challenge["challengeIdentifier"],
            "firstFactor": assertion,
        }

        signature_response = self._client.request(
            method="POST",
            url="/auth/action",
            headers=self._build_headers(),
            json=signature_body,
        )
        result = self._handle_response(signature_response)

        return result["userAction"]

    def request(
        self,
        method: str,
        path: str,
        path_params: Optional[dict[str, Any]] = None,
        query_params: Optional[dict[str, Any]] = None,
        body: Optional[Any] = None,
        requires_signature: bool = False,
    ) -> Any:
        """Make an HTTP request to the API."""
        url = self._build_url(path, path_params, query_params)

        # Get user action token if required
        user_action_token = None
        if requires_signature:
            # Use the path with params substituted for signing
            signing_path = path
            if path_params:
                for key, value in path_params.items():
                    signing_path = signing_path.replace(f"{{{key}}}", str(value))
            user_action_token = self._get_user_action_token(method, signing_path, body)

        headers = self._build_headers(user_action_token)

        response = self._client.request(
            method=method,
            url=url,
            headers=headers,
            json=body if body is not None else None,
        )

        return self._handle_response(response)

    def close(self) -> None:
        """Close the HTTP client."""
        self._client.close()

    def __enter__(self) -> "HttpClient":
        return self

    def __exit__(self, *args: Any) -> None:
        self.close()


class AsyncHttpClient:
    """Async HTTP client for Dfns API requests."""

    def __init__(self, config: DfnsClientConfig):
        self.config = config
        self._client = httpx.AsyncClient(
            base_url=config.base_url,
            timeout=30.0,
        )

    def _build_headers(self, user_action_token: Optional[str] = None) -> dict[str, str]:
        """Build request headers."""
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.config.auth_token}",
            **self.config.headers,
        }

        if user_action_token:
            headers["X-DFNS-USERACTION"] = user_action_token

        return headers

    def _build_url(
        self,
        path: str,
        path_params: Optional[dict[str, Any]] = None,
        query_params: Optional[dict[str, Any]] = None,
    ) -> str:
        """Build the full URL with path and query parameters."""
        url = path

        if path_params:
            for key, value in path_params.items():
                url = url.replace(f"{{{key}}}", str(value))

        if query_params:
            filtered_params = {k: v for k, v in query_params.items() if v is not None}
            if filtered_params:
                url = f"{url}?{urlencode(filtered_params)}"

        return url

    def _handle_response(self, response: httpx.Response) -> Any:
        """Handle API response and raise errors if needed."""
        if response.status_code >= 400:
            try:
                error_data = response.json()
                raise DfnsError(
                    message=error_data.get("message", "Unknown error"),
                    status_code=response.status_code,
                    error_code=error_data.get("error"),
                    details=error_data.get("details"),
                )
            except json.JSONDecodeError:
                raise DfnsError(
                    message=response.text or "Unknown error",
                    status_code=response.status_code,
                )

        if response.status_code == 204 or not response.content:
            return None

        return response.json()

    async def _get_user_action_token(
        self,
        method: str,
        path: str,
        body: Optional[Any] = None,
    ) -> str:
        """
        Get a user action token by creating and signing a challenge.

        Args:
            method: HTTP method.
            path: Request path.
            body: Request body.

        Returns:
            The user action token to include in the request header.

        Raises:
            DfnsError: If no signer is configured or signing fails.
        """
        if not self.config.signer:
            raise DfnsError(
                message="Signer required for this operation. Configure a signer in DfnsClientConfig.",
                status_code=None,
                error_code="SIGNER_REQUIRED",
            )

        # Step 1: Create user action challenge
        challenge_body = {
            "userActionPayload": json.dumps(body, separators=(",", ":")) if body else "",
            "userActionHttpMethod": method,
            "userActionHttpPath": path,
            "userActionServerKind": "Api",
        }

        challenge_response = await self._client.request(
            method="POST",
            url="/auth/action/init",
            headers=self._build_headers(),
            json=challenge_body,
        )
        challenge = self._handle_response(challenge_response)

        # Step 2: Sign the challenge
        assertion = self.config.signer.sign(challenge)

        # Step 3: Submit signed challenge to get user action token
        signature_body = {
            "challengeIdentifier": challenge["challengeIdentifier"],
            "firstFactor": assertion,
        }

        signature_response = await self._client.request(
            method="POST",
            url="/auth/action",
            headers=self._build_headers(),
            json=signature_body,
        )
        result = self._handle_response(signature_response)

        return result["userAction"]

    async def request(
        self,
        method: str,
        path: str,
        path_params: Optional[dict[str, Any]] = None,
        query_params: Optional[dict[str, Any]] = None,
        body: Optional[Any] = None,
        requires_signature: bool = False,
    ) -> Any:
        """Make an async HTTP request to the API."""
        url = self._build_url(path, path_params, query_params)

        # Get user action token if required
        user_action_token = None
        if requires_signature:
            # Use the path with params substituted for signing
            signing_path = path
            if path_params:
                for key, value in path_params.items():
                    signing_path = signing_path.replace(f"{{{key}}}", str(value))
            user_action_token = await self._get_user_action_token(method, signing_path, body)

        headers = self._build_headers(user_action_token)

        response = await self._client.request(
            method=method,
            url=url,
            headers=headers,
            json=body if body is not None else None,
        )

        return self._handle_response(response)

    async def close(self) -> None:
        """Close the HTTP client."""
        await self._client.aclose()

    async def __aenter__(self) -> "AsyncHttpClient":
        return self

    async def __aexit__(self, *args: Any) -> None:
        await self.close()
