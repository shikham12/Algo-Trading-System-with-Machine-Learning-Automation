from data_fetcher import fetch_stock_data
from strategy import apply_indicators, generate_signals
from backtester import backtest
from sheets_logger import log_to_sheets
from ml_model import train_model
from telegram_bot import send_alert 

tickers = ['RELIANCE.NS', 'TCS.NS', 'INFY.NS']
for ticker in tickers:
    print(f"\n=== Processing {ticker} ===")
    df = fetch_stock_data(ticker)
    
    if df is None or df.empty:
        print(f"{ticker}: Data unavailable. Skipping.")
        continue

    df = apply_indicators(df)
    signals = generate_signals(df)
    print(f"Signals for {ticker}: {signals}")
    if signals == "BUY":
        send_alert("Buy signal generated for {ticker}.")

    trades, pnl = backtest(df, signals)
    log_to_sheets(trades, pnl)
    print(f"Logged trades and P&L for {ticker} to Google Sheets.\n")

    model, accuracy = train_model(df)
    if model:
        print(f"{ticker} ML Prediction Accuracy: {accuracy:.2f}")
    else:
        print(f"{ticker} ML model skipped (insufficient data)")

