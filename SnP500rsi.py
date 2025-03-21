import yfinance as yf
import pandas
import datetime
import talib
import numpy as np
import pickle
class ticker_with_rsi:
    def __init__(self,ticker,rsi):
        self.ticker=ticker
        self.rsi=rsi

def save_pickle(data):
    today_date=datetime.date.today()
    with open(f"SnP500rsi{today_date}.pkl",'wb') as file:
        pickle.dump(data,file,protocol=pickle.HIGHEST_PROTOCOL)
def get_RSI(ticker_symbol):
    year_now=datetime.datetime.now().year
    date_today=datetime.date.today()
    date_14_days_back=date_today-datetime.timedelta(days=15)
    first_day=datetime.datetime(year_now,1,1)
    last_day=datetime.datetime(year_now,12,31)
    data=yf.download(ticker_symbol,start=first_day, end=last_day)
    close_=data['Close'][ticker_symbol].to_numpy()
    rsi = talib.RSI(close_, timeperiod=14)[-1]
    rsi_data=(ticker_with_rsi(ticker_symbol,rsi))
    return rsi_data


def snp500():
    list_ofSnP500_companies=[]
    SnP500wiki="https://en.wikipedia.org/wiki/List_of_S%26P_500_companies"
    tables = pandas.read_html(SnP500wiki)
    Snptable=tables[0]

    list_of_TSX60_companies=[]
    tsx60wiki="https://en.wikipedia.org/wiki/S%26P/TSX_60"
    tables_tsx60=pandas.read_html(tsx60wiki)
    k=0
    for ticker in Snptable['Symbol']:
        list_ofSnP500_companies.append(ticker)
        k+=1
    l=[]
    # canadian_banks=['BNS.TO',"CWB.TO","RY.TO","TD.TO","BMO.TO","NA.TO"]
    for i in list_ofSnP500_companies:
        try:
            obj_data=get_RSI(i)
            l.append(obj_data)
        except Exception as ex:
            print(ex)
    sorted_acc_rsi=sorted(l,key=lambda ticker_with_rsi:ticker_with_rsi.rsi)
    for i in sorted_acc_rsi:
        print(f"Name: {i.ticker} RSI: {i.rsi}")
    save_pickle(sorted_acc_rsi)
    breakpoint()

def tsx60():
    list_of_TSX60_companies=[]
    tsx60wiki="https://en.wikipedia.org/wiki/S%26P/TSX_60"
    tables_tsx60=pandas.read_html(tsx60wiki)
    k=0
    for ticker in tables_tsx60[1]['Symbol']:
        ticker=str(ticker)
        ticker.replace(".B","")
        ticker.replace(".A","")
        ticker=ticker + ".TO"
        list_of_TSX60_companies.append(ticker)
        k+=1
    l=[]
    # canadian_banks=['BNS.TO',"CWB.TO","RY.TO","TD.TO","BMO.TO","NA.TO"]
    for i in list_of_TSX60_companies:
        try:
            obj_data=get_RSI(i)
            l.append(obj_data)
        except Exception as ex:
            print(ex)
    sorted_acc_rsi=sorted(l,key=lambda ticker_with_rsi:ticker_with_rsi.rsi)
    for i in sorted_acc_rsi:
        print(f"Name: {i.ticker} RSI: {i.rsi}")
    save_pickle(sorted_acc_rsi)
    breakpoint()
def main():
    tsx60()
main()

# l=[]
# l.append(get_RSI("msft"))
# breakpoint()



