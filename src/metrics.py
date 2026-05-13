import numpy as np

def final_return(df):
    return df["strategy_value"].iloc[-1] - 1

def sharpe_ratio(df):
    returns = df["strategy_return"].dropna()

    if returns.std() == 0:
        return 0

    return np.sqrt(252) * returns.mean() / returns.std()

def max_drawdown(df):
    running_max = df["strategy_value"].cummax()
    drawdown = df["strategy_value"] / running_max - 1
    return drawdown.min()

def number_of_trades(df):
    return df["trade"].sum()

def print_metrics(df):
    print("Final Return:", round(final_return(df) * 100, 2), "%")
    print("Sharpe Ratio:", round(sharpe_ratio(df), 2))
    print("Max Drawdown:", round(max_drawdown(df) * 100, 2), "%")
    print("Number of Trades:", int(number_of_trades(df)))