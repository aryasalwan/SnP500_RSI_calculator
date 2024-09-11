import yfinance as yf
import pandas
import datetime
import talib
import pickle

def get_moving_avg(ticker):
    data = yf.download(ticker, start='2020-01-01', end='2024-12-31')

    # Calculate the 50-day moving average
    data['50_MA'] = data['Close'].rolling(window=50).mean()
    data['200_MA'] = data['Close'].rolling(window=200).mean()
    # Display the data with the moving average
    print(data[['Close', '50_MA']])
    print(data[['Close', '200_MA']])

get_moving_avg("MSFT")