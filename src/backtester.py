def run_backtest(df, transaction_cost=0.001):
    df["market_return"] = df["Close"].pct_change()

    df["position"] = df["signal"].shift(1)

    df["trade"] = df["position"].diff().abs()

    df["strategy_return"] = (
        df["position"] * df["market_return"]
        - df["trade"] * transaction_cost
    )

    df["market_value"] = (1 + df["market_return"]).cumprod()
    df["strategy_value"] = (1 + df["strategy_return"]).cumprod()

    return df