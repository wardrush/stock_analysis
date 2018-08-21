import requests.exceptions

# Import strategies
from stock_analysis.strategy.weekly_rotation_sp500 import strategy_weekly_rotation_sp500
from stock_analysis.strategy.mean_reversion_long import strategy_mean_reversion_long
from stock_analysis.strategy.mean_reversion_short import strategy_mean_reversion_short

# Set up strategy list to use function closures then pass them to the main loop
strategies = [strategy_mean_reversion_long]  # [strategy_weekly_rotation_sp500]


if __name__ == "__main__":

    for strategy in strategies:
        try:
            strategy()
        except requests.exceptions.ConnectionError:
            print('Could not retrieve data. Please make sure you are connected to the internet')



