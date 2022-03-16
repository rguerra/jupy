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

# Install a pip package in the current Jupyter kernel
import sys
!{sys.executable} -m pip install pycoingecko

# +
from pycoingecko import CoinGeckoAPI
import json
cg = CoinGeckoAPI()

def _download_coin_data(coin, timePeriod):
    try:
        # nested_lists = cg.get_coin_market_chart_by_id(
        #            id=coin, vs_currency="usd", days=timePeriod
        nested_lists = cg.get_coin_market_chart_range_by_id(
                id=coin, vs_currency="usd", from_timestamp=1635945880, to_timestamp=1636032280

        )
        prices = nested_lists['prices']
        market_caps = nested_lists['market_caps']
        total_volumes = nested_lists['total_volumes']

    except Exception as e:
        print(e)
        print("coin: " + coin)
        
    for price_tuple, marketc_tuple, vol_tuple in zip(prices, market_caps, total_volumes):
        # The Core Data Representation [CDR] is:
        #{
        #  "Time_Stamp": 1635986416964,
        #  "Price": 63085.00903965155,
        #  "Market_Cap": 1188756041114.7732,
        #  "Total_Volume": 36261159346.2718
        #}
        if(price_tuple[0] == marketc_tuple[0] == vol_tuple[0]):
            entry = {"Crypto": coin}
            entry["Time_Stamp"] = price_tuple[0]
            entry["Price"] = price_tuple[1]        
            entry["Market_Cap"] = marketc_tuple[1]
            entry["Total_Volume"] = vol_tuple[0]
            entry["Source"] = "CoinGeckoAPI"
            yield json.dumps(entry)
        

coin="bitcoin"
timePeriod=1
for xx in _download_coin_data(coin, timePeriod):
    print(xx)

# +

coins = [
    "bitcoin",
    "ethereum",
    "ripple",  # xrp
    "tether",
    "bitcoin-cash",
    "cardano",
    "bitcoin-cash-sv",
    "litecoin",
    "chainlink",
    "binancecoin",
    "eos",
    "tron",
]

data = {}
for coin in gecko_list:
    try:
        nested_lists = cg.get_coin_market_chart_by_id(
            id=coin, vs_currency="usd", days=timePeriod
        )["prices"]
        data[coin] = {}
        data[coin]["timestamps"], data[coin]["values"] = zip(*nested_lists)

    except Exception as e:
        print(e)
        print("coin: " + coin)
# -


