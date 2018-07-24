"""
Mean Revision Long

Objectives:
- Trade only long
- Take advantage of oversold stocks

Trading Universe:
- AMEX, NASDAQ, NYSE

Filters:
- No ETFs, pink sheets, or bulletin board stocks
- Minimum Average Daily Volume (50 days) >= 500,000 shares
- Dollar Volume >= 2,500,000 USD
- Minimum Price >= 1 USD

Position Sizing:
- Maximum of 10 positions
- Each positions risks 2% of total equity [(entry - stop loss) * # of shares]
    i.e. If entry = 20 USD, stop loss = 17 USD, and equity = 100,000 USD -> Dollar risk per share = 3 USD
         Therefore the position should be (2% * total equity) / cost per share -> 2,000 USD / 3 USD = 666 shares
- Max size is 10 % of equity. Following up with above calculation, the position would be 666 * 3 USD = 13,320 USD
    That is too big, so it would be clipped to 10,000 USD -> 500 shares

Entry Rules:
- Close of stock >= 150-day SMA
- 7-day ADX >= 45
- 10-day ADR >= 4%
- 3-day RSI <= 30

Ranking:
- Stocks should be ranked by decreasing RSI

Enter:
- Place limit order at market open of 4% lower than previous days close

Exit:
- Stop loss set at 2.5x the 10-day ATR
- When position has made >= 3% profit, close on next day open
- When 4 days have passed without either of above, exit market on close **Maybe change to open**
"""
from stock_analysis.stock import Stock
from stock_analysis.technical_analysis import trend
import pandas as pd

# Trading universe is AMEX, NYSE, NASDAQ
amex = pd.read_csv('amex.csv').iloc[:,0]
nyse = pd.read_csv('nyse.csv').iloc[:,0]
nasdaq = pd.read_csv('nasdaq.csv').iloc[:,0]
trading_universe = amex.append([nyse, nasdaq]).sort_values()

potential_trades_tickers = []
potential_trades_200dayROC = []


sma_days = 150
adx_days = 7
adr_days = 10
rsi_days = 3