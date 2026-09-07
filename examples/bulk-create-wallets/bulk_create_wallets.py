#!/usr/bin/env python3
"""Bulk-create wallets from one shared master key, using the Dfns Python SDK.

Takes a single "range" spec — a master key plus a derivation-path prefix and an
index range — and creates one wallet per index by looping `POST /wallets`. Each
wallet derives from the shared master key at `<pathPrefix><index>`.

The calls are not atomic: it makes one request per wallet (sequentially),
reports per-item ok/error, and keeps going if one fails.

Input (a single spec object) — via --input or stdin:
    {
      "network": "TronNile",
      "name": "deposit",                     # optional; index appended per wallet (deposit-10000, …)
      "signingKey": {
        "deriveFrom": {
          "keyId": "key-...",                # the shared master key
          "pathPrefix": "m/44/195/0/0/",     # derivation path prefix
          "pathStartIndex": 10000,           # first index (inclusive)
          "pathEndIndex": 19999              # last index (inclusive)
        }
      },
      "tags": ["deposit", "hot"]             # optional; applied to every wallet
    }

The spec above creates 10000 wallets at m/44/195/0/0/10000 ... m/44/195/0/0/19999.

Output (JSON list, one entry per created wallet, with its derivation path):
    [
      {"index": 0, "ok": true,
       "id": "wa-...", "network": "TronNile", "status": "Active", "address": "T...",
       "signingKey": {"id": "key-...", "scheme": "ECDSA", "curve": "secp256k1", "publicKey": "..."},
       "derivedFrom": {"keyId": "key-...", "path": "m/44/195/0/0/10000"}},
      {"index": 1, "ok": false, "error": "..."},
      ...
    ]

Auth (env vars):
    DFNS_AUTH_TOKEN        service-account / PAT bearer token   (required)
    DFNS_CRED_ID           signing credential id, cr-...        (required)
    DFNS_PRIVATE_KEY       inline PEM private key for that cred  (required)
    DFNS_API_URL           default https://api.dfns.io

Examples:
    # Validate + preview (shows the wallet count and the first/last path):
    python3 bulk_create_wallets.py --input wallets.json --dry-run

    # Create the wallets and write the results to a file:
    python3 bulk_create_wallets.py --input wallets.json -o out.json

To test first, use a one-wallet range (pathStartIndex == pathEndIndex).
"""

import argparse
import json
import os
import re
import sys
import time

from dotenv import load_dotenv

# Automatic retry on HTTP 429 (rate limited) — handled by the script, no tuning.
MAX_RETRIES = 6
BASE_DELAY_SECONDS = 1.0
MAX_BACKOFF_SECONDS = 30.0

# The API accepts only canonical HD paths (no hardened "'" notation), with each
# non-hardened segment in 0 <= n < 2**31. We validate the same way, up front.
MAX_PATH_SEGMENT = 2**31
PATH_RE = re.compile(r"^m(/(0|[1-9]\d{0,9}))+$")


def load_spec(path):
    """Read one range spec from a file or stdin, validate it, and return it."""
    if path in (None, "-"):
        raw = sys.stdin.read()
    else:
        with open(path, encoding="utf-8") as f:
            raw = f.read()

    try:
        spec = json.loads(raw)
    except json.JSONDecodeError as e:
        sys.exit(f"input is not valid JSON: {e}")

    if isinstance(spec, list):
        sys.exit("input must be a single wallet spec object, not a list.")
    _validate_spec(spec)
    return spec


def _path_for(prefix, index):
    """Join a path prefix and an index into a single derivation path."""
    return f"{prefix.rstrip('/')}/{index}"


def _is_valid_path(path):
    """True if `path` is a canonical HD path the API will accept."""
    if not PATH_RE.match(path):
        return False
    segments = path.split("/")[1:]  # drop the leading "m"
    return all(int(segment) < MAX_PATH_SEGMENT for segment in segments)


def _validate_spec(spec):
    """Fail fast with a clear message if the range spec is malformed."""
    if not isinstance(spec, dict):
        sys.exit("spec must be a JSON object.")
    if not spec.get("network"):
        sys.exit("missing required 'network'.")

    derive = (spec.get("signingKey") or {}).get("deriveFrom") or {}
    if not derive.get("keyId"):
        sys.exit(
            "expected signingKey.deriveFrom.keyId (the shared master key). "
            "Create the master key first via POST /keys, then reference it here."
        )
    prefix = derive.get("pathPrefix")
    if not prefix:
        sys.exit("expected signingKey.deriveFrom.pathPrefix (e.g. m/44/195/0/0/).")

    start, end = derive.get("pathStartIndex"), derive.get("pathEndIndex")
    for name, value in (("pathStartIndex", start), ("pathEndIndex", end)):
        if not isinstance(value, int) or isinstance(value, bool):
            sys.exit(f"{name} must be an integer.")
    if start < 0:
        sys.exit(f"pathStartIndex ({start}) must be >= 0.")
    if start > end:
        sys.exit(f"pathStartIndex ({start}) must be <= pathEndIndex ({end}).")

    # Checking the two endpoints covers the whole range (prefix is constant and
    # every index in between is >= start and <= end).
    for path in (_path_for(prefix, start), _path_for(prefix, end)):
        if not _is_valid_path(path):
            sys.exit(f"derivation path {path!r} is not a valid canonical HD path.")


def _wallet_body(spec, index):
    """Build one POST /wallets body for a single derivation index."""
    derive = spec["signingKey"]["deriveFrom"]
    body = {
        "network": spec["network"],
        "signingKey": {"deriveFrom": {"keyId": derive["keyId"], "path": _path_for(derive["pathPrefix"], index)}},
    }
    if spec.get("name"):
        body["name"] = f"{spec['name']}-{index}"  # unique per wallet
    if spec.get("tags"):
        body["tags"] = spec["tags"]
    return body


