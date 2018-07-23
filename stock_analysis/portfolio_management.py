import pandas as pd
#from pandas import ExcelWriter
#from pandas import ExcelFile
import os

if os.path.isfile('Trades.csv'):
    trades = pd.read_csv('Trades.csv')
else:
    pd.DataFrame(columns=['Date', 'Symbol', 'Purchase?', 'Price per Share', 'Number of Shares',
                          'Total Cost', 'Running Return']).to_csv('Trades.csv', index=False)

# TODO Figure out to deal with portfolio
if os.path.isfile('Portfolio.csv'):
    portfolio = pd.read_csv('Portfolio.csv')


"""
Need to track:
1. total equity
2. Positions
3. Commission
4. risk adjusted returns
"""