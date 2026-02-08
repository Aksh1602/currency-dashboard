from typing import Dict, Tuple
import folium
import streamlit as st
from streamlit_folium import st_folium

def get_exchange_location(country: str) -> Tuple[float, float]:
    """
    Get latitude and longitude of stock exchange for a country.
    
    Args:
        country: Country name
        
    Returns:
        Tuple of (latitude, longitude)
    """
    locations = {
        "Japan": (35.6762, 139.7674),
        "India": (19.0760, 72.5762),
        "United States": (40.7074, -74.0113),
        "South Korea": (37.5665, 126.9780),
        "China": (31.2304, 121.4737),
        "United Kingdom": (51.5128, -0.0843),
    }
    
    return locations.get(country, (0, 0))

def create_map(country: str, exchange_name: str, latitude: float, longitude: float) -> folium.Map:
    """
    Create an interactive map showing the stock exchange location.
    
    Args:
        country: Country name
        exchange_name: Name of the stock exchange
        latitude: Latitude of the exchange
        longitude: Longitude of the exchange
        
    Returns:
        Folium map object
    """
    # Create map centered on the exchange
    map_obj = folium.Map(
        location=[latitude, longitude],
        zoom_start=13,
        tiles="OpenStreetMap"
    )
    
    # Add marker for the exchange
    folium.Marker(
        location=[latitude, longitude],
        popup=f"{exchange_name}\n{country}",
        tooltip=exchange_name,
        icon=folium.Icon(color="blue", icon="info-sign")
    ).add_to(map_obj)
    
    return map_obj

def display_map(country: str, latitude: float, longitude: float):
    """
    Display map in Streamlit.
    
    Args:
        country: Country name
        latitude: Latitude of the exchange
        longitude: Longitude of the exchange
    """
    from config import COUNTRY_CONFIG
    
    exchange_name = COUNTRY_CONFIG.get(country, {}).get("stock_exchange", "Stock Exchange")
    
    m = create_map(country, exchange_name, latitude, longitude)
    st_folium(m, width=700, height=500)

def format_location(country: str, latitude: float, longitude: float) -> str:
    """
    Format location information.
    
    Args:
        country: Country name
        latitude: Latitude
        longitude: Longitude
        
    Returns:
        Formatted string
    """
    return f"""
    **Stock Exchange Location**
    - Country: {country}
    - Latitude: {latitude}
    - Longitude: {longitude}
    - Google Maps Link: [View on Google Maps](https://www.google.com/maps?q={latitude},{longitude})
    """
