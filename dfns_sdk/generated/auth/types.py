"""Types for the auth domain."""

from typing import Any, Literal, NotRequired, Optional, TypedDict, Union

class CreateUserActionSignatureRequest(TypedDict, total=False):
    """createUserActionSignature request body."""

    challenge_identifier: str
    first_factor: TypedDict
    second_factor: NotRequired[TypedDict]

class CreateUserActionSignatureResponse(TypedDict, total=False):
    """createUserActionSignature response."""

    user_action: str

class CreateUserActionChallengeRequest(TypedDict, total=False):
    """createUserActionChallenge request body."""

    user_action_server_kind: NotRequired[Literal["Api"]]
    user_action_http_method: Literal["POST", "PUT", "DELETE", "GET"]
    user_action_http_path: str
    user_action_payload: str

class CreateUserActionChallengeResponse(TypedDict, total=False):
    """createUserActionChallenge response."""

    challenge: str
    challenge_identifier: str
    rp: NotRequired[TypedDict]
    supported_credential_kinds: list[TypedDict]
    user_verification: Literal["required", "preferred", "discouraged"]
    attestation: Literal["none", "indirect", "direct", "enterprise"]
    allow_credentials: TypedDict
    external_authentication_url: str

class ListAuditLogsQuery(TypedDict, total=False):
    """listAuditLogs query parameters."""

    start_time: str
    end_time: str
    user_id: NotRequired[str]

class GetAuditLogResponse(TypedDict, total=False):
    """getAuditLog response."""

    id: str
    action: str
    action_token: str
    user_id: Any
    username: Any
    date_performed: str
    first_factor_credential: TypedDict

class ListApplicationsResponse(TypedDict, total=False):
    """listApplications response."""

    items: list[TypedDict]

class GetApplicationResponse(TypedDict, total=False):
    """getApplication response."""

    app_id: str
    kind: Literal["ServerSideApplication", "ClientSideApplication"]
    org_id: str
    expected_rp_id: NotRequired[str]
    name: str
    is_active: bool
    expected_origin: NotRequired[str]
    permission_assignments: list[TypedDict]
    access_tokens: list[TypedDict]

class ListCredentialsResponse(TypedDict, total=False):
    """listCredentials response."""

    items: list[TypedDict]

class CreateCredentialResponse(TypedDict, total=False):
    """createCredential response."""

    kind: Literal["Fido2", "Key", "Password", "Totp", "RecoveryKey", "PasswordProtectedKey"]
    credential_id: str
    credential_uuid: str
    date_created: str
    is_active: bool
    name: str
    public_key: str
    relying_party_id: str
    origin: str

class CreateCredentialChallengeRequest(TypedDict, total=False):
    """createCredentialChallenge request body."""

    kind: TypedDict

class ActivateCredentialRequest(TypedDict, total=False):
    """activateCredential request body."""

    credential_uuid: str

class ActivateCredentialResponse(TypedDict, total=False):
    """activateCredential response."""

    message: str

class DeactivateCredentialRequest(TypedDict, total=False):
    """deactivateCredential request body."""

    credential_uuid: str

class DeactivateCredentialResponse(TypedDict, total=False):
    """deactivateCredential response."""

    message: str

class CreateCredentialCodeRequest(TypedDict, total=False):
    """createCredentialCode request body."""

    expiration: Union[str, int]

class CreateCredentialCodeResponse(TypedDict, total=False):
    """createCredentialCode response."""

    code: str
    expiration: str

class CreateCredentialChallengeWithCodeRequest(TypedDict, total=False):
    """createCredentialChallengeWithCode request body."""

    credential_kind: Literal["Fido2", "Key", "Password", "Totp", "RecoveryKey", "PasswordProtectedKey"]
    code: str

class CreateCredentialWithCodeResponse(TypedDict, total=False):
    """createCredentialWithCode response."""

    kind: Literal["Fido2", "Key", "Password", "Totp", "RecoveryKey", "PasswordProtectedKey"]
    credential_id: str
    credential_uuid: str
    date_created: str
    is_active: bool
    name: str
    public_key: str
    relying_party_id: str
    origin: str

