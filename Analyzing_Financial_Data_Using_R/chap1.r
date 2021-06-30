# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .r
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.11.1
#   kernelspec:
#     display_name: R
#     language: R
#     name: ir
# ---

# # Chapter 1

data.AMZN <- read.csv("data/AMZN.csv")

head(data.AMZN)

class(data.AMZN$Date)

date <- as.Date(data.AMZN$Date, format="%Y-%m-%d")

head(date)

class(date)

data.AMZN<-cbind(data, data.AMZN[,-1])


