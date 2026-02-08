# ❓ FAQ & Troubleshooting

Quick answers to common questions and solutions to common problems.

---

## ❓ Frequently Asked Questions

### General Questions

**Q: Do I need to be a programmer to use this?**
A: No! Just follow the setup instructions. No coding knowledge required.

**Q: Is this free to use?**
A: Yes! The app itself is free. APIs have free tiers that are more than enough for personal use.

**Q: Is my data secure?**
A: Yes! API keys are stored locally in .env file (not shared), all connections are encrypted (HTTPS).

**Q: Can I use this for day trading?**
A: It's good for analysis and monitoring, but not designed for high-frequency trading. Always verify data before trading.

**Q: How often is data updated?**
A: Stock indices update in real-time, exchange rates update hourly, locations are static.

**Q: Can I add more countries?**
A: Yes! Edit `config.py` to add more countries. See FEATURE_GUIDE.md for details.

**Q: Does this work offline?**
A: No, you need internet to fetch live data from APIs.

**Q: Can I deploy this to my own server?**
A: Yes! See DEPLOYMENT.md for multiple options (Docker, cloud platforms, etc.).

---

## 🔑 API Key Questions

**Q: Where do I get a Google API key?**
A: Visit https://makersuite.google.com/app/apikey - it's free!

**Q: How do I get an ExchangeRate-API key?**
A: Go to https://www.exchangerate-api.com/, sign up (free), get key from dashboard.

**Q: Is the free tier good enough?**
A: Yes! Google's free tier is generous for personal use. ExchangeRate-API gives 1,500 requests/month.

**Q: What if I hit the API limit?**
A: For ExchangeRate-API, you can: upgrade plan, or wait until next month.

**Q: Can I use different API providers?**
A: Yes, with code modifications. See API_SETUP.md for alternatives.

---

## 🚀 Installation & Setup

**Q: How do I install Python?**
A: 
- **Mac**: `brew install python3`
- **Windows**: Download from python.org
- **Linux**: `sudo apt install python3`
Check version: `python3 --version` (should be 3.8+)

**Q: What if pip doesn't work?**
A: Try `pip3` instead. Or `python3 -m pip install ...`

**Q: Should I use a virtual environment?**
A: Yes! It's a best practice. Keeps dependencies isolated.
```bash
python3 -m venv venv
source venv/bin/activate  # Mac/Linux
venv\Scripts\activate     # Windows
```

**Q: What if requirements installation fails?**
A: Common issues:
- Check internet connection
- Use `pip3` instead of `pip`
- Try: `pip install --upgrade pip`
- Check Python version is 3.8+

**Q: Do I need Docker?**
A: No, it's optional. Only for containerized deployment.

---

## ⚙️ Configuration Issues

**Q: My .env file isn't being read**
A: 
- Check file is named `.env` (not `.env.txt`)
- It should be in the root directory
- Restart Streamlit after editing .env
- Try: `source .env` to verify syntax

