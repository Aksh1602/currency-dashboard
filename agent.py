from langchain.agents import AgentType, initialize_agent, Tool
from langchain_google_genai import ChatGoogleGenerativeAI
from config import GOOGLE_API_KEY, COUNTRY_CONFIG
from currency_utils import get_exchange_rates, format_exchange_rates
from stock_utils import get_stock_indices, get_index_names, format_indices_data
from typing import Any
import warnings

# Suppress LangChain deprecation warnings
warnings.filterwarnings('ignore', message='.*initialize_agent.*deprecated.*')

def create_tools():
    """
    Create tools for the LangChain agent.
    
    Returns:
        List of Tool objects
    """
    
    def get_currency_tool(country: str) -> str:
        """Get currency information for a country."""
        if country not in COUNTRY_CONFIG:
            return f"Country {country} not found. Available: {', '.join(COUNTRY_CONFIG.keys())}"
        
        currency_code = COUNTRY_CONFIG[country]["code"]
        return f"Official currency of {country}: {currency_code}"
    
    def get_exchange_rate_tool(currency: str) -> str:
        """Get exchange rates for a currency."""
        rates = get_exchange_rates(currency)
        return format_exchange_rates(rates)
    
    def get_stock_indices_tool(country: str) -> str:
        """Get stock market indices for a country."""
        if country not in COUNTRY_CONFIG:
            return f"Country {country} not found."
        
        config = COUNTRY_CONFIG[country]
        indices = get_stock_indices(config["major_indices"])
        index_names = get_index_names(config["major_indices"])
        return format_indices_data(indices, index_names)
    
    def get_exchange_info_tool(country: str) -> str:
        """Get stock exchange information for a country."""
        if country not in COUNTRY_CONFIG:
            return f"Country {country} not found."
        
        config = COUNTRY_CONFIG[country]
        return f"Stock Exchange: {config['stock_exchange']}\nMajor Indices: {', '.join(config['major_indices'])}"
    
    tools = [
        Tool(
            name="Get Currency",
            func=get_currency_tool,
            description="Get the official currency code for a country. Input: country name (e.g., 'Japan')"
        ),
        Tool(
            name="Get Exchange Rate",
            func=get_exchange_rate_tool,
            description="Get exchange rates for a currency against USD, INR, GBP, EUR. Input: currency code (e.g., 'JPY')"
        ),
        Tool(
            name="Get Stock Indices",
            func=get_stock_indices_tool,
            description="Get current values of major stock indices for a country. Input: country name"
        ),
        Tool(
            name="Get Exchange Info",
            func=get_exchange_info_tool,
            description="Get information about the stock exchange in a country. Input: country name"
        ),
    ]
    
    return tools

def create_llm_agent():
    """
    Create a LangChain agent with Google Generative AI (Gemini).
    
    Returns:
        Agent executor
    """
    llm = ChatGoogleGenerativeAI(
        model="gemini-2.5-pro",
        google_api_key=GOOGLE_API_KEY,
        temperature=0.3
    )
    
    tools = create_tools()
    
    # Use initialize_agent (simpler and works with LangChain 0.1.0)
    agent = initialize_agent(
        tools=tools,
        llm=llm,
        agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
        verbose=False,  # Set to False to reduce noise
        handle_parsing_errors=True,
        max_iterations=10
    )
    
    return agent

def query_agent(agent: Any, query: str) -> str:
    """
    Query the LangChain agent.
    
    Args:
        agent: The agent executor
        query: User query
        
    Returns:
        Agent response
    """
    try:
        response = agent.invoke({"input": query})
        return response.get("output", str(response))
    except Exception as e:
        return f"Error: {str(e)}"
