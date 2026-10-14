# Crypto Portfolio Tracker

A desktop app for tracking cryptocurrency holdings spread across several exchanges in one place, with live prices, profit/loss and a portfolio breakdown.

Built in Python with CustomTkinter as my first larger programming project (Kaplan International College London, 2025).

## Features

- Live prices and 24-hour change from the [CoinGecko API](https://www.coingecko.com/en/api)
- Search coins by name or symbol and add them with amount and buy price
- Current value, 24h change and net profit/loss per coin and for the whole wallet
- Pie chart of wallet distribution (Plotly)
- Sort holdings by name, amount, profit, price or 24h change
- Wallet saved automatically to `wallet.json` and reloaded on start
- Input validation and error messages for empty or non-numeric input, missing selection and API failures

## Tech stack

| Layer | Technology |
|---|---|
| Language | Python 3 |
| GUI | CustomTkinter |
| Data | CoinGecko REST API (`requests`), `pandas` |
| Charts | Plotly |
| Storage | JSON file |

## Getting started

```bash
pip install -r requirements.txt
python app.py
```

## How to use

1. Search for a coin by name or symbol and select it from the list.
2. Enter the amount you hold and your buy price, then click **Add Coin**.
3. Click **Update Prices** to refresh values from the API.
4. Click **Pie Chart** to see how your wallet is distributed.

## Project structure

```
app.py        # Application: GUI, API calls, calculations
wallet.json   # Saved wallet data (starts empty, filled as you add coins)
requirements.txt
```

## What I learned

Working with a third-party REST API and handling its failures, structuring a GUI application, persisting data to a file, and validating user input.