**Q: Streamlit says "GOOGLE_API_KEY not found"**
A:
1. Does `.env` file exist? (check it's not `.env.example`)
2. Does it have `GOOGLE_API_KEY=...`?
3. Is the key valid (39+ characters)?
4. Restart Streamlit: press `Ctrl+C`, then run again

**Q: Should I use quotes around API keys?**
A: No! Format should be:
```
GOOGLE_API_KEY=AIzaSyD1234...
```
NOT:
```
GOOGLE_API_KEY="AIzaSyD1234..."  # Wrong!
```

---

## 🌐 App Not Working

**Q: App won't start at all**
A: Check:
1. `streamlit run app.py` command is correct
2. You're in the right directory
3. All dependencies installed: `pip install -r requirements.txt`
4. Python version is 3.8+

**Q: App starts but shows blank page**
A: 
- Wait 5-10 seconds for initial load
- Check browser console (F12) for errors
- Try refreshing page
- Check internet connection

**Q: Getting "ModuleNotFoundError"**
A: A package isn't installed:
```bash
# Reinstall everything
pip install -r requirements.txt
```

**Q: App very slow**
A: Normal for first request. Subsequent requests are faster.
- First load: 3-5 seconds
- Subsequent: 1-2 seconds
- If consistently slow, check internet

**Q: Streamlit crashes with error**
A: 
1. Note the error message
2. Check if internet is working
3. Try restarting: `Ctrl+C` then `streamlit run app.py`
4. Check .env file syntax
5. Verify API keys are valid

---

## 📊 Data Issues

**Q: Exchange rates showing "N/A"**
A: 
- EXCHANGE_RATE_API_KEY might be missing or invalid
- Add it to .env: `EXCHANGE_RATE_API_KEY=your_key`
- Restart Streamlit
- Check API status: https://www.exchangerate-api.com/status

**Q: Stock indices showing "Error"**
A:
- Yahoo Finance might be down (rare)
- Some indices might not be available
- Internet connection issue
- Try again in a moment

**Q: Map showing wrong location**
A:
- Check coordinates in `config.py`
- Zoom in to verify
- Use Google Maps (link provided) to double-check

**Q: Data is old**
A:
- Refresh with Browser refresh or `R` key
- Exchange rates update hourly
- Stock data updates in real-time
- Maps/locations are static

---

## 🤖 AI Agent Issues

**Q: AI Agent not responding**
A:
1. Check GOOGLE_API_KEY is valid
2. Wait 5+ seconds (it's thinking)
3. Try simpler question
4. Check internet connection

**Q: Agent giving wrong information**
A:
- AI can make mistakes
- Always verify important data
- Phrase question differently
- Use Dashboard view as reference

**Q: Agent response too slow**
A:
- First response: 3-5 seconds (normal)
- Complex queries: 5+ seconds
- Complex queries take longer
- Network latency affects speed

**Q: Agent can't find my country**
A:
- Only 6 countries supported (Japan, India, US, SK, China, UK)
- Try asking differently
- Use Dashboard view instead

---

## 📱 Map Issues

**Q: Maps not displaying**
A:
1. Check internet connection
2. Try refreshing page
3. Wait 2-3 seconds for load
4. Check browser console (F12) for errors
5. Try different browser

**Q: Map zoom not working**
A:
- Try scrolling instead
- Use browser zoom (Ctrl/Cmd + +/-)
- Try different browser

**Q: Can't see marker on map**
A:
- Check zoom level (13 is usually good)
- Click on map area to focus it
- Scroll to see full map
- Use Google Maps link provided below map

---

## 🚀 Deployment Issues

**Q: How do I deploy this?**
A: See DEPLOYMENT.md for 5 options:
1. Streamlit Cloud (easiest, free)
2. Heroku (easy, low cost)
3. AWS EC2 (powerful, free tier available)
4. Google Cloud Run (serverless, cheap)
5. DigitalOcean (simple, affordable)

**Q: Streamlit Cloud deployment fails**
A:
1. Check repository is public
2. Verify requirements.txt exists
3. Check app.py is in root directory
4. Set environment variables in Cloud console
5. Check build logs for specific errors

**Q: Docker build fails**
A:
1. Check Dockerfile is valid
2. Try: `docker build -t test .` to get full error
3. Ensure all files are included
4. Check Python version in Dockerfile

---

## 🔐 Security Questions

**Q: Is it safe to put API keys in .env?**
A: Yes, if:
- .env is in .gitignore (don't commit to git)
- .env is local only (don't share)
- Permissions are restricted (chmod 600)
- Keys are regularly rotated

**Q: How do I rotate API keys?**
A:
1. Go to each API provider's dashboard
2. Generate new key
3. Update .env file
4. Delete old key
5. Restart app

**Q: Someone got my API key - what do I do?**
A:
1. Go to API provider immediately
2. Delete the compromised key
3. Generate new key
4. Update .env and redeploy
5. Monitor usage/billing

**Q: Can I share my .env file?**
A: NO! Never share .env files. It contains sensitive credentials.
Share .env.example instead.

---

## 🐛 Uncommon Issues

**Q: "Port 8501 is already in use"**
A: Another process is using the port:
```bash
# Mac/Linux: Kill the process
lsof -i :8501
kill -9 <PID>

# Or use different port
streamlit run app.py --server.port 8502
```

**Q: "Permission denied" error**
A: Fix file permissions:
```bash
chmod +x quick_start.sh
chmod 600 .env
```

**Q: "Memory error" on weak computers**
A: 
- Close other applications
- Run: `python3 -m streamlit run app.py --logger.level=error`
- Consider cloud deployment

**Q: Encoding/Unicode errors**
A:
- Ensure file is UTF-8 encoded
- Set: `export PYTHONIOENCODING=utf-8`

---

## 📞 Getting Help

### Before Asking

1. **Check the docs** - START HERE
   - README.md (overview)
   - API_SETUP.md (API issues)
   - FEATURE_GUIDE.md (usage)
   - This file (FAQ)

2. **Check error message** - Read it carefully
   - Google the exact error text
   - Error often contains solution

3. **Try restarting**
   - Close app: Ctrl+C
   - Clear cache: streamlit cache clear
   - Restart: streamlit run app.py

4. **Verify basics**
   - Internet connection working?
   - API keys valid?
   - .env file exists and readable?
   - Python 3.8+ installed?

### Where to Get Help

| Issue | Where to Ask |
|-------|-------------|
| Python issues | https://stackoverflow.com/questions/tagged/python |
| Streamlit help | https://discuss.streamlit.io/ |
| LangChain help | https://python.langchain.com/ / GitHub Issues |
| API help | Check API provider documentation pages |
| Project issues | GitHub Issues (if shared on GitHub) |

### How to Report an Issue

Include:
1. Error message (exact text)
2. Command you ran (e.g., `streamlit run app.py`)
3. Your Python version (`python3 --version`)
4. Operating system (Windows, Mac, Linux)
5. Steps to reproduce
6. What you expected vs. what happened

---

## 🎓 Learning Resources

|  Topic | Resource |
|--------|----------|
| Python Basics | https://python.org/doc |
| Streamlit | https://docs.streamlit.io/ |
| LangChain | https://python.langchain.com/ |
| APIs | Check individual API documentation |
| Git/GitHub | https://docs.github.com/en/get-started |
| Docker | https://docs.docker.com/ |

---

## ✅ Troubleshooting Checklist

Use this checklist to debug issues:

- [ ] Restarted the app (Ctrl+C + run again)
- [ ] Refreshed browser (Ctrl+R or Cmd+R)
- [ ] Checked internet connection
- [ ] Verified .env file exists and has API keys
- [ ] Checked Python version is 3.8+
- [ ] Reinstalled requirements: `pip install -r requirements.txt`
- [ ] Checked browser console (F12) for errors
- [ ] Tried clearing Streamlit cache: `streamlit cache clear`
- [ ] Restarted computer (as last resort!)
- [ ] Checked API provider status pages

---

## 🎯 Quick Solutions

| Problem | Quick Fix |
|---------|-----------|
| App won't start | Check GOOGLE_API_KEY in .env |
| Data showing "N/A" | Add EXCHANGE_RATE_API_KEY to .env |
| Maps not loading | Refresh browser, check internet |
| AI Agent slow | Wait 5 seconds, check internet |
| Old data showing | Press R or refresh browser |
| Wrong country | Use Dashboard, change selector |
| Error on startup | `pip install -r requirements.txt` |

---

## 💭 Still Having Issues?

1. **Re-read relevant doc** - Most issues are covered
2. **Check API status pages** - Might be API problem
3. **Test individual modules** - Use Python shell to test
4. **Ask in community** - StackOverflow, GitHub Discussions
5. **Use web search** - "streamlit" + error message

---

## 🎊 Success!

If you got everything working, congratulations! 🎉

**Now enjoy exploring global markets! Share your dashboard with others!**

---

**Last updated**: February 2024
**For latest info**: Check README.md and other .md files
