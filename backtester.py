def backtest(df, signals):
    cash = 100000
    shares = 0
    trade_log = []
    
    for date, price, action in signals:
        if action == "BUY" and cash >= price:
            shares = cash // price
            cash -= shares * price
            trade_log.append((date, "BUY", price, shares))

    if shares > 0:
        final_price = df['Close'].iloc[-1]
        cash += shares * final_price
        trade_log.append((df.index[-1], "SELL", final_price, shares))

    pnl = cash - 100000
    return trade_log, pnl
