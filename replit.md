# 🛡️ OriginStamp - Replit Project Documentation

## Overview

**OriginStamp** is an open-source payment layer for the C2PA (Coalition for Content Provenance and Authenticity) standard. It allows creators to embed payment and licensing information directly into digital files alongside their C2PA provenance data.

**Current Status:** Fully functional - Complete CLI tool with stamping and reading capabilities  
**Project Start Date:** November 3, 2025  
**Build Approach:** Building in public with AI assistance from a Samsung tablet  
**Replit Setup Date:** November 3, 2025

## Purpose & Goals

OriginStamp solves a critical gap in the C2PA standard: while C2PA provides the "nutrition label" for content provenance (who created it, how it was modified), there's no standard way to embed the "price tag" (how to pay the creator, licensing terms).

### Core Functionality
- Read C2PA manifests from files
- Write custom `com.originstamp.payment` assertions to files
- Embed payment metadata: wallet addresses, Stripe links, license URLs

## Project Architecture

### Technology Stack
- **Language:** Python 3.11
- **Core Tool:** c2patool (v0.16.5) - Official C2PA command-line tool
- **Project Type:** CLI tool (command-line interface)
- **Build System:** Native Python, no virtual environments needed

### Directory Structure
```
.
├── src/
│   └── originstamp/
│       ├── __init__.py          # Package initialization
│       └── cli.py               # Main CLI implementation
├── examples/
│   ├── sample_manifest.json     # Example payment assertion manifest
│   └── README.md                # Usage examples
├── main.py                      # Entry point for OriginStamp CLI
├── test_originstamp.py          # Test suite
├── requirements.txt             # Python dependencies (currently none)
└── README.md                    # Project README
```

### Key Files
- **src/originstamp/cli.py** - Core CLI with three commands:
  - `read` - Read C2PA manifests from files
  - `stamp` - Add payment metadata to files
  - `version` - Show version information
- **test_originstamp.py** - Automated test suite that verifies installation
- **examples/sample_manifest.json** - Example payment assertion structure

## Recent Changes

### November 3, 2025 - Initial Setup & Implementation
- ✅ Installed Python 3.11 and Rust toolchain
- ✅ Installed c2patool v0.16.5 via Nix package manager
- ✅ Created basic Python CLI structure with argparse
- ✅ Implemented `read`, `stamp`, and `version` commands
- ✅ Fully implemented stamping functionality with c2patool integration
- ✅ Created comprehensive test suite with 4 passing tests (including end-to-end)
- ✅ Set up console workflow for automated testing
- ✅ Added examples directory with sample manifests and test images
- ✅ Generated test images for demonstration purposes
- ✅ Verified end-to-end workflow: stamp → read → verify payment assertion

## Dependencies

### System Dependencies (Nix)
- **c2patool** - Official C2PA tool for reading/writing manifests

### Python Modules
- **Pillow** - For creating test images
- Standard library: `argparse`, `json`, `subprocess`, `pathlib`, `sys`

## Development Workflow

### Running the CLI
```bash
# Show help
python main.py --help

# Check version
python main.py version

# Read a file's C2PA manifest
python main.py read <file>

# Stamp a file with payment info
python main.py stamp input.jpg output.jpg --wallet 0x123... --stripe https://...
```

### Running Tests
```bash
python test_originstamp.py
```

The workflow is configured to automatically run the test suite, which verifies:
1. c2patool is installed and accessible
2. OriginStamp CLI is functional
3. Help system works correctly

## Payment Assertion Format

The custom `com.originstamp.payment` assertion follows this structure:

```json
{
  "label": "com.originstamp.payment",
  "data": {
    "wallet_address": "cryptocurrency wallet address (optional)",
    "stripe_link": "Stripe payment link (optional)",
    "license_url": "License or terms URL (optional)"
  }
}
```

## Roadmap Progress

### Sprint 0 (First 7 Days)
- ✅ **Day 1:** Project initialization
- ✅ **Day 2:** Cloud environment setup & c2patool installation
- ✅ **Day 3:** Successfully read a C2PA manifest from a test image
- ✅ **Day 4:** Define the `com.originstamp.payment` JSON assertion
- ✅ **Day 5-6:** Successfully write and embed assertions into files
- ✅ **Day 7:** Publicly demo the "stamped" file

**Note:** All roadmap items for Sprint 0 were completed during Replit environment setup on November 3, 2025. The project accelerated through the planned milestones and now has a fully functional implementation.

## User Preferences

None documented yet.

## Notes

- This project is built entirely in Replit without Docker or virtual environments
- Uses Nix for system package management
- The CLI is fully functional with complete stamping and reading capabilities
- All tests currently pass (4/4) including end-to-end stamping verification
- This is a CLI tool, not a web application - it runs in console mode
- Payment assertions are successfully embedded and verified in C2PA manifests
- Example files demonstrate the complete workflow in the `examples/` directory
