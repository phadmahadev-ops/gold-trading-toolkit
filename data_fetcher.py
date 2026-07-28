import os
import pandas as pd
import yfinance as yf
import requests
from datetime import datetime, timedelta

TICKER = "GC=F"

timeframes = {
    "5m": {"period": "60d", "interval": "5m"},
    "15m": {"period": "60d", "interval": "15m"},
    "1h": {"period": "2y", "interval": "1h"},
    "1d": {"period": "2y", "interval": "1d"},
    "1wk": {"period": "2y", "interval": "1wk"},
}

def download_backtest_data(output_dir="gold_data"):
    os.makedirs(output_dir, exist_ok=True)
    print("Gold Data Download Started...\n")
    for tf_name, config in timeframes.items():
        print(f"Downloading {tf_name} data (Period: {config['period']}, Interval: {config['interval']})...")
        data = yf.download(tickers=TICKER, period=config["period"], interval=config["interval"], progress=False)
        if not data.empty:
            if isinstance(data.columns, pd.MultiIndex):
                data.columns = data.columns.get_level_values(0)
            df_clean = data[["Open", "High", "Low", "Close", "Volume"]].dropna()
            filename = os.path.join(output_dir, f"gold_{tf_name}.csv")
            df_clean.to_csv(filename)
            print(f"Successfully saved: {filename} ({len(df_clean)} rows)\n")
        else:
            print(f"Failed to fetch data for {tf_name}\n")

if __name__ == "__main__":
    download_backtest_data()
