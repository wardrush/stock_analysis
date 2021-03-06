import pandas as pd
import requests


def retrieve_single_data(symbol, debug=False):
    """
    Use Robinhood's API to get one year of historical data for A SINGLE string symbol called
    :param symbol: string of stock symbols used when finding historical data
    :param debug: bool to determine how verbose the output should be
    :return: Only mildly processed formerly-JSON data from Robinhood. Use 'clean_single_data' function to put into dataframes
    :rtype: dataframe
    """
    historical_endpoint = "https://api.robinhood.com/quotes/historicals/"
    url = str(historical_endpoint + f"?symbols={symbol}&interval=day")
    raw_data = requests.get(url)
    if debug:
        print(f'Downloaded data for {symbol.upper()} with response code: {raw_data.status_code()}')
    return raw_data


def clean_single_data(raw_data, debug=False):
    """Use Robinhood's unofficial historical API to clean the return value from the return value of retrieve_single_data

    :param raw_data: the requests return value from the retrieve_single_data function
    :param debug: bool to determine if a non-accepted return value raises an error or is silent
    :return: a pandas dataframe formatted with columns (in order): Symbol, Date, Open, High, Low, Close, Volume
    :rtype: pandas.DataFrame
    """
    for dict_result in raw_data.json()['results']:
        stock_symbol = dict_result['symbol']
        if stock_symbol:
            data_frame_data = {
                'Symbol': stock_symbol,
                'Date': [trading_day['begins_at'] for trading_day in dict_result['historicals']],
                'Open': [trading_day['open_price'] for trading_day in dict_result['historicals']],
                'High': [trading_day['high_price'] for trading_day in dict_result['historicals']],
                'Low': [trading_day['low_price'] for trading_day in dict_result['historicals']],
                'Close': [trading_day['close_price'] for trading_day in dict_result['historicals']],
                'Volume': [trading_day['volume'] for trading_day in dict_result['historicals']]
                               }
        elif 'stock_symbol' in locals() == True | debug:
            raise RuntimeWarning(f'Stock was not found. Return value was: {dict_result}')
    try:
        frame = pd.DataFrame(data=data_frame_data)
    except NameError:
        return None
    return frame


def retrieve_bulk_data(symbols, debug=False):
    """
    Use Robinhood's API to get one year of historical data for each symbol called.
    Maybe make more generalizable if other data sources are to be used
    :param symbols: list of string stock symbols used when finding historical data
    :param debug: bool If == True, opens a section of code that prints out api calls to help troubleshoot errors
    :return: Only mildly processed formerly-JSON data from Robinhood. Use 'clean_data' function to put into dataframes
    :rtype: list
    """
    historical_endpoint = "https://api.robinhood.com/quotes/historicals/"
    if len(symbols) <= 75:
        url = str(historical_endpoint + f"?symbols={','.join(symbols)}&interval=day")
        data_list = [requests.get(url)]
        return data_list
    else:
        # Break up lists so that API calls are manageable
        sublists = [symbols[i: (i + 75)] for i in range(0, len(symbols), 75)]
        data_list = []
        call_tracker = []
        for call_data in sublists:
            url = str(historical_endpoint + f"?symbols={','.join(call_data)}&interval=day")
            call_tracker.append(call_data)
            data_list.append(requests.get(url))

        # Check over the list if there is a bad response code
        if debug:
            for index, _ in enumerate(data_list):
                if int(data_list[index].status_code) != 200:
                    print("Error when searching most recent list.\nNow trying each code individually in form "
                          "(Ticker, Code)\n")
                    # Check each individual item if there is an error
                    check_list = []
                    for ticker in call_tracker[index]:
                        url = str(historical_endpoint + f"?symbols={ticker}&interval=day")
                        check_list.append((ticker, requests.get(url).status_code))
                        print(check_list[-1])
                        if int(check_list[-1][1]) != 200:
                            print(f'{check_list[-1][0]} Did not receive a good response from server')
        return data_list


def clean_bulk_data(raw_data):
    """
    Take the data from function 'retrieve_data' and make it usable in pandas dataframes
    :param raw_data:
    :return: #TODO currently returns only dataframe of last stock called. Should return more useful information
    :rtype: pandas.DataFrame
    """

    for api_call in raw_data:
        for dict_result in api_call.json()['results']:
            stock_symbol = dict_result['symbol']
            if stock_symbol:
                data_frame_data = {
                                    'Symbol': stock_symbol,
                                    'Date': [trading_day['begins_at'] for trading_day in dict_result['historicals']],
                                    'Open': [trading_day['open_price'] for trading_day in dict_result['historicals']],
                                    'Close': [trading_day['close_price'] for trading_day in dict_result['historicals']],
                                    'High': [trading_day['high_price'] for trading_day in dict_result['historicals']],
                                    'Low': [trading_day['low_price'] for trading_day in dict_result['historicals']],
                                    'Volume': [trading_day['volume'] for trading_day in dict_result['historicals']]
                                   }
            else:
                raise RuntimeWarning('Stock was not found')
    frame = pd.DataFrame(data=data_frame_data)
    return frame

