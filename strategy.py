import ta
import pandas as pd

def apply_indicators(df):
    # Ensure we're working with a proper DataFrame structure
    if isinstance(df.columns, pd.MultiIndex):
        # If columns are multi-level, flatten them
        df.columns = [col[0] if isinstance(col, tuple) else col for col in df.columns]
    
    # Ensure Close column is a Series, not DataFrame
    close_series = df['Close'].squeeze() if hasattr(df['Close'], 'squeeze') else df['Close']
    
    df['RSI'] = ta.momentum.RSIIndicator(close_series).rsi()
    df['MA20'] = close_series.rolling(window=20).mean()
    df['MA50'] = close_series.rolling(window=50).mean()
    return df

def generate_signals(df):
    signals = []
    for i in range(1, len(df)):
        if df['Close'].iloc[i] > df['Close'].iloc[i-1]:  # Buy if price is up from yesterday
            signals.append((df.index[i], df['Close'].iloc[i], "BUY"))
    return signals

