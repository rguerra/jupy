# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.11.3
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# Install a conda package in the current Jupyter kernel
import sys
# !conda install --yes --prefix {sys.prefix} pymongo

from pymongo import MongoClient
from pprint import pprint
client = MongoClient('data-mongodb', 27017)
db = client.admin
serverStatusResult=db.command("serverStatus")
pprint(serverStatusResult)


