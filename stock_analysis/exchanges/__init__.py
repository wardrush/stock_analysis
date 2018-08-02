import pandas as pd
import os

big50 = pd.read_csv(os.path.join(os.getcwd(), "exchanges", "big50.csv"))
amex = pd.read_csv(os.path.join(os.getcwd(), "exchanges", "amex.csv"))
nasdaq = pd.read_csv(os.path.join(os.getcwd(), "exchanges", "nasdaq.csv"))
nyse = pd.read_csv(os.path.join(os.getcwd(), "exchanges", "nyse.csv"))
sp500 = pd.read_csv(os.path.join(os.getcwd(), "exchanges", "sp500.csv"))
sp500_cleaned = pd.read_csv(os.path.join(os.getcwd(), "exchanges", "sp500_cleaned.csv"))

