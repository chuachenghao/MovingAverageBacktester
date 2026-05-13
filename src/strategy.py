import pandas as pd

def add_moving_averages(df, short_window = 3, long_window = 5):
    df["short_ma"] = df["Close"].rolling(short_window).mean()
    df["long_ma"] = df["Close"].rolling(long_window).mean()
    return df

def generate_signals(df):
    df["signal"] = 0
    df.loc[df["short_ma"] > df["long_ma"], "signal"] = 1
    return df