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
import datetime
import tqdm
import logging
import pandas as pd
# Begin package specific imports
from stock_analysis.stock import Stock
from stock_analysis.technical_analysis import momentum
from stock_analysis.exchanges import sp500, sp500_cleaned, big50


class WeeklyRotationSP500:

    def __init__(self, debug=False):
        print('Beginning analysis for Weekly Rotation Strategy')
        self.debug = debug
        self.logger = logging.getLogger(__name__)
        self.logger.info('Strategy: Weekly Rotation S&P 500')
        self.trading_universe = sp500.iloc[:, 0].sort_values()
        self.potential_trades_tickers = []
        self.potential_trades_200dayROC = []
        self.sp500_filter = Stock.filter_sp500_200day_sma_w_buffer()

    @staticmethod
    def weekly_rotation_filters(stock, debug=False):
        if debug:
            price_filter = stock.filter_price(min_price=1)
            avg_vol_filter = stock.filter_avg_vol(n_days=20, min_volume=1000000)
            issue_type_filter = stock.filter_issue_type(accepted_issue_types=['cs'])
            rsi_filter = stock.filter_rsi(n_days=3, max_val=50)
            if price_filter & avg_vol_filter & issue_type_filter & rsi_filter:
                return True
        else:
            if stock.filter_price(min_price=1) & stock.filter_avg_vol(n_days=20, min_volume=1000000) & \
                    stock.filter_issue_type(accepted_issue_types=['cs']) & stock.filter_rsi(n_days=3, max_val=50):
                return True

    def __call__(self):
        with tqdm.tqdm(total=len(self.trading_universe)) as prog_bar:
            if self.sp500_filter: # So that the calculation does not have to happen more than once
                for ticker in self.trading_universe:
                    self.logger.debug(f'Checking stock: {ticker}')
                    ticker = Stock(ticker)
                    ticker.get_issueType()
                    ticker.rb_lookup()
                    prog_bar.update()  # For progress bar in TQDM

                    if self.weekly_rotation_filters(ticker, debug=self.debug):
                        self.potential_trades_tickers.append(ticker.ticker)
                        self.potential_trades_200dayROC.append(momentum.roc(ticker.close).tail(1).iloc[-1])
                        self.logger.info(f'Stock {ticker.ticker} passed tests')
                temp = list(zip(self.potential_trades_tickers, self.potential_trades_200dayROC))
                potential_trades = pd.DataFrame(temp, columns=['Symbol','200 Day ROC']
                                                ).sort_values(by='200 Day ROC',ascending=False).reset_index(drop=True)
            else:
                potential_trades = 'Market is unfavorable. Close current positions and do not open new ones'
                self.info(f'Market benchmark is below chosen buffer. No more tests run.')

            # Visual non-logging
            print('\nAnalysis of trading universe completed. Results below...\n')
            print(potential_trades[:10])
            print(f'Printing to csv with filename: WeeklyRotation week of {datetime.date.isoformat(datetime.date.today())}')
            potential_trades.to_csv(f'WeeklyRotation week of {datetime.date.isoformat(datetime.date.today())}')
        return potential_trades
