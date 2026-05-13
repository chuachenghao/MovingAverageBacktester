import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf

from strategy import add_moving_averages, generate_signals
from metrics import calculate_returns

ticker = "U11.SI"

df = yf.download(ticker, start="2020-01-01", end="2026-01-01")

df = df.reset_index()

df = add_moving_averages(df, short_window = 20, long_window = 50)
df = generate_signals(df)
df = calculate_returns(df)

print(df.tail())

plt.plot(df["Date"], df["market_value"], label="Buy and Hold")
plt.plot(df["Date"], df["strategy_value"], label="Moving Average Strategy")
plt.legend()
plt.title(f"{ticker} Backtest Results")
plt.xlabel("Date")
plt.ylabel("Portfolio Value")
plt.show()