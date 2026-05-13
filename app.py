import sys
sys.path.append("src")

import streamlit as st

from dataloader import load_data
from strategy import add_moving_averages, generate_signals
from backtester import run_backtest
from metrics import final_return, sharpe_ratio, max_drawdown, number_of_trades
from datetime import date


st.title("Moving Average Backtester")

ticker = st.text_input("Ticker", "U11.SI")

start = st.date_input("Start Date", value = date(2020, 1, 1))
end = st.date_input("End Date")

short_window = st.slider("Short Moving Average", 5, 100, 20)
long_window = st.slider("Long Moving Average", 20, 250, 50)

transaction_cost = st.slider(
    "Transaction Cost",
    0.0,
    0.01,
    0.001
)

if st.button("Run Backtest"):
    df = load_data(ticker, start, end)

    df = add_moving_averages(df, short_window, long_window)
    df = generate_signals(df)
    df = run_backtest(df, transaction_cost)

    st.subheader("Performance")

    st.write("Final Return:", round(final_return(df) * 100, 2), "%")
    st.write("Sharpe Ratio:", round(sharpe_ratio(df), 2))
    st.write("Max Drawdown:", round(max_drawdown(df) * 100, 2), "%")
    st.write("Number of Trades:", int(number_of_trades(df)))

    st.line_chart(
        df.set_index("Date")[["market_value", "strategy_value"]]
    )