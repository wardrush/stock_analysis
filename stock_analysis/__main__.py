import requests.exceptions

# Import strategies
from stock_analysis.strategy.weekly_rotation_sp500 import WeeklyRotationSP500
from stock_analysis.strategy.mean_reversion_long import MeanReversionLong
from stock_analysis.strategy.mean_reversion_short import MeanReversionShort

# Set up strategy list to call classes
strategies = [MeanReversionLong]


if __name__ == "__main__":

    for strategy in strategies:
        try:
            strategy_call = strategy()
            strategy_call()
        except requests.exceptions.ConnectionError:
            print('Could not retrieve data. Please make sure you are connected to the internet')



