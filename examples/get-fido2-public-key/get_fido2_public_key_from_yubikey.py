import getpass
import sys

from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import ec, ed25519, rsa
from fido2.ctap2 import ClientPin, CredentialManagement, Ctap2
from fido2.hid import CtapHidDevice


def cose_to_pem(cose_key):
    """
    Converts a COSE key dictionary to a PEM string.
    """
    try:
        # COSE Key Types (kty): 1=OKP, 2=EC2, 3=RSA
        kty = cose_key.get(1)

        # --- Handle EC2 (Elliptic Curve, usually P-256) ---
        if kty == 2:
            curve = cose_key.get(-1)
            if curve == 1: # P-256
                x = cose_key[-2]
                y = cose_key[-3]
                public_numbers = ec.EllipticCurvePublicNumbers(
                    x=int.from_bytes(x, 'big'),
                    y=int.from_bytes(y, 'big'),
                    curve=ec.SECP256R1()
                )
                public_key = public_numbers.public_key()
            else:
                return f"Unsupported EC curve ID: {curve}"

        # --- Handle OKP (Octet Key Pair, usually Ed25519) ---
        elif kty == 1:
            curve = cose_key.get(-1)
            if curve == 6: # Ed25519
                x_bytes = cose_key[-2]
                public_key = ed25519.Ed25519PublicKey.from_public_bytes(x_bytes)
            else:
                return f"Unsupported OKP curve ID: {curve}"

        # --- Handle RSA ---
        elif kty == 3:
            n = cose_key.get(-1)
            e = cose_key.get(-2)
            public_numbers = rsa.RSAPublicNumbers(
                e=int.from_bytes(e, 'big'),
                n=int.from_bytes(n, 'big')
            )
            public_key = public_numbers.public_key()
        else:
            return f"Unsupported Key Type (kty): {kty}"

        # Convert to PEM
        pem = public_key.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
        )
        return pem.decode('utf-8')

    except Exception as e:
        return f"Error converting key: {str(e)}"

def main():
    # 1. Connect to YubiKey
    try:
        dev = next(CtapHidDevice.list_devices(), None)
        if not dev:
            print("[-] No YubiKey detected.")
            sys.exit(1)
        print(f"[+] Connected to: {dev}")
    except Exception as e:
        print(f"[-] Device connection error: {e}")
        sys.exit(1)

    # 2. Setup CTAP2
    try:
        ctap2 = Ctap2(dev)
    except Exception as e:
        print(f"[-] Error initializing CTAP2: {e}")
        sys.exit(1)

    if not ctap2.info.options.get("credentialMgmtPreview"):
        print("[-] This YubiKey does not support Credential Management (FW < 5.2).")
        sys.exit(1)

    # 3. Authenticate (PIN)
    pin = getpass.getpass(prompt="Enter FIDO2 PIN: ")

    try:
        client_pin = ClientPin(ctap2)
        token = client_pin.get_pin_token(pin)
        cred_mgmt = CredentialManagement(ctap2, client_pin.protocol, token)
    except Exception as e:
        print(f"[-] PIN Error: {e}")
        sys.exit(1)

    # 4. Enumerate and Dump
    print("\n--- SCANNING RESIDENT CREDENTIALS ---")

    rp_list = cred_mgmt.enumerate_rps()
    if not rp_list:
        print("[-] No resident credentials found.")
        return

    for rp_entry in rp_list:
        # Defensive extraction of RP info
        # Try using Enum constants (integers), fallback to strings
        rp_data = rp_entry.get(CredentialManagement.RESULT.RP) or rp_entry.get('rp')
        rp_hash = rp_entry.get(CredentialManagement.RESULT.RP_ID_HASH) or rp_entry.get('rpIdHash')

        rp_id = "Unknown"

        if rp_data:
            rp_id = rp_data.get('id', 'Unknown')

        print("\n==================================================")
        print(f"Relying Party: {rp_id}")

        try:
            creds = cred_mgmt.enumerate_creds(rp_hash)
            for cred in creds:
                print("--------------------------------------------------")

                # 1. Extract Credential ID safely
                cred_id = cred.get(CredentialManagement.RESULT.CREDENTIAL_ID) or cred.get('credentialId')
                # Fallback if it's not bytes (prevents the 'dict has no attribute hex' crash)
                cred_id_hex = cred_id.hex() if isinstance(cred_id, bytes) else f"RAW: {str(cred_id)}"

                # 2. Extract User safely
                user_data = cred.get(CredentialManagement.RESULT.USER) or cred.get('user')
                user_name = "Unknown"
                if user_data:
                    user_name = user_data.get('name', 'Unknown')

                print(f"User: {user_name}")
                print(f"Credential ID: {cred_id_hex}")

                # 3. Extract and Convert Public Key
                cose_key = cred.get(CredentialManagement.RESULT.PUBLIC_KEY) or cred.get('publicKey')

                if cose_key:
                    pem_key = cose_to_pem(cose_key)
                    print("\nPublic Key (PEM):")
                    print(pem_key)
                else:
                    print("\n[!] No public key found in this record.")

        except Exception as e:
            print(f"[-] Error reading credentials for this RP: {e}")
            # If it crashes, let's see why
            import traceback
            traceback.print_exc()

if __name__ == "__main__":
    main()
