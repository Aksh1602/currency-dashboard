# 🚀 Deployment Guide

This guide explains how to deploy your Currency & Stock Market Dashboard to various platforms.

## Option 1: Streamlit Cloud (Recommended - Easiest)

Streamlit Cloud is the easiest way to deploy Streamlit apps with minimal configuration.

### Prerequisites
- GitHub account
- Your repository pushed to GitHub

### Steps

1. **Push code to GitHub**
   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   git remote add origin https://github.com/YOUR_USERNAME/currency.git
   git push -u origin main
   ```

2. **Go to Streamlit Cloud**
   - Visit [share.streamlit.io](https://share.streamlit.io/)
   - Sign in with GitHub
   - Click "New app"

3. **Configure deployment**
   - Repository: Select your GitHub repo
   - Branch: `main`
   - Main file path: `app.py`

4. **Set environment variables**
   - Click "Advanced settings"
   - Under "Secrets" (equivalent to environment variables):
     ```
     GOOGLE_API_KEY = "your_key_here"
     EXCHANGE_RATE_API_KEY = "your_key_here"
     GOOGLE_MAPS_API_KEY = "your_key_here"
     ```

5. **Deploy**
   - Click "Deploy"
   - Wait for the app to build (2-3 minutes)
   - Your app will be live at `https://YOUR_USERNAME-currency.streamlit.app`

### Advantages
- ✅ FREE hosting
- ✅ Automatic deployments on git push
- ✅ Built-in SSL/HTTPS
- ✅ Easy secret management
- ✅ Automatic scaling

---

## Option 2: Docker + Heroku

Deploy using Docker containers on Heroku's platform.

### Prerequisites
- Docker installed
- Heroku CLI installed
- Heroku account

### Steps

1. **Create Dockerfile**
   ```dockerfile
   FROM python:3.10-slim
   
   WORKDIR /app
   
   COPY requirements.txt .
   RUN pip install -r requirements.txt
   
   COPY . .
   
   EXPOSE 8501
   
   CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
   ```

2. **Create .dockerignore**
   ```
   .env
   venv/
   .git
   __pycache__
   .DS_Store
   ```

3. **Build and push to Heroku**
   ```bash
   heroku login
   heroku container:login
   heroku create YOUR-APP-NAME
   heroku container:push web -a YOUR-APP-NAME
   heroku container:release web -a YOUR-APP-NAME
   ```

4. **Set environment variables**
   ```bash
   heroku config:set GOOGLE_API_KEY="your_key" -a YOUR-APP-NAME
   heroku config:set EXCHANGE_RATE_API_KEY="your_key" -a YOUR-APP-NAME
   heroku config:set GOOGLE_MAPS_API_KEY="your_key" -a YOUR-APP-NAME
   ```

5. **View your app**
   ```bash
   heroku open -a YOUR-APP-NAME
   ```

### Advantages
- ✅ Good for custom configurations
- ✅ Docker containerization
- ✅ Heroku has free tier (though limited)

---

## Option 3: AWS EC2

Deploy on Amazon EC2 for more control and scalability.

### Prerequisites
- AWS account
- SSH key pair created
- Basic Linux knowledge

### Steps

1. **Launch EC2 Instance**
   - Go to AWS Console → EC2
   - Click "Launch Instance"
   - Choose: Ubuntu 22.04 LTS (t3.micro for free tier)
   - Configure security group:
     - Allow SSH (22)
     - Allow HTTP (80)
     - Allow custom TCP (8501) for Streamlit

2. **Connect and setup**
   ```bash
   # SSH into instance
   ssh -i your-key.pem ubuntu@YOUR-EC2-IP
   
   # Update system
   sudo apt update && sudo apt upgrade -y
   
   # Install Python and dependencies
   sudo apt install python3-pip python3-venv -y
   
   # Clone your repository
   git clone https://github.com/YOUR_USERNAME/currency.git
   cd currency
   
   # Create virtual environment
   python3 -m venv venv
   source venv/bin/activate
   
   # Install requirements
   pip install -r requirements.txt
   ```

3. **Configure environment variables**
   ```bash
   nano .env
   # Add your API keys
   # Press Ctrl+X, Y, Enter to save
   ```

4. **Run Streamlit with Nginx reverse proxy**
   ```bash
   # Install Nginx
   sudo apt install nginx -y
   
   # Create Nginx config
   sudo nano /etc/nginx/sites-available/streamlit
   ```
   
   Add this configuration:
   ```nginx
   server {
       listen 80;
       server_name YOUR-DOMAIN-OR-IP;
   
       location / {
           proxy_pass http://localhost:8501;
           proxy_set_header Host $host;
           proxy_set_header X-Real-IP $remote_addr;
       }
   }
   ```

