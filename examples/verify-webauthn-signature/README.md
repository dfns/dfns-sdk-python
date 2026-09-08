# WebAuthn Signature Verifier

This is a Python 3 command-line tool to verify a WebAuthn/FIDO2 credential assertion signature. It takes the signature, public key, client data, and authenticator data as inputs and outputs whether the signature is valid. 🔐

---

## Setup

It's recommended to use a Python virtual environment to manage dependencies and avoid conflicts with system-wide packages.

This script requires the `cryptography` library.

1.  **Create a virtual environment**:
    Navigate to your project directory and run the following command to create a virtual environment named `venv`:
    ```bash
    python3 -m venv venv
    ```

2.  **Activate the virtual environment**:
    * On macOS and Linux:
        ```bash
        source venv/bin/activate
        ```
    * On Windows:
        ```powershell
        .\venv\Scripts\activate
        ```
    Your terminal prompt should now be prefixed with `(venv)`, indicating that the virtual environment is active.

3.  **Install the required library**:
    With the virtual environment active, you can install the dependency using `pip`:
    ```bash
    pip install cryptography
    ```
Now you're ready to run the script. When you're finished, you can deactivate the virtual environment by simply typing `deactivate` in your terminal.

---

## Usage

You can run the script in two ways: by providing command-line flags (recommended) or by using the interactive mode.

### Using Command-Line Flags (Recommended)

You can provide all the necessary data directly as arguments when you run the script. This is the best method for automation and quick verification.

**Arguments:**

* `--signature` or `-s`: The **base64url-encoded signature** from the assertion.
* `--publicKey` or `-p`: The **PEM-formatted public key**. **Note:** Wrap this value in quotes (`"`) to handle special characters and newlines correctly.
* `--clientData` or `-c`: The **base64url-encoded `clientDataJSON`** from the assertion.
* `--authenticatorData` or `-a`: The **base64url-encoded `authenticatorData`** from the assertion.

**Example:**

```bash
python3 dfns_webauthn_signature_validation.py \
  --signature "MEUC..." \
  --publicKey "-----BEGIN PUBLIC KEY-----\nMFkwEwYHKoZIzj0CAQYIKoZIzj0DAQcDQgAEL65uG...=\n-----END PUBLIC KEY-----" \
  --clientData "eyJ0eX..." \
  --authenticatorData "SZYN5..."
```

### Using Interactive Mode

If you run the script without any flags, it will launch in interactive mode and prompt you to enter each piece of data one by one.

**Example:**

1.  Run the script:
    ```bash
    python3 dfns_webauthn_signature_validation.py
    ```

2.  The script will then ask for each piece of data:
    ```
    No flags provided. Entering interactive mode...
    Enter signature: <paste_signature_here>
    Enter publicKey: <paste_public_key_here>
    Enter clientData: <paste_client_data_here>
    Enter authenticatorData: <paste_authenticator_data_here>
    ```

---

## Output

The script will print one of two possible results to the console:

✅ **Signature is valid**

or

❌ **Signature is NOT valid**

If an error occurs during processing (e.g., the public key is malformed), an error message will be printed before the final result.
