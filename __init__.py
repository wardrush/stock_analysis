# set up plotly if not done
import plotly
import os
from pathlib import Path
import pandas as pd
import stockanalysis


##############################################
# Remove for production
os.environ["PLT_USRNM"] = 'wrush'
os.environ["PLT_API"] = 'ZEqaUmnaOj4QNoxcF7Iy'

##############################################


#  Create config file at "C:\Users\<Your Username>\.plotly if it does not exist
plotly_config = Path.home() / '.plotly' / '.credentials'
if plotly_config.exists():
    pass
else:
    plotly.tools.set_credentials_file(username=os.environ.get('PLT_USRNM'), api_key=os.environ.get('PLT_API'))





if __name__ == "__main__":
    stockanalysis.my_func(tickers)

