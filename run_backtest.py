import os
import pandas as pd
from backtesting import Backtest
from strategies import SmaCross

def run_strategy():
    csv_path = "gold_data/gold_1d.csv"
    if not os.path.exists(csv_path):
        print(f"Data file {csv_path} not found. Please run data_fetcher.py first.")
        return
    
    df = pd.read_csv(csv_path, parse_dates=True, index_col=0)
    bt = Backtest(df, SmaCross, cash=10000, commission=0.002)
    stats = bt.run()
    print(stats)
    return stats

if __name__ == "__main__":
    run_strategy()
