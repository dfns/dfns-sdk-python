# Bulk-create wallets from a shared master key

Create many wallets in one run, all deriving from a **single master key you
already control**. You give a derivation-path prefix and an index range; the
script creates one wallet per index and returns each wallet's derivation path.

It loops the single [`POST /wallets`](https://docs.dfns.co/api-reference/wallets/create-wallet)
endpoint, which accepts `signingKey.deriveFrom.{keyId, path}`. It is a thin
wrapper, not a native bulk job (see [Notes](#notes)).

## Prerequisites

- Python 3.10+
- `pip install dfns_sdk python-dotenv`
- A **master key** already created via [`POST /keys`](https://docs.dfns.co/api-reference/keys/create-key)
  with `"masterKey": true`. Every wallet in your input derives from this key's `keyId`.
- A signing credential (`cr-...`) and its private key in PEM format, plus an
  auth token for a service account or PAT.

## Setup

Copy `.env.example` to `.env` and fill it in:

```bash
cp .env.example .env
# edit .env
```

The script loads `.env` automatically (via `python-dotenv`), so there's nothing
to export.

| Variable | Required | Description |
| --- | --- | --- |
| `DFNS_AUTH_TOKEN` | yes | Service-account / PAT bearer token |
| `DFNS_CRED_ID` | yes | Signing credential id (`cr-...`) |
| `DFNS_PRIVATE_KEY` | yes | Inline PEM private key for that credential (paste the whole key) |
| `DFNS_API_URL` | no | API base URL (default `https://api.dfns.io`) |

## Input

A single **range spec** naming a master key, a derivation-path prefix, and an
inclusive index range; the script expands it into one wallet per index at
`<pathPrefix><index>`. See [`wallets.example.json`](./wallets.example.json):

```json
{
  "network": "EthereumSepolia",
  "name": "deposit",
  "signingKey": {
    "deriveFrom": {
      "keyId": "key-xxxxx-xxxxx-xxxxxxxxxxxxxxxx",
      "pathPrefix": "m/44/60/0/0/",
      "pathStartIndex": 0,
      "pathEndIndex": 4
    }
  },
  "tags": ["deposit", "hot"]
}
```

| Field | Required | Notes |
| --- | --- | --- |
| `network` | yes | Any Dfns network name (e.g. `EthereumSepolia`, `TronNile`) |
| `signingKey.deriveFrom.keyId` | yes | The shared master key to derive from |
| `signingKey.deriveFrom.pathPrefix` | yes | Path prefix; a trailing `/` is optional |
| `signingKey.deriveFrom.pathStartIndex` | yes | First index, **inclusive** |
| `signingKey.deriveFrom.pathEndIndex` | yes | Last index, **inclusive** |
| `name` | no | Name prefix; the index is appended per wallet (e.g. `deposit-10000`) |
| `tags` | no | Applied to every wallet in the range |

The example above creates 5 wallets at `m/44/60/0/0/0` … `m/44/60/0/0/4`. The
paths are validated locally against the API's canonical format (no hardened `'`
notation; each segment `0 <= n < 2^31`) before anything is created.

## Usage

```bash
# 1. Validate + preview: prints the wallet count and the first/last path:
python3 bulk_create_wallets.py --input wallets.example.json --dry-run

# 2. Create the wallets and write the results to a file:
python3 bulk_create_wallets.py --input wallets.example.json -o out.json
```

To test first, use a one-wallet range (`pathStartIndex == pathEndIndex`). Input
can also come from stdin (`cat wallets.json | python3 bulk_create_wallets.py`),
and output goes to stdout unless you pass `-o/--output`. Progress is printed to
stderr, so it stays out of the JSON on stdout.

### Options

| Flag | Description |
| --- | --- |
| `-i, --input` | JSON file with the range spec (default: stdin) |
| `-o, --output` | Write result JSON here (default: stdout) |
| `--dry-run` | Preview the count + first/last path; create nothing |

## Output

A JSON list, one entry per created wallet, in index order:

```json
[
  {
    "index": 0,
    "ok": true,
    "id": "wa-xxxxx-xxxxx-xxxxxxxxxxxxxxxx",
    "network": "EthereumSepolia",
    "status": "Active",
    "address": "0x...",
    "signingKey": { "id": "key-...", "scheme": "ECDSA", "curve": "secp256k1", "publicKey": "..." },
    "derivedFrom": { "keyId": "key-...", "path": "m/44/60/0/0/0" }
  },
  { "index": 1, "ok": false, "network": "EthereumSepolia", "error": "..." }
]
```

The `derivedFrom.path` is echoed straight from your request. The API validates
the path against a strict canonical format and stores it verbatim — it never
rewrites it — so the value you sent is authoritative and no read-back is needed.

The process exits non-zero if any wallet failed.

## Notes

- **Why loop `POST /wallets` instead of `POST /wallets/bulk-create`?** The native
  bulk endpoint mints a brand-new HD master key each run (you cannot pass your
  own `keyId`), and its result does not return the derivation path. When you want
  many wallets that all derive from a master key *you already control*, each at a
  path you choose, single-create is the right tool.
- **Not atomic.** This makes one signed request per wallet, sequentially. A
  failure partway through leaves the wallets created so far in place; the script
  reports per-item `ok`/`error` and continues. Re-running with a corrected input
  is safe as long as you don't reuse a derivation path you already created.
- **Rate limits (429).** Handled automatically — nothing to configure. A large
  batch can hit the API rate limit; each wallet is retried on HTTP 429 with
  exponential backoff (1s, 2s, 4s, … capped at 30s, up to 6 attempts). A wallet
  that still fails after its retries is reported as an error and the run
  continues. (The SDK's error doesn't surface the `Retry-After` header, so the
  backoff is exponential rather than server-directed.)
- **Large ranges are slow.** Each wallet is one signed creation = three sequential
  API round trips (challenge, sign, create), and this script does them one at a
  time. Throughput is bound by latency, so expect very roughly a few wallets per
  second — on the order of hours for tens of thousands. Run it somewhere it can
  keep going uninterrupted (and `-o out.json` so you keep the results). For
  millions of wallets this single-threaded loop isn't the right tool.
