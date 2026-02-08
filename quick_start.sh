#!/bin/bash

# Quick Start Script for Currency & Stock Market Dashboard
# This script helps you get up and running in minutes

echo "🌍 Global Currency & Stock Market Dashboard - Quick Start"
echo "=========================================================="
echo ""

# Check Python version
echo "✓ Checking Python version..."
python_version=$(python3 -c 'import sys; print(".".join(map(str, sys.version_info[:2])))')
echo "  Found Python $python_version"
echo ""

# Create virtual environment
echo "✓ Creating virtual environment..."
python3 -m venv venv
echo "  Virtual environment created"
echo ""

# Activate virtual environment
echo "✓ Activating virtual environment..."
source venv/bin/activate  # On Windows, use: venv\Scripts\activate
echo "  Virtual environment activated"
echo ""

# Install requirements
echo "✓ Installing dependencies..."
pip install -r requirements.txt
echo "  Dependencies installed successfully"
echo ""

# Setup environment variables
echo "✓ Setting up environment variables..."
if [ ! -f .env ]; then
    cp .env.example .env
    echo "  Created .env file from template"
    echo ""
    echo "⚠️  IMPORTANT: Edit the .env file with your API keys:"
    echo "   1. GOOGLE_API_KEY - Get from https://makersuite.google.com/app/apikey"
    echo "   2. EXCHANGE_RATE_API_KEY - Get from https://www.exchangerate-api.com/"
    echo "   3. GOOGLE_MAPS_API_KEY (optional) - Get from https://cloud.google.com/maps-platform/"
    echo ""
else
    echo "  .env file already exists"
    echo ""
fi

# Run the app
echo "✓ Starting the application..."
echo "  Your dashboard will open at http://localhost:8501"
echo ""
streamlit run app.py
