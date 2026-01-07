# Dfns Python SDK

Auto-generated Python SDK for the Dfns API.

## Installation

```bash
pip install dfns_sdk
```

Or install from source:

```bash
pip install -e .
```

## Quick Start

```python
from dfns_sdk import DfnsClient, DfnsClientConfig

# Configure the client
config = DfnsClientConfig(
    auth_token="your-auth-token",
    base_url="https://api.dfns.io",  # Optional, this is the default
)

# Create the client
client = DfnsClient(config)

# Use the client
wallets = client.wallets.list_wallets()
print(wallets)

# Clean up
client.close()
```

## Using as a Context Manager

```python
from dfns_sdk import DfnsClient, DfnsClientConfig

config = DfnsClientConfig(
    auth_token="your-auth-token",
)

with DfnsClient(config) as client:
    wallets = client.wallets.list_wallets()
    print(wallets)
```

## User Action Signing

Some operations (like creating wallets or signing transactions) require user action signing.
Configure a signer to enable these operations:

```python
from dfns_sdk import DfnsClient, DfnsClientConfig, KeySigner

# Load your private key
with open("private_key.pem") as f:
    private_key = f.read()

# Create a signer
signer = KeySigner(
    credential_id="cr-xxx-xxx",  # Your credential ID
    private_key=private_key,
    app_origin="https://app.dfns.io",
)

# Configure the client with the signer
config = DfnsClientConfig(
    auth_token="your-auth-token",
    signer=signer,
)

with DfnsClient(config) as client:
    # Operations requiring signatures will automatically sign
    wallet = client.wallets.create_wallet({
        "network": "EthereumSepolia",
    })
    print(wallet)
```

## Available Domains

The client provides access to the following API domains:

- `client.auth` - Authentication and user management
- `client.wallets` - Wallet operations
- `client.policies` - Policy management
- `client.permissions` - Permission management
- `client.webhooks` - Webhook subscriptions
- And more...

Each domain provides typed methods for all available API endpoints.

## Error Handling

```python
from dfns_sdk import DfnsClient, DfnsClientConfig, DfnsError

config = DfnsClientConfig(auth_token="your-auth-token")
client = DfnsClient(config)

try:
    wallet = client.wallets.get_wallet(wallet_id="invalid-id")
except DfnsError as e:
    print(f"Error: {e.message}")
    print(f"Status: {e.status_code}")
    print(f"Code: {e.error_code}")
```

## License

MIT License - See LICENSE file for details.
