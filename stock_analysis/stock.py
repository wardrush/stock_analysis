import pandas as pd
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

    def morningstar_lookup(self):
        """
        OHLC and Volume data from Morningstar.
        Start and end dates must be specified
        No apparent limit to how far back quotes go
        """
        temp = web.DataReader(self.ticker, 'morningstar')
        temp = temp.reset_index()  # Remove multiindexing
        self.close = temp.loc[:, "Close"]
        self.high = temp.loc[:, "High"]
        self.low = temp.loc[:, "Low"]
        self.open = temp.loc[:, "Open"]
        self.volume = temp.loc[:, "Volume"]
        self.dates = temp.loc[:, "Date"]
        self.lookup = 'morningstar'

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