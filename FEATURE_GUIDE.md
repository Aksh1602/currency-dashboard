# 📖 Feature Walkthrough

Complete guide to using every feature of the Global Currency & Stock Market Dashboard.

---

## 🎯 Dashboard View

The **Dashboard** is your main interface to view real-time financial data for a single country.

### How to Use the Dashboard

#### Step 1: Select a Country
1. Look at the left sidebar
2. Find the **"Select a Country"** dropdown
3. Choose from: Japan, India, USA, South Korea, China, or UK
4. The dashboard automatically updates with new data

#### Step 2: View Currency Information
In the **💱 Currency Information** card at the top:
- **Country**: Your selected country
- **Official Currency**: The currency code (e.g., JPY, INR, USD)

#### Step 3: Check Stock Exchange Details
In the **📍 Stock Exchange** card:
- **Exchange Name**: Official name of the stock exchange
- Located in the right column of the top section

#### Step 4: Analyze Exchange Rates
In the **💹 Exchange Rates** section:
- See how much 1 unit of the local currency is worth in:
  - **USD**: US Dollar
  - **INR**: Indian Rupee
  - **GBP**: British Pound
  - **EUR**: Euro

**Example**: If viewing Japan, you'll see:
```
1 JPY to USD = 0.0065
1 JPY to INR = 0.54
1 JPY to GBP = 0.0051
1 JPY to EUR = 0.0060
```

#### Step 5: Monitor Stock Market Indices
In the **📊 Stock Market Indices** section:
- **Index Name**: Full name of the index
- **Current Value**: Latest price or level
- **Change %**: Percentage change from previous close
  - 📈 Green up arrow = index went up
  - 📉 Red down arrow = index went down

**Example for Japan**:
```
Nikkei 225
Value: 28,500.50
Change: 📈 1.45%

TOPIX (Tokyo Stock Price Index)
Value: 2,010.25
Change: 📉 -0.23%
```

#### Step 6: View Stock Exchange Location
In the **📍 Stock Exchange Location** section:
- **Interactive Map**: Shows where the exchange is located
- **Zoom**: Scroll to zoom in/out
- **Click**: Blue marker shows the exact location

**Map Features**:
- Zoom in for detailed street view
- Hover over marker to see exchange name
- Fullscreen option available

### Dashboard Tips

💡 **Refresh Data**: Streamlit automatically refreshes when you change country
💡 **Performance**: First load may take 3-5 seconds while fetching data
💡 **Data Freshness**: Stock data is real-time, exchange rates update hourly
💡 **Compare Changes**: Switch between countries to spot market trends
💡 **Track Favorites**: Take notes of indices you want to monitor

---

## 🤖 AI Agent View

The **AI Agent** is a natural language assistant powered by Google's Gemini AI that answers questions about currencies and stock markets.

### How to Use the AI Agent

#### Step 1: Access AI Agent Mode
1. Click **"AI Agent"** in the sidebar under "Select View"
2. You'll see the agent interface with a text input box

