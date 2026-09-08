# Get a FIDO2 Public Key from a YubiKey

Command-line tool that enumerates the **resident (discoverable) FIDO2 credentials**
stored on a YubiKey and prints each one's public key in PEM format, along with its
relying party, user name, and credential ID.

This is useful when you need the PEM public key of a passkey/security-key credential
— for example, to inspect or register it as a Dfns credential.

> Reading resident credentials requires the device's **Credential Management**
> feature (YubiKey firmware 5.2+) and the FIDO2 PIN.

---

## Setup

It's recommended to use a Python virtual environment.

This script requires the [`fido2`](https://pypi.org/project/fido2/) and
[`cryptography`](https://pypi.org/project/cryptography/) libraries.

```bash
python3 -m venv venv
source venv/bin/activate          # Windows: .\venv\Scripts\activate
pip install fido2 cryptography
```

---

## Usage

1. Plug in your YubiKey.
2. Run the script:

   ```bash
   python3 get_fido2_public_key_from_yubikey.py
   ```

3. Enter your FIDO2 PIN when prompted.

The script scans every resident credential on the device and, for each, prints:

```
Relying Party: <rp id>
--------------------------------------------------
User: <user name>
Credential ID: <hex>

Public Key (PEM):
-----BEGIN PUBLIC KEY-----
...
-----END PUBLIC KEY-----
```

EC2 (P-256), OKP (Ed25519), and RSA COSE key types are supported.
