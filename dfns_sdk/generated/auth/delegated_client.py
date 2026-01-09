"""Delegated client for the auth domain."""

import json
from typing import Any, Literal, Optional, TypedDict, Union
from warnings import deprecated


from ..._internal import HttpClient
from ...base_auth_api import (
    BaseAuthApi,
    SignUserActionChallengeRequest,
    UserActionChallengeResponse,
)
from . import types as T


class DelegatedAuthClient:
    """
    Delegated client for auth operations.

    This client separates user action signing into _init() and _complete() method pairs,
    allowing external systems to handle the signing process.
    """

    def __init__(self, http_client: HttpClient):
        self._http = http_client

    def create_user_action_signature(self, body: T.CreateUserActionSignatureRequest) -> T.CreateUserActionSignatureResponse:
        """
        Create User Action Signature.

        Completes the user action signing process and provides a signing token that can be used to verify the user intended to perform the action.

This is the first step of the [User Action Signing flow](http://docs.dfns.co/api-reference/auth/signing-flows).

The type of credentials used to sign the action is determined by the `kind` field in the nested objects (`firstFactor` and `secondFactor`). Supported credential kinds are:
* `Fido2`: User action is signed by a user's signing device using `WebAuthn`.
* `Key`: User action is signed by a user's, or token's, private key.
* `PasswordProtectedKey`: Login challenge is signed by the decrypted user's private key that was sent during [Create User Action Signature Challenge](https://docs.dfns.co/api-reference/auth/create-user-action-challenge) step.

        Args:
        body: Request body.

        Returns:
            T.CreateUserActionSignatureResponse: The API response.
        """
        return self._http.request(
            method="POST",
            path="/auth/action",
            path_params={},
            query_params=None,
            body=body,
            requires_signature=False,
        )

    def create_user_action_challenge(self, body: T.CreateUserActionChallengeRequest) -> T.CreateUserActionChallengeResponse:
        """
        Create User Action Challenge.

        Starts a user action signing session, returning a challenge that will be used to verify the user's intent to perform an action.
  
  This is the first step of the [User Action Signing flow](http://docs.dfns.co/api-reference/auth/signing-flows).

        Args:
        body: Request body.

        Returns:
            T.CreateUserActionChallengeResponse: The API response.
        """
        return self._http.request(
            method="POST",
            path="/auth/action/init",
            path_params={},
            query_params=None,
            body=body,
            requires_signature=False,
        )

    def list_audit_logs(self, query: T.ListAuditLogsQuery) -> None:
        """
        List Audit Logs.

        Gets all signature events which have occurred in the over the timeframe.  The max range the API supports is 7 days.

StartTime and EndTime are URL-encoded UTC ISO timestamps:    
`startTime=2025-08-29T02%3A46%3A40Z`   
`endTime=2025-09-01T02%3A46%3A40Z`   

An additional optional query parameter, `userId` can be specified to filter down events to a particular user. The API will return results found in CSV format.


Dfns maintains a script which can be used for audit log signature validation: [WebAuthn Signature Verifier](https://github.com/dfns/example-scripts/tree/m/python/utils)

        Args:
        query: Query parameters.
        """
        return self._http.request(
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

Dfns maintains a script which can be used for audit log signature validation: [WebAuthn Signature Verifier](https://github.com/dfns/example-scripts/tree/m/python/utils)

        Args:
        id: Log id you need information about.

        Returns:
            T.GetAuditLogResponse: The API response.
        """
        return self._http.request(
            method="GET",
            path="/auth/action/logs/{id}",
            path_params={"id": id},
            query_params=None,
            body=None,
            requires_signature=False,
        )

    @deprecated("This endpoint is deprecated.")
    def list_applications(self) -> T.ListApplicationsResponse:
        """
        List Applications.

        <Warning>
  Applications are deprecated and will be removed in a future release. See details [here](https://docs.dfns.co/developers/guides/applications-deprecation).
  </Warning>

        Returns:
            T.ListApplicationsResponse: The API response.
        """
        return self._http.request(
            method="GET",
            path="/auth/apps",
            path_params={},
            query_params=None,
            body=None,
            requires_signature=False,
        )

    @deprecated("This endpoint is deprecated.")
    def get_application(self, app_id: str) -> T.GetApplicationResponse:
        """
        Get Application.

        <Warning>
  Applications are deprecated and will be removed in a future release. See details [here](https://docs.dfns.co/developers/guides/applications-deprecation).
  </Warning>

        Args:
        app_id: Path parameter.

        Returns:
            T.GetApplicationResponse: The API response.
        """
        return self._http.request(
            method="GET",
            path="/auth/apps/{appId}",
            path_params={"appId": app_id},
            query_params=None,
            body=None,
            requires_signature=False,
        )

    def list_credentials(self) -> T.ListCredentialsResponse:
        """
        List Credentials.

        List all credentials for a user.

        Returns:
            T.ListCredentialsResponse: The API response.
        """
        return self._http.request(
            method="GET",
            path="/auth/credentials",
            path_params={},
            query_params=None,
            body=None,
            requires_signature=False,
        )

    def create_credential_init(self, body: dict[str, Any]) -> UserActionChallengeResponse:
        """
        Initialize Create Credential.

        Creates a user action challenge for external signing.

        Args:
        body: Request body.

        Returns:
            UserActionChallengeResponse: The challenge to sign externally.
        """
        path = "/auth/credentials"
        payload = json.dumps(body, separators=(",", ":")) if body else ""

        return BaseAuthApi.create_user_action_challenge(
            self._http,
            user_action_http_method="POST",
            user_action_http_path=path,
            user_action_payload=payload,
        )

    def create_credential_complete(self, body: dict[str, Any], signed_challenge: SignUserActionChallengeRequest) -> T.CreateCredentialResponse:
        """
        Complete Create Credential.

        Submits the signed challenge and makes the API request.

        Args:
        body: Request body.
        signed_challenge: The signed challenge from external signing.

        Returns:
            T.CreateCredentialResponse: The API response.
        """
        user_action_result = BaseAuthApi.sign_user_action_challenge(
            self._http, signed_challenge
        )
        user_action_token = user_action_result["userAction"]

        return self._http.request_with_user_action(
            method="POST",
            path="/auth/credentials",
            path_params={},
            query_params=None,
            body=body,
            user_action=user_action_token,
        )

    def create_credential_challenge(self, body: T.CreateCredentialChallengeRequest) -> TypedDict:
        """
        Create Credential Challenge.

        Part of the flow [Create Credential Regular flow](https://docs.dfns.co/api-reference/auth/credentials#regular-flow).
  
  Starts a create user credential session, returning a challenge that will be used to verify the user's identity.

        Args:
        body: Request body.

        Returns:
            TypedDict: The API response.
        """
        return self._http.request(
            method="POST",
            path="/auth/credentials/init",
            path_params={},
            query_params=None,
            body=body,
            requires_signature=False,
        )

    def activate_credential_init(self, body: T.ActivateCredentialRequest) -> UserActionChallengeResponse:
        """
        Initialize Activate Credential.

        Creates a user action challenge for external signing.

        Args:
        body: Request body.

        Returns:
            UserActionChallengeResponse: The challenge to sign externally.
        """
        path = "/auth/credentials/activate"
        payload = json.dumps(body, separators=(",", ":")) if body else ""

        return BaseAuthApi.create_user_action_challenge(
            self._http,
            user_action_http_method="PUT",
            user_action_http_path=path,
            user_action_payload=payload,
        )

    def activate_credential_complete(self, body: T.ActivateCredentialRequest, signed_challenge: SignUserActionChallengeRequest) -> T.ActivateCredentialResponse:
        """
        Complete Activate Credential.

        Submits the signed challenge and makes the API request.

        Args:
        body: Request body.
        signed_challenge: The signed challenge from external signing.

        Returns:
            T.ActivateCredentialResponse: The API response.
        """
        user_action_result = BaseAuthApi.sign_user_action_challenge(
            self._http, signed_challenge
        )
        user_action_token = user_action_result["userAction"]

        return self._http.request_with_user_action(
            method="PUT",
            path="/auth/credentials/activate",
            path_params={},
            query_params=None,
            body=body,
            user_action=user_action_token,
        )

    def deactivate_credential_init(self, body: T.DeactivateCredentialRequest) -> UserActionChallengeResponse:
        """
        Initialize Deactivate Credential.

        Creates a user action challenge for external signing.

        Args:
        body: Request body.

        Returns:
            UserActionChallengeResponse: The challenge to sign externally.
        """
        path = "/auth/credentials/deactivate"
        payload = json.dumps(body, separators=(",", ":")) if body else ""

        return BaseAuthApi.create_user_action_challenge(
            self._http,
            user_action_http_method="PUT",
            user_action_http_path=path,
            user_action_payload=payload,
        )

    def deactivate_credential_complete(self, body: T.DeactivateCredentialRequest, signed_challenge: SignUserActionChallengeRequest) -> T.DeactivateCredentialResponse:
        """
        Complete Deactivate Credential.

        Submits the signed challenge and makes the API request.

        Args:
        body: Request body.
        signed_challenge: The signed challenge from external signing.

        Returns:
            T.DeactivateCredentialResponse: The API response.
        """
        user_action_result = BaseAuthApi.sign_user_action_challenge(
            self._http, signed_challenge
        )
        user_action_token = user_action_result["userAction"]

        return self._http.request_with_user_action(
            method="PUT",
            path="/auth/credentials/deactivate",
            path_params={},
            query_params=None,
            body=body,
            user_action=user_action_token,
        )

    def create_credential_code_init(self, body: T.CreateCredentialCodeRequest) -> UserActionChallengeResponse:
        """
        Initialize Create Credential Code.

        Creates a user action challenge for external signing.

        Args:
        body: Request body.

        Returns:
            UserActionChallengeResponse: The challenge to sign externally.
        """
        path = "/auth/credentials/code"
        payload = json.dumps(body, separators=(",", ":")) if body else ""

        return BaseAuthApi.create_user_action_challenge(
            self._http,
            user_action_http_method="POST",
            user_action_http_path=path,
            user_action_payload=payload,
        )

    def create_credential_code_complete(self, body: T.CreateCredentialCodeRequest, signed_challenge: SignUserActionChallengeRequest) -> T.CreateCredentialCodeResponse:
        """
        Complete Create Credential Code.

        Submits the signed challenge and makes the API request.

        Args:
        body: Request body.
        signed_challenge: The signed challenge from external signing.

        Returns:
            T.CreateCredentialCodeResponse: The API response.
        """
        user_action_result = BaseAuthApi.sign_user_action_challenge(
            self._http, signed_challenge
        )
        user_action_token = user_action_result["userAction"]

        return self._http.request_with_user_action(
            method="POST",
            path="/auth/credentials/code",
            path_params={},
            query_params=None,
            body=body,
            user_action=user_action_token,
        )

    def create_credential_challenge_with_code(self, body: T.CreateCredentialChallengeWithCodeRequest) -> TypedDict:
        """
        Create Credential Challenge With Code.

        Part of the flow [Create Credential With Code](https://docs.dfns.co/api-reference/auth/credentials#create-credential-with-code-flow).

Creates a credential challenge using a one time code-time-code. This challenge must then be signed by the new credential, before finalizing the flow.

        Args:
        body: Request body.

        Returns:
            TypedDict: The API response.
        """
        return self._http.request(
            method="POST",
            path="/auth/credentials/code/init",
            path_params={},
            query_params=None,
            body=body,
            requires_signature=False,
        )

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
        """
        return self._http.request(
            method="POST",
            path="/auth/credentials/code/verify",
            path_params={},
            query_params=None,
            body=body,
            requires_signature=False,
        )

    def create_login_challenge(self, body: T.CreateLoginChallengeRequest) -> T.CreateLoginChallengeResponse:
        """
        Create Login Challenge.

        Start a user login session, returning a challenge that will be used to verify the user's identity.

If the user has a credential of kind `PasswordProtectedKey` a temporary one time code needs to be passed in the `loginCode` field.

If the user has at least one discoverable webauthn credential, `username` is optional (usernamless flow).

        Args:
        body: Request body.

        Returns:
            T.CreateLoginChallengeResponse: The API response.
        """
        return self._http.request(
            method="POST",
            path="/auth/login/init",
            path_params={},
            query_params=None,
            body=body,
            requires_signature=False,
        )

    def delegated_login_init(self, body: T.DelegatedLoginRequest) -> UserActionChallengeResponse:
        """
        Initialize Delegated Login.

        Creates a user action challenge for external signing.

        Args:
        body: Request body.

        Returns:
            UserActionChallengeResponse: The challenge to sign externally.
        """
        path = "/auth/login/delegated"
        payload = json.dumps(body, separators=(",", ":")) if body else ""

        return BaseAuthApi.create_user_action_challenge(
            self._http,
            user_action_http_method="POST",
            user_action_http_path=path,
            user_action_payload=payload,
        )

    def delegated_login_complete(self, body: T.DelegatedLoginRequest, signed_challenge: SignUserActionChallengeRequest) -> T.DelegatedLoginResponse:
        """
        Complete Delegated Login.

        Submits the signed challenge and makes the API request.

        Args:
        body: Request body.
        signed_challenge: The signed challenge from external signing.

        Returns:
            T.DelegatedLoginResponse: The API response.
        """
        user_action_result = BaseAuthApi.sign_user_action_challenge(
            self._http, signed_challenge
        )
        user_action_token = user_action_result["userAction"]

        return self._http.request_with_user_action(
            method="POST",
            path="/auth/login/delegated",
            path_params={},
            query_params=None,
            body=body,
            user_action=user_action_token,
        )

    def complete_user_login(self, body: T.CompleteUserLoginRequest) -> TypedDict:
        """
        Complete User Login.

        Completes the login process and provides the authenticated user with their authentication token.

The type of credentials used to login is determined by the `kind` field in the nested objects (`firstFactor` and `secondFactor`). Supported credential kinds are:
* `Fido2`: Login challenge is signed by a user's signing device using `WebAuthn`.
* `Key`: Login challenge is signed by a user's private key.
* `PasswordProtectedKey`: Login challenge is signed by the decrypted user's private key that was sent during [Create User Login Challenge](../registration/inituserregistration) step.

        Args:
        body: Request body.

        Returns:
            TypedDict: The API response.
        """
        return self._http.request(
            method="POST",
            path="/auth/login",
            path_params={},
            query_params=None,
            body=body,
            requires_signature=False,
        )

    def logout(self, body: T.LogoutRequest) -> T.LogoutResponse:
        """
        Logout.

        Completes the user logout process.

        Args:
        body: Request body.

        Returns:
            T.LogoutResponse: The API response.
        """
        return self._http.request(
            method="PUT",
            path="/auth/logout",
            path_params={},
            query_params=None,
            body=body,
            requires_signature=False,
        )

    def send_login_code(self, body: T.SendLoginCodeRequest) -> T.SendLoginCodeResponse:
        """
        Send Login Code.

        Sends a temporary one time code to the user that can be used during login flow.

If the user has a credential of kind `PasswordProtectedKey` a temporary one time code needs to be passed in the `loginCode` field. That's because the [Create Login Challenge](https://docs.dfns.co/api-reference/auth/create-login-challenge) is unauthenticated and returns the encrypted private key of the user. So we need a first step to verify the identity of the user to prevent anybody from fetching the encrypted private key and trying to brute force it offline.

        Args:
        body: Request body.

        Returns:
            T.SendLoginCodeResponse: The API response.
        """
        return self._http.request(
            method="POST",
            path="/auth/login/code",
            path_params={},
            query_params=None,
            body=body,
            requires_signature=False,
        )

    def social_login(self, body: T.SocialLoginRequest) -> T.SocialLoginResponse:
        """
        Social Login.

        Completes the login process and provides the authenticated user with their authentication token.

        Args:
        body: Request body.

        Returns:
            T.SocialLoginResponse: The API response.
        """
        return self._http.request(
            method="POST",
            path="/auth/login/social",
            path_params={},
            query_params=None,
            body=body,
            requires_signature=False,
        )

    def complete_sso_login(self, body: T.CompleteSsoLoginRequest) -> T.CompleteSsoLoginResponse:
        """
        Complete SSO Login.

        Completes the login process and provides the authenticated user with their authentication token.

        Args:
        body: Request body.

        Returns:
            T.CompleteSsoLoginResponse: The API response.
        """
        return self._http.request(
            method="POST",
            path="/auth/login/sso",
            path_params={},
            query_params=None,
            body=body,
            requires_signature=False,
        )

    def initiate_sso_login(self, body: T.InitiateSsoLoginRequest) -> T.InitiateSsoLoginResponse:
        """
        Initiate SSO Login.

        Initialize the login process with SSO by returning the IdP Url to call.

        Args:
        body: Request body.

        Returns:
            T.InitiateSsoLoginResponse: The API response.
        """
        return self._http.request(
            method="POST",
            path="/auth/login/sso/init",
            path_params={},
            query_params=None,
            body=body,
            requires_signature=False,
        )

    def list_personal_access_tokens(self) -> T.ListPersonalAccessTokensResponse:
        """
        List Personal Access Tokens.

        Retrieve the list of your Personal Access Tokens.

        Returns:
            T.ListPersonalAccessTokensResponse: The API response.
        """
        return self._http.request(
            method="GET",
            path="/auth/pats",
            path_params={},
            query_params=None,
            body=None,
            requires_signature=False,
        )

    def create_personal_access_token_init(self, body: T.CreatePersonalAccessTokenRequest) -> UserActionChallengeResponse:
        """
        Initialize Create Personal Access Token.

        Creates a user action challenge for external signing.

        Args:
        body: Request body.

        Returns:
            UserActionChallengeResponse: The challenge to sign externally.
        """
        path = "/auth/pats"
        payload = json.dumps(body, separators=(",", ":")) if body else ""

        return BaseAuthApi.create_user_action_challenge(
            self._http,
            user_action_http_method="POST",
            user_action_http_path=path,
            user_action_payload=payload,
        )

    def create_personal_access_token_complete(self, body: T.CreatePersonalAccessTokenRequest, signed_challenge: SignUserActionChallengeRequest) -> T.CreatePersonalAccessTokenResponse:
        """
        Complete Create Personal Access Token.

        Submits the signed challenge and makes the API request.

        Args:
        body: Request body.
        signed_challenge: The signed challenge from external signing.

        Returns:
            T.CreatePersonalAccessTokenResponse: The API response.
        """
        user_action_result = BaseAuthApi.sign_user_action_challenge(
            self._http, signed_challenge
        )
        user_action_token = user_action_result["userAction"]

        return self._http.request_with_user_action(
            method="POST",
            path="/auth/pats",
            path_params={},
            query_params=None,
            body=body,
            user_action=user_action_token,
        )

    def get_personal_access_token(self, token_id: str) -> T.GetPersonalAccessTokenResponse:
        """
        Get Personal Access Token.

        Retrieve a specific Personal Access Token.

        Args:
        token_id: Path parameter.

        Returns:
            T.GetPersonalAccessTokenResponse: The API response.
        """
        return self._http.request(
            method="GET",
            path="/auth/pats/{tokenId}",
            path_params={"tokenId": token_id},
            query_params=None,
            body=None,
            requires_signature=False,
        )

    def update_personal_access_token_init(self, token_id: str, body: T.UpdatePersonalAccessTokenRequest) -> UserActionChallengeResponse:
        """
        Initialize Update Personal Access Token.

        Creates a user action challenge for external signing.

        Args:
        token_id: Path parameter.
        body: Request body.

        Returns:
            UserActionChallengeResponse: The challenge to sign externally.
        """
        path = "/auth/pats/{tokenId}"
        path = path.replace("{tokenId}", str(token_id))
        payload = json.dumps(body, separators=(",", ":")) if body else ""

        return BaseAuthApi.create_user_action_challenge(
            self._http,
            user_action_http_method="PUT",
            user_action_http_path=path,
            user_action_payload=payload,
        )

    def update_personal_access_token_complete(self, token_id: str, body: T.UpdatePersonalAccessTokenRequest, signed_challenge: SignUserActionChallengeRequest) -> T.UpdatePersonalAccessTokenResponse:
        """
        Complete Update Personal Access Token.

        Submits the signed challenge and makes the API request.

        Args:
        token_id: Path parameter.
        body: Request body.
        signed_challenge: The signed challenge from external signing.

        Returns:
            T.UpdatePersonalAccessTokenResponse: The API response.
        """
        user_action_result = BaseAuthApi.sign_user_action_challenge(
            self._http, signed_challenge
        )
        user_action_token = user_action_result["userAction"]

        return self._http.request_with_user_action(
            method="PUT",
            path="/auth/pats/{tokenId}",
            path_params={"tokenId": token_id},
            query_params=None,
            body=body,
            user_action=user_action_token,
        )

    def delete_personal_access_token_init(self, token_id: str) -> UserActionChallengeResponse:
        """
        Initialize Delete Personal Access Token.

        Creates a user action challenge for external signing.

        Args:
        token_id: Path parameter.

        Returns:
            UserActionChallengeResponse: The challenge to sign externally.
        """
        path = "/auth/pats/{tokenId}"
        path = path.replace("{tokenId}", str(token_id))
        payload = ""

        return BaseAuthApi.create_user_action_challenge(
            self._http,
            user_action_http_method="DELETE",
            user_action_http_path=path,
            user_action_payload=payload,
        )

    def delete_personal_access_token_complete(self, token_id: str, signed_challenge: SignUserActionChallengeRequest) -> T.DeletePersonalAccessTokenResponse:
        """
        Complete Delete Personal Access Token.

        Submits the signed challenge and makes the API request.

        Args:
        token_id: Path parameter.
        signed_challenge: The signed challenge from external signing.

        Returns:
            T.DeletePersonalAccessTokenResponse: The API response.
        """
        user_action_result = BaseAuthApi.sign_user_action_challenge(
            self._http, signed_challenge
        )
        user_action_token = user_action_result["userAction"]

        return self._http.request_with_user_action(
            method="DELETE",
            path="/auth/pats/{tokenId}",
            path_params={"tokenId": token_id},
            query_params=None,
            body=None,
            user_action=user_action_token,
        )

    def activate_personal_access_token_init(self, token_id: str) -> UserActionChallengeResponse:
        """
        Initialize Activate Personal Access Token.

        Creates a user action challenge for external signing.

        Args:
        token_id: Path parameter.

        Returns:
            UserActionChallengeResponse: The challenge to sign externally.
        """
        path = "/auth/pats/{tokenId}/activate"
        path = path.replace("{tokenId}", str(token_id))
        payload = ""

        return BaseAuthApi.create_user_action_challenge(
            self._http,
            user_action_http_method="PUT",
            user_action_http_path=path,
            user_action_payload=payload,
        )

    def activate_personal_access_token_complete(self, token_id: str, signed_challenge: SignUserActionChallengeRequest) -> T.ActivatePersonalAccessTokenResponse:
        """
        Complete Activate Personal Access Token.

        Submits the signed challenge and makes the API request.

        Args:
        token_id: Path parameter.
        signed_challenge: The signed challenge from external signing.

        Returns:
            T.ActivatePersonalAccessTokenResponse: The API response.
        """
        user_action_result = BaseAuthApi.sign_user_action_challenge(
            self._http, signed_challenge
        )
        user_action_token = user_action_result["userAction"]

        return self._http.request_with_user_action(
            method="PUT",
            path="/auth/pats/{tokenId}/activate",
            path_params={"tokenId": token_id},
            query_params=None,
            body=None,
            user_action=user_action_token,
        )

    def deactivate_personal_access_token_init(self, token_id: str) -> UserActionChallengeResponse:
        """
        Initialize Deactivate Personal Access Token.

        Creates a user action challenge for external signing.

        Args:
        token_id: Path parameter.

        Returns:
            UserActionChallengeResponse: The challenge to sign externally.
        """
        path = "/auth/pats/{tokenId}/deactivate"
        path = path.replace("{tokenId}", str(token_id))
        payload = ""

        return BaseAuthApi.create_user_action_challenge(
            self._http,
            user_action_http_method="PUT",
            user_action_http_path=path,
            user_action_payload=payload,
        )

    def deactivate_personal_access_token_complete(self, token_id: str, signed_challenge: SignUserActionChallengeRequest) -> T.DeactivatePersonalAccessTokenResponse:
        """
        Complete Deactivate Personal Access Token.

        Submits the signed challenge and makes the API request.

        Args:
        token_id: Path parameter.
        signed_challenge: The signed challenge from external signing.

        Returns:
            T.DeactivatePersonalAccessTokenResponse: The API response.
        """
        user_action_result = BaseAuthApi.sign_user_action_challenge(
            self._http, signed_challenge
        )
        user_action_token = user_action_result["userAction"]

        return self._http.request_with_user_action(
            method="PUT",
            path="/auth/pats/{tokenId}/deactivate",
            path_params={"tokenId": token_id},
            query_params=None,
            body=None,
            user_action=user_action_token,
        )

    def create_delegated_recovery_challenge_init(self, body: T.CreateDelegatedRecoveryChallengeRequest) -> UserActionChallengeResponse:
        """
        Initialize Create Delegated Recovery Challenge.

        Creates a user action challenge for external signing.

        Args:
        body: Request body.

        Returns:
            UserActionChallengeResponse: The challenge to sign externally.
        """
        path = "/auth/recover/user/delegated"
        payload = json.dumps(body, separators=(",", ":")) if body else ""

        return BaseAuthApi.create_user_action_challenge(
            self._http,
            user_action_http_method="POST",
            user_action_http_path=path,
            user_action_payload=payload,
        )

    def create_delegated_recovery_challenge_complete(self, body: T.CreateDelegatedRecoveryChallengeRequest, signed_challenge: SignUserActionChallengeRequest) -> T.CreateDelegatedRecoveryChallengeResponse:
        """
        Complete Create Delegated Recovery Challenge.

        Submits the signed challenge and makes the API request.

        Args:
        body: Request body.
        signed_challenge: The signed challenge from external signing.

        Returns:
            T.CreateDelegatedRecoveryChallengeResponse: The API response.
        """
        user_action_result = BaseAuthApi.sign_user_action_challenge(
            self._http, signed_challenge
        )
        user_action_token = user_action_result["userAction"]

        return self._http.request_with_user_action(
            method="POST",
            path="/auth/recover/user/delegated",
            path_params={},
            query_params=None,
            body=body,
            user_action=user_action_token,
        )

    def recover_user(self, body: T.RecoverUserRequest) -> T.RecoverUserResponse:
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
            T.RecoverUserResponse: The API response.
        """
        return self._http.request(
            method="POST",
            path="/auth/recover/user",
            path_params={},
            query_params=None,
            body=body,
            requires_signature=False,
        )

    def create_recovery_challenge(self, body: T.CreateRecoveryChallengeRequest) -> T.CreateRecoveryChallengeResponse:
        """
        Create Recovery Challenge.

        Starts a user recovery session, returning a challenge that will be used to verify the user's identity.

        Args:
        body: Request body.

        Returns:
            T.CreateRecoveryChallengeResponse: The API response.
        """
        return self._http.request(
            method="POST",
            path="/auth/recover/user/init",
            path_params={},
            query_params=None,
            body=body,
            requires_signature=False,
        )

    def send_recovery_code_email(self, body: T.SendRecoveryCodeEmailRequest) -> T.SendRecoveryCodeEmailResponse:
        """
        Send Recovery Code Email.

        Send the user a recovery verification code. This code is used as a second factor to verify the user initiated the recovery request.

        Args:
        body: Request body.

        Returns:
            T.SendRecoveryCodeEmailResponse: The API response.
        """
        return self._http.request(
            method="POST",
            path="/auth/recover/user/code",
            path_params={},
            query_params=None,
            body=body,
            requires_signature=False,
        )

    def create_delegated_registration_challenge_init(self, body: T.CreateDelegatedRegistrationChallengeRequest) -> UserActionChallengeResponse:
        """
        Initialize Create Delegated Registration Challenge.

        Creates a user action challenge for external signing.

        Args:
        body: Request body.

        Returns:
            UserActionChallengeResponse: The challenge to sign externally.
        """
        path = "/auth/registration/delegated"
        payload = json.dumps(body, separators=(",", ":")) if body else ""

        return BaseAuthApi.create_user_action_challenge(
            self._http,
            user_action_http_method="POST",
            user_action_http_path=path,
            user_action_payload=payload,
        )

    def create_delegated_registration_challenge_complete(self, body: T.CreateDelegatedRegistrationChallengeRequest, signed_challenge: SignUserActionChallengeRequest) -> T.CreateDelegatedRegistrationChallengeResponse:
        """
        Complete Create Delegated Registration Challenge.

        Submits the signed challenge and makes the API request.

        Args:
        body: Request body.
        signed_challenge: The signed challenge from external signing.

        Returns:
            T.CreateDelegatedRegistrationChallengeResponse: The API response.
        """
        user_action_result = BaseAuthApi.sign_user_action_challenge(
            self._http, signed_challenge
        )
        user_action_token = user_action_result["userAction"]

        return self._http.request_with_user_action(
            method="POST",
            path="/auth/registration/delegated",
            path_params={},
            query_params=None,
            body=body,
            user_action=user_action_token,
        )

    def create_registration_challenge(self, body: T.CreateRegistrationChallengeRequest) -> T.CreateRegistrationChallengeResponse:
        """
        Create Registration Challenge.

        Starts a user registration session. It returns a challenge that will need to be signed by a passkey and used to perform the step [Complete User Registration](/api-reference/auth/register)

        Args:
        body: Request body.

        Returns:
            T.CreateRegistrationChallengeResponse: The API response.
        """
        return self._http.request(
            method="POST",
            path="/auth/registration/init",
            path_params={},
            query_params=None,
            body=body,
            requires_signature=False,
        )

    def create_social_registration_challenge(self, body: T.CreateSocialRegistrationChallengeRequest) -> T.CreateSocialRegistrationChallengeResponse:
        """
        Create Social Registration Challenge.

        Starts an end-user registration session by passing a JWT obtained by an IdP. It returns a challenge that will need to be signed by a passkey and used to perform [Complete End User Registration with Wallets](/api-reference/auth/register-end-user).

        Args:
        body: Request body.

        Returns:
            T.CreateSocialRegistrationChallengeResponse: The API response.
        """
        return self._http.request(
            method="POST",
            path="/auth/registration/social",
            path_params={},
            query_params=None,
            body=body,
            requires_signature=False,
        )

    def complete_user_registration(self, body: T.CompleteUserRegistrationRequest) -> T.CompleteUserRegistrationResponse:
        """
        Complete User Registration.

        Completes the user registration process and creates the user's initial credentials.

The type of credentials being registered is determined by the `credentialKind` field in the nested objects (`firstFactorCredential` , `secondFactorCredential` and `RecoveryCredential`). Supported credential kinds are:
* `Fido2`: User action is signed by a user's signing device using `WebAuthn`.
* `Key`: User action is signed by a user's, or token's, private key.
* `PasswordProtectedKey`: User action is signed by a user's, or token's, private key. The encrypted version of the private key is stored by Dfns and returns during the signing flow for the user to decrypt it.
* `RecoveryKey` : Similar to `PasswordProtectedKey`, but this credential can only be used to recover an account not to sign an action or login. Once this credential is used all the other user's credentials are invalidated.

        Args:
        body: Request body.

        Returns:
            T.CompleteUserRegistrationResponse: The API response.
        """
        return self._http.request(
            method="POST",
            path="/auth/registration",
            path_params={},
            query_params=None,
            body=body,
            requires_signature=False,
        )

    def complete_end_user_registration_with_wallets(self, body: T.CompleteEndUserRegistrationWithWalletsRequest) -> T.CompleteEndUserRegistrationWithWalletsResponse:
        """
        Complete End User Registration with Wallets.

        Completes the end user registration process and creates the user's initial credentials along with delegated wallets for the new end user.

The type of credentials being registered is determined by the `credentialKind` field in the nested objects (`firstFactorCredential` , `secondFactorCredential` and `RecoveryCredential`). Supported credential kinds are:
* `Fido2`: User action is signed by a user's signing device using `WebAuthn`.
* `Key`: User action is signed by a user's, or token's, private key.
* `PasswordProtectedKey`: User action is signed by a user's, or token's, private key. The encrypted version of the private key is stored by Dfns and returns during the signing flow for the user to decrypt it.

The number of delegated wallets created and the wallet types are determined by the `wallets` specifications. The end user is automatically assigned `ManagedDefaultEndUserAccess` managed permission that grants the end user full access to the wallets.

        Args:
        body: Request body.

        Returns:
            T.CompleteEndUserRegistrationWithWalletsResponse: The API response.
        """
        return self._http.request(
            method="POST",
            path="/auth/registration/enduser",
            path_params={},
            query_params=None,
            body=body,
            requires_signature=False,
        )

    def resend_registration_code(self, body: T.ResendRegistrationCodeRequest) -> T.ResendRegistrationCodeResponse:
        """
        Resend Registration Code.

        Sends the user a new registration code. The previous registration code will be marked invalid. If the user has already completed their registration no action will be taken.

        Args:
        body: Request body.

        Returns:
            T.ResendRegistrationCodeResponse: The API response.
        """
        return self._http.request(
            method="PUT",
            path="/auth/registration/code",
            path_params={},
            query_params=None,
            body=body,
            requires_signature=False,
        )

    def list_service_accounts(self) -> T.ListServiceAccountsResponse:
        """
        List Service Accounts.

        List all Service Accounts in your organization.

        Returns:
            T.ListServiceAccountsResponse: The API response.
        """
        return self._http.request(
            method="GET",
            path="/auth/service-accounts",
            path_params={},
            query_params=None,
            body=None,
            requires_signature=False,
        )

    def create_service_account_init(self, body: T.CreateServiceAccountRequest) -> UserActionChallengeResponse:
        """
        Initialize Create Service Account.

        Creates a user action challenge for external signing.

        Args:
        body: Request body.

        Returns:
            UserActionChallengeResponse: The challenge to sign externally.
        """
        path = "/auth/service-accounts"
        payload = json.dumps(body, separators=(",", ":")) if body else ""

        return BaseAuthApi.create_user_action_challenge(
            self._http,
            user_action_http_method="POST",
            user_action_http_path=path,
            user_action_payload=payload,
        )

    def create_service_account_complete(self, body: T.CreateServiceAccountRequest, signed_challenge: SignUserActionChallengeRequest) -> T.CreateServiceAccountResponse:
        """
        Complete Create Service Account.

        Submits the signed challenge and makes the API request.

        Args:
        body: Request body.
        signed_challenge: The signed challenge from external signing.

        Returns:
            T.CreateServiceAccountResponse: The API response.
        """
        user_action_result = BaseAuthApi.sign_user_action_challenge(
            self._http, signed_challenge
        )
        user_action_token = user_action_result["userAction"]

        return self._http.request_with_user_action(
            method="POST",
            path="/auth/service-accounts",
            path_params={},
            query_params=None,
            body=body,
            user_action=user_action_token,
        )

    def get_service_account(self, service_account_id: str) -> T.GetServiceAccountResponse:
        """
        Get Service Account.

        Get information about a specific Service Account.

        Args:
        service_account_id: Path parameter.

        Returns:
            T.GetServiceAccountResponse: The API response.
        """
        return self._http.request(
            method="GET",
            path="/auth/service-accounts/{serviceAccountId}",
            path_params={"serviceAccountId": service_account_id},
            query_params=None,
            body=None,
            requires_signature=False,
        )

    def update_service_account_init(self, service_account_id: str, body: T.UpdateServiceAccountRequest) -> UserActionChallengeResponse:
        """
        Initialize Update Service Account.

        Creates a user action challenge for external signing.

        Args:
        service_account_id: Path parameter.
        body: Request body.

        Returns:
            UserActionChallengeResponse: The challenge to sign externally.
        """
        path = "/auth/service-accounts/{serviceAccountId}"
        path = path.replace("{serviceAccountId}", str(service_account_id))
        payload = json.dumps(body, separators=(",", ":")) if body else ""

        return BaseAuthApi.create_user_action_challenge(
            self._http,
            user_action_http_method="PUT",
            user_action_http_path=path,
            user_action_payload=payload,
        )

    def update_service_account_complete(self, service_account_id: str, body: T.UpdateServiceAccountRequest, signed_challenge: SignUserActionChallengeRequest) -> T.UpdateServiceAccountResponse:
        """
        Complete Update Service Account.

        Submits the signed challenge and makes the API request.

        Args:
        service_account_id: Path parameter.
        body: Request body.
        signed_challenge: The signed challenge from external signing.

        Returns:
            T.UpdateServiceAccountResponse: The API response.
        """
        user_action_result = BaseAuthApi.sign_user_action_challenge(
            self._http, signed_challenge
        )
        user_action_token = user_action_result["userAction"]

        return self._http.request_with_user_action(
            method="PUT",
            path="/auth/service-accounts/{serviceAccountId}",
            path_params={"serviceAccountId": service_account_id},
            query_params=None,
            body=body,
            user_action=user_action_token,
        )

    def delete_service_account_init(self, service_account_id: str) -> UserActionChallengeResponse:
        """
        Initialize Delete Service Account.

        Creates a user action challenge for external signing.

        Args:
        service_account_id: Path parameter.

        Returns:
            UserActionChallengeResponse: The challenge to sign externally.
        """
        path = "/auth/service-accounts/{serviceAccountId}"
        path = path.replace("{serviceAccountId}", str(service_account_id))
        payload = ""

        return BaseAuthApi.create_user_action_challenge(
            self._http,
            user_action_http_method="DELETE",
            user_action_http_path=path,
            user_action_payload=payload,
        )

    def delete_service_account_complete(self, service_account_id: str, signed_challenge: SignUserActionChallengeRequest) -> T.DeleteServiceAccountResponse:
        """
        Complete Delete Service Account.

        Submits the signed challenge and makes the API request.

        Args:
        service_account_id: Path parameter.
        signed_challenge: The signed challenge from external signing.

        Returns:
            T.DeleteServiceAccountResponse: The API response.
        """
        user_action_result = BaseAuthApi.sign_user_action_challenge(
            self._http, signed_challenge
        )
        user_action_token = user_action_result["userAction"]

        return self._http.request_with_user_action(
            method="DELETE",
            path="/auth/service-accounts/{serviceAccountId}",
            path_params={"serviceAccountId": service_account_id},
            query_params=None,
            body=None,
            user_action=user_action_token,
        )

    def activate_service_account_init(self, service_account_id: str) -> UserActionChallengeResponse:
        """
        Initialize Activate Service Account.

        Creates a user action challenge for external signing.

        Args:
        service_account_id: Path parameter.

        Returns:
            UserActionChallengeResponse: The challenge to sign externally.
        """
        path = "/auth/service-accounts/{serviceAccountId}/activate"
        path = path.replace("{serviceAccountId}", str(service_account_id))
        payload = ""

        return BaseAuthApi.create_user_action_challenge(
            self._http,
            user_action_http_method="PUT",
            user_action_http_path=path,
            user_action_payload=payload,
        )

    def activate_service_account_complete(self, service_account_id: str, signed_challenge: SignUserActionChallengeRequest) -> T.ActivateServiceAccountResponse:
        """
        Complete Activate Service Account.

        Submits the signed challenge and makes the API request.

        Args:
        service_account_id: Path parameter.
        signed_challenge: The signed challenge from external signing.

        Returns:
            T.ActivateServiceAccountResponse: The API response.
        """
        user_action_result = BaseAuthApi.sign_user_action_challenge(
            self._http, signed_challenge
        )
        user_action_token = user_action_result["userAction"]

        return self._http.request_with_user_action(
            method="PUT",
            path="/auth/service-accounts/{serviceAccountId}/activate",
            path_params={"serviceAccountId": service_account_id},
            query_params=None,
            body=None,
            user_action=user_action_token,
        )

    def deactivate_service_account_init(self, service_account_id: str) -> UserActionChallengeResponse:
        """
        Initialize Deactivate Service Account.

        Creates a user action challenge for external signing.

        Args:
        service_account_id: Path parameter.

        Returns:
            UserActionChallengeResponse: The challenge to sign externally.
        """
        path = "/auth/service-accounts/{serviceAccountId}/deactivate"
        path = path.replace("{serviceAccountId}", str(service_account_id))
        payload = ""

        return BaseAuthApi.create_user_action_challenge(
            self._http,
            user_action_http_method="PUT",
            user_action_http_path=path,
            user_action_payload=payload,
        )

    def deactivate_service_account_complete(self, service_account_id: str, signed_challenge: SignUserActionChallengeRequest) -> T.DeactivateServiceAccountResponse:
        """
        Complete Deactivate Service Account.

        Submits the signed challenge and makes the API request.

        Args:
        service_account_id: Path parameter.
        signed_challenge: The signed challenge from external signing.

        Returns:
            T.DeactivateServiceAccountResponse: The API response.
        """
        user_action_result = BaseAuthApi.sign_user_action_challenge(
            self._http, signed_challenge
        )
        user_action_token = user_action_result["userAction"]

        return self._http.request_with_user_action(
            method="PUT",
            path="/auth/service-accounts/{serviceAccountId}/deactivate",
            path_params={"serviceAccountId": service_account_id},
            query_params=None,
            body=None,
            user_action=user_action_token,
        )

    def activate_user_init(self, user_id: str) -> UserActionChallengeResponse:
        """
        Initialize Activate User.

        Creates a user action challenge for external signing.

        Args:
        user_id: Path parameter.

        Returns:
            UserActionChallengeResponse: The challenge to sign externally.
        """
        path = "/auth/users/{userId}/activate"
        path = path.replace("{userId}", str(user_id))
        payload = ""

        return BaseAuthApi.create_user_action_challenge(
            self._http,
            user_action_http_method="PUT",
            user_action_http_path=path,
            user_action_payload=payload,
        )

    def activate_user_complete(self, user_id: str, signed_challenge: SignUserActionChallengeRequest) -> T.ActivateUserResponse:
        """
        Complete Activate User.

        Submits the signed challenge and makes the API request.

        Args:
        user_id: Path parameter.
        signed_challenge: The signed challenge from external signing.

        Returns:
            T.ActivateUserResponse: The API response.
        """
        user_action_result = BaseAuthApi.sign_user_action_challenge(
            self._http, signed_challenge
        )
        user_action_token = user_action_result["userAction"]

        return self._http.request_with_user_action(
            method="PUT",
            path="/auth/users/{userId}/activate",
            path_params={"userId": user_id},
            query_params=None,
            body=None,
            user_action=user_action_token,
        )

    def deactivate_user_init(self, user_id: str) -> UserActionChallengeResponse:
        """
        Initialize Deactivate User.

        Creates a user action challenge for external signing.

        Args:
        user_id: Path parameter.

        Returns:
            UserActionChallengeResponse: The challenge to sign externally.
        """
        path = "/auth/users/{userId}/deactivate"
        path = path.replace("{userId}", str(user_id))
        payload = ""

        return BaseAuthApi.create_user_action_challenge(
            self._http,
            user_action_http_method="PUT",
            user_action_http_path=path,
            user_action_payload=payload,
        )

    def deactivate_user_complete(self, user_id: str, signed_challenge: SignUserActionChallengeRequest) -> T.DeactivateUserResponse:
        """
        Complete Deactivate User.

        Submits the signed challenge and makes the API request.

        Args:
        user_id: Path parameter.
        signed_challenge: The signed challenge from external signing.

        Returns:
            T.DeactivateUserResponse: The API response.
        """
        user_action_result = BaseAuthApi.sign_user_action_challenge(
            self._http, signed_challenge
        )
        user_action_token = user_action_result["userAction"]

        return self._http.request_with_user_action(
            method="PUT",
            path="/auth/users/{userId}/deactivate",
            path_params={"userId": user_id},
            query_params=None,
            body=None,
            user_action=user_action_token,
        )

    def get_user(self, user_id: str) -> T.GetUserResponse:
        """
        Get User.

        Retrieve information about a specific User.

        Args:
        user_id: Path parameter.

        Returns:
            T.GetUserResponse: The API response.
        """
        return self._http.request(
            method="GET",
            path="/auth/users/{userId}",
            path_params={"userId": user_id},
            query_params=None,
            body=None,
            requires_signature=False,
        )

    def update_user_init(self, user_id: str, body: T.UpdateUserRequest) -> UserActionChallengeResponse:
        """
        Initialize Update User.

        Creates a user action challenge for external signing.

        Args:
        user_id: Path parameter.
        body: Request body.

        Returns:
            UserActionChallengeResponse: The challenge to sign externally.
        """
        path = "/auth/users/{userId}"
        path = path.replace("{userId}", str(user_id))
        payload = json.dumps(body, separators=(",", ":")) if body else ""

        return BaseAuthApi.create_user_action_challenge(
            self._http,
            user_action_http_method="PUT",
            user_action_http_path=path,
            user_action_payload=payload,
        )

    def update_user_complete(self, user_id: str, body: T.UpdateUserRequest, signed_challenge: SignUserActionChallengeRequest) -> T.UpdateUserResponse:
        """
        Complete Update User.

        Submits the signed challenge and makes the API request.

        Args:
        user_id: Path parameter.
        body: Request body.
        signed_challenge: The signed challenge from external signing.

        Returns:
            T.UpdateUserResponse: The API response.
        """
        user_action_result = BaseAuthApi.sign_user_action_challenge(
            self._http, signed_challenge
        )
        user_action_token = user_action_result["userAction"]

        return self._http.request_with_user_action(
            method="PUT",
            path="/auth/users/{userId}",
            path_params={"userId": user_id},
            query_params=None,
            body=body,
            user_action=user_action_token,
        )

    def delete_user_init(self, user_id: str) -> UserActionChallengeResponse:
        """
        Initialize Delete User.

        Creates a user action challenge for external signing.

        Args:
        user_id: Path parameter.

        Returns:
            UserActionChallengeResponse: The challenge to sign externally.
        """
        path = "/auth/users/{userId}"
        path = path.replace("{userId}", str(user_id))
        payload = ""

        return BaseAuthApi.create_user_action_challenge(
            self._http,
            user_action_http_method="DELETE",
            user_action_http_path=path,
            user_action_payload=payload,
        )

    def delete_user_complete(self, user_id: str, signed_challenge: SignUserActionChallengeRequest) -> T.DeleteUserResponse:
        """
        Complete Delete User.

        Submits the signed challenge and makes the API request.

        Args:
        user_id: Path parameter.
        signed_challenge: The signed challenge from external signing.

        Returns:
            T.DeleteUserResponse: The API response.
        """
        user_action_result = BaseAuthApi.sign_user_action_challenge(
            self._http, signed_challenge
        )
        user_action_token = user_action_result["userAction"]

        return self._http.request_with_user_action(
            method="DELETE",
            path="/auth/users/{userId}",
            path_params={"userId": user_id},
            query_params=None,
            body=None,
            user_action=user_action_token,
        )

    def list_users(self, query: Optional[T.ListUsersQuery] = None) -> T.ListUsersResponse:
        """
        List Users.

        List all Users in your organization.

        Args:
        query: Query parameters.

        Returns:
            T.ListUsersResponse: The API response.
        """
        return self._http.request(
            method="GET",
            path="/auth/users",
            path_params={},
            query_params=query,
            body=None,
            requires_signature=False,
        )

    def create_user_init(self, body: T.CreateUserRequest) -> UserActionChallengeResponse:
        """
        Initialize Create User.

        Creates a user action challenge for external signing.

        Args:
        body: Request body.

        Returns:
            UserActionChallengeResponse: The challenge to sign externally.
        """
        path = "/auth/users"
        payload = json.dumps(body, separators=(",", ":")) if body else ""

        return BaseAuthApi.create_user_action_challenge(
            self._http,
            user_action_http_method="POST",
            user_action_http_path=path,
            user_action_payload=payload,
        )

    def create_user_complete(self, body: T.CreateUserRequest, signed_challenge: SignUserActionChallengeRequest) -> T.CreateUserResponse:
        """
        Complete Create User.

        Submits the signed challenge and makes the API request.

        Args:
        body: Request body.
        signed_challenge: The signed challenge from external signing.

        Returns:
            T.CreateUserResponse: The API response.
        """
        user_action_result = BaseAuthApi.sign_user_action_challenge(
            self._http, signed_challenge
        )
        user_action_token = user_action_result["userAction"]

        return self._http.request_with_user_action(
            method="POST",
            path="/auth/users",
            path_params={},
            query_params=None,
            body=body,
            user_action=user_action_token,
        )
