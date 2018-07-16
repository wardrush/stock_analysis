import unittest
from unittest import expectedFailure, skip
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

    @classmethod
    def setUpClass(cls):
        """
        Create model stock data so that the download data tests can be independent
        Use 4 stocks' data: AAPL, GE, JPM, SVU
        """
        print('Creating Testing Class\n')
        # AAPL
        temp = pd.read_csv('AAPL.csv', delimiter='\t')
        cls.aapl = Stock('AAPL')
        cls.aapl.open = temp['Open']
        cls.aapl.high = temp['High']
        cls.aapl.low = temp['Low']
        cls.aapl.close = temp['Close']
        cls.aapl.lookup = 'Testing'
        # GE
        temp = pd.read_csv('GE.csv', delimiter='\t')
        cls.ge = Stock('GE')
        cls.ge.open = temp['Open']
        cls.ge.high = temp['High']
        cls.ge.low = temp['Low']
        cls.ge.close = temp['Close']
        cls.ge.lookup = 'Testing'
        # JPM
        temp = pd.read_csv('JPM.csv', delimiter='\t')
        cls.jpm = Stock('JPM')
        cls.jpm.open = temp['Open']
        cls.jpm.high = temp['High']
        cls.jpm.low = temp['Low']
        cls.jpm.close = temp['Close']
        cls.jpm.lookup = 'Testing'
        # SVU
        temp = pd.read_csv('SVU.csv', delimiter='\t')
        cls.svu = Stock('SVU')
        cls.svu.open = temp['Open']
        cls.svu.high = temp['High']
        cls.svu.low = temp['Low']
        cls.svu.close = temp['Close']
        cls.svu.lookup = 'Testing'

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
        print(trend.sma(self.aapl.close))

    def test_sma_50_days(self):
        pass

    @expectedFailure
    def test_sma_nonint_days(self):
        pass

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

    """
    Testing Momentum
    RSI, MFI, and TSI
    """
    # Test RSI
    # Test MFI
    # Test TSI

    """
    Testing Volatility
    ATR, Bollinger, KC, and DC
    """
    # Test ATR
    # Test Bollinger
    # Test KC
    # Test DC

    """
    Testing Volume
    ADI, OBV, OBV_mean, CMF, FI, EoM, and VPT 
    """
    # Test ADI
    # Test OBV, OBV_mean
    # Test CMF
    # Test FI
    # Test EoM
    # Test VPT





if __name__ == '__main__':
    unittest.main