class CreateLoginChallengeRequest(TypedDict, total=False):
    """createLoginChallenge request body."""

    username: NotRequired[str]
    org_id: str
    login_code: NotRequired[str]

class CreateLoginChallengeResponse(TypedDict, total=False):
    """createLoginChallenge response."""

    challenge: str
    challenge_identifier: str
    rp: NotRequired[TypedDict]
    supported_credential_kinds: list[TypedDict]
    user_verification: Literal["required", "preferred", "discouraged"]
    attestation: Literal["none", "indirect", "direct", "enterprise"]
    allow_credentials: TypedDict
    external_authentication_url: str

class DelegatedLoginRequest(TypedDict, total=False):
    """delegatedLogin request body."""

    username: str

class DelegatedLoginResponse(TypedDict, total=False):
    """delegatedLogin response."""

    token: str

class CompleteUserLoginRequest(TypedDict, total=False):
    """completeUserLogin request body."""

    challenge_identifier: str
    first_factor: TypedDict
    second_factor: NotRequired[TypedDict]

class LogoutRequest(TypedDict, total=False):
    """logout request body."""

    all_sessions: NotRequired[bool]

class LogoutResponse(TypedDict, total=False):
    """logout response."""

    message: str

class SendLoginCodeRequest(TypedDict, total=False):
    """sendLoginCode request body."""

    username: str
    org_id: str

class SendLoginCodeResponse(TypedDict, total=False):
    """sendLoginCode response."""

    message: str

class SocialLoginRequest(TypedDict, total=False):
    """socialLogin request body."""

    org_id: NotRequired[str]
    social_login_provider_kind: Literal["Oidc"]
    id_token: str

class SocialLoginResponse(TypedDict, total=False):
    """socialLogin response."""

    token: str

class CompleteSsoLoginRequest(TypedDict, total=False):
    """completeSsoLogin request body."""

    code: str
    state: str

class CompleteSsoLoginResponse(TypedDict, total=False):
    """completeSsoLogin response."""

    token: str

class InitiateSsoLoginRequest(TypedDict, total=False):
    """initiateSsoLogin request body."""

    org_id: str
    client_id: str
    redirect_uri: str

class InitiateSsoLoginResponse(TypedDict, total=False):
    """initiateSsoLogin response."""

    sso_redirect_url: str

class ListPersonalAccessTokensResponse(TypedDict, total=False):
    """listPersonalAccessTokens response."""

    items: list[TypedDict]

class CreatePersonalAccessTokenRequest(TypedDict, total=False):
    """createPersonalAccessToken request body."""

    name: str
    public_key: str
    permission_id: NotRequired[str]
    external_id: NotRequired[str]
    days_valid: NotRequired[int]
    seconds_valid: NotRequired[int]

class CreatePersonalAccessTokenResponse(TypedDict, total=False):
    """createPersonalAccessToken response."""

    access_token: str
    date_created: str
    cred_id: str
    is_active: bool
    kind: Literal["Pat", "ServiceAccount", "Token", "Code", "Recovery", "Temp", "Application"]
    linked_user_id: str
    linked_app_id: str
    name: str
    org_id: str
    public_key: str
    token_id: str
    permission_assignments: list[TypedDict]

class GetPersonalAccessTokenResponse(TypedDict, total=False):
    """getPersonalAccessToken response."""

    access_token: NotRequired[str]
    date_created: str
    cred_id: str
    is_active: bool
    kind: Literal["Pat", "ServiceAccount", "Token", "Code", "Recovery", "Temp", "Application"]
    linked_user_id: str
    linked_app_id: str
    name: str
    org_id: str
    permission_assignments: list[TypedDict]
    public_key: str
    token_id: str

class UpdatePersonalAccessTokenRequest(TypedDict, total=False):
    """updatePersonalAccessToken request body."""

    name: NotRequired[str]
    external_id: NotRequired[str]