#### Step 2: Ask Natural Language Questions
Type your question in natural language (like you're speaking to a person):
- "What is the currency of Japan?"
- "Show me exchange rates for India"
- "What are the major stock indices in the US?"

#### Step 3: Use Sample Queries
Streamlit provides pre-made sample queries you can click:
- "Give me currency and stock market details for [Country]"
- "Compare currency exchange rates for [Country1] and [Country2]"
- "What are the major stock indices in [Country]?"
- "Get live/indexed values of indices..."

#### Step 4: View Agent Response
The agent will:
1. Analyze your question
2. Identify what information you need
3. Call the relevant tools (currency, indices, etc.)
4. Provide a comprehensive answer

**Example Query**:
```
Q: "Give me currency and stock market details for Japan"

Agent will respond with:
- Official Currency: JPY
- Exchange Rates: JPY to USD, INR, GBP, EUR
- Major Indices: Nikkei 225, TOPIX
- Current Values: [real-time data]
- Stock Exchange: Tokyo Stock Exchange
```

#### Step 5: Track Query History
1. Look for **"📜 Query History"** at the bottom
2. Click to expand and see previous questions and answers
3. Useful for reference and pattern recognition

### AI Agent Capabilities

The AI Agent can handle:

✅ **Currency Queries**
- "What is the official currency of South Korea?"
- "Get exchange rates for the British Pound"
- "Show me INR to USD conversion rate"

✅ **Stock Market Queries**
- "What are major indices in China?"
- "Get latest S&P 500 value"
- "Compare stock exchanges in Japan and India"

✅ **Complex Multi-step Queries**
- "Give me complete financial details for [country]"
- "Compare economic indicators between two countries"
- "What's the current state of the US stock market?"

✅ **Combination Queries**
- "Show me currency and market data for Japan"
- "List all indices and their current values for [country]"
- "Get exchange rates and stock prices for..."

### AI Agent Tips

💡 **Clear Language**: Ask like you're speaking naturally
💡 **Specific**: More specific queries get better answers
💡 **Wait Time**: AI takes 3-5 seconds to think and respond
💡 **Errors**: If something fails, ask differently
💡 **Follow-ups**: Ask follow-up questions based on responses
💡 **Complex Queries**: The agent is intelligent enough to ask multiple tools for answers

### Sample Conversations

**Conversation 1: Getting Started**
```
User: "Tell me about Japan's currency"
Agent: "The official currency of Japan is the Japanese Yen (JPY)..."

User: "What are the exchange rates?"
Agent: "1 JPY equals: USD 0.0065, INR 0.54, GBP 0.0051, EUR 0.0060"

User: "And the stock market?"
Agent: "Major indices are Nikkei 225 and TOPIX with values..."
```

**Conversation 2: Market Analysis**
```
User: "Compare India and China stock markets"
Agent: "India has BSE with SENSEX and NIFTY indices, while China has SSE with..."

User: "Which is stronger?"
Agent: "Based on [analysis], India's market shows [metrics]..."
```

---

## 🔀 Compare Countries View

The **Compare** feature lets you analyze multiple countries side-by-side.

### How to Use Compare View

#### Step 1: Access Compare Mode
1. Click **"Compare Countries"** in the sidebar
2. You'll see a multi-select dropdown

#### Step 2: Select Countries to Compare
1. Click the dropdown that says **"Select countries to compare"**
2. Check multiple countries
   - Example: Japan, India, USA
3. Up to 6 countries can be compared

#### Step 3: View Comparison Table
A table appears showing:
| Country | Currency | Exchange | To USD | To INR | To GBP | To EUR |
|---------|----------|----------|--------|--------|--------|--------|
| Japan | JPY | TSE | value | value | value | value |
| India | INR | BSE | value | value | value | value |
| USA | USD | NYSE | value | value | value | value |

**Features**:
- All data is side-by-side
- Easy currency rate comparison
- Identify strongest/weakest currencies
- Compare stock exchanges

#### Step 4: Review Stock Exchange Locations
Below the table:
1. Each country has an expandable section
2. Click any country to see its details:
   - **Stock Exchange Name**
   - **Coordinates** (latitude, longitude)
   - **Interactive Map** showing location

### Compare View Tips

💡 **Analysis**: Quickly spot which currency is strongest against major currencies
💡 **Insights**: Compare multiple countries' financial infrastructure
💡 **Export**: You can screenshot the table for reports
💡 **Trading**: Useful for cross-border investment decisions
💡 **Research**: Compare economic indicators across regions

### Example Comparisons

**Asia-Pacific Analysis**
- Select: Japan, India, South Korea, China
- Compare: Exchange rates and market sizes
- Insights: Currency volatility and market depth

**BRICS Comparison**
- Select: India, China, South Africa (if added)
- Compare: Emerging market dynamics
- Insights: Trade opportunities

**G7 Comparison**
- Select: USA, UK (and others if added)
- Compare: Developed market dynamics
- Insights: Stable currency valuations

---

## 🗺️ Map Features

Maps are integrated throughout the dashboard showing stock exchange locations.

### How to Use Maps

#### Interactive Features
- **Zoom**: Scroll up/down to zoom
- **Pan**: Click and drag to move around
- **Marker**: Blue pin shows exchange HQ
- **Info**: Click marker for exchange name
- **Fullscreen**: Button to expand (usually top-right)

#### Understanding the Map
- **Blue Marker**: Exact location of stock exchange
- **Street Map**: OpenStreetMap (free, detailed)
- **Zoom Level**: 13 for detailed city view
- **Coordinates**: Latitude and Longitude shown

#### Map Locations
```
🇯🇵 Japan (Tokyo Stock Exchange)
   Coordinates: 35.6762°N, 139.7674°E

🇮🇳 India (Bombay Stock Exchange)
   Coordinates: 19.0760°N, 72.5762°E

🇺🇸 USA (New York Stock Exchange)
   Coordinates: 40.7074°N, -74.0113°W

🇰🇷 South Korea (Korea Exchange)
   Coordinates: 37.5665°N, 126.9780°E

🇨🇳 China (Shanghai Stock Exchange)
   Coordinates: 31.2304°N, 121.4737°E

🇬🇧 UK (London Stock Exchange)
   Coordinates: 51.5128°N, -0.0843°W
```

### Map Tips

💡 **Street View**: Zoom in to street-level detail
💡 **Precise Location**: Perfect for visiting the exchange
💡 **Google Maps Link**: Available in text info below map
💡 **Multiple Maps**: Compare View shows all exchanges
💡 **Navigation**: Use maps for travel planning

---

## 📊 Understanding the Data

### Exchange Rates Explained

An exchange rate shows how much of one currency you get for another.

**Example**: If JPY to USD = 0.0065:
- You get 0.0065 US Dollars for 1 Japanese Yen
- OR you need 154.5 Yen to get 1 Dollar (1 ÷ 0.0065)

**Use Case**: 
```
You want to buy: $100 USD worth of goods while in Japan
1 USD = 154.5 JPY
So you need: 100 × 154.5 = 15,450 JPY
```

### Stock Index Explained

A stock index is like a report card for a country's stock market.

**Example**: Nikkei 225
- Tracks: 225 largest Japanese companies
- Range: Typically 20,000 - 35,000
- Change: +1.45% means up 1.45% today
- Use: Gauge overall market health

**Why it matters**:
- 📈 Going up = economy doing well
- 📉 Going down = economic concerns
- Volatile = uncertain markets
- Stable = confident markets

### Percentage Changes

`Change: 📈 +1.45%` means:
- Yesterday's close: 28,000
- Today's close: 28,406 (1.45% higher)
- Good for investors holding these stocks

---

## 🎨 Customization Tips

### Change Default Country
Edit `config.py`, find `COUNTRY_CONFIG`, modify the order.

### Add More Countries
Add to `COUNTRY_CONFIG` dictionary with:
- Currency code
- Stock exchange name
- Index symbols
- Coordinates

### Customize AI Behavior
Edit `agent.py` to add:
- More tools
- Different tools
- Tool descriptions
- Tool logic

### Adjust Update Frequency
Streamlit re-runs entire script when you change input. Data is always fresh.

---

## ⌨️ Keyboard Shortcuts

| Shortcut | Action |
|----------|--------|
| `R` | Refresh/Rerun app |
| `C` | Clear cache |
| `↑` or `↓` | Navigate dropdowns |
| `Enter` | Confirm selection |

---

## 🆘 When Something Goes Wrong

### Issue: "No data for index"
**Solution**: 
- Market may be closed
- API temporary issue
- Try again in a moment
- Check ExchangeRate-API status

### Issue: "Map not loading"
**Solution**:
- Check internet connection
- Refresh browser
- Verify coordinates are valid
- Check browser console for errors

### Issue: "AI Agent not responding"
**Solution**:
- Check GOOGLE_API_KEY is valid
- Verify internet connection
- Wait - AI takes 3-5 seconds
- Try simpler query

### Issue: "Old data showing"
**Solution**:
- Click `R` key to refresh
- Streamlit will re-run and fetch new data
- Data is live, but may have slight delay

---

## 📱 Mobile Usage

The dashboard works on mobile but with limitations:

✅ **Works Well**:
- Dashboard view
- Comparison table
- Reading data

⚠️ **Limitations**:
- Maps may be small
- Dashboard may require scrolling
- Dropdowns work but harder to use

**Mobile Tips**:
- Use landscape mode for better view
- Pinch to zoom on maps
- Tap country dropdown carefully
- Use AI Agent (easier on mobile)

---

## 🔄 Workflows & Use Cases

### Workflow 1: Daily Market Check
1. Open Dashboard
2. Select your target country
3. Check exchange rates and indices
4. Note any significant changes
5. Share insights with team

### Workflow 2: Investment Analysis
1. Go to Compare View
2. Select 2-3 countries to compare
3. Analyze currency strength
4. View market indices
5. Make investment decisions

### Workflow 3: Travel Planning
1. Dashboard view
2. Select destination country
3. Check current exchange rate
4. Plan currency exchange
5. View location on map

### Workflow 4: Market Research
1. Use AI Agent
2. Ask questions about multiple countries
3. Get detailed financial information
4. Compare responses
5. Export findings

---

## ✨ Best Practices

✅ **DO**:
- Refresh regularly for latest data
- Use AI Agent for complex questions
- Compare multiple countries
- Check maps for locations
- Export important findings

❌ **DON'T**:
- Rely solely on this for trading
- Trust data older than 1 hour
- Share API keys publicly
- Use in high-frequency trading
- Ignore risk warnings

---

**Now you're ready to explore! Start with the Dashboard and try all features. Happy analyzing! 📊**
