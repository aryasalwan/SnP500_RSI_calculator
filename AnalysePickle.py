import pickle
from SnP500rsi import ticker_with_rsi
def open_pickle(path):
    with open(path,'rb') as file:
        data=pickle.load(file)
    return data
def print_rsi_data(data):
    for i in data:
        print(f"Name: {i.ticker} RSI: {i.rsi}")

data=open_pickle("/Users/arya/PycharmProjects/Yfinance/SnP500rsi2024-09-07.pkl")

print_rsi_data(data)