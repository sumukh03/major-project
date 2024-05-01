import yfinance as yf
from pandas_datareader import data as pdr
from datetime import date
import pandas as pd
import json

START="2015-01-01"
END=date.today().strftime("%Y-%m-%d") #setting the end date as today
JSON_PATH="predictions.json"

def get_json_data(ticker):
    with open(JSON_PATH, 'r') as file:
        data = json.load(file)
        return pd.read_json(data[ticker])

def get_train_data(ticker):
    yf.pdr_override()
    data=pdr.get_data_yahoo(ticker,"2015-01-01","2024-01-01")
    data.reset_index(inplace=True)
    train_length=int(len(data)*0.9)
    return data[["Date","Close","Open","High","Low"]][:train_length]


def get_data(ticker):
    json_data=get_json_data(ticker)
    train_data=get_train_data(ticker)
    test_dates,test_data,predictions=json_data["Date"],json_data["Close"],json_data["Predictions"]
    return test_dates,train_data,test_data,predictions


if __name__=="__main__":
    print(("GOOG"))