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
import pandas as pd
import tqdm
# Begin package specific imports
from stock_analysis.exchanges import amex, nyse, nasdaq
from stock_analysis.stock import Stock
from stock_analysis.technical_analysis import momentum



def strategy_mean_reversion_short():

    # Filters:
    def mean_reversion_short_filters(stock, debug=False):
        if debug:
            price_filter = stock.filter_price(min_price=10)
            avg_vol_filter = stock.filter_avg_vol(n_days=50, min_volume=500000)
            issue_type_filter = stock.filter_issue_type(non_accepted_issue_types=['et'])
            rsi_filter = stock.filter_rsi(n_days=3, min_val=85)
            adx_filter = stock.filter_adx(n_days=7, min_val=50)
            if price_filter & avg_vol_filter & issue_type_filter & rsi_filter & adx_filter:
                return True
        else:
            if stock.filter_price(min_price=10) & stock.filter_avg_vol(n_days=50, min_volume=500000) & \
                    stock.filter_issue_type(non_accepted_issue_types=['et']) & stock.filter_rsi(n_days=3, min_val=85) & \
                stock.filter_adx(n_days=7, min_val=50):
                return True
            
    print('Beginning Mean Reversion Short strategy')
    trading_universe = amex.append([nyse, nasdaq]).sort_values()
    potential_trades_tickers = []
    potential_trades_3DayRSI = []
    # Progress bar
    with tqdm.tqdm(total=len(trading_universe)) as prog_bar:


        for ticker in trading_universe:
            ticker = Stock(ticker)
            ticker.morningstar_lookup()
            prog_bar.update()
            if mean_reversion_short_filters(ticker):
                potential_trades_tickers.append(ticker.ticker)
                potential_trades_3DayRSI.append(momentum.roc(ticker.close).tail(1).iloc[-1])
        temp = list(zip(potential_trades_tickers, potential_trades_3DayRSI))
        potential_trades = pd.DataFrame(temp, columns=['Symbol', '3 Day RSI']
                                        ).sort_values(by=potential_trades_3DayRSI).reset_index(drop=True)

        print('Analysis of trading universe completed. Results below...')
        print(potential_trades[:10])
        print(f'Printing to csv: Mean Reversion Short week of {datetime.date.isoformat(datetime.date.today())}')
        potential_trades.to_csv(f'Mean Reversion Short week of {datetime.date.isoformat(datetime.date.today())}')