class UpdatePersonalAccessTokenResponse(TypedDict, total=False):
    """updatePersonalAccessToken response."""

    access_token: NotRequired[str]
    date_created: str
    cred_id: str
    is_active: bool
    kind: Literal["Pat", "ServiceAccount", "Token", "Code", "Recovery", "Temp", "Application"]
    linked_user_id: str
    linked_app_id: str
    name: str
    org_id: str
    permission_assignments: list[TypedDict]
    public_key: str
    token_id: str

class DeletePersonalAccessTokenResponse(TypedDict, total=False):
    """deletePersonalAccessToken response."""

    access_token: NotRequired[str]
    date_created: str
    cred_id: str
    is_active: bool
    kind: Literal["Pat", "ServiceAccount", "Token", "Code", "Recovery", "Temp", "Application"]
    linked_user_id: str
    linked_app_id: str
    name: str
    org_id: str
    permission_assignments: list[TypedDict]
    public_key: str
    token_id: str

class ActivatePersonalAccessTokenResponse(TypedDict, total=False):
    """activatePersonalAccessToken response."""

    access_token: NotRequired[str]
    date_created: str
    cred_id: str
    is_active: bool
    kind: Literal["Pat", "ServiceAccount", "Token", "Code", "Recovery", "Temp", "Application"]
    linked_user_id: str
    linked_app_id: str
    name: str
    org_id: str
    permission_assignments: list[TypedDict]
    public_key: str
    token_id: str

class DeactivatePersonalAccessTokenResponse(TypedDict, total=False):
    """deactivatePersonalAccessToken response."""

    access_token: NotRequired[str]
    date_created: str
    cred_id: str
    is_active: bool
    kind: Literal["Pat", "ServiceAccount", "Token", "Code", "Recovery", "Temp", "Application"]
    linked_user_id: str
    linked_app_id: str
    name: str
    org_id: str
    permission_assignments: list[TypedDict]
    public_key: str
    token_id: str

class CreateDelegatedRecoveryChallengeRequest(TypedDict, total=False):
    """createDelegatedRecoveryChallenge request body."""

    username: str
    credential_id: str

class CreateDelegatedRecoveryChallengeResponse(TypedDict, total=False):
    """createDelegatedRecoveryChallenge response."""

    user: TypedDict
    temporary_authentication_token: str
    challenge: str
    rp: NotRequired[TypedDict]
    supported_credential_kinds: TypedDict
    authenticator_selection: TypedDict
    attestation: Literal["none", "indirect", "direct", "enterprise"]
    pub_key_cred_params: list[TypedDict]
    exclude_credentials: list[TypedDict]
    otp_url: str
    allowed_recovery_credentials: list[TypedDict]

class RecoverUserRequest(TypedDict, total=False):
    """recoverUser request body."""

    recovery: TypedDict
    new_credentials: TypedDict

class RecoverUserResponse(TypedDict, total=False):
    """recoverUser response."""

    credential: TypedDict
    user: TypedDict

class CreateRecoveryChallengeRequest(TypedDict, total=False):
    """createRecoveryChallenge request body."""

    username: str
    verification_code: str
    org_id: str
    credential_id: str

class CreateRecoveryChallengeResponse(TypedDict, total=False):
    """createRecoveryChallenge response."""

    user: TypedDict
    temporary_authentication_token: str
    challenge: str
    rp: NotRequired[TypedDict]
    supported_credential_kinds: TypedDict
    authenticator_selection: TypedDict
    attestation: Literal["none", "indirect", "direct", "enterprise"]
    pub_key_cred_params: list[TypedDict]
    exclude_credentials: list[TypedDict]
    otp_url: str
    allowed_recovery_credentials: list[TypedDict]

class SendRecoveryCodeEmailRequest(TypedDict, total=False):
    """sendRecoveryCodeEmail request body."""

    username: str
    org_id: str

class SendRecoveryCodeEmailResponse(TypedDict, total=False):
    """sendRecoveryCodeEmail response."""

    message: str

class CreateDelegatedRegistrationChallengeRequest(TypedDict, total=False):
    """createDelegatedRegistrationChallenge request body."""

    email: str
    kind: Literal["EndUser"]
    external_id: NotRequired[str]

