# 🧪 Testing Guide

This guide helps you test the Currency & Stock Market Dashboard locally and in production.

## Local Testing

### 1. Basic Setup Test

Verify that your environment is correctly configured.

```bash
# Test Python version
python3 --version  # Should be 3.8+

# Test virtual environment
source venv/bin/activate
pip list  # Should show all installed packages

# Test imports
python3 -c "import streamlit; import langchain; import yfinance; print('✅ All imports successful')"
```

### 2. API Key Test

Verify that your API keys are valid.

```bash
# Create test_apis.py
python3 << 'EOF'
import os
from dotenv import load_dotenv

load_dotenv()

# Test Google API Key
google_key = os.getenv("GOOGLE_API_KEY")
if google_key:
    print(f"✅ Google API Key found: {google_key[:10]}...")
else:
    print("❌ Google API Key not found")

# Test Exchange Rate API Key
exchange_key = os.getenv("EXCHANGE_RATE_API_KEY")
if exchange_key:
    print(f"✅ Exchange Rate API Key found: {exchange_key[:10]}...")
else:
    print("⚠️  Exchange Rate API Key not found (optional)")

# Test Google Maps API Key
maps_key = os.getenv("GOOGLE_MAPS_API_KEY")
if maps_key:
    print(f"✅ Google Maps API Key found: {maps_key[:10]}...")
else:
    print("⚠️  Google Maps API Key not found (optional)")
EOF
```

### 3. Individual Module Test

Test each module independently.

#### Test Currency Utils
```bash
python3 << 'EOF'
from currency_utils import get_exchange_rates, format_exchange_rates
from dotenv import load_dotenv

load_dotenv()

# Test JPY exchange rates
print("Testing JPY exchange rates...")
rates = get_exchange_rates("JPY")

if "error" not in rates:
    print("✅ Exchange rates fetched successfully:")
    print(f"  JPY to USD: {rates.get('USD')}")
    print(f"  JPY to INR: {rates.get('INR')}")
    print(f"  JPY to GBP: {rates.get('GBP')}")
    print(f"  JPY to EUR: {rates.get('EUR')}")
else:
    print(f"❌ Error: {rates.get('error')}")
    print("   Check your EXCHANGE_RATE_API_KEY in .env")
EOF
```

#### Test Stock Utils
```bash
python3 << 'EOF'
from stock_utils import get_stock_indices, get_index_names, format_indices_data

# Test Nikkei 225
print("Testing Nikkei 225 (^N225)...")
indices = get_stock_indices(["^N225"])

if "error" not in indices:
    print("✅ Stock indices fetched successfully:")
    for symbol, data in indices.items():
        if "error" not in data:
            print(f"  {symbol}: {data.get('current')} ({data.get('change_percent')}%)")
        else:
            print(f"  ❌ {symbol}: {data.get('error')}")
else:
    print(f"❌ Error: {indices.get('error')}")
EOF
```

#### Test Configuration
```bash
python3 << 'EOF'
from config import COUNTRY_CONFIG

print("Configured Countries:")
for country, config in COUNTRY_CONFIG.items():
    print(f"✅ {country}")
    print(f"   Currency: {config['code']}")
    print(f"   Exchange: {config['stock_exchange']}")
    print(f"   Indices: {config['major_indices']}")
EOF
```

### 4. Run the Application

```bash
streamlit run app.py
```

In your browser, test:
- ✅ Dashboard loads correctly
- ✅ Can select different countries
- ✅ Exchange rates display
- ✅ Stock indices display
- ✅ Maps load and display
- ✅ AI Agent mode works

### 5. Test Data Accuracy

Verify that displayed data is accurate by comparing with external sources.

```
Test Case 1: JPY Exchange Rate
- Go to app & note JPY to USD rate
- Cross-check with: https://www.xe.com/
- Should be very similar (within 0.01%)

Test Case 2: Nikkei 225
- Go to app & note Nikkei value
- Cross-check with: https://finance.yahoo.com/ (^N225)
- Should match exactly or differ by < 0.5%

Test Case 3: S&P 500
- Go to app & note S&P 500 value
- Cross-check with: https://finance.yahoo.com/ (^GSPC)
- Should match
```

## Automated Testing

### Create test_app.py

