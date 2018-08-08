import pandas as pd
import requests
from datetime import datetime, timedelta
from stock_analysis.retrieve_data import retrieve_single_data, clean_single_data
from stock_analysis.technical_analysis import trend
from stock_analysis.technical_analysis import momentum
from stock_analysis.technical_analysis import volatility


class Stock:
    """
    The main class for passing information through this package-holds various relevant data to stock analysis
    """
    def __init__(self, ticker):
        self.ticker = ticker
        self.lookup = None  # Define lookup element to troubleshoot
        self.issueType = None

    def get_issueType(self):
        # Using Requests, 1. lookup company type 2. Decode JSON 3. Choose information from key 'issueType'
        self.issueType = requests.get(
            f'https://api.iextrading.com/1.0/stock/{self.ticker}/company').json()['issueType']

    def rb_lookup(self):
        """
        Robinhood API lookup used to update object attributes.
        Uses functions retrieve_single_data, clean_single_data from retrieve_data
        """
        temp = clean_single_data(retrieve_single_data(self.ticker))
        self.close = pd.to_numeric(temp.loc[:, "Close"])
        self.high = temp.loc[:, "High"]
        self.low = temp.loc[:, "Low"]
        self.open = temp.loc[:, "Open"]
        self.volume = temp.loc[:, "Volume"]
        self.dates = temp.loc[:, "Date"]
        self.lookup = 'robinhood_api'

    def morningstar_lookup(self, days_ago=300):
        """
        IMMEDIATELY DEPRECATED
        An OHLC lookup for n days_ago using morningstar's API
        Deprecation due to reliance on pandas_datareader
        #TODO put together a new version of this function in the same manner as the robinhood function

        :param days_ago:
        :return:
        """
        pass

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
        sp500.rb_lookup()
        try:
            sma_w_buffer = trend.sma(sp500.close * (1 - buffer))
            if sp500.close.iloc[-1] < sma_w_buffer.iloc[-1]:
                sp500_above_200_sma_w_buffer = False
            elif sp500.close.iloc[-1] > sma_w_buffer.iloc[-1]:
                sp500_above_200_sma_w_buffer = True
        except:
            # Find exception
            raise NotImplementedError
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

    def filter_issue_type(self, accepted_issue_types=None, non_accepted_issue_types=None):
        is_valid = False
        if accepted_issue_types:
            if self.issueType in accepted_issue_types:
                is_valid = True
        elif non_accepted_issue_types:
            if self.issueType in non_accepted_issue_types:
                is_valid = False
        return is_valid

    def filter_rsi(self, n_days=3, max_val=None, min_val=None):
        rsi = momentum.rsi(self.close, n_days).tail(1).iloc[-1]
        if min_val:
            if rsi >= min_val:
                is_valid = True
            else:
                is_valid = False
        elif max_val:
            if rsi <= max_val:
                is_valid = True
            else:
                is_valid = False
        else:
            is_valid = False
        return is_valid

    def filter_adx(self, n_days=7, max_val=None, min_val=None):
        adx = trend.adx(high=self.high, low=self.low, close=self.close, n_days=n_days).tail(1).iloc[-1]
        if min_val:
            if adx >= min_val:
                is_valid = True
            else:
                is_valid = False
        elif max_val:
            if adx <= max_val:
                is_valid = True
            else:
                is_valid = False
        else:
            is_valid = False
        return is_valid

    def filter_adr(self, n_days=10, max_val=None, min_val=None):
        adr = volatility.adr(self.close, n_days).tail(1).iloc[-1]
        if min_val:
            if adr >= min_val:
                is_valid = True
            else:
                is_valid = False
        elif max_val:
            if adr <= max_val:
                is_valid = True
            else:
                is_valid = False
        else:
            is_valid = False
        return is_valid

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



