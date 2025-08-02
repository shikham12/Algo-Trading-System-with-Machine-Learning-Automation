import yfinance as yf

import time

def fetch_stock_data(ticker, period="1y", interval="1d", retries=3):
    for attempt in range(retries):
        try:
            df = yf.download(
                ticker,
                period=period,
                interval=interval,
                progress=False,
                timeout=30,
                auto_adjust=False
            )
            if not df.empty:
                df.dropna(inplace=True)
                return df
        except Exception as e:
            print(f"Error fetching {ticker}: {e}")
        
        print(f"Retrying {ticker} in 5 seconds... (Attempt {attempt+1}/{retries})")
        time.sleep(5)

    print(f"Skipping {ticker} after {retries} failed attempts.")
    return None
