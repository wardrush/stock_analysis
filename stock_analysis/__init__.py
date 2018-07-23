import os
from stock_analysis.stock import Stock
from stock_analysis.technical_analysis import trend


# Create a user-specific portfolio file
if not os.path.exists('portfolio'):
    os.mkdir('portfolio')

# Pull general market data into global var so that data is not retrieved for every stock
buffer = 0.02
global sp500_above_200_sma_w_buffer
sp500 = Stock('SPY')
sp500.morningstar_lookup()
sma_w_buffer = trend.sma(sp500.close * (1 - buffer))
if sp500.close.iloc[-1] < sma_w_buffer.iloc[-1]:
    sp500_above_200_sma_w_buffer = False
elif sp500.close.iloc[-1] > sma_w_buffer.iloc[-1]:
    sp500_above_200_sma_w_buffer = True



__version__ = 0.0  # Pre-release
#__all__ = ['momentum', 'trend', 'volatility', 'volume', 'retrieve_data']