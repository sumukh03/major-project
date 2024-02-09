import yfinance as yf
from pandas_datareader import data as pdr
from datetime import date
import pandas as pd

START="2015-01-01"
END=date.today().strftime("%Y-%m-%d") #setting the end date as today

def get_raw_data(ticker):
    yf.pdr_override()
    data=pdr.get_data_yahoo(ticker,START,END)
    data.reset_index(inplace=True)
    return data

def get_data(ticker):
    data=get_raw_data(ticker)
    train_data_length=int(len(data)*0.90)
    train_data=data[["Date","Close"]][:train_data_length]
    test_data=data[["Date","Close"]][train_data_length:]
    return train_data,test_data

def get_test_data(ticker):
    data=get_raw_data(ticker)
    data_length=int(len(data)*0.90)
    
    return data

if __name__=="__main__":
    print(("GOOG"))