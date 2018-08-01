from stock_analysis.exchanges import big50
import pandas as pd
import requests


def retrieve_data(symbols, debug=False):
    """
    Use Robinhood's API to get one year of historical data for each symbol called.
    :param symbols:
    :return data_list: A list with variable numbers of objects by number of API calls
    """
    historical_endpoint = "https://api.robinhood.com/quotes/historicals/"

    if len(symbols) <= 75:
        url = str(historical_endpoint + f"?symbols={','.join(symbols)}&interval=day")
        data_list = [requests.get(url)]
        return data_list
    else:
        # Break up lists so that API calls work with robinhood (>= 75)
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


searches = big50.iloc[:,0].sort_values()
result = retrieve_data(searches, debug=True)
new_data = pd.DataFrame.from_dict(data=result[0].json(), orient='index')
newer_data = pd.DataFrame.from_records(result[0].json())
"""
This works but is incredibly clunky"""
pd.DataFrame.from_dict(pd.DataFrame.from_records(newer_data.iloc[10])['historicals'][0])

print(new_data)
print(result[0].json())

