# 🔑 API Setup Guide

This guide will help you set up all the necessary API keys for the Global Currency & Stock Market Dashboard.

## Required APIs

### 1. Google Generative AI (Gemini) - **REQUIRED**

This is essential for the AI agent functionality.

**Steps:**
1. Go to [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Sign in with your Google account (create one if needed)
3. Click on "Create API Key"
4. Copy the generated API key
5. Paste it in your `.env` file:
   ```
   GOOGLE_API_KEY=your_copied_key_here
   ```

**Free Tier:** Generous free tier with 60 requests per minute

---

### 2. ExchangeRate-API - **RECOMMENDED**

For real-time currency exchange rates.

**Steps:**
1. Go to [ExchangeRate-API](https://www.exchangerate-api.com/)
2. Click "Sign Up" (Free tier available)
3. Create your account with email
4. Check your email and verify your account
5. Go to your Dashboard
6. Copy your API Key from the "Your API Key" section
7. Paste it in your `.env` file:
   ```
   EXCHANGE_RATE_API_KEY=your_key_here
   ```

**Free Tier:** 
- 1,500 requests per month (enough for ~50 per day)
- Updated hourly
- All major currencies supported

---

### 3. Maps (OpenStreetMap default, Google Maps OPTIONAL)

The app uses Folium with OpenStreetMap tiles by default — no API key or billing required. If you don't want to use Google Maps (which requires billing), you don't need to set `GOOGLE_MAPS_API_KEY`.

If you prefer to use Google Maps features, follow these steps to create a key (optional):

1. Go to [Google Cloud Console](https://console.cloud.google.com/)
2. Create a new project and enable the Maps Platform if desired
3. Create an API Key under "Credentials" and optionally restrict it
4. Paste the key into your `.env` file as `GOOGLE_MAPS_API_KEY=your_key_here`

Alternatives (no/low-cost):

- OpenStreetMap (used by default via Folium) — free and open-source
- Mapbox — free tier available (requires API key)
- Here Maps — developer tier available

Recommendation: For most users, keep `GOOGLE_MAPS_API_KEY` empty and rely on OpenStreetMap.

---

## Complete .env Configuration

After setting up all APIs, your `.env` file should look like:

```env
# Google Generative AI (Gemini) - REQUIRED
GOOGLE_API_KEY=AIzaSyD... (your 39-character key)

# ExchangeRate-API - RECOMMENDED
EXCHANGE_RATE_API_KEY=6a1c2b3d4e5f... (your key)

# Google Maps API - OPTIONAL
GOOGLE_MAPS_API_KEY=AIzaSyC7... (your key)

# CurrencyAPI (currently not used, for future expansion)
CURRENCY_API_KEY=your_currency_api_key_here
```

---

## Verification Checklist

After setting up your API keys, verify everything works:

✅ Can you open the .env file in an editor?
✅ Are all API keys properly formatted (no extra spaces)?
✅ Did you save the .env file?
✅ Is the .env file in the root directory of the project?

---

## Troubleshooting

### "GOOGLE_API_KEY not found" Error
- Make sure you created the `.env` file (not just `.env.example`)
- Verify the GOOGLE_API_KEY is spelled correctly
- Check there are no extra spaces around the `=` sign
- Ensure there are no quotes around the key value

### "Exchange rate features may be limited" Warning
- This is just a warning; the app will still work
- The dashboard will show "N/A" for exchange rates
- To fix, add your EXCHANGE_RATE_API_KEY to the `.env` file

### Maps not displaying
- Make sure the coordinates in `config.py` are correct
- Check if you have an internet connection
- If using Google Maps API, ensure it's enabled in Google Cloud Console

### "API rate limit exceeded"
- Your API has hit its monthly quota
- For ExchangeRate-API, you'll need to wait until next month or upgrade to paid plan
- For Google Maps, usage is tracked per calendar month

---

## API Service Status Pages

Monitor these pages if you encounter issues:

- [Google Cloud Status](https://status.cloud.google.com/)
- [ExchangeRate-API Status](https://www.exchangerate-api.com/status)

---

## Security Best Practices

⚠️ **IMPORTANT:**

1. **Never commit `.env` to git**
   - Add `.env` to your `.gitignore` file
   - Use `.env.example` as a template for others

2. **Rotate keys regularly**
   - Change your API keys every 3-6 months
   - Immediately if you suspect compromise

3. **Use environment variables in production**
   - Don't hardcode API keys in source files
   - Use platform-specific secret management

4. **Monitor API usage**
   - Check your API dashboards regularly
   - Set up billing alerts on Google Cloud

5. **Restrict API permissions**
   - Use IP restrictions if possible
   - Limit HTTP referrers for web APIs

---

## Alternative APIs (Optional Replacements)

If you prefer different providers:

### Alternative Exchange Rate APIs:
- ForexAPI (https://forexapi.io/)
- Fixer.io (https://fixer.io/)
- Open Exchange Rates (https://openexchangerates.org/)

### Alternative LLM Providers:
- OpenAI (GPT-4)
- Anthropic (Claude)
- Mistral AI
- DeepSeek

### Alternative Stock Data:
- Alpha Vantage (https://www.alphavantage.co/)
- IEX Cloud (https://iexcloud.io/)
- Polygon.io (https://polygon.io/)

---

## Next Steps

1. ✅ Set up all required API keys
2. ✅ Create your `.env` file with the keys
3. ✅ Run: `pip install -r requirements.txt`
4. ✅ Run: `streamlit run app.py`
5. ✅ Open http://localhost:8501 in your browser

---

**Need help?** Check the main README.md for more information!
