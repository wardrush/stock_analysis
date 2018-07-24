"""
Weekly Rotation S&P 500

Objectives:
- Trade only long, large index stocks
- Only execute trades once a week
- Jump on upward trending stocks with expectation they will continue

Trading Universe:
- S&P 500

Filters:
- Minimum Average Volume (20 days) >= 1,000,000 shares
- Minimum Price >= 1 USD

Position Sizing:
- Maximum of 10 positions, so positions of 1/10 total equity

Entry Rules:
- End-of-week close of SPY >= 200-SMA with a 2% downside buffer
- 3-day RSI of a stock <= 50

Ranking:
- Stocks should be ranked by increasing 200-day ROC

Enter:
- Upon market open in new trading week

Exit:
- When stock is no longer in the top 10 S&P 500 ranked (replace with new outranker)
- When SPY is below the 200-SMA with a 2% downside buffer at end of week close
"""
from stock_analysis.stock import Stock
from stock_analysis import sp500_above_200_sma_w_buffer
from stock_analysis.technical_analysis import trend
import pandas as pd

# Trading universe is sp500
trading_universe = list(open('sp500.txt').readlines())
potential_trades_tickers = []
potential_trades_200dayROC = []


# Filters:
def weekly_rotation_filters(stock):
    if stock.filter_price(min_price=1) & stock.filter_avg_vol(n_days=20, min_volume=1000000) & \
            stock.filter_issue_type() & stock.filter_rsi(n_days=3, max_val=50):
        return True


if sp500_above_200_sma_w_buffer:
    for ticker in trading_universe:
        ticker = Stock(ticker)
        ticker.morningstar_lookup()
        if weekly_rotation_filters(ticker):
            potential_trades_tickers.append(ticker.ticker)
            potential_trades_200dayROC.append(trend.roc(ticker.close).tail(1).iloc[-1])
    temp = list(zip(potential_trades_tickers, potential_trades_200dayROC))
    potential_trades = pd.DataFrame(temp, columns=['Symbol', '200 Day ROC']).sort_values(by=potential_trades_200dayROC)
else:
    potential_trades = 'Market is unfavorable. Close current positions and do not open new ones'


