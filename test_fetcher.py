import os
import pandas as pd
from data_fetcher import download_backtest_data

def test_download():
    download_backtest_data("test_gold_data")
    assert os.path.exists("test_gold_data/gold_1d.csv")
    df = pd.read_csv("test_gold_data/gold_1d.csv")
    assert not df.empty
    assert "Close" in df.columns
    # Cleanup
    for f in os.listdir("test_gold_data"):
        os.remove(os.path.join("test_gold_data", f))
    os.rmdir("test_gold_data")
