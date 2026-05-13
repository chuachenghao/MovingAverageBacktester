import yfinance as yf
import pandas as pd

def load_data(ticker, start, end):
    df = yf.download(ticker, start=start, end=end, progress=False)

    if isinstance(df.columns, pd.MultiIndex):
        tickers = df.columns.get_level_values(-1).unique()
        if len(tickers) == 1:
            df = df.droplevel(-1, axis=1)
        else:
            df.columns = [
                "_".join(str(part) for part in column if part)
                for column in df.columns
            ]

    df = df.reset_index()
    return df
