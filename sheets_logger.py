import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd

def log_to_sheets(trades, pnl, sheet_name="AlgoTradeLog"):
    scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
    creds = ServiceAccountCredentials.from_json_keyfile_name('credentials.json', scope)
    client = gspread.authorize(creds)
    
    sheet = client.open(sheet_name)
    
    # Trade log
    trade_ws = sheet.worksheet("TradeLog")
    trade_df = pd.DataFrame(trades, columns=["Date", "Action", "Price", "Shares"])
    # Convert all datetime columns to string format (ISO 8601)
    for col in trade_df.columns:
        if pd.api.types.is_datetime64_any_dtype(trade_df[col]):
            trade_df[col] = trade_df[col].dt.strftime('%Y-%m-%d %H:%M:%S')

    # Now update
    trade_ws.update([trade_df.columns.values.tolist()] + trade_df.values.tolist())

    # P&L summary
    pnl_ws = sheet.worksheet("Summary")
    pnl_ws.update('A1', [[f"Total P&L: {pnl}"]])