5. **Start services**
   ```bash
   # Enable Nginx
   sudo systemctl enable nginx
   sudo systemctl start nginx
   
   # Run Streamlit in background
   nohup streamlit run app.py > app.log 2>&1 &
   ```

6. **Access your app**
   - Visit `http://YOUR-EC2-IP` in your browser

### Advantages
- ✅ Full control
- ✅ EC2 free tier available (12 months)
- ✅ Scalable
- ✅ Better performance

---

## Option 4: Google Cloud Run

Serverless deployment on Google Cloud.

### Prerequisites
- Google Cloud account
- Google Cloud CLI installed
- Docker installed

### Steps

1. **Create Dockerfile** (same as Heroku section)

2. **Build and push to Google Container Registry**
   ```bash
   # Set your project ID
   export PROJECT_ID="your-gcp-project-id"
   
   # Build image
   docker build -t gcr.io/$PROJECT_ID/currency-app .
   
   # Push to registry
   docker push gcr.io/$PROJECT_ID/currency-app
   ```

3. **Deploy to Cloud Run**
   ```bash
   gcloud run deploy currency-app \
     --image gcr.io/$PROJECT_ID/currency-app \
     --region us-central1 \
     --platform managed \
     --allow-unauthenticated \
     --set-env-vars \
       GOOGLE_API_KEY=your_key,\
       EXCHANGE_RATE_API_KEY=your_key,\
       GOOGLE_MAPS_API_KEY=your_key
   ```

4. **Access your app**
   - Google Cloud will provide a public URL

### Advantages
- ✅ Serverless (pay only for usage)
- ✅ Auto-scaling
- ✅ Google Cloud free tier
- ✅ Good for variable traffic

---

## Option 5: DigitalOcean App Platform

Simple deployment with minimal setup.

### Prerequisites
- DigitalOcean account
- GitHub repository

### Steps

1. **Create App via DigitalOcean**
   - Go to DigitalOcean Console
   - Click "Create" → "App"
   - Connect to GitHub
   - Select repository and branch

2. **Configure App Settings**
   - Source: main
   - Auto-deploy: Enabled
   - HTTP Port: 8501

3. **Add Environment Variables**
   - In App Settings → Environment
   - Add GOOGLE_API_KEY, EXCHANGE_RATE_API_KEY, etc.

4. **Deploy**
   - Click "Create App"
   - Wait for deployment

### Advantages
- ✅ Simple UI
- ✅ GitHub integration
- ✅ Affordable pricing
- ✅ Good documentation

---

## Comparison Table

| Platform | Cost | Setup Time | Scalability | Static IPs | Best For |
|----------|------|-----------|------------|-----------|----------|
| **Streamlit Cloud** | Free | 5 min | ⭐⭐⭐ | ❌ | Hobbyists, Prototypes |
| **AWS EC2** | $0-10/mo | 20 min | ⭐⭐⭐⭐ | ✅ | Production |
| **Heroku** | Free-$50 | 10 min | ⭐⭐⭐ | ❌ | Small projects |
| **Google Cloud Run** | $0-10/mo | 15 min | ⭐⭐⭐⭐ | ❌ | Variable load |
| **DigitalOcean** | $5-40/mo | 10 min | ⭐⭐⭐ | ✅ | Growing apps |

---

## Monitoring & Maintenance

### After Deployment

1. **Monitor API usage**
   - Check ExchangeRate-API quota
   - Monitor Google Cloud API usage
   - Set up billing alerts

2. **Maintain your dependencies**
   - Keep Python packages updated
   - Security patches for dependencies
   ```bash
   pip install --upgrade -r requirements.txt
   ```

3. **Monitor application**
   - Check error logs regularly
   - Monitor response times
   - Track user activity

4. **Database backups** (if added later)
   - Regular automated backups
   - Test recovery procedures

---

## Troubleshooting Deployments

### App not starting
- Check logs: `docker logs` or platform-specific logs
- Verify all API keys are set
- Check Python version compatibility

### Slow performance
- Consider caching API responses
- Add database for historical data
- Optimize API calls

### API rate limits
- Implement caching
- Queue requests
- Upgrade API tier

---

## Next Steps

1. Choose your deployment platform
2. Follow the step-by-step guide above
3. Test the deployed app thoroughly
4. Set up monitoring and alerts
5. Plan for scaling as traffic grows

---

**Happy deploying! 🚀**
