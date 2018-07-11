import json
import requests

def investment_profile(self):
    self.session.get(self.endpoints['investment_profile'])


def instruments(self, stock=None):
    res = self.session.get(
        self.endpoints['instruments'],
        params={'query': stock.upper()})
    res = res.json()
    return res['results']


def quote_data(self, stock=None):
    # Prompt for stock if not entered
    if stock is None:
        stock = input("Symbol: ")
    url = str(self.endpoints['quotes']) + str(stock) + "/"
    # Check for validity of symbol
    try:
        res = requests.get(url).json()
        if len(res) > 0:
            return res
        else:
            raise NameError("Invalid Symbol: " + stock)
    except ValueError:
        raise NameError("Invalid Symbol: " + stock)


def get_quote(self, stock=None):
    data = self.quote_data(stock)
    return data["symbol"]


def get_symbol_by_instrument(self, url=None):
    return requests.get(url).json()['symbol']


def get_name_by_instrument(self, url=None):
    return requests.get(url).json()['name']


def get_historical_quotes(self, symbol, interval, span, bounds='regular'):
    # Valid combination
    # interval = 5minute | 10minute + span = day, week
    # interval = day + span = year
    # interval = week
    # bounds can be 'regular' for regular hours or 'extended' for extended hours
    res = self.session.get(
        self.endpoints['historicals'],
        params={
            'symbols': ','.join(symbol).upper(),
            'interval': interval, 'span': span, 'bounds': bounds
        })
    return res.json()


def get_news(self, symbol):
    return self.session.get(self.endpoints['news'] + symbol.upper() + "/").json()


def print_quote(self, stock=None):
    data = self.quote_data(stock)
    print(data["symbol"] + ": $" + data["last_trade_price"])


def print_quotes(self, stocks):
    for i in range(len(stocks)):
        self.print_quote(stocks[i])


def ask_price(self, stock=None):
    return float(self.quote_data(stock)['ask_price'])


def ask_size(self, stock=None):
    return float(self.quote_data(stock)['ask_size'])


def bid_price(self, stock=None):
    return float(self.quote_data(stock)['bid_price'])


def bid_size(self, stock=None):
    return float(self.quote_data(stock)['bid_size'])


def last_trade_price(self, stock=None):
    return float(self.quote_data(stock)['last_trade_price'])


def previous_close(self, stock=None):
    return float(self.quote_data(stock)['previous_close'])


def previous_close_date(self, stock=None):
    return self.quote_data(stock)['previous_close_date']


def adjusted_previous_close(self, stock=None):
    return float(self.quote_data(stock)['adjusted_previous_close'])


def symbol(self, stock=None):
    return self.quote_data(stock)['symbol']


def last_updated_at(self, stock=None):
    return self.quote_data(stock)['updated_at']


def get_account(self):
    res = self.session.get(self.endpoints['accounts'])
    res = res.json()
    return res['results'][0]


def get_url(self, url):
    return self.session.get(url).json()
