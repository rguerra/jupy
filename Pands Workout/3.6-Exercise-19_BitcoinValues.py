# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.13.7
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# %pylab inline
import pandas as pd
from pandas import Series, DataFrame
df = pd.read_csv('https://api.blockchain.info/charts/market-price?format=csv',
                header=None,
                names=['date', 'value'])
df.tail(1)[['value']]
df.loc[df['value'] == df['value'].min(), ['date', 'value']]
df.loc[df['value'] == df['value'].max(), ['date', 'value']]


