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
'''
def generate_signals(df):
    signals = []
    for i in range(1, len(df)):
        rsi = df['RSI'].iloc[i]
        ma20 = df['MA20'].iloc[i]
        ma50 = df['MA50'].iloc[i]
        prev_ma20 = df['MA20'].iloc[i-1]
        prev_ma50 = df['MA50'].iloc[i-1]
        print(f"Day {i}: RSI={rsi}, MA20={ma20}, MA50={ma50}, Prev MA20={prev_ma20}, Prev MA50={prev_ma50}")
        
        # Relaxed condition for testing
        if rsi < 40 and ma20 > ma50 and prev_ma20 <= prev_ma50:
            print(f"Signal BUY at index {i}, date {df.index[i]}")
            signals.append((df.index[i], df['Close'].iloc[i], "BUY"))
    return signals
'''
