import pandas_datareader.data as web


class Stock:
    def __init__(self, ticker):
        self.ticker = ticker
        self.lookup = None  # Define lookup element to troubleshoot

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
        self.close_price = temp.loc[:, "Close"]
        self.high_price = temp.loc[:, "High"]
        self.low_price = temp.loc[:, "Low"]
        self.open_price = temp.loc[:, "Open"]
        self.volume = temp.loc[:, "Volume"]
        self.dates = temp.loc[:, "Date"]
        self.lookup = 'rb'

    def morningstar_lookup(self):
        """
        OHLC and Volume data from Morningstar.
        Start and end dates must be specified
        No apparent limit to how far back quotes go
        """
        temp = web.DataReader(self.ticker, 'morningstar')
        temp = temp.reset_index()  # Remove multiindexing

        self.close_price = temp.loc[:, "Close"]
        self.high_price = temp.loc[:, "High"]
        self.low_price = temp.loc[:, "Low"]
        self.open_price = temp.loc[:, "Open"]
        self.volume = temp.loc[:, "Volume"]
        self.dates = temp.loc[:, "Date"]
        self.lookup = 'morningstar'


