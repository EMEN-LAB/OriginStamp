#!/usr/bin/env python3
"""
Test script for OriginStamp - Verify c2patool integration works
"""

import subprocess
import sys

def test_c2patool_installation():
    """Test if c2patool is installed and accessible."""
    print("=" * 60)
    print("TEST 1: Verify c2patool installation")
    print("=" * 60)
    try:
        result = subprocess.run(
            ["c2patool", "--version"],
            capture_output=True,
            text=True,
            check=True
        )
        print(f"✓ c2patool is installed: {result.stdout.strip()}")
        return True
    except subprocess.CalledProcessError as e:
        print(f"✗ Error: {e.stderr}")
        return False
    except FileNotFoundError:
        print("✗ c2patool not found in PATH")
        return False


def test_originstamp_cli():
    """Test if OriginStamp CLI is accessible."""
    print("\n" + "=" * 60)
    print("TEST 2: Verify OriginStamp CLI")
    print("=" * 60)
    try:
        result = subprocess.run(
            ["python", "main.py", "version"],
            capture_output=True,
            text=True,
            check=True
        )
        print(f"✓ OriginStamp CLI works:\n{result.stdout}")
        return True
    except subprocess.CalledProcessError as e:
        print(f"✗ Error: {e.stderr}")
        return False


def test_originstamp_help():
    """Test if OriginStamp help works."""
    print("\n" + "=" * 60)
    print("TEST 3: Display OriginStamp help")
    print("=" * 60)
    try:
        result = subprocess.run(
            ["python", "main.py", "--help"],
            capture_output=True,
            text=True,
            check=True
        )
        print(f"✓ Help output:\n{result.stdout}")
        return True
    except subprocess.CalledProcessError as e:
        print(f"✗ Error: {e.stderr}")
        return False


def main():
    """Run all tests."""
    print("\n🛡️  OriginStamp Test Suite\n")
    
    tests = [
        test_c2patool_installation,
        test_originstamp_cli,
        test_originstamp_help
    ]
    
    results = []
    for test in tests:
        results.append(test())
    
    print("\n" + "=" * 60)
    print("TEST SUMMARY")
    print("=" * 60)
    passed = sum(results)
    total = len(results)
    print(f"Passed: {passed}/{total}")
    
    if passed == total:
        print("\n✓ All tests passed! OriginStamp is ready.")
        return 0
    else:
        print(f"\n✗ {total - passed} test(s) failed.")
        return 1


if __name__ == "__main__":
    sys.exit(main())
