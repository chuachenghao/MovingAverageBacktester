import matplotlib.pyplot as plt

def plot_results(df, ticker):
    plt.plot(df["Date"], df["market_value"], label="Buy and Hold")
    plt.plot(df["Date"], df["strategy_value"], label="Moving Average Strategy")

    plt.legend()
    plt.title(f"{ticker} Backtest Results")
    plt.xlabel("Date")
    plt.ylabel("Portfolio Value")
    plt.show()