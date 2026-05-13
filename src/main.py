from data_loader import load_data
from strategy import add_moving_averages, generate_signals
from backtester import run_backtest
from metrics import print_metrics
from plot import plot_results

ticker = "U11.SI"
start = "2020-01-01"
end = "2026-01-01"
short_window = 20
long_window = 50
transaction_cost = 0.001

df = load_data(ticker, start, end)

df = add_moving_averages(df, short_window, long_window)
df = generate_signals(df)
df = run_backtest(df, transaction_cost)

print(df.tail())
print_metrics(df)

plot_results(df, ticker)