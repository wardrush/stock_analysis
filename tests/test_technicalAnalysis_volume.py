@classmethod
def setUpClass(cls):
    """
    Create model stock data so that the download data tests can be independent
    Use 4 stocks' data: AAPL, GE, JPM, SVU
    """
    print('Creating Testing Class\n')
    print('Importing Model Data\n')

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

    # Manually Calculated Solutions

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
Testing Volume
ADI, OBV, OBV_mean, CMF, FI, EoM, and VPT 
"""
# Test ADI
# Test OBV, OBV_mean
# Test CMF
# Test FI
# Test EoM
# Test VPT

