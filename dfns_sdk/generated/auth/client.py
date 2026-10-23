"""Client for the auth domain."""

from typing import Any, cast

from typing_extensions import deprecated

from ..._internal import HttpClient
from . import types as T


class AuthClient:
    """Client for auth operations."""

    def __init__(self, http_client: HttpClient):
        self._http = http_client

    def create_user_action_signature(
        self, body: T.CreateUserActionSignatureRequest
    ) -> T.CreateUserActionSignatureResponse:
        """
                Create User Action Signature.

                Completes the user action signing process and provides a signing token that can be used to verify the user intended to perform the action.

        This is the first step of the [User Action Signing flow](https://docs.dfns.co/api-reference/auth/signing-flows).

        The type of credentials used to sign the action is determined by the `kind` field in the nested objects (`firstFactor` and `secondFactor`). Supported credential kinds are:
        * `Fido2`: User action is signed by a user's signing device using `WebAuthn`.
        * `Key`: User action is signed by a user's, or token's, private key.
        * `PasswordProtectedKey`: Login challenge is signed by the decrypted user's private key that was sent during [Create User Action Signature Challenge](https://docs.dfns.co/api-reference/auth/create-user-action-challenge) step.

                Args:
                    body: Request body.

                Returns:
                    T.CreateUserActionSignatureResponse: The API response.
        """  # noqa: E501
        response = self._http.request(
            method="POST",
            path="/auth/action",
            path_params={},
            query_params=None,
            body=body,
            requires_signature=False,
        )
        return cast(T.CreateUserActionSignatureResponse, response)

    def create_user_action_challenge(
        self, body: T.CreateUserActionChallengeRequest
    ) -> T.CreateUserActionChallengeResponse:
        """
              Create User Action Challenge.

              Starts a user action signing session, returning a challenge that will be used to verify the user's intent to perform an action.

        This is the first step of the [User Action Signing flow](https://docs.dfns.co/api-reference/auth/signing-flows).

              Args:
                  body: Request body.

              Returns:
                  T.CreateUserActionChallengeResponse: The API response.
        """  # noqa: E501
        response = self._http.request(
            method="POST",
            path="/auth/action/init",
            path_params={},
            query_params=None,
            body=body,
            requires_signature=False,
        )
        return cast(T.CreateUserActionChallengeResponse, response)

    def list_audit_logs(self, query: T.ListAuditLogsQuery) -> None:
        """
                List Audit Logs.

                Gets all signature events which have occurred in the over the timeframe. The time range is unbounded, but the export is capped at 100,000 rows. When the result is truncated, the `X-Dfns-Result-Truncated: true` response header is set and a trailing `# TRUNCATED ...` line is appended to the CSV; narrow the time range to retrieve all data.

        StartTime and EndTime are URL-encoded UTC ISO timestamps:
        `startTime=2025-08-29T02%3A46%3A40Z`
        `endTime=2025-09-01T02%3A46%3A40Z`

        An additional optional query parameter, `userId` can be specified to filter down events to a particular user. The API will return results found in CSV format.


        Dfns maintains a script which can be used for audit log signature validation: [WebAuthn Signature Verifier](https://github.com/dfns/dfns-sdk-python/tree/main/examples/verify-webauthn-signature)

                Args:
                    query: Query parameters.
        """  # noqa: E501
        self._http.request(
            method="GET",
            path="/auth/action/logs",
            path_params={},
            query_params=query,
            body=None,
            requires_signature=False,
        )

    def get_audit_log(self, id: str) -> T.GetAuditLogResponse:
        """
                Get Audit Log.

                Gets detailed information for a particular audit log. Specifically, the API returns the action performed, as well as the `firstFactorCredential` in which you will find the signature information required to validate it.

        Dfns maintains a script which can be used for audit log signature validation: [WebAuthn Signature Verifier](https://github.com/dfns/dfns-sdk-python/tree/main/examples/verify-webauthn-signature)

        Because the response includes the full signed action (request body and path), details are only returned for actions on routes that Dfns has marked as safe to expose (the same set forwarded to SIEM exports). Requesting details for any other event returns `403 Forbidden`.

                Args:
                    id: Log id you need information about.

                Returns:
                    T.GetAuditLogResponse: The API response.
        """  # noqa: E501
        response = self._http.request(
            method="GET",
            path="/auth/action/logs/{id}",
            path_params={"id": id},
            query_params=None,
            body=None,
            requires_signature=False,
        )
        return cast(T.GetAuditLogResponse, response)

    @deprecated("This endpoint is deprecated.")
    def list_applications(self) -> T.ListApplicationsResponse:
        """
              List Applications.

              <Warning>
        Applications are deprecated and will be removed in a future release. See details [here](https://docs.dfns.co/deprecation/applications-deprecation).
        </Warning>

              Returns:
                  T.ListApplicationsResponse: The API response.
        """  # noqa: E501
        response = self._http.request(
            method="GET",
            path="/auth/apps",
            path_params={},
            query_params=None,
            body=None,
            requires_signature=False,
        )
        return cast(T.ListApplicationsResponse, response)

    @deprecated("This endpoint is deprecated.")
    def get_application(self, app_id: str) -> T.GetApplicationResponse:
        """
              Get Application.

              <Warning>
        Applications are deprecated and will be removed in a future release. See details [here](https://docs.dfns.co/deprecation/applications-deprecation).
        </Warning>

              Args:
                  app_id: ID of the application (deprecated).

              Returns:
                  T.GetApplicationResponse: The API response.
        """  # noqa: E501
        response = self._http.request(
            method="GET",
            path="/auth/apps/{appId}",
            path_params={"appId": app_id},
            query_params=None,
            body=None,
            requires_signature=False,
        )
        return cast(T.GetApplicationResponse, response)

    def list_credentials(self) -> T.ListCredentialsResponse:
        """
        List Credentials.

        List all credentials for a user.

        Returns:
            T.ListCredentialsResponse: The API response.
        """  # noqa: E501
        response = self._http.request(
            method="GET",
            path="/auth/credentials",
            path_params={},
            query_params=None,
            body=None,
            requires_signature=False,
        )
        return cast(T.ListCredentialsResponse, response)

    def create_credential(self, body: dict[str, Any]) -> T.CreateCredentialResponse:
        """
                Create Credential.

                Part of the flow [Create Credential Regular flow](https://docs.dfns.co/api-reference/auth/credentials#regular-flow).

        Adds a new credential to a user's account. See [Credential Kinds](https://docs.dfns.co/api-reference/auth/credentials#credential-kinds) for all supported credential types.

                Args:
                    body: Request body.

                Returns:
                    T.CreateCredentialResponse: The API response.
        """  # noqa: E501
        response = self._http.request(
            method="POST",
            path="/auth/credentials",
            path_params={},
            query_params=None,
            body=body,
            requires_signature=True,
        )
        return cast(T.CreateCredentialResponse, response)

    def create_credential_challenge(self, body: T.CreateCredentialChallengeRequest) -> dict[str, Any]:
        """
              Create Credential Challenge.

              Part of the flow [Create Credential Regular flow](https://docs.dfns.co/api-reference/auth/credentials#regular-flow).

        Starts a create user credential session, returning a challenge that will be used to verify the user's identity.

              Args:
                  body: Request body.

              Returns:
                  dict[str, Any]: The API response.
        """  # noqa: E501
        response = self._http.request(
            method="POST",
            path="/auth/credentials/init",
            path_params={},
            query_params=None,
            body=body,
            requires_signature=False,
        )
        return cast(dict[str, Any], response)

    def activate_credential(self, body: T.ActivateCredentialRequest) -> T.ActivateCredentialResponse:
        """
        Activate Credential.

        Activates a credential that was previously deactivated. If the credential is already activated no action is taken.

        Args:
            body: Request body.

        Returns:
            T.ActivateCredentialResponse: The API response.
        """  # noqa: E501
        response = self._http.request(
            method="PUT",
            path="/auth/credentials/activate",
            path_params={},
            query_params=None,
            body=body,
            requires_signature=True,
        )
        return cast(T.ActivateCredentialResponse, response)

    def delete_credential(self, credential_uuid: str) -> T.DeleteCredentialResponse:
        """
        Delete Credential.

        Delete a specific credential.

        Args:
            credential_uuid: Path parameter.

        Returns:
            T.DeleteCredentialResponse: The API response.
        """  # noqa: E501
        response = self._http.request(
            method="DELETE",
            path="/auth/credentials/{credentialUuid}",
            path_params={"credentialUuid": credential_uuid},
            query_params=None,
            body=None,
            requires_signature=True,
        )
        return cast(T.DeleteCredentialResponse, response)

    def deactivate_credential(self, body: T.DeactivateCredentialRequest) -> T.DeactivateCredentialResponse:
        """
        Deactivate Credential.

        Deactivates a credential that was previously active. If the credential is already deactivated no action is taken.

        Args:
            body: Request body.

        Returns:
            T.DeactivateCredentialResponse: The API response.
        """  # noqa: E501
        response = self._http.request(
            method="PUT",
            path="/auth/credentials/deactivate",
            path_params={},
            query_params=None,
            body=body,
            requires_signature=True,
        )
        return cast(T.DeactivateCredentialResponse, response)

    def create_credential_code(self, body: T.CreateCredentialCodeRequest) -> T.CreateCredentialCodeResponse:
        """
                Create Credential Code.

                Part of the [Create Credential With Code flow](https://docs.dfns.co/api-reference/auth/credentials#create-credential-with-code-flow).

        Creates a one-time-code that can then be used to create a new credential from a place you don't have access to one of your existing credential.

                Args:
                    body: Request body.

                Returns:
                    T.CreateCredentialCodeResponse: The API response.
        """  # noqa: E501
        response = self._http.request(
            method="POST",
            path="/auth/credentials/code",
            path_params={},
            query_params=None,
            body=body,
            requires_signature=True,
        )
        return cast(T.CreateCredentialCodeResponse, response)

    def create_credential_challenge_with_code(self, body: T.CreateCredentialChallengeWithCodeRequest) -> dict[str, Any]:
        """
                Create Credential Challenge With Code.

                Part of the flow [Create Credential With Code](https://docs.dfns.co/api-reference/auth/credentials#create-credential-with-code-flow).

        Creates a credential challenge using a one time code-time-code. This challenge must then be signed by the new credential, before finalizing the flow.

                Args:
                    body: Request body.

                Returns:
                    dict[str, Any]: The API response.
        """  # noqa: E501
        response = self._http.request(
            method="POST",
            path="/auth/credentials/code/init",
            path_params={},
            query_params=None,
            body=body,
            requires_signature=False,
        )
        return cast(dict[str, Any], response)

    def create_credential_with_code(self, body: dict[str, Any]) -> T.CreateCredentialWithCodeResponse:
        """
                Create Credential With Code.

                Finalizes the flow [Create Credential With Code](https://docs.dfns.co/api-reference/auth/credentials#create-credential-with-code-flow).

        Adds a new credential to a user's account. This endpoint is similar to the [Create Credential](https://docs.dfns.co/api-reference/auth/create-credential) endpoint, except:
        * it does not need the user to be authenticated
        * it does not need user action signing
        * it will only work with the challenge gotten from the [Create Credential Challenge With Code](https://docs.dfns.co/api-reference/auth/create-credential-challenge-with-code) endpoint

                Args:
                    body: Request body.

                Returns:
                    T.CreateCredentialWithCodeResponse: The API response.
        """  # noqa: E501
        response = self._http.request(
            method="POST",
            path="/auth/credentials/code/verify",
            path_params={},
            query_params=None,
            body=body,
            requires_signature=False,
        )
        return cast(T.CreateCredentialWithCodeResponse, response)

    def create_login_challenge(self, body: T.CreateLoginChallengeRequest) -> T.CreateLoginChallengeResponse:
        """
                Create Login Challenge.

                Start a user login session, returning a challenge that will be used to verify the user's identity.

        If the user has a credential of kind `PasswordProtectedKey` a temporary one time code needs to be passed in the `loginCode` field.

        If the user has at least one discoverable WebAuthn credential, `username` is optional (username-less flow).

                Args:
                    body: Request body.

                Returns:
                    T.CreateLoginChallengeResponse: The API response.
        """  # noqa: E501
        response = self._http.request(
            method="POST",
            path="/auth/login/init",
            path_params={},
            query_params=None,
            body=body,
            requires_signature=False,
        )
        return cast(T.CreateLoginChallengeResponse, response)

    def delegated_login(self, body: T.DelegatedLoginRequest) -> T.DelegatedLoginResponse:
        """
                Delegated Login.

                <Warning>
        Only a [Service Account](https://docs.dfns.co/api-reference/auth/service-accounts) can use this endpoint.
        </Warning>

        Logs a user into an organization without the user's credentials.

        If you want to use your own authentication system, while still using `Delegated Signing`, you can use this endpoint to authenticate a user without needing the user's credentials.

        The user authentication token can be used for read operations within the Dfns API, however, write operations will still require the user to sign the action.

                Args:
                    body: Request body.

                Returns:
                    T.DelegatedLoginResponse: The API response.
        """  # noqa: E501
        response = self._http.request(
            method="POST",
            path="/auth/login/delegated",
            path_params={},
            query_params=None,
            body=body,
            requires_signature=True,
        )
        return cast(T.DelegatedLoginResponse, response)

    def login(self, body: T.LoginRequest) -> dict[str, Any]:
        """
                Complete User Login.

                Completes the login process and provides the authenticated user with their authentication token.

        The type of credentials used to login is determined by the `kind` field in the nested objects (`firstFactor` and `secondFactor`). Supported credential kinds are:
        * `Fido2`: Login challenge is signed by a user's signing device using `WebAuthn`.
        * `Key`: Login challenge is signed by a user's private key.
        * `PasswordProtectedKey`: Login challenge is signed by the decrypted user's private key that was sent during the [Create Login Challenge](https://docs.dfns.co/api-reference/auth/create-login-challenge) step.

                Args:
                    body: Request body.

                Returns:
                    dict[str, Any]: The API response.
        """  # noqa: E501
        response = self._http.request(
            method="POST",
            path="/auth/login",
            path_params={},
            query_params=None,
            body=body,
            requires_signature=False,
        )
        return cast(dict[str, Any], response)

    @deprecated("Use login instead.")
    def complete_user_login(self, body: T.LoginRequest) -> dict[str, Any]:
        """Deprecated: use login instead."""
        return self.login(body=body)

    def logout(self, body: T.LogoutRequest) -> T.LogoutResponse:
        """
        Logout.

        Completes the user logout process.

        Args:
            body: Request body.

        Returns:
            T.LogoutResponse: The API response.
        """  # noqa: E501
        response = self._http.request(
            method="PUT",
            path="/auth/logout",
            path_params={},
            query_params=None,
            body=body,
            requires_signature=False,
        )
        return cast(T.LogoutResponse, response)

    def oidc_login_credentials(self, body: dict[str, Any]) -> T.OidcLoginCredentialsResponse:
        """
        Oidc Login Credentials.

        Registers the first credential for an OIDC-authenticated user, bootstrapping from the credential challenge issued by [Complete OIDC Login](/api-reference/auth/complete-oidc-login). Rejected if the user already has an active first-factor credential; use [Create Credential](/api-reference/auth/create-credential) in that case.

        Args:
            body: Request body.

        Returns:
            T.OidcLoginCredentialsResponse: The API response.
        """  # noqa: E501
        response = self._http.request(
            method="POST",
            path="/auth/login/oidc/credentials",
            path_params={},
            query_params=None,
            body=body,
            requires_signature=False,
        )
        return cast(T.OidcLoginCredentialsResponse, response)

    def oidc_login(self, body: T.OidcLoginRequest) -> T.OidcLoginResponse:
        """
        Complete OIDC Login.

        Completes the OIDC login process by exchanging the authorization code obtained from the identity provider. Returns the user's authentication token; when the verified user has no active first-factor credential yet, the response also includes a credential challenge so the client can register one before performing any user-action-signed operation.

        Args:
            body: Request body.

        Returns:
            T.OidcLoginResponse: The API response.
        """  # noqa: E501
        response = self._http.request(
            method="POST",
            path="/auth/login/oidc",
            path_params={},
            query_params=None,
            body=body,
            requires_signature=False,
        )
        return cast(T.OidcLoginResponse, response)

    @deprecated("Use oidc_login instead.")
    def complete_oidc_login(self, body: T.OidcLoginRequest) -> T.OidcLoginResponse:
        """Deprecated: use oidc_login instead."""
        return self.oidc_login(body=body)

    def oidc_login_init(self, body: T.OidcLoginInitRequest) -> T.OidcLoginInitResponse:
        """
        Initiate OIDC Login.

        Initialize the OIDC login process by returning the identity provider authorization URL to redirect the user to.

        Args:
            body: Request body.

        Returns:
            T.OidcLoginInitResponse: The API response.
        """  # noqa: E501
        response = self._http.request(
            method="POST",
            path="/auth/login/oidc/init",
            path_params={},
            query_params=None,
            body=body,
            requires_signature=False,
        )
        return cast(T.OidcLoginInitResponse, response)

    @deprecated("Use oidc_login_init instead.")
    def initiate_oidc_login(self, body: T.OidcLoginInitRequest) -> T.OidcLoginInitResponse:
        """Deprecated: use oidc_login_init instead."""
        return self.oidc_login_init(body=body)

    def send_login_code(self, body: T.SendLoginCodeRequest) -> T.SendLoginCodeResponse:
        """
                Send Login Code.

                Sends a temporary one time code to the user that can be used during login flow.

        If the user has a credential of kind `PasswordProtectedKey` a temporary one time code needs to be passed in the `loginCode` field. That's because the [Create Login Challenge](https://docs.dfns.co/api-reference/auth/create-login-challenge) is unauthenticated and returns the encrypted private key of the user. So we need a first step to verify the identity of the user to prevent anybody from fetching the encrypted private key and trying to brute force it offline.

                Args:
                    body: Request body.

                Returns:
                    T.SendLoginCodeResponse: The API response.
        """  # noqa: E501
        response = self._http.request(
            method="POST",
            path="/auth/login/code",
            path_params={},
            query_params=None,
            body=body,
            requires_signature=False,
        )
        return cast(T.SendLoginCodeResponse, response)

    def social_login(self, body: T.SocialLoginRequest) -> T.SocialLoginResponse:
        """
        Social Login.

        Logs a user in with a JWT id token issued by a social login provider and provides the authenticated user with their authentication token.

        Args:
            body: Request body.

        Returns:
            T.SocialLoginResponse: The API response.
        """  # noqa: E501
        response = self._http.request(
            method="POST",
            path="/auth/login/social",
            path_params={},
            query_params=None,
            body=body,
            requires_signature=False,
        )
        return cast(T.SocialLoginResponse, response)

    def sso_login(self, body: T.SsoLoginRequest) -> T.SsoLoginResponse:
        """
        Complete SSO Login.

        Completes the SSO login process by exchanging the authorization code obtained from the identity provider for the user's authentication token.

        Args:
            body: Request body.

        Returns:
            T.SsoLoginResponse: The API response.
        """  # noqa: E501
        response = self._http.request(
            method="POST",
            path="/auth/login/sso",
            path_params={},
            query_params=None,
            body=body,
            requires_signature=False,
        )
        return cast(T.SsoLoginResponse, response)

    @deprecated("Use sso_login instead.")
    def complete_sso_login(self, body: T.SsoLoginRequest) -> T.SsoLoginResponse:
        """Deprecated: use sso_login instead."""
        return self.sso_login(body=body)

    def sso_login_init(self, body: T.SsoLoginInitRequest) -> T.SsoLoginInitResponse:
        """
        Initiate SSO Login.

        Initialize the login process with SSO by returning the IdP URL to call.

        Args:
            body: Request body.

        Returns:
            T.SsoLoginInitResponse: The API response.
        """  # noqa: E501
        response = self._http.request(
            method="POST",
            path="/auth/login/sso/init",
            path_params={},
            query_params=None,
            body=body,
            requires_signature=False,
        )
        return cast(T.SsoLoginInitResponse, response)

    @deprecated("Use sso_login_init instead.")
    def initiate_sso_login(self, body: T.SsoLoginInitRequest) -> T.SsoLoginInitResponse:
        """Deprecated: use sso_login_init instead."""
        return self.sso_login_init(body=body)

    def exchange_access_token(self, body: T.ExchangeAccessTokenRequest) -> T.ExchangeAccessTokenResponse:
        """
        Exchange Access Token.

        Only for TenantUsers - Exchanges the current user access token, for an org-bound or tenant-bound token. The user must have access to the target org / tenant. The new access token expiration won't exceed the current token's one.

        Args:
            body: Request body.

        Returns:
            T.ExchangeAccessTokenResponse: The API response.
        """  # noqa: E501
        response = self._http.request(
            method="POST",
            path="/auth/tokens",
            path_params={},
            query_params=None,
            body=body,
            requires_signature=False,
        )
        return cast(T.ExchangeAccessTokenResponse, response)

    def list_personal_access_tokens(self) -> T.ListPersonalAccessTokensResponse:
        """
        List Personal Access Tokens.

        Retrieve the list of your Personal Access Tokens.

        Returns:
            T.ListPersonalAccessTokensResponse: The API response.
        """  # noqa: E501
        response = self._http.request(
            method="GET",
            path="/auth/pats",
            path_params={},
            query_params=None,
            body=None,
            requires_signature=False,
        )
        return cast(T.ListPersonalAccessTokensResponse, response)

    def create_personal_access_token(
        self, body: T.CreatePersonalAccessTokenRequest
    ) -> T.CreatePersonalAccessTokenResponse:
        """
        Create Personal Access Token.

        Create a new Personal Access Token for the caller.

        Args:
            body: Request body.

        Returns:
            T.CreatePersonalAccessTokenResponse: The API response.
        """  # noqa: E501
        response = self._http.request(
            method="POST",
            path="/auth/pats",
            path_params={},
            query_params=None,
            body=body,
            requires_signature=True,
        )
        return cast(T.CreatePersonalAccessTokenResponse, response)

    def get_personal_access_token(self, token_id: str) -> T.GetPersonalAccessTokenResponse:
        """
        Get Personal Access Token.

        Retrieve a specific Personal Access Token.

        Args:
            token_id: Token id.

        Returns:
            T.GetPersonalAccessTokenResponse: The API response.
        """  # noqa: E501
        response = self._http.request(
            method="GET",
            path="/auth/pats/{tokenId}",
            path_params={"tokenId": token_id},
            query_params=None,
            body=None,
            requires_signature=False,
        )
        return cast(T.GetPersonalAccessTokenResponse, response)

    def update_personal_access_token(
        self, token_id: str, body: T.UpdatePersonalAccessTokenRequest
    ) -> T.UpdatePersonalAccessTokenResponse:
        """
        Update Personal Access Token.

        Update a specific Personal Access Token.

        Args:
            token_id: Token id.
            body: Request body.

        Returns:
            T.UpdatePersonalAccessTokenResponse: The API response.
        """  # noqa: E501
        response = self._http.request(
            method="PUT",
            path="/auth/pats/{tokenId}",
            path_params={"tokenId": token_id},
            query_params=None,
            body=body,
            requires_signature=True,
        )
        return cast(T.UpdatePersonalAccessTokenResponse, response)

    def delete_personal_access_token(self, token_id: str) -> T.DeletePersonalAccessTokenResponse:
        """
        Delete Personal Access Token.

        Delete a specific Personal Access Token.

        Args:
            token_id: Token id.

        Returns:
            T.DeletePersonalAccessTokenResponse: The API response.
        """  # noqa: E501
        response = self._http.request(
            method="DELETE",
            path="/auth/pats/{tokenId}",
            path_params={"tokenId": token_id},
            query_params=None,
            body=None,
            requires_signature=True,
        )
        return cast(T.DeletePersonalAccessTokenResponse, response)

    def activate_personal_access_token(self, token_id: str) -> T.ActivatePersonalAccessTokenResponse:
        """
        Activate Personal Access Token.

        Activate a specific Personal Access Token.

        Args:
            token_id: Token id.

        Returns:
            T.ActivatePersonalAccessTokenResponse: The API response.
        """  # noqa: E501
        response = self._http.request(
            method="PUT",
            path="/auth/pats/{tokenId}/activate",
            path_params={"tokenId": token_id},
            query_params=None,
            body=None,
            requires_signature=True,
        )
        return cast(T.ActivatePersonalAccessTokenResponse, response)

    def deactivate_personal_access_token(self, token_id: str) -> T.DeactivatePersonalAccessTokenResponse:
        """
        Deactivate Personal Access Token.

        Deactivates a personal access token that was previously active. If the token is already deactivated no action is taken.

        Args:
            token_id: Token id.

        Returns:
            T.DeactivatePersonalAccessTokenResponse: The API response.
        """  # noqa: E501
        response = self._http.request(
            method="PUT",
            path="/auth/pats/{tokenId}/deactivate",
            path_params={"tokenId": token_id},
            query_params=None,
            body=None,
            requires_signature=True,
        )
        return cast(T.DeactivatePersonalAccessTokenResponse, response)

    def create_delegated_recovery_challenge(
        self, body: T.CreateDelegatedRecoveryChallengeRequest
    ) -> T.CreateDelegatedRecoveryChallengeResponse:
        """
                Create Delegated Recovery Challenge.

                <Warning>
        Only a [Service Account](https://docs.dfns.co/api-reference/auth/service-accounts) can use this endpoint.
        </Warning>

        Starts a recovery session for a user under your brand, without sending a Dfns recovery email. Call this after you have verified the user's identity with your own auth system.

        The response returns a recovery challenge. Pass it to your frontend so the user can decrypt their recovery credential and sign, then call [Recover User](https://docs.dfns.co/api-reference/auth/recover-user) to complete the recovery and register fresh credentials.

        <Note>This endpoint is for users that registered through the "Delegated" registration flow. For users registered through the "Direct" registration flow, the endpoints [Send Recovery Code Email](https://docs.dfns.co/api-reference/auth/send-recovery-code-email) + [Create Recovery Challenge](https://docs.dfns.co/api-reference/auth/create-recovery-challenge) should be used.</Note>

                Args:
                    body: Request body.

                Returns:
                    T.CreateDelegatedRecoveryChallengeResponse: The API response.
        """  # noqa: E501
        response = self._http.request(
            method="POST",
            path="/auth/recover/user/delegated",
            path_params={},
            query_params=None,
            body=body,
            requires_signature=True,
        )
        return cast(T.CreateDelegatedRecoveryChallengeResponse, response)

    def recover(self, body: T.RecoverRequest) -> T.RecoverResponse:
        """
                Recover User.

                Recovers a user, using a recovery credential. After successfully recovering the user, all of the user's previous credentials and personal access tokens will be invalidated.

        This flow requires cryptographic validation of newly created credential(s) using a recovery credential. The `recovery.credentialAssertion.clientData` field's challenge must be the _base64url-encoded_ representation of the `newCredential` object.

        The process is as follows:

        1. Construct the `newCredential` object, using the challenge obtained from either the [Create Recovery Challenge](https://docs.dfns.co/api-reference/auth/create-recovery-challenge) or [Create Delegated Recovery Challenge](https://docs.dfns.co/api-reference/auth/create-delegated-recovery-challenge) endpoints.
        2. Serialize the `newCredential` object to JSON and then base64url-encode the resulting JSON string. This _base64url-encoded_ string will serve as the challenge for the `recovery.credentialAssertion` object.
        3. Construct the `recovery.credentialAssertion` object, using the _base64url-encoded_ string generated in step 2 as its challenge.

                Args:
                    body: Request body.

                Returns:
                    T.RecoverResponse: The API response.
        """  # noqa: E501
        response = self._http.request(
            method="POST",
            path="/auth/recover/user",
            path_params={},
            query_params=None,
            body=body,
            requires_signature=False,
        )
        return cast(T.RecoverResponse, response)

    @deprecated("Use recover instead.")
    def recover_user(self, body: T.RecoverRequest) -> T.RecoverResponse:
        """Deprecated: use recover instead."""
        return self.recover(body=body)

    def create_recovery_challenge(self, body: T.CreateRecoveryChallengeRequest) -> T.CreateRecoveryChallengeResponse:
        """
                Create Recovery Challenge.

                Starts a user recovery session from the recovery code received by email. It returns a challenge that will be used to verify the user's identity.

        <Note>This endpoint is for users that registered through the "Direct" registration flow. For users registered through the "Delegated" registration flow, the endpoint [Create Delegated Recovery Challenge](https://docs.dfns.co/api-reference/auth/create-delegated-recovery-challenge) should be used.</Note>

                Args:
                    body: Request body.

                Returns:
                    T.CreateRecoveryChallengeResponse: The API response.
        """  # noqa: E501
        response = self._http.request(
            method="POST",
            path="/auth/recover/user/init",
            path_params={},
            query_params=None,
            body=body,
            requires_signature=False,
        )
        return cast(T.CreateRecoveryChallengeResponse, response)

    def send_recovery_code(self, body: T.SendRecoveryCodeRequest) -> T.SendRecoveryCodeResponse:
        """
              Send Recovery Code Email.

              Send the user a recovery verification code. This code is used as a second factor to verify the user initiated the recovery request.

        <Note>This endpoint is for users that registered through the "Direct" registration flow. For users registered through the "Delegated" registration flow, the endpoint [Create Delegated Recovery Challenge](https://docs.dfns.co/api-reference/auth/create-delegated-recovery-challenge) should be used.</Note>

              Args:
                  body: Request body.

              Returns:
                  T.SendRecoveryCodeResponse: The API response.
        """  # noqa: E501
        response = self._http.request(
            method="POST",
            path="/auth/recover/user/code",
            path_params={},
            query_params=None,
            body=body,
            requires_signature=False,
        )
        return cast(T.SendRecoveryCodeResponse, response)

    @deprecated("Use send_recovery_code instead.")
    def send_recovery_code_email(self, body: T.SendRecoveryCodeRequest) -> T.SendRecoveryCodeResponse:
        """Deprecated: use send_recovery_code instead."""
        return self.send_recovery_code(body=body)

    def create_delegated_registration_challenge(
        self, body: T.CreateDelegatedRegistrationChallengeRequest
    ) -> T.CreateDelegatedRegistrationChallengeResponse:
        """
                Create Delegated Registration Challenge.

                <Warning>
        Only a [Service Account](https://docs.dfns.co/api-reference/auth/service-accounts) can use this endpoint.
        </Warning>

        Returns a registration challenge for the targeted user, which can be passed to the user for passkey creation and registration completion.

        The response includes:
        - Basic info about the targeted user
        - A registration challenge
        - A `temporaryAuthenticationToken` to authenticate the next request in the flow

        Next steps are
        1. pass the challenge to your user in your frontend / app, so he can create new passkey & recovery credentials and sign the challenge with it. All credentials registered need to sign this challenge. See [Implement end-user recovery](https://docs.dfns.co/guides/developers/end-user-recovery).
        2. then call [Complete User Registration](https://docs.dfns.co/api-reference/auth/complete-user-registration) or [Complete End User Registration with Wallets](https://docs.dfns.co/api-reference/auth/complete-end-user-registration-with-wallets) with that signed challenge, using the `temporaryAuthenticationToken` as Bearer token.

        <Note>
        This endpoint is for users previously created through [Create User](https://docs.dfns.co/api-reference/auth/create-user) endpoint with `registration: 'Delegated'`(*).

        _(*) Legacy behaviour - still supported:_

        If you target an `EndUser`, which was not previously created with "Create User" endpoint, then this end user will be created on-the-fly within this endpoint.
        If you previously relied on this behaviour, update your code, before this legacy behaviour deprecation. Instead, you should call the "Create User" endpoint first, passing `registration: "Delegated"`, after which you can call this endpoint.
        </Note>

                Args:
                    body: Request body.

                Returns:
                    T.CreateDelegatedRegistrationChallengeResponse: The API response.
        """  # noqa: E501
        response = self._http.request(
            method="POST",
            path="/auth/registration/delegated",
            path_params={},
            query_params=None,
            body=body,
            requires_signature=True,
        )
        return cast(T.CreateDelegatedRegistrationChallengeResponse, response)

    def create_registration_challenge(
        self, body: T.CreateRegistrationChallengeRequest
    ) -> T.CreateRegistrationChallengeResponse:
        """
                Create Registration Challenge.

                Starts a user registration session from the registration code received by email. It returns a challenge that will need to be signed by a passkey and used to perform the step [Complete User Registration](/api-reference/auth/complete-user-registration). Either `orgId` or `tenantId` needs to be specified.

        <Note>
        This endpoint is for users previously created through [Create User](https://docs.dfns.co/api-reference/auth/create-user) endpoint with `registration: "Direct"`, and received a registration code by email.
        </Note>

                Args:
                    body: Request body.

                Returns:
                    T.CreateRegistrationChallengeResponse: The API response.
        """  # noqa: E501
        response = self._http.request(
            method="POST",
            path="/auth/registration/init",
            path_params={},
            query_params=None,
            body=body,
            requires_signature=False,
        )
        return cast(T.CreateRegistrationChallengeResponse, response)

    def create_social_registration_challenge(
        self, body: T.CreateSocialRegistrationChallengeRequest
    ) -> T.CreateSocialRegistrationChallengeResponse:
        """
        Create Social Registration Challenge.

        Starts an end-user registration session by passing a JWT obtained by an IdP. It returns a challenge that will need to be signed by a passkey and used to perform [Complete End User Registration with Wallets](/api-reference/auth/complete-end-user-registration-with-wallets).

        Args:
            body: Request body.

        Returns:
            T.CreateSocialRegistrationChallengeResponse: The API response.
        """  # noqa: E501
        response = self._http.request(
            method="POST",
            path="/auth/registration/social",
            path_params={},
            query_params=None,
            body=body,
            requires_signature=False,
        )
        return cast(T.CreateSocialRegistrationChallengeResponse, response)

    def register(self, body: T.RegisterRequest) -> T.RegisterResponse:
        """
                Complete User Registration.

                Completes the user registration process and creates the user's initial credentials.

        All credentials submitted in this call (`firstFactorCredential`, `secondFactorCredential`, `recoveryCredential`) sign the same challenge returned by the registration init endpoint ([Create Registration Challenge](https://docs.dfns.co/api-reference/auth/create-registration-challenge), [Create Delegated Registration Challenge](https://docs.dfns.co/api-reference/auth/create-delegated-registration-challenge), or [Create Social Registration Challenge](https://docs.dfns.co/api-reference/auth/create-social-registration-challenge)).

        Always include a `recoveryCredential` for end users. Without one, a user who loses their device cannot recover access and you must initiate a delegated recovery manually. See [Implement end-user recovery](https://docs.dfns.co/guides/developers/end-user-recovery).

        The type of credentials being registered is determined by the `credentialKind` field in the nested objects (`firstFactorCredential` , `secondFactorCredential` and `recoveryCredential`). Supported credential kinds are:
        * `Fido2`: User action is signed by a user's signing device using `WebAuthn`.
        * `Key`: User action is signed by a user's, or token's, private key.
        * `PasswordProtectedKey`: User action is signed by a user's, or token's, private key. The encrypted version of the private key is stored by Dfns and returns during the signing flow for the user to decrypt it.
        * `RecoveryKey` : Similar to `PasswordProtectedKey`, but this credential can only be used to recover an account not to sign an action or login. Once this credential is used all the other user's credentials are invalidated.

                Args:
                    body: Request body.

                Returns:
                    T.RegisterResponse: The API response.
        """  # noqa: E501
        response = self._http.request(
            method="POST",
            path="/auth/registration",
            path_params={},
            query_params=None,
            body=body,
            requires_signature=False,
        )
        return cast(T.RegisterResponse, response)

    @deprecated("Use register instead.")
    def complete_user_registration(self, body: T.RegisterRequest) -> T.RegisterResponse:
        """Deprecated: use register instead."""
        return self.register(body=body)

    def register_end_user(self, body: T.RegisterEndUserRequest) -> T.RegisterEndUserResponse:
        """
                Complete End User Registration with Wallets.

                Completes the end user registration process and creates the user's initial credentials along with delegated wallets for the new end user.

        All credentials submitted in this call (`firstFactorCredential`, `secondFactorCredential`, `recoveryCredential`) sign the same challenge returned by the registration init endpoint ([Create Delegated Registration Challenge](https://docs.dfns.co/api-reference/auth/create-delegated-registration-challenge) or [Create Social Registration Challenge](https://docs.dfns.co/api-reference/auth/create-social-registration-challenge)).

        Always include a `recoveryCredential` for end users. Without one, a user who loses their device cannot recover access and you must initiate a delegated recovery manually. See [Implement end-user recovery](https://docs.dfns.co/guides/developers/end-user-recovery).

        The type of credentials being registered is determined by the `credentialKind` field in the nested objects (`firstFactorCredential` , `secondFactorCredential` and `recoveryCredential`). Supported credential kinds are:
        * `Fido2`: User action is signed by a user's signing device using `WebAuthn`.
        * `Key`: User action is signed by a user's, or token's, private key.
        * `PasswordProtectedKey`: User action is signed by a user's, or token's, private key. The encrypted version of the private key is stored by Dfns and returns during the signing flow for the user to decrypt it.
        * `RecoveryKey`: Similar to `PasswordProtectedKey`, but this credential can only be used to recover an account, not to sign an action or login. Once this credential is used, all the other user's credentials are invalidated.

        The number of delegated wallets created and the wallet types are determined by the `wallets` specifications. The end user is automatically assigned `ManagedDefaultEndUserAccess` managed permission that grants the end user full access to the wallets.

                Args:
                    body: Request body.

                Returns:
                    T.RegisterEndUserResponse: The API response.
        """  # noqa: E501
        response = self._http.request(
            method="POST",
            path="/auth/registration/enduser",
            path_params={},
            query_params=None,
            body=body,
            requires_signature=False,
        )
        return cast(T.RegisterEndUserResponse, response)

    @deprecated("Use register_end_user instead.")
    def complete_end_user_registration_with_wallets(self, body: T.RegisterEndUserRequest) -> T.RegisterEndUserResponse:
        """Deprecated: use register_end_user instead."""
        return self.register_end_user(body=body)

    def resend_registration_code(self, body: T.ResendRegistrationCodeRequest) -> T.ResendRegistrationCodeResponse:
        """
                Resend Registration Code.

                Sends the user a new registration code. The previous registration code will be marked invalid. If the user has already completed their registration no action will be taken.

        <Note>
        This endpoint is for users previously created through [Create User](https://docs.dfns.co/api-reference/auth/create-user) endpoint with `registration: "Direct"`, and received a registration code by email.
        </Note>

                Args:
                    body: Request body.

                Returns:
                    T.ResendRegistrationCodeResponse: The API response.
        """  # noqa: E501
        response = self._http.request(
            method="PUT",
            path="/auth/registration/code",
            path_params={},
            query_params=None,
            body=body,
            requires_signature=False,
        )
        return cast(T.ResendRegistrationCodeResponse, response)

    def list_service_accounts(self) -> T.ListServiceAccountsResponse:
        """
        List Service Accounts.

        List all Service Accounts in your organization.

        Returns:
            T.ListServiceAccountsResponse: The API response.
        """  # noqa: E501
        response = self._http.request(
            method="GET",
            path="/auth/service-accounts",
            path_params={},
            query_params=None,
            body=None,
            requires_signature=False,
        )
        return cast(T.ListServiceAccountsResponse, response)

    def create_service_account(self, body: T.CreateServiceAccountRequest) -> T.CreateServiceAccountResponse:
        """
        Create Service Account.

        Create a new Service Account for your organization.

        Args:
            body: Request body.

        Returns:
            T.CreateServiceAccountResponse: The API response.
        """  # noqa: E501
        response = self._http.request(
            method="POST",
            path="/auth/service-accounts",
            path_params={},
            query_params=None,
            body=body,
            requires_signature=True,
        )
        return cast(T.CreateServiceAccountResponse, response)

    def get_service_account(self, service_account_id: str) -> T.GetServiceAccountResponse:
        """
        Get Service Account.

        Get information about a specific Service Account.

        Args:
            service_account_id: ID of the service account.

        Returns:
            T.GetServiceAccountResponse: The API response.
        """  # noqa: E501
        response = self._http.request(
            method="GET",
            path="/auth/service-accounts/{serviceAccountId}",
            path_params={"serviceAccountId": service_account_id},
            query_params=None,
            body=None,
            requires_signature=False,
        )
        return cast(T.GetServiceAccountResponse, response)

    def update_service_account(
        self, service_account_id: str, body: T.UpdateServiceAccountRequest
    ) -> T.UpdateServiceAccountResponse:
        """
        Update Service Account.

        Update a specific Service Account.

        Args:
            service_account_id: ID of the service account.
            body: Request body.

        Returns:
            T.UpdateServiceAccountResponse: The API response.
        """  # noqa: E501
        response = self._http.request(
            method="PUT",
            path="/auth/service-accounts/{serviceAccountId}",
            path_params={"serviceAccountId": service_account_id},
            query_params=None,
            body=body,
            requires_signature=True,
        )
        return cast(T.UpdateServiceAccountResponse, response)

    def delete_service_account(
        self, service_account_id: str, query: T.DeleteServiceAccountQuery | None = None
    ) -> T.DeleteServiceAccountResponse:
        """
        Delete Service Account.

        Delete a specific Service Account.

        Args:
            service_account_id: ID of the service account.
            query: Query parameters.

        Returns:
            T.DeleteServiceAccountResponse: The API response.
        """  # noqa: E501
        response = self._http.request(
            method="DELETE",
            path="/auth/service-accounts/{serviceAccountId}",
            path_params={"serviceAccountId": service_account_id},
            query_params=query,
            body=None,
            requires_signature=True,
        )
        return cast(T.DeleteServiceAccountResponse, response)

    def activate_service_account(self, service_account_id: str) -> T.ActivateServiceAccountResponse:
        """
        Activate Service Account.

        Re-activate a previously deactivated Service Account. New Service Accounts are active as soon as they are created, so this is only needed after a Service Account has been deactivated.

        Args:
            service_account_id: ID of the service account.

        Returns:
            T.ActivateServiceAccountResponse: The API response.
        """  # noqa: E501
        response = self._http.request(
            method="PUT",
            path="/auth/service-accounts/{serviceAccountId}/activate",
            path_params={"serviceAccountId": service_account_id},
            query_params=None,
            body=None,
            requires_signature=True,
        )
        return cast(T.ActivateServiceAccountResponse, response)

    def deactivate_service_account(
        self, service_account_id: str, body: T.DeactivateServiceAccountRequest
    ) -> T.DeactivateServiceAccountResponse:
        """
        Deactivate Service Account.

        Deactivate a specific Service Account.

        Args:
            service_account_id: ID of the service account.
            body: Request body.

        Returns:
            T.DeactivateServiceAccountResponse: The API response.
        """  # noqa: E501
        response = self._http.request(
            method="PUT",
            path="/auth/service-accounts/{serviceAccountId}/deactivate",
            path_params={"serviceAccountId": service_account_id},
            query_params=None,
            body=body,
            requires_signature=True,
        )
        return cast(T.DeactivateServiceAccountResponse, response)

    def create_service_account_credential(
        self, body: T.CreateServiceAccountCredentialRequest
    ) -> T.CreateServiceAccountCredentialResponse:
        """
        Create Service Account Credential.

        Add a new Key credential to the OIDC service account authenticated by this request. The caller must be an OIDC service account — the IdP access token identifies the SA; the user-action is signed with an existing active credential to prove rotation authority.

        Args:
            body: Request body.

        Returns:
            T.CreateServiceAccountCredentialResponse: The API response.
        """  # noqa: E501
        response = self._http.request(
            method="POST",
            path="/auth/service-accounts/credentials",
            path_params={},
            query_params=None,
            body=body,
            requires_signature=True,
        )
        return cast(T.CreateServiceAccountCredentialResponse, response)

    def delete_service_account_credential(self, credential_uuid: str) -> T.DeleteServiceAccountCredentialResponse:
        """
        Delete Service Account Credential.

        Delete a credential of the OIDC service account authenticated by this request. The caller must be an OIDC service account. At least one active credential must remain after the delete.

        Args:
            credential_uuid: Path parameter.

        Returns:
            T.DeleteServiceAccountCredentialResponse: The API response.
        """  # noqa: E501
        response = self._http.request(
            method="DELETE",
            path="/auth/service-accounts/credentials/{credentialUuid}",
            path_params={"credentialUuid": credential_uuid},
            query_params=None,
            body=None,
            requires_signature=True,
        )
        return cast(T.DeleteServiceAccountCredentialResponse, response)

    def activate_user(self, user_id: str) -> T.ActivateUserResponse:
        """
        Activate User.

        Activate a specific User.

        Args:
            user_id: User id.

        Returns:
            T.ActivateUserResponse: The API response.
        """  # noqa: E501
        response = self._http.request(
            method="PUT",
            path="/auth/users/{userId}/activate",
            path_params={"userId": user_id},
            query_params=None,
            body=None,
            requires_signature=True,
        )
        return cast(T.ActivateUserResponse, response)

    def deactivate_user(self, user_id: str, body: T.DeactivateUserRequest) -> T.DeactivateUserResponse:
        """
        Deactivate User.

        Deactivate a specific User.

        Args:
            user_id: User id.
            body: Request body.

        Returns:
            T.DeactivateUserResponse: The API response.
        """  # noqa: E501
        response = self._http.request(
            method="PUT",
            path="/auth/users/{userId}/deactivate",
            path_params={"userId": user_id},
            query_params=None,
            body=body,
            requires_signature=True,
        )
        return cast(T.DeactivateUserResponse, response)

    def get_user(self, user_id: str) -> T.GetUserResponse:
        """
        Get User.

        Retrieve information about a specific User.

        Args:
            user_id: User id.

        Returns:
            T.GetUserResponse: The API response.
        """  # noqa: E501
        response = self._http.request(
            method="GET",
            path="/auth/users/{userId}",
            path_params={"userId": user_id},
            query_params=None,
            body=None,
            requires_signature=False,
        )
        return cast(T.GetUserResponse, response)

    def update_user(self, user_id: str, body: T.UpdateUserRequest) -> T.UpdateUserResponse:
        """
        Update User.

        Update a specific User.

        Args:
            user_id: User id.
            body: Request body.

        Returns:
            T.UpdateUserResponse: The API response.
        """  # noqa: E501
        response = self._http.request(
            method="PUT",
            path="/auth/users/{userId}",
            path_params={"userId": user_id},
            query_params=None,
            body=body,
            requires_signature=True,
        )
        return cast(T.UpdateUserResponse, response)

    def delete_user(self, user_id: str) -> T.DeleteUserResponse:
        """
        Delete User.

        Delete a specific User.

        Args:
            user_id: User id.

        Returns:
            T.DeleteUserResponse: The API response.
        """  # noqa: E501
        response = self._http.request(
            method="DELETE",
            path="/auth/users/{userId}",
            path_params={"userId": user_id},
            query_params=None,
            body=None,
            requires_signature=True,
        )
        return cast(T.DeleteUserResponse, response)

    def list_users(self, query: T.ListUsersQuery | None = None) -> T.ListUsersResponse:
        """
        List Users.

        List all Users in your organization.

        Args:
            query: Query parameters.

        Returns:
            T.ListUsersResponse: The API response.
        """  # noqa: E501
        response = self._http.request(
            method="GET",
            path="/auth/users",
            path_params={},
            query_params=query,
            body=None,
            requires_signature=False,
        )
        return cast(T.ListUsersResponse, response)

    def create_user(self, body: T.CreateUserRequest) -> T.CreateUserResponse:
        """
                Create User.

                Creates a new user in the caller's org.

        The registration flow this user will go through depends on the `registration` kind specified:
        - If `Direct`, we orchestrate the user's registration: he will receive an email from us directly. Then be redirected to our dashboard to finish registration and onboard there. This is only available for `CustomerEmployee`. This is for users meant to use our dashboard directly (in addition to custom apps you may build).
        - if `Delegated`, you orchestrate the user's registration: he won't receive an email from us. It's your responsibility to verify your user's identity & email, before you programmatically kick-off their registration (cf [Delegated Registration doc](https://docs.dfns.co/api-reference/auth/registration-flows#delegated-users-registration-flow)). This is available for either `CustomerEmployee` or `EndUser`. This is for users meant to only use your own apps (not our dashboard), who should not interact with us directly.

        If `registration` is unspecified, the default behaviour depends on the user kind:
        - `CustomerEmployee`: defaults to `Direct` registration: sends a registration email from us.
        - `EndUser`: defaults to `Delegated` registration (only option for those): does not send a registration email.

        Permission-wise, when the new user gets created:
        - `CustomerEmployee` hold no permissions upon creation. Use permission endpoints to grant some.
        - `EndUser` hold the default `ManagedDefaultEndUserAccess` which is granted by default to all EndUsers. Use permission endpoints to update this default end-user permission. (cf [Managed Permissions](https://docs.dfns.co/core-concepts/roles-and-permissions#manageddefaultenduseraccess))

                Args:
                    body: Request body.

                Returns:
                    T.CreateUserResponse: The API response.
        """  # noqa: E501
        response = self._http.request(
            method="POST",
            path="/auth/users",
            path_params={},
            query_params=None,
            body=body,
            requires_signature=True,
        )
        return cast(T.CreateUserResponse, response)

    def invite_tenant_user(self, body: T.InviteTenantUserRequest) -> T.InviteTenantUserResponse:
        """
        Invite Tenant User.

        Invite an existing Tenant User in the caller's org. The invited Tenant User starts without any permissions within the org.

        Args:
            body: Request body.

        Returns:
            T.InviteTenantUserResponse: The API response.
        """  # noqa: E501
        response = self._http.request(
            method="POST",
            path="/auth/users/invite",
            path_params={},
            query_params=None,
            body=body,
            requires_signature=True,
        )
        return cast(T.InviteTenantUserResponse, response)

    def list_user_groups(self, query: T.ListUserGroupsQuery | None = None) -> T.ListUserGroupsResponse:
        """
        List User Groups.

        List the user groups in the caller's org.

        Args:
            query: Query parameters.

        Returns:
            T.ListUserGroupsResponse: The API response.
        """  # noqa: E501
        response = self._http.request(
            method="GET",
            path="/auth/user-groups",
            path_params={},
            query_params=query,
            body=None,
            requires_signature=False,
        )
        return cast(T.ListUserGroupsResponse, response)

    def create_user_group(self, body: T.CreateUserGroupRequest) -> T.CreateUserGroupResponse:
        """
        Create User Group.

        Create a user group in the caller's org. A group holds permissions through the regular permission assignment endpoint, and its members hold those permissions in addition to their own.

        Args:
            body: Request body.

        Returns:
            T.CreateUserGroupResponse: The API response.
        """  # noqa: E501
        response = self._http.request(
            method="POST",
            path="/auth/user-groups",
            path_params={},
            query_params=None,
            body=body,
            requires_signature=True,
        )
        return cast(T.CreateUserGroupResponse, response)

    def get_user_group(self, user_group_id: str) -> T.GetUserGroupResponse:
        """
        Get User Group.

        Get a specific user group.

        Args:
            user_group_id: User group id.

        Returns:
            T.GetUserGroupResponse: The API response.
        """  # noqa: E501
        response = self._http.request(
            method="GET",
            path="/auth/user-groups/{userGroupId}",
            path_params={"userGroupId": user_group_id},
            query_params=None,
            body=None,
            requires_signature=False,
        )
        return cast(T.GetUserGroupResponse, response)

    def update_user_group(self, user_group_id: str, body: T.UpdateUserGroupRequest) -> T.UpdateUserGroupResponse:
        """
        Update User Group.

        Rename a user group or change its description. Fields left out keep their value. Its permissions and members are unaffected. Returns the group on success (200), or the pending user action if a policy requires approval (202).

        Args:
            user_group_id: User group id.
            body: Request body.

        Returns:
            T.UpdateUserGroupResponse: The API response.
        """  # noqa: E501
        response = self._http.request(
            method="PUT",
            path="/auth/user-groups/{userGroupId}",
            path_params={"userGroupId": user_group_id},
            query_params=None,
            body=body,
            requires_signature=True,
        )
        return cast(T.UpdateUserGroupResponse, response)

    def delete_user_group(self, user_group_id: str) -> T.DeleteUserGroupResponse:
        """
        Delete User Group.

        Delete a user group. Its permission assignments are revoked and its members are removed. The name can be reused. Returns an empty body on success (200), or the pending user action if a policy requires approval (202).

        Args:
            user_group_id: User group id.

        Returns:
            T.DeleteUserGroupResponse: The API response.
        """  # noqa: E501
        response = self._http.request(
            method="DELETE",
            path="/auth/user-groups/{userGroupId}",
            path_params={"userGroupId": user_group_id},
            query_params=None,
            body=None,
            requires_signature=True,
        )
        return cast(T.DeleteUserGroupResponse, response)

    def list_user_group_members(
        self, user_group_id: str, query: T.ListUserGroupMembersQuery | None = None
    ) -> T.ListUserGroupMembersResponse:
        """
        List User Group Members.

        List the members of a user group.

        Args:
            user_group_id: User group id.
            query: Query parameters.

        Returns:
            T.ListUserGroupMembersResponse: The API response.
        """  # noqa: E501
        response = self._http.request(
            method="GET",
            path="/auth/user-groups/{userGroupId}/members",
            path_params={"userGroupId": user_group_id},
            query_params=query,
            body=None,
            requires_signature=False,
        )
        return cast(T.ListUserGroupMembersResponse, response)

    def add_user_group_members(
        self, user_group_id: str, body: T.AddUserGroupMembersRequest
    ) -> T.AddUserGroupMembersResponse:
        """
        Add User Group Members.

        Add users to a user group. Each member gains every permission assigned to the group, in addition to their own. Returns an empty body on success (200), or the pending user action if a policy requires approval (202).

        Args:
            user_group_id: User group id.
            body: Request body.

        Returns:
            T.AddUserGroupMembersResponse: The API response.
        """  # noqa: E501
        response = self._http.request(
            method="POST",
            path="/auth/user-groups/{userGroupId}/members",
            path_params={"userGroupId": user_group_id},
            query_params=None,
            body=body,
            requires_signature=True,
        )
        return cast(T.AddUserGroupMembersResponse, response)

    def remove_user_group_members(
        self, user_group_id: str, body: T.RemoveUserGroupMembersRequest
    ) -> T.RemoveUserGroupMembersResponse:
        """
        Remove User Group Members.

        Remove users from a user group. Each removed user loses every permission they held only through this group. Returns an empty body on success (200), or the pending user action if a policy requires approval (202).

        Args:
            user_group_id: User group id.
            body: Request body.

        Returns:
            T.RemoveUserGroupMembersResponse: The API response.
        """  # noqa: E501
        response = self._http.request(
            method="DELETE",
            path="/auth/user-groups/{userGroupId}/members",
            path_params={"userGroupId": user_group_id},
            query_params=None,
            body=body,
            requires_signature=True,
        )
        return cast(T.RemoveUserGroupMembersResponse, response)
