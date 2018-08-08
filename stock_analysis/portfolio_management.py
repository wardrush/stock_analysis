import pandas as pd
import os

def portfolio_management():
    # Create a user-specific portfolio file if it does not exist
    if not os.path.exists('portfolio'):
        os.mkdir('portfolio')
    if os.path.isfile(os.path.join('portfolio', 'Trades.csv')):
        trades = pd.read_csv(os.path.join('portfolio', 'Trades.csv'))
    else:
        pd.DataFrame(columns=['Date', 'Symbol', 'Purchase?', 'Price per Share', 'Number of Shares','Total Cost',
                              'Running Return']).to_csv(os.path.join('portfolio', 'Trades.csv'), index=False)

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