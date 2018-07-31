import pandas as pd
import os

basedir = "exchanges" + os.sep
big50 = pd.read_csv(basedir + "50big.csv")
amex = pd.read_csv(basedir + "amex.csv")
nasdaq = pd.read_csv(basedir + "nasdaq.csv")
nyse = pd.read_csv(basedir + "nyse.csv")
sp500 = pd.read_csv(basedir + "sp500.csv")
sp500_cleaned = pd.read_csv(basedir + "sp500_cleaned.csv")



