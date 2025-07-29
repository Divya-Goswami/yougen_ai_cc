# Return Policy Configuration Guide

## Overview
This guide helps you configure the return policy for YouGen to avoid Google Search Console errors about missing `hasMerchantReturnPolicy` and `shippingDetails` fields.

## Available Return Policy Options

### 1. 30-Day Money-Back Guarantee (RECOMMENDED)
**Best for:** SaaS products, builds customer trust
```bash
export RETURN_POLICY_TYPE=money_back_30
```

**Features:**
- ✅ 30-day return window
- ✅ Free returns
- ✅ Builds customer confidence
- ✅ Standard SaaS practice
- ✅ Resolves Google Search Console warnings

### 2. 7-Day Money-Back Guarantee
**Best for:** Quick validation, shorter commitment
```bash
export RETURN_POLICY_TYPE=money_back_7
```

**Features:**
- ✅ 7-day return window
- ✅ Free returns
- ✅ Faster customer validation
- ✅ Still builds trust
- ✅ Resolves Google Search Console warnings

### 3. No Return Policy
**Best for:** Digital products with immediate value
```bash
export RETURN_POLICY_TYPE=no_returns
```

**Features:**
- ❌ No returns accepted
- ⚠️ May reduce conversion rates
- ⚠️ Still includes shipping details for Google
- ⚠️ May trigger Google Search Console warnings

## How to Configure

### Option 1: Environment Variable (Recommended)
Set the environment variable in your deployment platform:

**Render:**
- Go to your app dashboard
- Navigate to Environment
- Add: `RETURN_POLICY_TYPE=money_back_30`

**Heroku:**
```bash
heroku config:set RETURN_POLICY_TYPE=money_back_30
```

**Railway:**
- Go to your project
- Navigate to Variables
- Add: `RETURN_POLICY_TYPE=money_back_30`

### Option 2: Local Development
Create a `.env` file in your project root:
```bash
RETURN_POLICY_TYPE=money_back_30
SECRET_KEY=your-secret-key
FLASK_DEBUG=True
```

## Google Search Console Compliance

### What Gets Fixed:
1. ✅ **Missing hasMerchantReturnPolicy** - Now included with proper schema
2. ✅ **Missing shippingDetails** - Now included with digital product configuration

### Schema Structure:
```json
{
  "hasMerchantReturnPolicy": {
    "@type": "MerchantReturnPolicy",
    "applicableCountry": "US",
    "returnPolicyCategory": "https://schema.org/MerchantReturnFiniteReturnWindow",
    "merchantReturnDays": 30,
    "returnMethod": "https://schema.org/ReturnByMail",
    "returnFees": "https://schema.org/FreeReturn"
  },
  "shippingDetails": {
    "@type": "OfferShippingDetails",
    "shippingRate": {
      "@type": "MonetaryAmount",
      "value": "0",
      "currency": "USD"
    },
    "deliveryTime": {
      "@type": "ShippingDeliveryTime",
      "handlingTime": {
        "@type": "QuantitativeValue",
        "minValue": 0,
        "maxValue": 0,
        "unitCode": "DAY"
      },
      "transitTime": {
        "@type": "QuantitativeValue",
        "minValue": 0,
        "maxValue": 0,
        "unitCode": "DAY"
      }
    },
    "shippingDestination": {
      "@type": "DefinedRegion",
      "addressCountry": "US"
    }
  }
}
```

## Testing Your Configuration

### 1. Test Structured Data
Use Google's Rich Results Test:
https://search.google.com/test/rich-results

### 2. Verify Configuration
Check your deployed site's structured data by viewing page source and looking for the `application/ld+json` script.

### 3. Monitor Google Search Console
After deployment, monitor for:
- ✅ No more "Missing field" warnings
- ✅ Proper product schema recognition
- ✅ Enhanced search results

## Recommended Settings

**For YouGen (SaaS Product):**
```bash
RETURN_POLICY_TYPE=money_back_30
```

**Why this is recommended:**
- Builds customer trust and confidence
- Standard practice for SaaS products
- Resolves all Google Search Console warnings
- Improves conversion rates
- Easy to implement (just refund via payment processor)

## Troubleshooting

### If warnings persist:
1. **Wait 24-48 hours** for Google to re-crawl your site
2. **Verify deployment** - Check if changes are live
3. **Test structured data** - Use Google's Rich Results Test
4. **Check environment variables** - Ensure they're set correctly

### Common Issues:
- **Environment variable not set** - Defaults to 30-day policy
- **Deployment not complete** - Wait for build to finish
- **Cache issues** - Clear browser cache or wait for CDN refresh 