import pandas as pd
import matplotlib.pyplot as plt

from strategy import add_moving_averages, generate_signals
from metrics import calculate_returns


df = pd.read_csv("data/prices.csv")
df["Date"] = pd.to_datetime(df["Date"])

df = add_moving_averages(df)
df = generate_signals(df)
df = calculate_returns(df)

print(df)

plt.plot(df["Date"], df["market_value"], label="Buy and Hold")
plt.plot(df["Date"], df["strategy_value"], label="Moving Average Strategy")
plt.legend()
plt.title("Backtest Results")
plt.xlabel("Date")
plt.ylabel("Portfolio Value")
plt.show()