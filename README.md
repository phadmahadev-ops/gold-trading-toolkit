# 🌟 Gold Trading & Backtesting Toolkit (XAU/USD)

Welcome! This repository provides a complete, easy-to-use Python toolkit for downloading Gold market data and testing trading strategies automatically. Designed so simply that even a 10th-grade student can run it and put it on GitHub!

---

## 📂 What's Inside?
1. **`data_fetcher.py`**: Automatically downloads multi-timeframe Gold prices (`5m`, `15m`, `1h`, `1d`, `1wk`) for free using Yahoo Finance (`yfinance`).
2. **`strategies.py`**: Contains the Moving Average Crossover trading strategy.
3. **`run_backtest.py`**: Runs your strategy on historical gold data and shows you your profit/loss, win rate, and performance stats!
4. **`requirements.txt`**: List of required python libraries.

---

## 🚀 Step-by-Step Beginner Guide (GitHub & Local Setup)

### Step 1: Install Python
If you don't have Python installed, download and install it from [python.org](https://www.python.org/). Make sure to check **"Add Python to PATH"** during installation.

### Step 2: Download or Clone this Repository
Download this folder or clone it using Git:
```bash
git clone https://github.com/your-username/gold-trading-toolkit.git
cd gold-trading-toolkit
```

### Step 3: Install Required Libraries
Open your terminal (Command Prompt, PowerShell, or Terminal) inside the folder and run:
```bash
pip install -r requirements.txt
```

### Step 4: Download Gold Market Data
Run the data downloader script to fetch live and historical Gold prices (`GC=F`):
```bash
python data_fetcher.py
```
*This will create a `gold_data/` folder containing CSV files with historical prices.*

### Step 5: Run Your First Backtest!
Test how the Moving Average Crossover strategy performs on daily gold data:
```bash
python run_backtest.py
```
You will see a detailed performance report printed in your terminal!

---

## 🌐 How to Upload to GitHub (Step-by-Step)
1. Create a new repository on [GitHub.com](https://github.com).
2. Open your terminal in the project folder and run:
```bash
git init
git add .
git commit -m "Initial commit: Gold Trading & Backtesting Toolkit"
git branch -M main
git remote add origin https://github.com/YOUR-USERNAME/YOUR-REPO-NAME.git
git push -u origin main
```
3. Done! Your project is now live on GitHub for the world to see! 🚀

---
Made with ❤️ for traders, learners, and students.