class CreateDelegatedRegistrationChallengeResponse(TypedDict, total=False):
    """createDelegatedRegistrationChallenge response."""

    user: TypedDict
    temporary_authentication_token: str
    challenge: str
    rp: NotRequired[TypedDict]
    supported_credential_kinds: TypedDict
    authenticator_selection: TypedDict
    attestation: Literal["none", "indirect", "direct", "enterprise"]
    pub_key_cred_params: list[TypedDict]
    exclude_credentials: list[TypedDict]
    otp_url: str

class CreateRegistrationChallengeRequest(TypedDict, total=False):
    """createRegistrationChallenge request body."""

    org_id: str
    username: str
    registration_code: str

class CreateRegistrationChallengeResponse(TypedDict, total=False):
    """createRegistrationChallenge response."""

    user: TypedDict
    temporary_authentication_token: str
    challenge: str
    rp: NotRequired[TypedDict]
    supported_credential_kinds: TypedDict
    authenticator_selection: TypedDict
    attestation: Literal["none", "indirect", "direct", "enterprise"]
    pub_key_cred_params: list[TypedDict]
    exclude_credentials: list[TypedDict]
    otp_url: str

class CreateSocialRegistrationChallengeRequest(TypedDict, total=False):
    """createSocialRegistrationChallenge request body."""

    org_id: NotRequired[str]
    social_login_provider_kind: Literal["Oidc"]
    id_token: str

class CreateSocialRegistrationChallengeResponse(TypedDict, total=False):
    """createSocialRegistrationChallenge response."""

    user: TypedDict
    temporary_authentication_token: str
    challenge: str
    rp: NotRequired[TypedDict]
    supported_credential_kinds: TypedDict
    authenticator_selection: TypedDict
    attestation: Literal["none", "indirect", "direct", "enterprise"]
    pub_key_cred_params: list[TypedDict]
    exclude_credentials: list[TypedDict]
    otp_url: str

class CompleteUserRegistrationRequest(TypedDict, total=False):
    """completeUserRegistration request body."""

    first_factor_credential: TypedDict
    second_factor_credential: NotRequired[TypedDict]
    recovery_credential: NotRequired[TypedDict]

class CompleteUserRegistrationResponse(TypedDict, total=False):
    """completeUserRegistration response."""

    credential: TypedDict
    user: TypedDict

class CompleteEndUserRegistrationWithWalletsRequest(TypedDict, total=False):
    """completeEndUserRegistrationWithWallets request body."""

    first_factor_credential: TypedDict
    second_factor_credential: NotRequired[TypedDict]
    recovery_credential: NotRequired[TypedDict]
    wallets: list[TypedDict]

class CompleteEndUserRegistrationWithWalletsResponse(TypedDict, total=False):
    """completeEndUserRegistrationWithWallets response."""

    credential: TypedDict
    user: TypedDict
    authentication: TypedDict
    wallets: list[TypedDict]

class ResendRegistrationCodeRequest(TypedDict, total=False):
    """resendRegistrationCode request body."""

    username: str
    org_id: str

class ResendRegistrationCodeResponse(TypedDict, total=False):
    """resendRegistrationCode response."""

    message: str

class ListServiceAccountsResponse(TypedDict, total=False):
    """listServiceAccounts response."""

    items: list[TypedDict]

class CreateServiceAccountRequest(TypedDict, total=False):
    """createServiceAccount request body."""

    name: str
    public_key: str
    permission_id: NotRequired[str]
    external_id: NotRequired[str]
    days_valid: NotRequired[int]

class CreateServiceAccountResponse(TypedDict, total=False):
    """createServiceAccount response."""

    user_info: TypedDict
    access_tokens: list[TypedDict]

class GetServiceAccountResponse(TypedDict, total=False):
    """getServiceAccount response."""

    user_info: TypedDict
    access_tokens: list[TypedDict]

class UpdateServiceAccountRequest(TypedDict, total=False):
    """updateServiceAccount request body."""

    name: NotRequired[str]
    external_id: NotRequired[str]

