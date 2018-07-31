import pandas as pd
import requests
from datetime import datetime, timedelta
from stock_analysis.technical_analysis import trend
from stock_analysis.technical_analysis import momentum
pd.core.common.is_list_like = pd.api.types.is_list_like  # Add newer pandas functionality to datareader
import pandas_datareader.data as web



class Stock:
    def __init__(self, ticker):
        self.ticker = ticker
        self.lookup = None  # Define lookup element to troubleshoot
        try:
            # Using Requests, 1. lookup company type 2. Decode JSON 3. Choose information from key 'issueType'
            self.issueType = requests.get(
                f'https://api.iextrading.com/1.0/stock/{self.ticker}/company').json()['issueType']
        except: # Find the particular exception for not having internet
            self.issueType = None




    def rb_lookup(self):
        """
        Return 1 year of OHLC and Volume data from robinhood
        """
        try:
            temp = web.DataReader(self.ticker, 'robinhood')
            temp = temp.reset_index()  # Remove multiindexing
            temp = temp.drop(columns=["interpolated", "session"])
            temp.rename(
                columns={
                    "symbol": "Symbol",
                    "begins_at": "Date",
                    "close_price": "Close",
                    "high_price": "High",
                    "low_price": "Low",
                    "open_price": "Open",
                    "volume": "Volume"
                }, inplace=True)
            self.close = temp.loc[:, "Close"]
            self.high = temp.loc[:, "High"]
            self.low = temp.loc[:, "Low"]
            self.open = temp.loc[:, "Open"]
            self.volume = temp.loc[:, "Volume"]
            self.dates = temp.loc[:, "Date"]
            self.lookup = 'robinhood'
        except AttributeError as e:
            raise AttributeError('Only string lookups supported')


    def morningstar_lookup(self, days_ago=300):
        """
        OHLC and Volume data from Morningstar.
        Start and end dates must be specified
        No apparent limit to how far back quotes go

        #BUG figure out why there is not data for every day. Use IEX?
        """
        try:
            startdate = datetime.today() - timedelta(days=days_ago)
            temp = web.DataReader(self.ticker, 'morningstar', start=startdate, end=datetime.today())
            temp = temp.reset_index()  # Remove multiindexing
            self.close = temp.loc[:, "Close"]
            self.high = temp.loc[:, "High"]
            self.low = temp.loc[:, "Low"]
            self.open = temp.loc[:, "Open"]
            self.volume = temp.loc[:, "Volume"]
            self.dates = temp.loc[:, "Date"]
            self.lookup = 'morningstar'
        except AttributeError as e:
            raise AttributeError('Only string lookups supported')

    """
    Begin filtering functions
    - 200-day SP500 SMA
    - Minimum Price
    - Average n-day Volume
    - Issue Type
    - RSI
    - ADX
    - ADR
    """
    @staticmethod
    def filter_sp500_200day_sma_w_buffer(buffer=0.02):
        # Pull general market data into global var so that data is not retrieved for every stock
        sp500 = Stock('SPY')
        sp500.morningstar_lookup()
        sma_w_buffer = trend.sma(sp500.close * (1 - buffer))
        if sp500.close.iloc[-1] < sma_w_buffer.iloc[-1]:
            sp500_above_200_sma_w_buffer = False
        elif sp500.close.iloc[-1] > sma_w_buffer.iloc[-1]:
            sp500_above_200_sma_w_buffer = True
        return sp500_above_200_sma_w_buffer

    def filter_price(self, min_price):
        try:
            is_valid = (self.close > min_price).any()
        except AttributeError:
            is_valid = False
        return is_valid


    def filter_avg_vol(self, n_days=50, min_volume=500000):
        is_valid = self.volume.tail(n_days).mean() > min_volume
        return is_valid


    def filter_issue_type(self, accepted_issue_types=['cs']):
        is_valid = False
        if self.issueType in accepted_issue_types:
            is_valid = True
        return is_valid


    def filter_rsi(self, n_days=3, **kwargs):
        rsi = momentum.rsi(self.close, n_days).tail(1).iloc[-1]
        if 'min_val' in kwargs:
            if rsi >= kwargs['min_val']:
                is_valid = True
            else:
                is_valid = False
        elif 'max_val' in kwargs:
            if rsi <= kwargs['max_val']:
                is_valid = True
            else:
                is_valid = False
        return is_valid

    def filter_adx(self, n_days=7):
        pass

    def filter_adr(self, n_days=10):
        pass

    """
    Begin Entrance / Exit Strategy
    - 2.5x ATR
    - n-% Profit
    - n-days Inactive
    """
    # Functions for calculating entrance/exit strategy
    def stop_2_5x_atr(self, n_days=10):
        pass

    def stop_n_pct_profit(self, entrance_price, profit=0.03):
        pass

    def stop_n_days_inactive(self, entrance_date, n_days=2):
        pass



