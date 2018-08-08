import unittest
import pandas as pd
from stock_analysis.stock import Stock
from technical_analysis import trend


class TechnicalAnalysisTest(unittest.TestCase):
    """
    Test the technical analyses trend file using model data
    """

    @classmethod
    def setUpClass(cls):
        """
        Create model stock data so that the download data tests can be independent
        Use 4 stocks' data: AAPL, GE, JPM, SVU
        """
        print('Creating Testing Class\n')
        print('Importing Model Data\n')

        # AAPL
        temp = pd.read_csv('../test_data/AAPL.csv', delimiter='\t')
        cls.aapl = Stock('AAPL')
        cls.aapl.open = temp['Open']
        cls.aapl.high = temp['High']
        cls.aapl.low = temp['Low']
        cls.aapl.close = temp['Close']
        cls.aapl.lookup = 'Testing'
        # GE
        temp = pd.read_csv('../test_data/GE.csv', delimiter='\t')
        cls.ge = Stock('GE')
        cls.ge.open = temp['Open']
        cls.ge.high = temp['High']
        cls.ge.low = temp['Low']
        cls.ge.close = temp['Close']
        cls.ge.lookup = 'Testing'
        # JPM
        temp = pd.read_csv('../test_data/JPM.csv', delimiter='\t')
        cls.jpm = Stock('JPM')
        cls.jpm.open = temp['Open']
        cls.jpm.high = temp['High']
        cls.jpm.low = temp['Low']
        cls.jpm.close = temp['Close']
        cls.jpm.lookup = 'Testing'
        # SVU
        temp = pd.read_csv('../test_data/SVU.csv', delimiter='\t')
        cls.svu = Stock('SVU')
        cls.svu.open = temp['Open']
        cls.svu.high = temp['High']
        cls.svu.low = temp['Low']
        cls.svu.close = temp['Close']
        cls.svu.lookup = 'Testing'

        # Manually Calculated Solutions
        """
        print('Importing Manually Calculated Solutions\n')
        # AAPL
        cls.aapl.solns = pd.read_csv('AAPL_SOLNS.csv', delimiter='\t')

        # GE
        cls.ge.solns = pd.read_csv('GE_SOLNS.csv', delimiter='\t')

        # JPM
        cls.jpm.solns = pd.read_csv('JPM_SOLNS.csv', delimiter='\t')

        # SVU
        cls.svu.solns = pd.read_csv('SVU_SOLNS.csv', delimiter='\t')
        """


    @classmethod
    def tearDownClass(cls):
        print('Closing Testing Class')


    """
    Testing Trend
    SMA, MACD, MACD_SIGNAL, MACD_DIFF, EMA_FAST, EMA_SLOW, ADX, ADX_POS, ADX_NEG,
    ADX_INDICATOR, VI_POS, VI_NEG, TRIX, MI, CCI, DPO, KST, KST_SIG, and Ichimoku
    """
    # Test SMA
    def test_sma_default_days(self):
        sma_series = trend.sma(self.aapl.close)
        print(sma_series)



    # Test MACD, MACD_signal, MACD_difference
    # Test EMA (fast and slow)
    # Test ADX (pos, neg, indicator)
    # Test VI (pos, neg)
    # Test TRIX
    # Test MI
    # Test CCI
    # Test DPO
    # Test KST and KST_signal
    # Test Ichimoku, Ichimoku_b







if __name__ == '__main__':
    unittest.main