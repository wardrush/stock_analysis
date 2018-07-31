from stock_analysis.exchanges import *
import pandas
import requests


historical_endpoint = "https://api.robinhood.com/quotes/historicals/"
searches = big50.iloc[:,0].sort_values()
if len(searches) <= 1600:
    url = str(historical_endpoint + f"?symbols={','.join(searches)}&interval=day")
else:
    pass

data = requests.get(url)
new_data = data.json()
pd.DataFrame = new_data