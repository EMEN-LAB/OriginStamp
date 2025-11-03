#!/usr/bin/env python3
"""
OriginStamp CLI - A tool to read and write payment metadata to C2PA-enabled files.
"""

import argparse
import json
import subprocess
import sys
from pathlib import Path


def run_c2patool(args):
    """Run c2patool command and return output."""
    try:
        result = subprocess.run(
            ["c2patool"] + args,
            capture_output=True,
            text=True,
            check=True
        )
        return result.stdout
    except subprocess.CalledProcessError as e:
        print(f"Error running c2patool: {e.stderr}", file=sys.stderr)
        return None


def read_manifest(file_path):
    """Read C2PA manifest from a file."""
    print(f"Reading C2PA manifest from: {file_path}")
    output = run_c2patool([file_path, "--detailed"])
    if output:
        print("\nManifest Details:")
        print(output)
        return output
    return None


def create_payment_assertion(wallet_address=None, stripe_link=None, license_url=None):
    """Create a payment assertion JSON structure."""
    assertion = {
        "label": "com.originstamp.payment",
        "data": {}
    }
    
    if wallet_address:
        assertion["data"]["wallet_address"] = wallet_address
    if stripe_link:
        assertion["data"]["stripe_link"] = stripe_link
    if license_url:
        assertion["data"]["license_url"] = license_url
    
    return assertion


def stamp_file(input_file, output_file, wallet_address=None, stripe_link=None, license_url=None):
    """Stamp a file with payment metadata."""
    print(f"Stamping file: {input_file}")
    
    # Create payment assertion
    payment_assertion = create_payment_assertion(wallet_address, stripe_link, license_url)
    
    # Create a minimal manifest with the payment assertion
    manifest = {
        "claim_generator": "OriginStamp/0.1.0",
        "assertions": [payment_assertion]
    }
    
    # Save manifest to temporary file
    manifest_path = Path("temp_manifest.json")
    with open(manifest_path, "w") as f:
        json.dump(manifest, f, indent=2)
    
    print(f"\nPayment Assertion:")
    print(json.dumps(payment_assertion, indent=2))
    
    # Run c2patool to embed the manifest
    # Note: This will be implemented once we verify the manifest structure
    print(f"\nNote: Embedding functionality will be implemented in upcoming days.")
    print(f"Manifest saved to: {manifest_path}")
    
    manifest_path.unlink()  # Clean up temp file
    

def main():
    """Main CLI entry point."""
    parser = argparse.ArgumentParser(
        description="OriginStamp - Payment layer for the C2PA standard"
    )
    
    subparsers = parser.add_subparsers(dest="command", help="Available commands")
    
    # Read command
    read_parser = subparsers.add_parser("read", help="Read C2PA manifest from a file")
    read_parser.add_argument("file", help="Path to the file to read")
    
    # Stamp command
    stamp_parser = subparsers.add_parser("stamp", help="Stamp a file with payment metadata")
    stamp_parser.add_argument("input", help="Input file path")
    stamp_parser.add_argument("output", help="Output file path")
    stamp_parser.add_argument("--wallet", help="Cryptocurrency wallet address")
    stamp_parser.add_argument("--stripe", help="Stripe payment link")
    stamp_parser.add_argument("--license", help="License URL")
    
    # Version command
    version_parser = subparsers.add_parser("version", help="Show version information")
    
    args = parser.parse_args()
    
    if args.command == "read":
        read_manifest(args.file)
    elif args.command == "stamp":
        if not any([args.wallet, args.stripe, args.license]):
            print("Error: At least one payment method is required (--wallet, --stripe, or --license)", file=sys.stderr)
            sys.exit(1)
        stamp_file(args.input, args.output, args.wallet, args.stripe, args.license)
    elif args.command == "version":
        print("OriginStamp v0.1.0")
        output = run_c2patool(["--version"])
        if output:
            print(f"c2patool: {output.strip()}")
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
