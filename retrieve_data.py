from stock import Stock


def retrieve_data(ticker, lookup='morningstar'):
    """
    :type ticker: str
    :param lookup:
    Standardize tickers as all uppercase
    """
    try:
        lookup = lookup.lower()

        if ticker == ticker.upper():
            ticker = Stock(ticker)
            if lookup in ('robinhood', 'rb'):
                ticker.rb_lookup()
                return ticker
            elif lookup == 'morningstar':
                ticker.morningstar_lookup()
                return ticker
            else:
                raise NotImplementedError("Only robinhood and morningstar lookups are supported")
        elif type(ticker) is str:
            ticker = ticker.upper()
            retrieve_data(ticker, lookup=lookup)

    except AttributeError:
        raise AttributeError("Only string inputs accepted")
