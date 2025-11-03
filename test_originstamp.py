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


def test_stamp_and_read():
    """Test stamping a file and reading the manifest back."""
    print("\n" + "=" * 60)
    print("TEST 4: End-to-end stamp and read test")
    print("=" * 60)
    
    import os
    
    if not os.path.exists("examples/test_image.jpg"):
        print("✗ Test image not found")
        return False
    
    output_file = "examples/test_output_e2e.jpg"
    
    if os.path.exists(output_file):
        os.remove(output_file)
        print(f"Cleaned up old output file")
    
    try:
        result = subprocess.run(
            ["python", "main.py", "stamp", 
             "examples/test_image.jpg", 
             output_file,
             "--wallet", "0x1234567890abcdef",
             "--license", "https://creativecommons.org/licenses/by/4.0/"],
            capture_output=True,
            text=True
        )
        
        if result.returncode != 0:
            print(f"✗ Stamping command failed with exit code {result.returncode}")
            print(f"stderr: {result.stderr}")
            return False
        
        if not os.path.exists(output_file):
            print(f"✗ Output file was not created: {output_file}")
            return False
        
        if "Successfully stamped" in result.stdout:
            print("✓ Stamping successful and output file created")
            
            read_result = subprocess.run(
                ["python", "main.py", "read", output_file],
                capture_output=True,
                text=True
            )
            
            if read_result.returncode != 0:
                print(f"✗ Read command failed with exit code {read_result.returncode}")
                return False
            
            if "com.originstamp.payment" in read_result.stdout and "0x1234567890abcdef" in read_result.stdout:
                print("✓ Payment assertion with correct wallet address found in manifest")
                return True
            else:
                print("✗ Payment assertion or wallet address not found in manifest")
                return False
        else:
            print("✗ Stamping failed")
            print(result.stdout)
            return False
            
    except Exception as e:
        print(f"✗ Exception occurred: {e}")
        return False


def main():
    """Run all tests."""
    print("\n🛡️  OriginStamp Test Suite\n")
    
    tests = [
        test_c2patool_installation,
        test_originstamp_cli,
        test_originstamp_help,
        test_stamp_and_read
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
