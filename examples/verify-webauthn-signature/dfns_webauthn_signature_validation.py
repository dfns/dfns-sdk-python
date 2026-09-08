import argparse
import base64
import hashlib
import sys

from cryptography.exceptions import InvalidSignature
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import ec

# --- Helper Functions ---

def base64url_decode(input_str: str) -> bytes:
    """Decodes a base64url string to bytes, adding padding if necessary."""
    input_str = input_str.replace('-', '+').replace('_', '/')
    rem = len(input_str) % 4
    if rem > 0:
        input_str += '=' * (4 - rem)
    return base64.urlsafe_b64decode(input_str)

def load_pem_public_key(pem_key_str: str):
    """Loads a public key from a standard PEM-formatted string."""
    try:
        # The key might have escaped newlines if passed as an argument
        pem_key_str = pem_key_str.replace('\\n', '\n')
        pem_key_bytes = pem_key_str.encode('utf-8')
        public_key = serialization.load_pem_public_key(
            pem_key_bytes,
            backend=default_backend()
        )
        return public_key
    except Exception as e:
        print(f"Error: Could not parse the PEM public key. Details: {e}")
        return None

def verify_assertion_signature(
    signature_b64: str,
    public_key_pem: str,
    client_data_b64: str,
    authenticator_data_b64: str
) -> bool:
    """
    Verifies a WebAuthn credential assertion signature using a PEM public key.
    """
    try:
        signature_bytes = base64url_decode(signature_b64)
        client_data_bytes = base64url_decode(client_data_b64)
        authenticator_data_bytes = base64url_decode(authenticator_data_b64)

        client_data_hash = hashlib.sha256(client_data_bytes).digest()
        data_to_verify = authenticator_data_bytes + client_data_hash

        public_key = load_pem_public_key(public_key_pem)
        if not public_key:
            return False

        public_key.verify(
            signature=signature_bytes,
            data=data_to_verify,
            signature_algorithm=ec.ECDSA(hashes.SHA256())
        )
        return True
    except InvalidSignature:
        return False
    except Exception as e:
        print(f"An unexpected error occurred during verification: {e}")
        return False

# --- Main Execution Logic ---

def main():
    """Main function to run the tool."""
    parser = argparse.ArgumentParser(
        description=(
            "Verify a WebAuthn assertion signature. \n"
            "If no flags are provided, the script will run in interactive mode."
        ),
        formatter_class=argparse.RawTextHelpFormatter # Allows for newlines in help text
    )
    parser.add_argument(
        '-s', '--signature',
        help="The base64url-encoded signature from the assertion."
    )
    parser.add_argument(
        '-p', '--publicKey',
        help="The PEM-formatted public key.\n(e.g., \"-----BEGIN...\\n...END-----\")"
    )
    parser.add_argument(
        '-c', '--clientData',
        help="The base64url-encoded clientDataJSON from the assertion."
    )
    parser.add_argument(
        '-a', '--authenticatorData',
        help="The base64url-encoded authenticatorData from the assertion."
    )

    # If run with no arguments, go to interactive mode
    if len(sys.argv) == 1:
        print("No flags provided. Entering interactive mode...")
        signature = input("Enter signature: ")
        public_key = input("Enter publicKey: ")
        client_data = input("Enter clientData: ")
        authenticator_data = input("Enter authenticatorData: ")
        # Handle escaped newlines from pasted input
        public_key = public_key.replace('\\n', '\n')
    else:
        args = parser.parse_args()
        # Check that all required arguments were provided via flags
        if not all([args.signature, args.publicKey, args.clientData, args.authenticatorData]):
            parser.print_help()
            print(
                "\n❌ Error: All four arguments (--signature, --publicKey, "
                "--clientData, --authenticatorData) are required when using flags."
            )
            sys.exit(1)
        
        signature = args.signature
        public_key = args.publicKey
        client_data = args.clientData
        authenticator_data = args.authenticatorData

    # Perform the verification
    is_valid = verify_assertion_signature(
        signature_b64=signature,
        public_key_pem=public_key,
        client_data_b64=client_data,
        authenticator_data_b64=authenticator_data
    )

    # Print the final result
    if is_valid:
        print("\n✅ Signature is valid")
    else:
        print("\n❌ Signature is NOT valid")

if __name__ == "__main__":
    main()
