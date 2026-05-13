def calculate_returns(df):
    df["market_return"] = df["Close"].pct_change()

    df["strategy_return"] = df["signal"].shift(1) * df["market_return"]

    df["market_value"] = (1 + df["market_return"]).cumprod()
    df["strategy_value"] = (1 + df["strategy_return"]).cumprod()

    return df