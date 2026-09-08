# Examples

Examples illustrating how to use the Dfns Python SDK.

- [bulk-create-wallets](./bulk-create-wallets): Create many wallets in one run,
  all deriving from a single master key you control, each at its own derivation
  path — returning a list that includes each wallet's derivation path.
- [verify-webauthn-signature](./verify-webauthn-signature): Command-line tool to
  verify a WebAuthn/FIDO2 credential assertion signature from its signature,
  public key, client data, and authenticator data.
- [get-fido2-public-key](./get-fido2-public-key): Command-line tool to enumerate
  the resident FIDO2 credentials on a YubiKey and print each one's public key in
  PEM format.
