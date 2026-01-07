"""Client for the auth domain."""

from typing import Any, Literal, Optional, TypedDict, Union
from warnings import deprecated


from ..._internal import HttpClient
from . import types as T


class AuthClient:
    """Client for auth operations."""

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

    def create_credential(self, body: dict[str, Any]) -> T.CreateCredentialResponse:
        """
        Create Credential.

        Part of the flow [Create Credential Regular flow](https://docs.dfns.co/api-reference/auth/credentials#regular-flow).

Adds a new credential to a user's account. See [Credential Kinds](https://docs.dfns.co/api-reference/auth/credentials#credential-kinds) for all supported credential types.

        Args:
        body: Request body.

        Returns:
            T.CreateCredentialResponse: The API response.
        """
        return self._http.request(
            method="POST",
            path="/auth/credentials",
            path_params={},
            query_params=None,
            body=body,
            requires_signature=True,
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

    def activate_credential(self, body: T.ActivateCredentialRequest) -> T.ActivateCredentialResponse:
        """
        Activate Credential.

        Activates a credential that was previously deactivated. If the credential is already activated no action is taken.

        Args:
        body: Request body.

        Returns:
            T.ActivateCredentialResponse: The API response.
        """
        return self._http.request(
            method="PUT",
            path="/auth/credentials/activate",
            path_params={},
            query_params=None,
            body=body,
            requires_signature=True,
        )

    def deactivate_credential(self, body: T.DeactivateCredentialRequest) -> T.DeactivateCredentialResponse:
        """
        Deactivate Credential.

        Deactivates a credential that was previously active. If the credential is already deactivated no action is taken.

        Args:
        body: Request body.

        Returns:
            T.DeactivateCredentialResponse: The API response.
        """
        return self._http.request(
            method="PUT",
            path="/auth/credentials/deactivate",
            path_params={},
            query_params=None,
            body=body,
            requires_signature=True,
        )

    def create_credential_code(self, body: T.CreateCredentialCodeRequest) -> T.CreateCredentialCodeResponse:
        """
        Create Credential Code.

        Part of the [Create Credential With Code flow](https://docs.dfns.co/api-reference/auth/credentials#create-credential-with-code-flow).

Creates a one-time-code that can then be used to create a new credential from a place you don't have access to one of your existing credential.

        Args:
        body: Request body.

        Returns:
            T.CreateCredentialCodeResponse: The API response.
        """
        return self._http.request(
            method="POST",
            path="/auth/credentials/code",
            path_params={},
            query_params=None,
            body=body,
            requires_signature=True,
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
        """
        return self._http.request(
            method="POST",
            path="/auth/login/delegated",
            path_params={},
            query_params=None,
            body=body,
            requires_signature=True,
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

    def create_personal_access_token(self, body: T.CreatePersonalAccessTokenRequest) -> T.CreatePersonalAccessTokenResponse:
        """
        Create Personal Access Token.

        Create a new Personal Access Token for the caller.

        Args:
        body: Request body.

        Returns:
            T.CreatePersonalAccessTokenResponse: The API response.
        """
        return self._http.request(
            method="POST",
            path="/auth/pats",
            path_params={},
            query_params=None,
            body=body,
            requires_signature=True,
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

    def update_personal_access_token(self, token_id: str, body: T.UpdatePersonalAccessTokenRequest) -> T.UpdatePersonalAccessTokenResponse:
        """
        Update Personal Access Token.

        Update a specific Personal Access Token.

        Args:
        token_id: Path parameter.
        body: Request body.

        Returns:
            T.UpdatePersonalAccessTokenResponse: The API response.
        """
        return self._http.request(
            method="PUT",
            path="/auth/pats/{tokenId}",
            path_params={"tokenId": token_id},
            query_params=None,
            body=body,
            requires_signature=True,
        )

    def delete_personal_access_token(self, token_id: str) -> T.DeletePersonalAccessTokenResponse:
        """
        Delete Personal Access Token.

        Delete a specific Personal Access Token.

        Args:
        token_id: Path parameter.

        Returns:
            T.DeletePersonalAccessTokenResponse: The API response.
        """
        return self._http.request(
            method="DELETE",
            path="/auth/pats/{tokenId}",
            path_params={"tokenId": token_id},
            query_params=None,
            body=None,
            requires_signature=True,
        )

    def activate_personal_access_token(self, token_id: str) -> T.ActivatePersonalAccessTokenResponse:
        """
        Activate Personal Access Token.

        Activate a specific Personal Access Token.

        Args:
        token_id: Path parameter.

        Returns:
            T.ActivatePersonalAccessTokenResponse: The API response.
        """
        return self._http.request(
            method="PUT",
            path="/auth/pats/{tokenId}/activate",
            path_params={"tokenId": token_id},
            query_params=None,
            body=None,
            requires_signature=True,
        )

    def deactivate_personal_access_token(self, token_id: str) -> T.DeactivatePersonalAccessTokenResponse:
        """
        Deactivate Personal Access Token.

        Deactivates a credential that was previously active. If the credential is already deactivated no action is taken.

        Args:
        token_id: Path parameter.

        Returns:
            T.DeactivatePersonalAccessTokenResponse: The API response.
        """
        return self._http.request(
            method="PUT",
            path="/auth/pats/{tokenId}/deactivate",
            path_params={"tokenId": token_id},
            query_params=None,
            body=None,
            requires_signature=True,
        )

    def create_delegated_recovery_challenge(self, body: T.CreateDelegatedRecoveryChallengeRequest) -> T.CreateDelegatedRecoveryChallengeResponse:
        """
        Create Delegated Recovery Challenge.

        
<Warning>
Only a [Service Account](https://docs.dfns.co/api-reference/auth/service-accounts) can use this endpoint.
</Warning>

This endpoint enables setting up a recovery workflow for Delegated Signing. Via this configuration, the end user will not receive an email from Dfns but instead can establish recovery credentials that leverage the customer's brand for the recovery workflow.

Once the user has been verified by your auth system and this API has been called, you can call [Recover User](https://docs.dfns.co/api-reference/auth/recover-user) to complete the recovery process.


        Args:
        body: Request body.

        Returns:
            T.CreateDelegatedRecoveryChallengeResponse: The API response.
        """
        return self._http.request(
            method="POST",
            path="/auth/recover/user/delegated",
            path_params={},
            query_params=None,
            body=body,
            requires_signature=True,
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

    def create_delegated_registration_challenge(self, body: T.CreateDelegatedRegistrationChallengeRequest) -> T.CreateDelegatedRegistrationChallengeResponse:
        """
        Create Delegated Registration Challenge.

        <Warning>
Only a [Service Account](https://docs.dfns.co/api-reference/auth/service-accounts) can use this endpoint.
</Warning>

If you want to use your own authentication system, while still using `Delegated Signing`, you can use this endpoint to register a new End User in your organization, without your user needing to receive an email from Dfns.

This endpoint will:
1. Create a new User attached to your organization
2. Initiates a User Registration Challenge and returns the registration challenge.

On successful creation, the user's registration challenge will be returned. You will then need to call [Complete User Registration](https://docs.dfns.co/api-reference/auth/complete-user-registration) or [Complete End User Registration with Wallets](https://docs.dfns.co/api-reference/auth/complete-end-user-registration-with-wallets) to complete the user's registration.

        Args:
        body: Request body.

        Returns:
            T.CreateDelegatedRegistrationChallengeResponse: The API response.
        """
        return self._http.request(
            method="POST",
            path="/auth/registration/delegated",
            path_params={},
            query_params=None,
            body=body,
            requires_signature=True,
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

    def create_service_account(self, body: T.CreateServiceAccountRequest) -> T.CreateServiceAccountResponse:
        """
        Create Service Account.

        Create a new Service Account for your organization.

        Args:
        body: Request body.

        Returns:
            T.CreateServiceAccountResponse: The API response.
        """
        return self._http.request(
            method="POST",
            path="/auth/service-accounts",
            path_params={},
            query_params=None,
            body=body,
            requires_signature=True,
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

    def update_service_account(self, service_account_id: str, body: T.UpdateServiceAccountRequest) -> T.UpdateServiceAccountResponse:
        """
        Update Service Account.

        Update a specific Service Account.

        Args:
        service_account_id: Path parameter.
        body: Request body.

        Returns:
            T.UpdateServiceAccountResponse: The API response.
        """
        return self._http.request(
            method="PUT",
            path="/auth/service-accounts/{serviceAccountId}",
            path_params={"serviceAccountId": service_account_id},
            query_params=None,
            body=body,
            requires_signature=True,
        )

    def delete_service_account(self, service_account_id: str) -> T.DeleteServiceAccountResponse:
        """
        Delete Service Account.

        Delete a specific Service Account.

        Args:
        service_account_id: Path parameter.

        Returns:
            T.DeleteServiceAccountResponse: The API response.
        """
        return self._http.request(
            method="DELETE",
            path="/auth/service-accounts/{serviceAccountId}",
            path_params={"serviceAccountId": service_account_id},
            query_params=None,
            body=None,
            requires_signature=True,
        )

    def activate_service_account(self, service_account_id: str) -> T.ActivateServiceAccountResponse:
        """
        Activate Service Account.

        Activate a specific Service Account.

        Args:
        service_account_id: Path parameter.

        Returns:
            T.ActivateServiceAccountResponse: The API response.
        """
        return self._http.request(
            method="PUT",
            path="/auth/service-accounts/{serviceAccountId}/activate",
            path_params={"serviceAccountId": service_account_id},
            query_params=None,
            body=None,
            requires_signature=True,
        )

    def deactivate_service_account(self, service_account_id: str) -> T.DeactivateServiceAccountResponse:
        """
        Deactivate Service Account.

        Deactivate a specific Service Account.

        Args:
        service_account_id: Path parameter.

        Returns:
            T.DeactivateServiceAccountResponse: The API response.
        """
        return self._http.request(
            method="PUT",
            path="/auth/service-accounts/{serviceAccountId}/deactivate",
            path_params={"serviceAccountId": service_account_id},
            query_params=None,
            body=None,
            requires_signature=True,
        )

    def activate_user(self, user_id: str) -> T.ActivateUserResponse:
        """
        Activate User.

        Activate a specific User.

        Args:
        user_id: Path parameter.

        Returns:
            T.ActivateUserResponse: The API response.
        """
        return self._http.request(
            method="PUT",
            path="/auth/users/{userId}/activate",
            path_params={"userId": user_id},
            query_params=None,
            body=None,
            requires_signature=True,
        )

    def deactivate_user(self, user_id: str) -> T.DeactivateUserResponse:
        """
        Deactivate User.

        Deactivate a specific User.

        Args:
        user_id: Path parameter.

        Returns:
            T.DeactivateUserResponse: The API response.
        """
        return self._http.request(
            method="PUT",
            path="/auth/users/{userId}/deactivate",
            path_params={"userId": user_id},
            query_params=None,
            body=None,
            requires_signature=True,
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

    def update_user(self, user_id: str, body: T.UpdateUserRequest) -> T.UpdateUserResponse:
        """
        Update User.

        Update a specific User.

        Args:
        user_id: Path parameter.
        body: Request body.

        Returns:
            T.UpdateUserResponse: The API response.
        """
        return self._http.request(
            method="PUT",
            path="/auth/users/{userId}",
            path_params={"userId": user_id},
            query_params=None,
            body=body,
            requires_signature=True,
        )

    def delete_user(self, user_id: str) -> T.DeleteUserResponse:
        """
        Delete User.

        Delete a specific User.

        Args:
        user_id: Path parameter.

        Returns:
            T.DeleteUserResponse: The API response.
        """
        return self._http.request(
            method="DELETE",
            path="/auth/users/{userId}",
            path_params={"userId": user_id},
            query_params=None,
            body=None,
            requires_signature=True,
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

    def create_user(self, body: T.CreateUserRequest) -> T.CreateUserResponse:
        """
        Create User.

        Invite a new user in the caller's org. This will create the user and send a registration email to the created User's email, with a registration code, and pointing him to complete his registration on Dfns Dashboard. The user is created without any permissions.
  
  <Note>If you want the created User to not know about about Dfns, and don't want him to 
  receive the registration email from Dfns, you should rather use the Delegated Registration 
  endpoint.</Note>
  

        Args:
        body: Request body.

        Returns:
            T.CreateUserResponse: The API response.
        """
        return self._http.request(
            method="POST",
            path="/auth/users",
            path_params={},
            query_params=None,
            body=body,
            requires_signature=True,
        )
