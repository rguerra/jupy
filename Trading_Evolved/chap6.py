# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.11.1
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# %matplotlib inline
import pandas as  pd  
data = pd.read_csv('data/AMZN.csv', index_col='Date', parse_dates=['Date'])


data

data['SMA'] = data['Close'].rolling(50).mean()  
data.plot()


