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
import pandas as pd
import tqdm

# Begin package specific imports
from stock_analysis.stock import Stock
from stock_analysis.exchanges import amex, nyse, nasdaq
from stock_analysis.technical_analysis import trend


def strategy_mean_reversion_long():
    # Trading universe is AMEX, NYSE, NASDAQ
    trading_universe = amex.append([nyse, nasdaq]).iloc[:, 0].sort_values()
    potential_trades_tickers = []
    potential_trades_3DayRSI = []

    # Filters
    def mean_reversion_long_filters(stock, debug=False):
            if debug:
                price_filter = stock.filter_price(min_price=1)
                avg_vol_filter = stock.filter_avg_vol(n_days=50, min_volume=500000)
                issue_type_filter = stock.filter_issue_type(non_accepted_issue_types=['et'])
                rsi_filter = stock.filter_rsi(n_days=3, max_val=30)
                adx_filter = stock.filter_adx(n_days=7, min_val=45)
                if price_filter & avg_vol_filter & issue_type_filter & rsi_filter & adx_filter:
                    return True
            if stock.filter_price(min_price=1) & stock.filter_avg_vol(n_days=50, min_volume=500000) & \
                    stock.filter_issue_type(accepted_issue_types=['cs']) & stock.filter_rsi(n_days=3, max_val=30) & \
                    stock.filter_adx(n_days=7, min_val=45):
                return True

    with tqdm.tqdm(total=len(trading_universe)) as prog_bar:
        for ticker in trading_universe:
            try:
                ticker = Stock(ticker)
                ticker.rb_lookup()
                prog_bar.update()
                if mean_reversion_long_filters(ticker):
                    potential_trades_tickers.append(ticker.ticker)
                    potential_trades_3DayRSI.append(trend.roc(ticker.close).tail(1).iloc[-1])
            except AttributeError:
                log


        temp = list(zip(potential_trades_tickers, potential_trades_3DayRSI))
        potential_trades = pd.DataFrame(temp,
                                        columns=['Symbol', '3 Day RSI']).sort_values(by=potential_trades_3DayRSI,
                                                                                ascending=False).reset_index(drop=True)

