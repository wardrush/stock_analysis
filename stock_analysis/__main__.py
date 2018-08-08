from stock_analysis import portfolio_management
# Choose the strategy that you want to use
import requests.exceptions
from stock_analysis.strategy import strategy_weekly_rotation_sp500, strategy_mean_reversion_short,
                                    strategy_mean_reversion_long
# Set up strategy list to use function closures then pass them to the main loop
strategies = [
                strategy_weekly_rotation_sp500,
                strategy_mean_reversion_long,
                strategy_mean_reversion_short
            ]

if __name__ == "__main__":
    # portfolio_management.portfolio_management()
    for strategy in strategies:
        try:
            strategy()
        except requests.exceptions.ConnectionError:
            print('Could not retrieve data. Please make sure you are connected to the internet')



