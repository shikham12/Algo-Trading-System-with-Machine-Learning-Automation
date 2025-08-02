# Algo-Trading System with ML & Automation

## 📌 Overview
A modular Python-based algorithmic trading system that:
- Fetches stock data for NIFTY 50 companies
- Applies an RSI + Moving Average crossover trading strategy
- Backtests on 6 months of historical data
- Predicts next-day movement using Logistic Regression
- Logs trades & P&L to Google Sheets automatically
- Sends Telegram alerts

---

## 🛠 Tech Stack
- **Python** (pandas, yfinance, scikit-learn, ta)
- **Google Sheets API** (gspread, oauth2client)
- **Telegram Bot API** 
- **Yahoo Finance API**

---

## 🚀 Features
- RSI < 30 + 20-DMA > 50-DMA Buy signal
- 6-month backtesting with P&L calculation
- Logistic Regression model for price prediction
- Google Sheets automation (TradeLog + Summary)
- Telegram alerts for trade signals

---

## 📂 Project Structure
data_fetcher.py # Fetch stock data
strategy.py # Apply indicators & generate signals
backtester.py # Run backtesting & calculate P&L
ml_model.py # Train ML model & evaluate accuracy
sheets_logger.py # Log results to Google Sheets
telegram_bot.py # Send alerts to Telegram
main.py # Orchestration script

---

## 📋 Installation
```bash
git clone https://github.com/shikham12/algo-trading-ml-automation.git
cd algo-trading-ml-automation
pip install -r requirements.txt

---

🔑 Setup Google Sheets API
1. Create a Google Cloud Project
2. Enable Google Sheets & Drive APIs
3. Create a Service Account & download credentials.json
4. Share your sheet with the service account email

---

## ▶ Usage
python main.py


