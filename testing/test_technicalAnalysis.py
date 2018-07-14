import unittest
import pandas as pd
from stock import Stock
from technical_analysis import trend
from technical_analysis import momentum
from technical_analysis import volatility
from technical_analysis import volume


class TechnicalAnalysisTest(unittest.TestCase):
    """
    Test the technical analyses using model data
    """

    def setUp(self):
        """
        Create model stock data so that the download data tests can be independent
        Use 4 stocks' data: AAPL, GE, JPM, SVU
        """
        # AAPL
        temp = pd.read_csv('C:\Pythonfiles\stock_analysis\Test Data\AAPL.csv')
        aapl = Stock('AAPL')
        aapl.open = temp['Open']
        aapl.high = temp['High']
        aapl.low = temp['Low']
        aapl.close = temp['Close']
        aapl.lookup = 'Testing'
        # GE
        temp = pd.read_csv('Test Data/GE')
        ge = Stock('GE')
        ge.open = temp['Open']
        ge.high = temp['High']
        ge.low = temp['Low']
        ge.close = temp['Close']
        ge.lookup = 'Testing'
        #JPM
        temp = pd.read_csv('Test Data/JPM')
        jpm = Stock('JPM')
        jpm.open = temp['Open']
        jpm.high = temp['High']
        jpm.low = temp['Low']
        jpm.close = temp['Close']
        jpm.lookup = 'Testing'
        #SVU
        temp = pd.read_csv('Test Data/SVU')
        svu = Stock('SVU')
        svu.open = temp['Open']
        svu.high = temp['High']
        svu.low = temp['Low']
        svu.close = temp['Close']
        svu.lookup = 'Testing'

    def test_sma_default_days(self):
        trend.sma(aapl.close)






if __name__ == '__main__':
    unittest.main