```python
import pytest
from currency_utils import get_exchange_rates, format_exchange_rates
from stock_utils import get_stock_indices, get_index_names
from config import COUNTRY_CONFIG

class TestCurrencyUtils:
    def test_get_exchange_rates(self):
        """Test exchange rate fetching."""
        rates = get_exchange_rates("JPY")
        assert "USD" in rates or "error" in rates
    
    def test_format_exchange_rates(self):
        """Test formatting of exchange rates."""
        rates = {
            "base": "JPY",
            "USD": 0.0065,
            "INR": 0.54,
            "GBP": 0.0051,
            "EUR": 0.0060
        }
        formatted = format_exchange_rates(rates)
        assert "JPY" in formatted
        assert "USD" in formatted

class TestStockUtils:
    def test_get_stock_indices(self):
        """Test stock index fetching."""
        indices = get_stock_indices(["^N225"])
        assert "^N225" in indices or "error" in indices
    
    def test_get_index_names(self):
        """Test index name mapping."""
        names = get_index_names(["^N225"])
        assert names["^N225"] == "Nikkei 225"

class TestConfiguration:
    def test_country_configuration(self):
        """Test that all countries are properly configured."""
        required_keys = ["code", "stock_exchange", "major_indices", "exchange_lat", "exchange_lng"]
        
        for country, config in COUNTRY_CONFIG.items():
            for key in required_keys:
                assert key in config, f"Missing {key} for {country}"
            
            # Validate coordinates
            assert -90 <= config["exchange_lat"] <= 90
            assert -180 <= config["exchange_lng"] <= 180

# Run tests
if __name__ == "__main__":
    pytest.main([__file__, "-v"])
```

Run tests:
```bash
pip install pytest
pytest test_app.py -v
```

## Integration Testing

Test the complete workflow end-to-end.

### Test Scenario 1: Dashboard View
1. Start the app: `streamlit run app.py`
2. Select a country (e.g., Japan)
3. Verify all data loads within 5 seconds
4. Check that metrics display correctly
5. Verify map loads and is centered correctly

### Test Scenario 2: AI Agent
1. Enter query: "Give me currency and stock market details for Japan"
2. Agent should return structured information
3. Verify it includes currency code and exchange rates
4. Check if stock indices are mentioned

### Test Scenario 3: Country Comparison
1. Select "Compare Countries" view
2. Select multiple countries
3. Verify comparison table displays
4. Check that all countries are compared

## Performance Testing

Test response times and load handling.

### Test Page Load Time
```bash
# Measure initial page load
time streamlit run app.py
```

Target: < 5 seconds for initial load

### Test API Response Times
```bash
python3 << 'EOF'
import time
from currency_utils import get_exchange_rates
from stock_utils import get_stock_indices

# Test currency API
start = time.time()
rates = get_exchange_rates("JPY")
duration = time.time() - start
print(f"Exchange Rate API: {duration:.2f}s")

# Test stock API
start = time.time()
indices = get_stock_indices(["^N225"])
duration = time.time() - start
print(f"Stock Index API: {duration:.2f}s")
EOF
```

Target times:
- Exchange Rate API: < 2 seconds
- Stock Index API: < 3 seconds

## Browser Compatibility Testing

Test on different browsers:

- ✅ Chrome/Chromium (latest)
- ✅ Firefox (latest)
- ✅ Safari (if on macOS)
- ✅ Edge (if on Windows)

## Mobile Testing

Test responsive design:

```bash
# Open in DevTools mobile mode (F12 → Toggle device toolbar)
# Or access: http://localhost:8501 on your phone on same network
```

## Error Handling Testing

Test how app handles errors:

### Test 1: Missing API Key
1. Remove GOOGLE_API_KEY from .env
2. Run app
3. Should show error message: "GOOGLE_API_KEY not found"

### Test 2: Invalid Country (if adding search)
1. Try to select non-existent country
2. Should handle gracefully

### Test 3: Network Timeout
1. Disconnect internet briefly
2. App should timeout gracefully with error message

### Test 4: Invalid API Key
1. Put random string in API key
2. Should fail with clear error message

## Production Testing Checklist

Before deploying:

- [ ] All API keys configured
- [ ] No console errors in browser DevTools
- [ ] All data loads without errors
- [ ] Maps display correctly
- [ ] AI Agent responds within reasonable time
- [ ] No sensitive data in logs
- [ ] .env file not committed to git
- [ ] requirements.txt up to date
- [ ] Dockerfile builds successfully
- [ ] Docker image runs correctly
- [ ] Environment variables properly set in deployment

## Continuous Integration (Optional)

### GitHub Actions Workflow

Create `.github/workflows/test.yml`:

```yaml
name: Tests

on: [push, pull_request]

jobs:
  test:
    runs-on: ubuntu-latest
    
    steps:
    - uses: actions/checkout@v2
    
    - name: Set up Python
      uses: actions/setup-python@v2
      with:
        python-version: 3.10
    
    - name: Install dependencies
      run: |
        pip install -r requirements.txt
        pip install pytest
    
    - name: Run tests
      run: pytest test_app.py -v
```

---

## Need Help?

- Check logs: Look in console/terminal for error messages
- Verify API keys: Test each API independently
- Check internet: Ensure stable connection
- Review documentation: Check README.md and API docs
- Check status pages: Verify APIs are operational

---

**Happy testing! 🎉**
