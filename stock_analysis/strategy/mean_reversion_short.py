"""
Mean Revision Short

Objectives:
- Trade only short
- Take advantage of overbought stocks

Trading Universe:
- AMEX, NASDAQ, NYSE (same as mean-reversion long)

Filters:
- No ETFs, pink sheets, or bulletin board stocks
- Minimum Average Daily Volume (50 days) >= 500,000 shares
- Minimum Price >= 10 USD

Position Sizing:
- Maximum of 10 positions
- Each positions risks 2% of total equity [(entry - stop loss) * # of shares]
    i.e. If entry = 20 USD, stop loss = 17 USD, and equity = 100,000 USD -> Dollar risk per share = 3 USD
         Therefore the position should be (2% * total equity) / cost per share -> 2,000 USD / 3 USD = 666 shares
- Max size is 10 % of equity. Following up with above calculation, the position would be 666 * 3 USD = 13, 320 USD
    That is too big, so it would be clipped to 10,000 USD -> 500 shares

Entry Rules:
- 7-day ADX >= 50
- 10-day ADR >= 5%
- 3-day RSI >= 85

Ranking:
- Stocks should be ranked by increasing RSI

Enter:
- Place short limit order at market open of previous days close

Exit:
- Stop loss set at 2.5x the 10-day ATR
- When position has made >= 4% profit, close on next day open
- When 2 days have passed without either of above, exit market on close **Maybe change to open**
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
def mean_reversion_short_filters(stock):
    if stock.filter_price(min_price=10) & stock.filter_avg_vol(n_days=50, min_volume=500000) & \
            stock.filter_issue_type() & stock.filter_rsi(n_days=3, min_val=85) & stock.filter_n_day_adx(n_days)
        return True


for ticker in trading_universe:
    ticker = Stock(ticker)
    ticker.morningstar_lookup()
    if mean_reversion_short_filters(ticker):
        potential_trades_tickers.append(ticker.ticker)
        potential_trades_200dayROC.append(trend.roc(ticker.close).tail(1).iloc[-1])
temp = list(zip(potential_trades_tickers, potential_trades_200dayROC))
potential_trades = pd.DataFrame(temp, columns=['Symbol', '200 Day ROC']).sort_values(by=potential_trades_200dayROC)
