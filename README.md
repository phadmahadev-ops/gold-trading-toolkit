# 🌟 🔱 Gold Trading & Backtesting Toolkit (XAU/USD) 🚀

> Professional Python toolkit for downloading institutional **Gold (XAU/USD)** market data, running algorithmic backtests (`backtesting.py`), and analyzing multi-timeframe trading strategies. Engineered by **[Monetry.in](https://monetry.in)**.

---

## ✨ What's Inside? 📂

| Component | Description |
|-----------|-------------|
| 📥 **`data_fetcher.py`** | Downloads multi-timeframe Gold prices (`5m`, `15m`, `1h`, `1d`, `1wk`) via Yahoo Finance (`GC=F`). |
| 🔑 **`goldapi_fetcher.py`** | Fetches live historical spot prices directly via GoldAPI.io (`goldapi-b349ad8284f99bb826d49464d3bfba50-io`). |
| 📊 **`Gold_XAU_USD_Historical_Data.xlsx`** | **Ready-to-use Excel sheet** featuring 2-year XAU/USD historical futures, EMAs, trend signals, and GoldAPI spot prices! |
| 📈 **`strategies.py`** | Moving Average Crossover (`SmaCross`) and RSI momentum strategies. |
| ⚡ **`run_backtest.py`** | Executes backtests, computes profit factor, Sharpe ratio, win rate, and max drawdown. |

---

## 🚀 Quick Start Guide (For Traders & Learners)

### Step 1: Install Python
Ensure Python 3.9+ is installed.

### Step 2: Install Required Libraries
```bash
pip install -r requirements.txt
```

### Step 3: Download Fresh Gold Market Data
```bash
python data_fetcher.py
```

### Step 4: Run the Algorithmic Backtest
```bash
python run_backtest.py
```

---

## 🔗 Monetry Ecosystem & Free Tools

- 📊 **[Monetry.in](https://monetry.in)** — Free live F&O dashboard (option chain, OI heatmap, EMA signals, Gann levels, VIX range).
- 🔱 **[MahadevLevels35 PRO](https://github.com/phadmahadev-ops/mahadev-levels-pro)** — Free TradingView Pine Script v6 indicator.
- 📣 **[Telegram: @peoplesin](https://t.me/peoplesin)** — Live updates, signals & community.

---

## ⚠️ Disclaimer
**Educational and research use only.** Not investment advice or SEBI-registered recommendation. Trading financial derivatives (F&O / Spot Gold) carries substantial risk of loss. Use at your own risk.

<p align="center">Made with 🔱 by <a href="https://monetry.in">Monetry.in</a></p>
