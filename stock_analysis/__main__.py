from stock_analysis import portfolio_management
# Choose the strategy that you want to use
import requests.exceptions
from stock_analysis.strategy import weekly_rotation_sp500
strategies = [weekly_rotation_sp500.weekly_rotation_sp500]

if __name__ == "__main__":
    for strategy in strategies:
        try:
            strategy()
        except requests.exceptions.ConnectionError:
            print('Could not retrieve data. Please make sure you are connected to the internet')
    #portfolio_management.portfolio_management()


