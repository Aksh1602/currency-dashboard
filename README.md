# 🌍 Global Currency & Stock Market Dashboard

An intelligent Streamlit application powered by LangChain and Google Generative AI (Gemini) that provides real-time currency exchange rates, stock market indices, and interactive AI agent assistance for global financial information.

## 📋 Features

### 1. **Currency Information**
   - Official currency code for selected country
   - Real-time exchange rates (1 unit to USD, INR, GBP, EUR)
   - Data sourced from ExchangeRate-API

### 2. **Stock Market Data**
   - Major stock indices for each country
   - Real-time index values and percentage changes
   - Support for multiple indices per country
   - Data from Yahoo Finance

### 3. **International Coverage**
   - Japan (JPY - Nikkei 225, TOPIX)
   - India (INR - BSE SENSEX, NIFTY 50)
   - United States (USD - S&P 500, Dow Jones, Nasdaq)
   - South Korea (KRW - KOSPI)
   - China (CNY - Shanghai Composite)
   - United Kingdom (GBP - FTSE 100)

### 3. **Interactive Maps**
   - Interactive Folium maps (OpenStreetMap tiles by default — no API key required)
   - Optional Google Maps integration (requires API key and billing)
   - Location coordinates for each exchange

### 5. **AI Agent Assistant**
   - Natural language queries about currency and stock information
   - Powered by Google Generative AI (Gemini)
   - Intelligent tool usage with LangChain
   - Query history tracking

### 6. **Comparison View**
   - Compare multiple countries simultaneously
   - Side-by-side currency and exchange information
   - Multi-location map viewing

## 🛠️ Setup Instructions

### Prerequisites
- Python 3.8 or higher
- API keys from:
  - [Google Generative AI](https://makersuite.google.com/app/apikey)
  - [ExchangeRate-API](https://www.exchangerate-api.com/)
  - [Google Maps API](https://cloud.google.com/maps-platform/) (optional)

### Installation

1. **Clone/Navigate to the project directory**
   ```bash
   cd /path/to/currency
   ```

2. **Create and activate a virtual environment** (optional but recommended)
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   ```bash
   # Copy the example file
   cp .env.example .env
   
   # Edit .env and add your API keys
   # GOOGLE_API_KEY=your_key_here
   # EXCHANGE_RATE_API_KEY=your_key_here
   # GOOGLE_MAPS_API_KEY=your_key_here (optional)
   ```

### Running the Application

```bash
streamlit run app.py
```

The application will open in your default browser at `http://localhost:8501`

## 📊 Project Structure

```
currency/
├── app.py                 # Main Streamlit application
├── agent.py              # LangChain agent setup and tools
├── config.py             # Configuration and constants
├── currency_utils.py     # Currency and exchange rate utilities
├── stock_utils.py        # Stock market data utilities
├── maps_utils.py         # Google Maps integration
├── requirements.txt      # Python dependencies
├── .env.example          # Environment variables template
└── README.md            # This file
```

## 🔑 API Configuration

### Google Generative AI (Required)
1. Go to [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Create a new API key
3. Add to your `.env` file:
   ```
   GOOGLE_API_KEY=your_key_here
   ```

### ExchangeRate-API (Recommended)
1. Go to [ExchangeRate-API](https://www.exchangerate-api.com/)
2. Sign up for a free account (1,500 requests/month)
3. Get your API key from the dashboard
4. Add to your `.env` file:
   ```
   EXCHANGE_RATE_API_KEY=your_key_here
   ```

### Google Maps API (Optional)
1. Go to [Google Cloud Console](https://console.cloud.google.com/)
2. Create a new project
3. Enable Maps Platform
4. Create an API key
5. Add to your `.env` file:
   ```
   GOOGLE_MAPS_API_KEY=your_key_here
   ```

## 💻 Usage Examples

### Dashboard View
- Select "Dashboard" from the sidebar
- Choose a country from the dropdown
- View real-time currency rates and stock indices
- See the stock exchange location on an interactive map

### AI Agent View
- Select "AI Agent" from the sidebar
- Type natural language queries like:
  - "Give me currency and stock market details for Japan"
  - "What are the exchange rates for Indian Rupee?"
  - "Show me the latest stock prices for the S&P 500"
- View historical queries in the expandable history section

### Compare View
- Select "Compare Countries" from the sidebar
- Choose multiple countries to compare
- View side-by-side comparison table
- Explore each country's map location

## 🤖 AI Agent Capabilities

The AI agent can:
- Retrieve official currency codes for countries
- Fetch real-time exchange rates
- Get current stock market indices
- Provide stock exchange information
- Answer complex multi-step financial queries

### Sample Queries
```
"Give me currency and stock market details for Japan"
"Compare exchange rates for India and China"
"What are the major indices in South Korea?"
"Show me the latest S&P 500 performance"
```

## 📱 Technologies Used

| Component | Technology |
|-----------|-----------|
| **Frontend** | Streamlit |
| **LLM Framework** | LangChain |
| **AI Model** | Google Generative AI (Gemini) |
| **Maps** | Folium + Streamlit-Folium |
| **Stock Data** | Yahoo Finance (`yfinance`) |
| **Currency Data** | ExchangeRate-API |
| **HTTP Requests** | requests |
| **Data Processing** | pandas |

## 🚀 Deployment

### Deploy to Streamlit Cloud
1. Push your code to GitHub
2. Go to [Streamlit Cloud](https://streamlit.io/cloud)
3. Click "New app"
4. Connect your GitHub repository
5. Set environment variables in the Streamlit Cloud console
6. Deploy!

### Deploy to Other Platforms
- **Heroku:** Create `Procfile` with `web: streamlit run app.py`
- **AWS:** Use EC2 with proper security groups
- **Docker:** Create a Dockerfile with Python and Streamlit

## 📈 Data Sources

- **Stock Indices:** Yahoo Finance (real-time)
- **Currency Rates:** ExchangeRate-API (hourly updates)
- **Locations:** Manually configured coordinates
- **AI Responses:** Google Generative AI (Gemini)

## ⚠️ Limitations & Notes

1. **Free API Tier:**
   - ExchangeRate-API: 1,500 requests/month
   - Exchange rates updated hourly
   - Some historical data may be delayed

2. **Stock Market Data:**
   - Real-time data available for major exchanges
   - Some markets may have delayed quotes
   - After-hours trading not fully supported

3. **AI Agent:**
   - Requires internet connection
   - Response time depends on API latency
   - Accurate within configured tools' capabilities

## 🔐 Security Notes

- Never commit `.env` file to version control
- Use environment variables for all sensitive data
- Rotate API keys regularly
- Consider rate limiting for production use

## 📝 License

This project is open source and available under the MIT License.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📧 Support

For issues, questions, or suggestions:
1. Check existing documentation
2. Review error messages carefully
3. Verify API keys and internet connection
4. Check API service status pages

## 🔄 Version History

### v1.0.0
- Initial release
- Dashboard view with real-time data
- AI agent with natural language queries
- Country comparison functionality
- Interactive maps integration

---

**Built with ❤️ using Streamlit, LangChain, and Google Generative AI**

*Last Updated: February 2024*
