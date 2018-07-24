import pandas as pd
from stock_analysis.technical_analysis import trend
from stock_analysis.technical_analysis import momentum
pd.core.common.is_list_like = pd.api.types.is_list_like  # Add newer pandas functionality
import pandas_datareader.data as web
import requests

class Stock:
    def __init__(self, ticker):
        self.ticker = ticker
        self.lookup = None  # Define lookup element to troubleshoot
        # Using Requests, 1. lookup company type 2. Decode JSON 3. Choose information from key 'issueType'
        self.issueType = requests.get(f'https://api.iextrading.com/1.0/stock/{self.ticker}/company').json()['issueType']


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



    def morningstar_lookup(self):
        """
        OHLC and Volume data from Morningstar.
        Start and end dates must be specified
        No apparent limit to how far back quotes go
        """
        try:
            temp = web.DataReader(self.ticker, 'morningstar')
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

    # Begin filtering functions
    def filter_price(self, min_price):
        is_valid = (self.close > min_price).any()
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

    # Functions for calculating entrance/exit strategy
    def stop_2_5x_atr(self, n_days=10):
        pass

    def stop_n_pct_profit(self, entrance_price, profit=0.03):
        pass

    def stop_n_days_inactive(self, entrance_date, n_days=2):
        pass

    def






