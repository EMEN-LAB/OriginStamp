# OriginStamp Examples

This directory contains example files and manifests for working with OriginStamp.

## Files

- `sample_manifest.json` - Example C2PA manifest with payment assertion

## Usage Examples

### Check Version
```bash
python main.py version
```

### Read C2PA Manifest from a File
```bash
python main.py read <image-file>
```

### Stamp a File with Payment Information
```bash
python main.py stamp input.jpg output.jpg --wallet 0x1234... --stripe https://buy.stripe.com/example
```

## Payment Assertion Format

The `com.originstamp.payment` assertion follows this structure:

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

At least one payment method should be provided.
