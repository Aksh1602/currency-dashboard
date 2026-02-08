import streamlit as st
import os
from dotenv import load_dotenv
from config import COUNTRY_CONFIG
from currency_utils import get_exchange_rates, format_exchange_rates
from stock_utils import get_stock_indices, get_index_names, format_indices_data
from maps_utils import get_exchange_location, display_map, format_location
from agent import create_llm_agent, query_agent

# Load environment variables
load_dotenv()

# Check if API key is available
if not os.getenv("GOOGLE_API_KEY"):
    st.error("⚠️ GOOGLE_API_KEY not found. Please set it in .env file")
    st.info("Get your API key from: https://makersuite.google.com/app/apikey")
    st.stop()

if not os.getenv("EXCHANGE_RATE_API_KEY"):
    st.warning("⚠️ EXCHANGE_RATE_API_KEY not found. Exchange rate features may be limited")

# Page config
st.set_page_config(
    page_title="🌍 Currency & Stock Market Dashboard",
    page_icon="💱",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
<style>
    .metric-card {
        padding: 20px;
        border-radius: 10px;
        background-color: #f0f2f6;
        margin: 10px 0;
    }
    .header-text {
        color: #1f77b4;
        font-size: 24px;
        font-weight: bold;
    }
    .info-text {
        color: #666666;
        font-size: 14px;
    }
</style>
""", unsafe_allow_html=True)

# Title
st.markdown("# 🌍 Global Currency & Stock Market Dashboard")
st.markdown("*Real-time currency exchange rates and stock market indices powered by AI*")

# Sidebar
st.sidebar.markdown("### 🔧 Configuration")
selected_country = st.sidebar.selectbox(
    "Select a Country",
    options=list(COUNTRY_CONFIG.keys()),
    help="Choose a country to view its currency and stock market information"
)

view_mode = st.sidebar.radio(
    "Select View",
    options=["Dashboard", "AI Agent", "Compare Countries"],
    help="Choose how you want to view the data"
)

# Initialize session state
if 'agent' not in st.session_state:
    with st.spinner("🤖 Initializing AI Agent..."):
        try:
            st.session_state.agent = create_llm_agent()
        except Exception as e:
            st.error(f"Failed to initialize AI Agent: {str(e)}")
            st.session_state.agent = None

# Main content
if view_mode == "Dashboard":
    st.markdown("---")
    
    # Get country config
    config = COUNTRY_CONFIG[selected_country]
    
    # Row 1: Currency Information
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown(f"### 💱 Currency Information")
        st.metric("Country", selected_country)
        st.metric("Official Currency", config["code"])
    
    with col2:
        st.markdown(f"### 📍 Stock Exchange")
        st.metric("Exchange", config["stock_exchange"])
    
    # Row 2: Exchange Rates
    st.markdown("---")
    st.markdown("### 💹 Exchange Rates")
    
    with st.spinner(f"Fetching exchange rates for {config['code']}..."):
        rates = get_exchange_rates(config["code"])
        
        if "error" not in rates:
            rate_col1, rate_col2, rate_col3, rate_col4 = st.columns(4)
            
            with rate_col1:
                st.metric(f"1 {config['code']} to USD", f"{rates.get('USD', 'N/A')}")
            
            with rate_col2:
                st.metric(f"1 {config['code']} to INR", f"{rates.get('INR', 'N/A')}")
            
            with rate_col3:
                st.metric(f"1 {config['code']} to GBP", f"{rates.get('GBP', 'N/A')}")
            
            with rate_col4:
                st.metric(f"1 {config['code']} to EUR", f"{rates.get('EUR', 'N/A')}")
        else:
            st.error(f"Could not fetch exchange rates: {rates.get('error')}")
    
    # Row 3: Stock Indices
    st.markdown("---")
    st.markdown("### 📊 Stock Market Indices (Real-time)")
    
    with st.spinner("Fetching stock indices..."):
        indices = get_stock_indices(config["major_indices"])
        index_names = get_index_names(config["major_indices"])
        
        if "error" not in indices:
            for symbol, data in indices.items():
                name = index_names.get(symbol, symbol)
                if "error" not in data:
                    current = data.get("current", "N/A")
                    change = data.get("change_percent", 0)
                    change_emoji = "📈" if change >= 0 else "📉"
                    
                    col1, col2 = st.columns([3, 1])
                    with col1:
                        st.markdown(f"**{name}**")
                    with col2:
                        st.markdown(f"{change_emoji} {change}%")
                    
                    st.metric("Value", f"{current}", delta=f"{change}%")
                else:
                    st.warning(f"Could not fetch data for {name}: {data['error']}")
        else:
            st.error(f"Could not fetch indices: {indices.get('error')}")
    
    # Row 4: Map
    st.markdown("---")
    st.markdown("### 📍 Stock Exchange Location")
    
    lat, lng = get_exchange_location(selected_country)
    
    try:
        display_map(selected_country, lat, lng)
    except Exception as e:
        st.error(f"Map loading error: {str(e)}")
        st.info(f"Stock Exchange Location: {config['stock_exchange']} at ({lat}, {lng})")

elif view_mode == "AI Agent":
    st.markdown("---")
    st.markdown("### 🤖 AI Agent Assistant")
    st.info(
        "Ask the AI agent about currency and stock market information for any country. "
        "The agent will use real-time data to answer your questions."
    )
    
    # Sample queries
    st.markdown("#### Sample Queries:")
    sample_queries = [
        f"Give me currency and stock market details for {selected_country}",
        "Compare currency exchange rates for Japan and India",
        "What are the major stock indices in South Korea?",
        "Get me the latest stock market data for the United States",
    ]
    
    col1, col2 = st.columns([3, 1])
    with col1:
        user_query = st.text_input(
            "Ask a question:",
            placeholder="e.g., Give me currency and stock market details for Japan"
        )
    with col2:
        submit_button = st.button("🔍 Search", use_container_width=True)
    
    # Show sample queries
    st.markdown("Or try one of these:")
    for query in sample_queries:
        if st.button(query, use_container_width=True, key=query):
            user_query = query
            submit_button = True
    
    # Process query
    if submit_button and user_query:
        if st.session_state.agent:
            with st.spinner("🤔 Agent is thinking..."):
                try:
                    response = query_agent(st.session_state.agent, user_query)
                    
                    st.markdown("### 📋 Agent Response:")
                    st.markdown(response)
                    
                    # Store in history
                    if 'query_history' not in st.session_state:
                        st.session_state.query_history = []
                    st.session_state.query_history.append({
                        "query": user_query,
                        "response": response
                    })
                except Exception as e:
                    st.error(f"Agent error: {str(e)}")
        else:
            st.error("AI Agent is not initialized. Please check your API key.")
    
    # Show query history
    if 'query_history' in st.session_state and st.session_state.query_history:
        with st.expander("📜 Query History"):
            for idx, item in enumerate(reversed(st.session_state.query_history), 1):
                st.markdown(f"**Query {len(st.session_state.query_history) - idx + 1}:** {item['query']}")
                st.markdown(f"**Response:** {item['response']}")
                st.divider()

elif view_mode == "Compare Countries":
    st.markdown("---")
    st.markdown("### 🔀 Compare Multiple Countries")
    
    # Select countries to compare
    countries_to_compare = st.multiselect(
        "Select countries to compare",
        options=list(COUNTRY_CONFIG.keys()),
        default=[selected_country]
    )
    
    if countries_to_compare:
        # Comparison table
        comparison_data = []
        
        for country in countries_to_compare:
            config = COUNTRY_CONFIG[country]
            
            with st.spinner(f"Fetching data for {country}..."):
                rates = get_exchange_rates(config["code"])
                indices = get_stock_indices(config["major_indices"])
            
            comparison_data.append({
                "Country": country,
                "Currency": config["code"],
                "Exchange": config["stock_exchange"],
                "To USD": rates.get("USD", "N/A") if "error" not in rates else "Error",
                "To INR": rates.get("INR", "N/A") if "error" not in rates else "Error",
                "To GBP": rates.get("GBP", "N/A") if "error" not in rates else "Error",
                "To EUR": rates.get("EUR", "N/A") if "error" not in rates else "Error",
            })
        
        # Display comparison table
        import pandas as pd
        df = pd.DataFrame(comparison_data)
        st.dataframe(df, use_container_width=True)
        
        # Map comparison
        st.markdown("---")
        st.markdown("### 📍 Stock Exchange Locations")
        
        for country in countries_to_compare:
            with st.expander(f"📌 {country}"):
                lat, lng = get_exchange_location(country)
                config = COUNTRY_CONFIG[country]
                st.write(f"**Stock Exchange:** {config['stock_exchange']}")
                st.write(f"**Coordinates:** ({lat}, {lng})")
                
                try:
                    display_map(country, lat, lng)
                except Exception as e:
                    st.error(f"Map loading error: {str(e)}")

# Footer
st.markdown("---")
st.markdown(
    """
    <div style='text-align: center; color: #666666; font-size: 12px;'>
    📊 Data provided by: Yahoo Finance, ExchangeRate-API<br>
    🤖 Powered by: Google Generative AI (Gemini) + LangChain<br>
    ⚡ Dashboard built with: Streamlit<br>
    © 2024 Global Financial Dashboard
    </div>
    """,
    unsafe_allow_html=True
)