class UpdateServiceAccountResponse(TypedDict, total=False):
    """updateServiceAccount response."""

    user_info: TypedDict
    access_tokens: list[TypedDict]

class DeleteServiceAccountResponse(TypedDict, total=False):
    """deleteServiceAccount response."""

    user_info: TypedDict
    access_tokens: list[TypedDict]

class ActivateServiceAccountResponse(TypedDict, total=False):
    """activateServiceAccount response."""

    user_info: TypedDict
    access_tokens: list[TypedDict]

class DeactivateServiceAccountResponse(TypedDict, total=False):
    """deactivateServiceAccount response."""

    user_info: TypedDict
    access_tokens: list[TypedDict]

class ActivateUserResponse(TypedDict, total=False):
    """activateUser response."""

    username: str
    name: str
    user_id: str
    kind: Literal["AccountUser", "CustomerEmployee", "EndUser"]
    credential_uuid: str
    org_id: str
    permissions: NotRequired[list[str]]
    is_active: bool
    is_service_account: bool
    is_registered: bool
    is_s_s_o_required: bool
    permission_assignments: list[TypedDict]

class DeactivateUserResponse(TypedDict, total=False):
    """deactivateUser response."""

    username: str
    name: str
    user_id: str
    kind: Literal["AccountUser", "CustomerEmployee", "EndUser"]
    credential_uuid: str
    org_id: str
    permissions: NotRequired[list[str]]
    is_active: bool
    is_service_account: bool
    is_registered: bool
    is_s_s_o_required: bool
    permission_assignments: list[TypedDict]

class GetUserResponse(TypedDict, total=False):
    """getUser response."""

    username: str
    name: str
    user_id: str
    kind: Literal["AccountUser", "CustomerEmployee", "EndUser"]
    credential_uuid: str
    org_id: str
    permissions: NotRequired[list[str]]
    is_active: bool
    is_service_account: bool
    is_registered: bool
    is_s_s_o_required: bool
    permission_assignments: list[TypedDict]

class UpdateUserRequest(TypedDict, total=False):
    """updateUser request body."""

    is_s_s_o_required: bool

class UpdateUserResponse(TypedDict, total=False):
    """updateUser response."""

    username: str
    name: str
    user_id: str
    kind: Literal["AccountUser", "CustomerEmployee", "EndUser"]
    credential_uuid: str
    org_id: str
    permissions: NotRequired[list[str]]
    is_active: bool
    is_service_account: bool
    is_registered: bool
    is_s_s_o_required: bool
    permission_assignments: list[TypedDict]

class DeleteUserResponse(TypedDict, total=False):
    """deleteUser response."""

    username: str
    name: str
    user_id: str
    kind: Literal["AccountUser", "CustomerEmployee", "EndUser"]
    credential_uuid: str
    org_id: str
    permissions: NotRequired[list[str]]
    is_active: bool
    is_service_account: bool
    is_registered: bool
    is_s_s_o_required: bool
    permission_assignments: list[TypedDict]

class ListUsersResponse(TypedDict, total=False):
    """listUsers response."""

    items: list[TypedDict]
    next_page_token: NotRequired[str]

class ListUsersQuery(TypedDict, total=False):
    """listUsers query parameters."""

    limit: NotRequired[int]
    pagination_token: NotRequired[str]
    kind: NotRequired[Literal["CustomerEmployee", "EndUser"]]

class CreateUserRequest(TypedDict, total=False):
    """createUser request body."""

    email: str
    kind: Literal["CustomerEmployee"]
    public_key: NotRequired[str]
    external_id: NotRequired[str]
    is_s_s_o_required: NotRequired[bool]

class CreateUserResponse(TypedDict, total=False):
    """createUser response."""

    username: str
    name: str
    user_id: str
    kind: Literal["AccountUser", "CustomerEmployee", "EndUser"]
    credential_uuid: str
    org_id: str
    permissions: NotRequired[list[str]]
    is_active: bool
    is_service_account: bool
    is_registered: bool
    is_s_s_o_required: bool
    permission_assignments: list[TypedDict]
