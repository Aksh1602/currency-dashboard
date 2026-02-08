import requests
from typing import Dict, Any
from config import EXCHANGE_RATE_API_URL, EXCHANGE_RATE_API_KEY, CURRENCY_API_KEY, CURRENCY_API_URL
import json

def get_exchange_rates(base_currency: str) -> Dict[str, float]:
    """
    Get exchange rates for a given currency against USD, INR, GBP, EUR using ExchangeRate-API.
    
    Args:
        base_currency: Currency code (e.g., 'JPY')
        
    Returns:
        Dictionary with exchange rates
    """
    try:
        url = f"{EXCHANGE_RATE_API_URL}/{EXCHANGE_RATE_API_KEY}/latest/{base_currency}"
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()
        
        if data.get("result") == "success":
            rates = data.get("conversion_rates", {})
            return {
                "base": base_currency,
                "USD": rates.get("USD", "N/A"),
                "INR": rates.get("INR", "N/A"),
                "GBP": rates.get("GBP", "N/A"),
                "EUR": rates.get("EUR", "N/A"),
                "timestamp": data.get("time_last_updated", ""),
            }
        else:
            return {"error": f"Failed to fetch rates for {base_currency}"}
    except Exception as e:
        return {"error": str(e)}

def get_currency_info(country: str) -> Dict[str, Any]:
    """
    Get currency information for a country.
    
    Args:
        country: Country name
        
    Returns:
        Dictionary with currency info
    """
    try:
        # Alternative approach using CurrencyAPI
        url = f"{CURRENCY_API_URL}/latest"
        params = {
            "apikey": CURRENCY_API_KEY,
            "base_currency": "USD",
            "currencies": "JPY,INR,GBP,EUR,KRW,CNY"
        }
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        return {"error": str(e)}

def format_exchange_rates(rates: Dict[str, Any]) -> str:
    """
    Format exchange rates for display.
    
    Args:
        rates: Dictionary of exchange rates
        
    Returns:
        Formatted string
    """
    if "error" in rates:
        return f"Error: {rates['error']}"
    
    base = rates.get("base", "")
    result = f"**Exchange Rates: 1 {base}**\n"
    result += f"- USD: {rates.get('USD', 'N/A')}\n"
    result += f"- INR: {rates.get('INR', 'N/A')}\n"
    result += f"- GBP: {rates.get('GBP', 'N/A')}\n"
    result += f"- EUR: {rates.get('EUR', 'N/A')}\n"
    
    return result
