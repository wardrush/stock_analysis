import pandas_datareader.data as web
import pandas as pd


class Stock:
    def __init__(self, ticker):
        self.ticker = ticker

    def rb_lookup(self):
        """
        Return 1 year of OHLC and Volume data from robinhood
        """
        temp = web.DataReader(self.ticker, 'robinhood')
        pvtdf = pd.pivot_table(temp, index=['Symbol', 'Date'], values=['high_price'], aggfunc=sum)
        """
        #temp = temp.insert(loc=len, column='Date', value=None)
        #temp = temp.insert(loc=0, column='Symbol', value=None)
        temp = temp.reset_index()
        self.close_price = temp.loc[:, 'close_price']
        self.high_price = temp.loc[:, 'high_price']
        self.low_price = temp.loc[:, 'low_price']
        self.open_price = temp.loc[:, 'open_price']
        self.volume = temp.loc[:, 'volume']
        self.dates = temp.loc[:, '']
        transdat = temp.loc[:, ["open_price", "high_price", "low_price", "close_price"]]
        transdat.rename(columns={"open_price": "Open", "high_price": "High", "low_price": "Low", "close_price": "Close"}, inplace=True)
        print(self.dates)
        """

    def morningstar_lookup(self):
        """
        OHLC and Volume data from Morningstar.
        Start and end dates must be specified
        No apparent limit to how far back quotes go
        """
        temp = web.DataReader(self.ticker, 'morningstar')
        temp = temp.reset_index(level=[0, 1])
        print(temp.head())
        """
        self.close_price = temp.loc[:, 'close_price']
        self.high_price = temp.loc[:, 'high_price']
        self.low_price = temp.loc[:, 'low_price']
        self.open_price = temp.loc[:, 'open_price']
        self.volume = temp.loc[:, 'volume']
        transdat = temp.loc[:, ["open_price", "high_price", "low_price", "close_price"]]
        transdat.rename(columns={"open_price": "Open", "high_price": "High", "low_price": "Low", "close_price": "Close"}, inplace=True)
        print(transdat.head())
        """


#######################################################
pos_path = 'C:\\Users\\Ward Rushton\\Documents\\Finances\\Portfolio\\2018_06 Portfolio Data\\mod_book1.csv'
########################################################

positions = pd.read_csv(pos_path)
tickers = ['O', 'GE']  # positions['Symbol']
for symbol in tickers:
    symbol = Stock(symbol)
    symbol.rb_lookup()
    #symbol.morningstar_lookup()
