import retrieve_data
import pandas as pd

#######################################################
pos_path = 'C:\\Users\\Ward Rushton\\Documents\\Finances\\Portfolio\\2018_06 Portfolio Data\\mod_book1.csv'
########################################################

positions = pd.read_csv(pos_path)
tickers = positions['Symbol']
stockslist = []
for symbol in tickers:
    try:
        symbol = retrieve_data.Stock(symbol)
        symbol.morningstar_lookup()
        stockslist.append(symbol)
    except ValueError:
        stockslist.append(f'ValueError: {symbol.ticker}')
        continue
ticker_dates_close = [(symbol.ticker, symbol.dates, symbol.close) for symbol in stockslist if type(symbol) != str]
