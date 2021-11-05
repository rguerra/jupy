# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.13.0
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

pip install ffn


import ffn


bitcoin = ffn.get('BTC-USD:Close', start='2021-01-01', end='2021-01-01') 
bitcoin.tail()


