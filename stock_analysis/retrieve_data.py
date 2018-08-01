from stock_analysis.exchanges import *
import requests


def retrieve_data(symbols, debug=False):
    """
    Use Robinhood's API to get one year of historical data for each symbol called.
    :param symbols: string or list of stock symbols used when finding historical data
    :param debug: bool If == True, opens a section of code that prints out api calls to help troubleshoot errors
    :return: Only mildly processed formerly-JSON data from Robinhood. Use 'clean_data' function to put into dataframes
    :rtype: list
    """
    historical_endpoint = "https://api.robinhood.com/quotes/historicals/"

    if len(symbols) <= 75:
        url = str(historical_endpoint + f"?symbols={','.join(symbols)}&interval=day")
        data = requests.get(url)
        return data
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


def clean_data(data_list):
    """
    Take the data from function 'retrieve_data' and make it usable in pandas dataframes
    :param data_list:
    :return:
    """
    """
    temp.rename(
        columns={
            "symbol": "Symbol",
            "begins_at": "Date",
            "close_price": "Close",
            "high_price": "High",
            "low_price": "Low",
            "open_price": "Open",
            "volume": "Volume"
        }, inplace=True)
    self.close = temp.loc[:, "Close"]
    self.high = temp.loc[:, "High"]
    self.low = temp.loc[:, "Low"]
    self.open = temp.loc[:, "Open"]
    self.volume = temp.loc[:, "Volume"]
    self.dates = temp.loc[:, "Date"]
    self.lookup = 'robinhood'
    """
    pass

searches = big50.iloc[:,0].sort_values()
result = retrieve_data(searches, debug=True)
print(result.json())

