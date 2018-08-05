import os

from stock_analysis import technical_analysis
from stock_analysis.stock import Stock

abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)


__version__ = 0.0  # Pre-release
#__all__ = ['momentum', 'trend', 'volatility', 'volume', 'retrieve_data']