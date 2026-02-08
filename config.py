import os
from dotenv import load_dotenv

load_dotenv()

# API Keys
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY", "")
EXCHANGE_RATE_API_KEY = os.getenv("EXCHANGE_RATE_API_KEY", "")
CURRENCY_API_KEY = os.getenv("CURRENCY_API_KEY", "")

# API Endpoints
EXCHANGE_RATE_API_URL = "https://v6.exchangerate-api.com/v6"
CURRENCY_API_URL = "https://api.currencyapi.com/v3"

# Country Configuration
COUNTRY_CONFIG = {
    "Japan": {
        "code": "JPY",
        "stock_exchange": "Tokyo Stock Exchange (TSE)",
        "major_indices": ["^N225", "^TOPIX"],  # Nikkei 225, TOPIX
        "exchange_lat": 35.6762,
        "exchange_lng": 139.7674,
    },
    "India": {
        "code": "INR",
        "stock_exchange": "Bombay Stock Exchange (BSE)",
        "major_indices": ["^BSESN", "^NSEI"],  # BSE SENSEX, NIFTY 50
        "exchange_lat": 19.0760,
        "exchange_lng": 72.5762,
    },
    "United States": {
        "code": "USD",
        "stock_exchange": "New York Stock Exchange (NYSE)",
        "major_indices": ["^GSPC", "^DJI", "^IXIC"],  # S&P 500, Dow Jones, Nasdaq
        "exchange_lat": 40.7074,
        "exchange_lng": -74.0113,
    },
    "South Korea": {
        "code": "KRW",
        "stock_exchange": "Korea Exchange (KRX)",
        "major_indices": ["^KS11"],  # KOSPI
        "exchange_lat": 37.5665,
        "exchange_lng": 126.9780,
    },
    "China": {
        "code": "CNY",
        "stock_exchange": "Shanghai Stock Exchange (SSE)",
        "major_indices": ["000001.SS"],  # Shanghai Composite
        "exchange_lat": 31.2304,
        "exchange_lng": 121.4737,
    },
    "United Kingdom": {
        "code": "GBP",
        "stock_exchange": "London Stock Exchange (LSE)",
        "major_indices": ["^FTSE"],  # FTSE 100
        "exchange_lat": 51.5128,
        "exchange_lng": -0.0843,
    },
}