def expand(spec):
    """Yield one POST /wallets body per index in the spec's range (inclusive).

    A generator, so even a very large range is never materialized all at once."""
    derive = spec["signingKey"]["deriveFrom"]
    for index in range(derive["pathStartIndex"], derive["pathEndIndex"] + 1):
        yield _wallet_body(spec, index)


def build_client():
    """Build a DfnsClient from env vars. Imports the SDK lazily so --dry-run works without it."""
    try:
        from dfns_sdk import DfnsClient, DfnsClientConfig, KeySigner
    except ImportError:
        sys.exit("dfns_sdk not importable. Install it first:  pip install dfns_sdk")

    token = os.environ.get("DFNS_AUTH_TOKEN")
    cred_id = os.environ.get("DFNS_CRED_ID")
    private_key = os.environ.get("DFNS_PRIVATE_KEY")
    base_url = os.environ.get("DFNS_API_URL", "https://api.dfns.io")

    missing = [
        name
        for name, value in {
            "DFNS_AUTH_TOKEN": token,
            "DFNS_CRED_ID": cred_id,
            "DFNS_PRIVATE_KEY": private_key,
        }.items()
        if not value
    ]
    if missing:
        sys.exit(
            "missing required auth config: "
            + ", ".join(missing)
            + "\nSet them in the environment or in a .env file next to this script."
        )

    signer = KeySigner(credential_id=cred_id, private_key=private_key)
    config = DfnsClientConfig(auth_token=token, base_url=base_url, signer=signer)
    return DfnsClient(config)


def format_result(index, wallet, derived_from):
    """Shape a created wallet (and its derivation path) into an output record."""
    signing_key = wallet.get("signingKey") or {}
    return {
        "index": index,
        "ok": True,
        "id": wallet.get("id"),
        "network": wallet.get("network"),
        "status": wallet.get("status"),
        "address": wallet.get("address"),
        "signingKey": {
            "id": signing_key.get("id"),
            "scheme": signing_key.get("scheme"),
            "curve": signing_key.get("curve"),
            "publicKey": signing_key.get("publicKey"),
        },
        "derivedFrom": {
            "keyId": derived_from.get("keyId"),
            "path": derived_from.get("path"),
        },
    }


def create_one(client, index, body):
    """Create one wallet from an expanded body. Never raises — returns a result dict.

    Retries automatically on HTTP 429 (rate limited) with exponential backoff.
    The SDK error does not expose the Retry-After header, so we back off
    exponentially rather than following a server-directed delay."""
    for attempt in range(MAX_RETRIES + 1):
        try:
            wallet = client.wallets.create_wallet(body)
            break
        except Exception as e:
            rate_limited = getattr(e, "status_code", None) == 429
            if not (rate_limited and attempt < MAX_RETRIES):
                return {"index": index, "ok": False, "network": body.get("network"), "error": str(e)}
            delay = min(BASE_DELAY_SECONDS * 2**attempt, MAX_BACKOFF_SECONDS)
            print(
                f"[{index + 1}] rate-limited (429); retrying in {delay:.1f}s "
                f"(attempt {attempt + 1}/{MAX_RETRIES})",
                file=sys.stderr,
            )
            time.sleep(delay)

    # The derivation path is echoed straight from the request: the API validates
    # it against a strict canonical format and stores it verbatim (it never
    # rewrites the path), so the value we sent is authoritative.
    derived_from = body["signingKey"]["deriveFrom"]
    return format_result(index, wallet, derived_from)


def print_progress(index, total, result):
    """Log one wallet's outcome to stderr (keeps stdout clean for the JSON)."""
    detail = (
        f"ok {result['id']} {result.get('address') or ''}".rstrip()
        if result["ok"]
        else f"ERROR {result['error']}"
    )
    print(f"[{index + 1}/{total}] {detail}", file=sys.stderr)


def write_json(data, path):
    """Write JSON to a file, or to stdout if no path was given."""
    text = json.dumps(data, indent=2)
    if path:
        with open(path, "w", encoding="utf-8") as f:
            f.write(text)
    else:
        print(text)


def parse_args():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("-i", "--input", help="JSON file with the range spec (default: stdin).")
    ap.add_argument("-o", "--output", help="Write result JSON here (default: stdout).")
    ap.add_argument("--dry-run", action="store_true", help="Preview the count + first/last path; create nothing.")
    return ap.parse_args()


def main():
    load_dotenv()  # load auth config from a local .env, if present
    args = parse_args()
    spec = load_spec(args.input)
    derive = spec["signingKey"]["deriveFrom"]
    start, end = derive["pathStartIndex"], derive["pathEndIndex"]
    total = end - start + 1

    if args.dry_run:
        # Only the endpoints are built — a huge range must not be materialized.
        preview = {"count": total, "first": _wallet_body(spec, start), "last": _wallet_body(spec, end)}
        write_json(preview, args.output)
        print(f"\n[dry-run] {total} wallet(s) would be created via POST /wallets.", file=sys.stderr)
        return

    client = build_client()
    results = []
    with client:
        for i, body in enumerate(expand(spec)):
            result = create_one(client, i, body)
            results.append(result)
            print_progress(i, total, result)

    write_json(results, args.output)

    created = sum(1 for r in results if r["ok"])
    failed = len(results) - created
    print(f"\nDone: {created} created, {failed} failed (of {len(results)}).", file=sys.stderr)
    if failed:
        sys.exit(1)


if __name__ == "__main__":
    main()
