import yfinance as yf
import ta
import pandas as pd
import math
import datetime
# Creating a Series
# s = pd.Series([10, 20, 30, 40], index=['a', 'b', 'c', 'd'])
# print(s)
# s.info()

tsx_midcap = [
    "FFH.TO",  # Fairfax Financial Holdings Limited
    "GWO.TO",  # Great-West Lifeco Inc.
    "GFL.TO",  # GFL Environmental Inc.
    "IVN.TO",  # Ivanhoe Mines Ltd.
    "CLS.TO",  # Celestica Inc.
    "ARX.TO",  # ARC Resources Ltd.
    "STN.TO",  # Stantec Inc.
    "ATRL.TO", # AtkinsRéalis Group Inc.
    "X.TO",    # TMX Group Limited
    "AGI.TO",  # Alamos Gold Inc.
    "PAAS.TO", # Pan American Silver Corp.
    "IAG.TO",  # iA Financial Corporation Inc.
    "BDGI.TO", # Badger Infrastructure Solutions Ltd.
    "CJT.TO",  # Cargojet Inc.
    "EQB.TO",  # EQB Inc.
    "FN.TO",   # First National Financial Corporation
    "LNR.TO",  # Lundin Mining Corporation
    "DOL.TO",  # Dollarama Inc.
    "TOU.TO",  # Tourmaline Oil Corp.
    "WSP.TO",  # WSP Global Inc.
    "GEI.TO",  # Granite Real Estate Investment Trust
    "KEY.TO",  # Keyera Corp.
    "MRE.TO",  # Methanex Corporation
    "WFG.TO",  # West Fraser Timber Co. Ltd.
    "CGO.TO",  # CI Financial Corp.
    "BTE.TO",  # Baytex Energy Corp.
    "MEG.TO",  # MEG Energy Corp.
    "NPI.TO",  # Northland Power Inc.
    "PPL.TO",  # Pembina Pipeline Corporation
    "RUS.TO",  # Russel Metals Inc.
    "WN.TO",   # George Weston Limited
    "CCA.TO",  # Canadian Western Bank
    "FM.TO",   # First Quantum Minerals Ltd.
    "IMO.TO",  # Imperial Oil Ltd.
    "L.TO",    # Loblaw Companies Ltd.
    "MRU.TO",  # Metro Inc.
    "RY.TO",   # Royal Bank of Canada
    "TD.TO",   # Toronto-Dominion Bank
    "ENB.TO",  # Enbridge Inc.
    "BAM.TO",  # Brookfield Asset Management Ltd.
    "BN.TO",   # Brookfield Corporation
    "TRI.TO",  # Thomson Reuters Corporation
    "CSU.TO",  # Constellation Software Inc.
    "CP.TO",   # Canadian Pacific Kansas City Limited
    "BMO.TO",  # Bank of Montreal
    "CNQ.TO",  # Canadian Natural Resources Limited
    "SHOP.TO", # Shopify Inc.
    "MFC.TO",  # Manulife Financial Corporation
    "SU.TO",   # Suncor Energy Inc.
    "SLF.TO",  # Sun Life Financial Inc.
    "NA.TO",   # National Bank of Canada
    "WPM.TO",  # Wheaton Precious Metals Corp.
    "QSR.TO",  # Restaurant Brands International Inc.
    "FNV.TO",  # Franco-Nevada Corporation
    "ABX.TO",  # Barrick Gold Corporation
    "NTR.TO",  # Nutrien Ltd.
    "CVE.TO"   # Cenovus Energy Inc.
]
momentum_stocks=['APP', 'CEG', 'IBKR', 'VST', 'ANET', 'PODD', 'TT', 'OKTA', 'TSLA', 'NVDA']
cdrs = [
    "MMM", "AXP", "BKNG", "CRWD", "F", "GE", "ISRG", "MU", "QCOM", "TXN", "SMCI",
    "BLK", "STZ", "DE", "LULU", "PANW", "NOW", "TMO", "ADBE", "AVGO", "CAT",
    "LLY", "JNJ", "RTX", "BA", "CHEV", "C", "XOM", "INTC", "UBER", "HON", "ABBV",
    "PG", "CVS", "UPS", "VZ", "UNH", "SBUX", "NKE", "MCDS", "COLA", "CSCO", "BAC",
    "GS", "HD", "NVDA", "WMT", "COST", "CRM", "AMD", "PFE", "MA", "JPM", "IBM",
    "DIS", "META", "MSFT", "PYPL", "V", "AAPL", "NFLX", "GOOG", "TSLA", "AMZN"
]

tsx60_stocks_tsx = [
    "RY.TO",
    "SHOP.TO",
    "TD.TO",
    "ENB.TO",
    "BN.TO",
    "BAM.TO",
    "TRI.TO",
    "CSU.TO",
    "BMO.TO",
    "CP.TO",
    "CNQ.TO",
    "CNR.TO",
    "BNS.TO",
    "CM.TO",
    "AEM.TO",
    "MFC.TO",
    "TRP.TO",
    "WCN.TO",
    "ATD.TO",
    "L.TO",
    "SU.TO",
    "WPM.TO",
    "IFC.TO",
    "IMO.TO",
    "SLF.TO",
    "NA.TO",
    "ABX.TO",
    "DOL.TO",
    "FNV.TO",
    "QSR.TO",
    "NTR.TO",
    "WSP.TO",
    "WN.TO",
    "T.TO",
    "CVE.TO",
    "FTS.TO",
    "H.TO",
    "POW.TO",
    "BCE.TO",
    "PPL.TO",
    "CNI",
    "EMA.TO",
    "IVN.TO",
    "ARX.TO",
    "MG.TO",
    "IAG.TO",
    "FM.TO",
    "LUN.TO",
    "GWO.TO",
    "MRU.TO",
    "TOU.TO",
    "STN.TO",
    "AGI.TO",
    "PAAS.TO",
    "ELD.TO",
    "FFH.TO",
    "DSG.TO"
]

bmo_etfs=[
    'ZDM.TO', 'ZEA.TO', 'ZIU.TO', 'ZCN.TO', 'ZEM.TO', 'ZSP.TO', 'ZUE.TO', 'ZJPN.TO',
    'ZMID.TO', 'ZDJ.TO', 'ZID.TO', 'ZNQ.TO', 'ZQQ.TO', 'ZLB.TO', 'ZLI.TO', 'ZLE.TO',
    'ZIQ.TO', 'ZGQ.TO', 'ZEQ.TO', 'ZDV.TO', 'ZDI.TO', 'ZVC.TO', 'ZXLF.TO', 'ZXLR.TO',
    'ZXLE.TO', 'ZXLU.TO', 'ZXLV.TO', 'ZXLK.TO', 'ZXLC.TO', 'ZXLB.TO', 'ZXLI.TO',
    'ZXLY.TO', 'ZXLP.TO', 'ZEB.TO', 'ZUB.TO', 'ZUT.TO', 'ZBK.TO', 'ZGLD.TO', 'ZGLH.TO',
    'ZEO.TO', 'ZRE.TO', 'ZIN.TO', 'ZUH.TO', 'ZHU.TO', 'ZGD.TO', 'ZEAT.TO', 'DISC.TO',
    'ZIG.TO', 'ZMT.TO', 'ZWS.TO', 'ZWH.TO', 'ZWC.TO', 'ZWA.TO', 'ZWK.TO', 'ZWEN.TO',
    'ZJAN.TO', 'ZAPR.TO', 'ZJUL.TO', 'ZOCT.TO', 'ZWE.TO', 'ZWP.TO', 'ZWG.TO', 'ZWU.TO',
    'ZWT.TO', 'ZPR.TO', 'ZHP.TO', 'ZUP.TO', 'ZPAY.TO', 'ZPH.TO', 'ZPW.TO', 'ZLSC.TO',
    'ZLSU.TO', 'ZCON.TO', 'ZBAL.TO', 'ZGRO.TO', 'ZEQT.TO', 'ZESG.TO', 'ZBAL.T.TO',
    'ZGRO.T.TO', 'ZMI.TO', 'ZWOT.TO', 'ZGI.TO', 'GRNI.TO', 'TOWR.TO', 'ESGA.TO',
    'ESGG.TO', 'ESGY.TO', 'ZGRN.TO', 'ESGE.TO', 'ZCLN.TO', 'ZFC.TO', 'ARKK.TO',
    'ARKG.TO', 'ARKW.TO', 'WOMN.TO', 'BGEQ.TO', 'BGHC.TO', 'BGIF.TO', 'BGIN.TO',
    'BGDV.TO', 'BGRT.TO', 'ZFN.TO', 'ZZZD.TO', 'ZACE.TO', 'ZCS.TO', 'ZCM.TO', 'ZLC.TO',
    'ZPS.TO', 'ZPL.TO', 'ZMP.TO', 'ZFS.TO', 'ZFM.TO', 'ZXCO.TO', 'ZXCP.TO', 'ZXCQ.TO',
    'ZAG.TO', 'ZDB.TO', 'ZMMK.TO', 'ZMBS.TO', 'ZBI.TO', 'ZSB.TO', 'ZCB.TO', 'ZSDB.TO',
    'ZCDB.TO', 'ZST.TO', 'ZGB.TO', 'ZRR.TO', 'ZBBB.TO', 'ZQB.TO', 'ESGB.TO', 'ZUAG.TO',
    'ZSU.TO', 'ZMU.TO', 'ZIC.TO', 'ZUCM.TO', 'ZTS.TO', 'ZTM.TO', 'ZTL.TO', 'ZTIP.TO',
    'ZHY.TO', 'ZFH.TO', 'ZEF.TO', 'ZAAA.TO', 'ZGSB.TO', 'ZMSB.TO', 'ZCPB.TO'
    ]


small_caps = [
    "GRID.TO",
    "GSY.TO",
    "DNTL.TO",
    "WELL.TO",
    "CTS.TO",
    "DOL.TO",
    "CPH.TO",
    "PRL.TO",
    "BDT.TO"
]

betapro = [
    "CNDU", "CNDD", "CNDI",
    "SPXU", "SPXD", "SPXI",
    "QQU", "QQD",
    "CFOU", "CFOD",
    "ATMU", "ATMD",
    "RITU", "RITD",
    "GDXU", "GDXD",
    "NRGU", "NRGD",
    "HOU", "HOD",
    "HNU", "HND",
    "GLDU", "GLDD",
    "SLVU", "SLVD"
]
senior_miners = ["ABX.TO", "AEM.TO", "TECK.B.TO", "NTR.TO", "FM.TO", "K.TO", "LUN.TO", "HBM.TO", "BTO.TO", "AGI.TO", "SSRM.TO", "CCO.TO", "FNV.TO", "NGD.TO", "ERO.TO", "CG.TO", "TXG.TO"]
junior_miners= [
    "K.TO", "AGI.TO", "OR.TO", "IMG.TO",
    "BTO.TO", "ELD.TO", "EQX.TO", "LUG.TO",
    "NGD.TO", "OGC.TO", "TXG.TO", "DPM.TO",
    "SSRM.TO", "KNT.TO", "CXB.TO", "SSL.TO",
    "WDO.TO", "OLA.TO", "CG.TO", "TFPM.TO",
    "SEA.TO", "SKE.TO", "ARIS.TO", "IAU.TO",
]
xgd = ["NEM", "AEM", "WPM", "ABX", "FNV", "GFI", "K", "AU", "AGI", "RGLD"]

slv_tickers = ["WPM", "PAAS", "CDE", "BVN", "OR.TO", "HL", "SSRM", "AG.TO", "FVI.TO", "MAG.TO", "TFPM.TO", "EXK", "AYA.TO"]
bear_etfs = [
    "AAPD", "AMDD", "AMZD", "AVS", "BRKD", "GGLS", "METD", "MSFD", "MUD", "NFXS",
    "NVDD", "PLTD", "TSLS", "TSMZ", "SPDN", "REKT", "QQQD", "AIBD", "ERY", "DUST",
    "JDST", "DRIP", "TMV", "TYO", "YANG", "EDZ", "SPXS", "TZA", "WEBS", "FAZ",
    "DRV", "HIBS", "LABD", "SOXS", "TECS"
]
list_of_leveraged_shares= [
    "MIDU", "SPXL", "SPXS", "TNA", "TZA", "EDC", "EDZ", "EURL", "KORU", "MEXX",
    "YINN", "YANG", "TYD", "TYO", "TMF", "TMV", "CURE", "DFEN", "DPST", "DRN",
    "DRV", "DUSL", "FAS", "FAZ", "HIBL", "HIBS", "LABU", "LABD", "NAIL", "PILL",
    "RETL", "SOXL", "SOXS", "TECL", "TECS", "TPOR", "UTSL", "WANT", "WEBL", "WEBS",
    "AIBU", "AIBD", "BRZU", "CHAU", "CLDL", "CWEB", "ERX", "ERY", "EVAV", "FNGG",
    "GUSH", "DRIP", "INDL", "JNUG", "JDST", "LMBO", "NUGT", "DUST", "OOTO", "QQQU",
    "SPUU", "UBOT", "URAA", "XXCH", "QQQD", "REKT", "SPDN", "AAPU", "AAPD", "AMUU",
    "AMDD", "AMZU", "AMZD", "AVL", "AVS", "BRKU", "BRKD", "GGLL", "GGLS", "METU",
    "METD", "MSFU", "MSFD", "MUU", "MUD", "NFXL", "NFXS", "NVDU", "NVDD", "PLTU",
    "PLTD", "TSLL", "TSLS", "TSMX", "TSMZ"
]
canadian_banks = ['BNS.TO', "EQB.TO", "RY.TO", "TD.TO", "BMO.TO", "NA.TO"]

list_ofSnP500_companies = []
SnP500wiki = "https://en.wikipedia.org/wiki/List_of_S%26P_500_companies"
nasdaq = "https://en.wikipedia.org/wiki/Nasdaq-100"
tables = pd.read_html(SnP500wiki)
Snptable = tables[0]
for ticker in Snptable["Symbol"]:
    list_ofSnP500_companies.append(ticker)

list_ofnasdaq_companies=[]
tables = pd.read_html(nasdaq)
nsdqtable = tables[4]["Ticker"]
for ticker in nsdqtable:
    list_ofnasdaq_companies.append(ticker)
list_of_tsx60_companies=[]
tsx60wiki="https://en.wikipedia.org/wiki/S%26P/TSX_60"
tables_tsx60=pd.read_html(tsx60wiki)
tsx60table=tables_tsx60[1]

# nasdaqtable = tables[4]
list_oftsx60_companies=[]
for ticker in tsx60table["Symbol"]:
    list_oftsx60_companies.append(f"{ticker}.TO")
class ticker_with_rsi:
    def __init__(self,ticker,rsi):
        self.ticker=ticker
        self.rsi=rsi
    def print(self):
        print(f"Ticker: {self.ticker} RSI: {self.rsi}")

# ma_dict={}
# for i in ["TSLZ","PLTD"]:
#     ma_dict[str(i)]=get_symbol_matches(f"{i}")
# breakpoint()
# for i in ma_dict.keys():
#     if len(ma_dict[i])>0:
#         print(ma_dict[i][-1])
#     else:
#         print(f"No matches in {i}")
# # print(data[['Close', 'ma50','ma10']])

def get_RSI(ticker_symbol,price_data):
    rsi = ta.momentum.rsi(price_data["Close"][ticker_symbol]).iloc[-1]
    # print(rsi)
    rsi_data=(ticker_with_rsi(ticker_symbol,rsi))
    return rsi_data
def new_get_symbol_matches(symbol,price_data):
    pd.set_option('display.max_rows', None)
    symbol_df=price_data.copy()
    #replace price_data[price_data.columns[0]] with price_data
    symbol_df['ma50'] = ta.trend.sma_indicator(symbol_df["Close"][symbol], window=50)
    symbol_df['ma10'] = ta.trend.sma_indicator(symbol_df["Close"][symbol], window=10)

    match_list=pd.DataFrame(columns=["Close", "ma50", "ma10"])
    matches=[]
    current_year=datetime.date.today().year
    #and idx.month==5 and idx.day>15
    def find_match():
        for idx,i in symbol_df.iterrows():
            if (pd.isna(i["ma50"]) is not True) and idx.year==current_year and idx.month==5 and idx.day>20:
                indx=symbol_df["ma50"].index.get_loc(idx)
                indxc = symbol_df["Close"].index.get_loc(idx)
                if i.isna().any()!=True:
                    if math.isclose(float(i["ma50"].iloc[0]),float(i["ma10"].iloc[0]),rel_tol=0.01) and symbol_df["ma10"].iloc[indx-5:indx].diff().gt(0).any():
                        if (float(symbol_df["Close"][symbol].iloc[indxc:indxc+5].mean()) > float(symbol_df["ma10"].iloc[indx]))==True:
                            match_str=f"Date:{str(i.name)} Close:{i["Close"][symbol]} ma50:{i["ma50"].iloc[0]} ma10:{i["ma10"].iloc[0]}"
                            matches.append(match_str)
                            # print(i[["Close", "ma50", "ma10"]])
                            # print(data["ma10"].iloc[indx-5:indx])
                            # print("Buy Signal")
    def find_match2():
        for idx,i in symbol_df.iterrows():
            if (pd.isna(i["ma50"]) is not True) and idx.year==current_year:
                indx=symbol_df["ma50"].index.get_loc(idx)
                indxc = symbol_df["Close"].index.get_loc(idx)
                if i.isna().any()!=True:
                    if math.isclose(float(i["ma50"].iloc[0]),float(i["ma10"].iloc[0]),rel_tol=0.001) and symbol_df["ma10"].iloc[indx-5:indx].diff().gt(0).any():
                        # if (float(symbol_df["Close"][symbol].iloc[indxc:indxc+5].mean()) > float(symbol_df["ma10"].iloc[indx]))==True:
                            match_str=f"Date:{str(i.name)} Close:{i["Close"][symbol]} ma50:{i["ma50"].iloc[0]} ma10:{i["ma10"].iloc[0]}"
                            matches.append(match_str)
                            # print(i[["Close", "ma50", "ma10"]])
                            # print(data["ma10"].iloc[indx-5:indx])
                            # print("Buy Signal")
    find_match()
    # if matches==[]:
    #     find_match2()
    #     breakpoint()
    return matches


def get_MACD_crosses(symbol,price_data):
    pd.set_option('display.max_rows', None)
    symbol_df=price_data.copy()
    breakpoint()
    #replace price_data[price_data.columns[0]] with price_data
    symbol_df['ma50'] = ta.trend.sma_indicator(symbol_df["Close"][symbol], window=50)
    symbol_df['ma10'] = ta.trend.sma_indicator(symbol_df["Close"][symbol], window=10)

    match_list=pd.DataFrame(columns=["Close", "ma50", "ma10"])
    matches=[]
    current_year=datetime.date.today().year
    def find_match():
        for idx,i in symbol_df.iterrows():
            if (pd.isna(i["ma50"]) is not True) and idx.year==current_year:
                indx=symbol_df["ma50"].index.get_loc(idx)
                indxc = symbol_df["Close"].index.get_loc(idx)
                if i.isna().any()!=True:
                    if math.isclose(float(i["ma50"].iloc[0]),float(i["ma10"].iloc[0]),rel_tol=0.01) and symbol_df["ma10"].iloc[indx-5:indx].diff().gt(0).any():
                        if (float(symbol_df["Close"][symbol].iloc[indxc:indxc+5].mean()) > float(symbol_df["ma10"].iloc[indx]))==True:
                            match_str=f"Date:{str(i.name)} Close:{i["Close"][symbol]} ma50:{i["ma50"].iloc[0]} ma10:{i["ma10"].iloc[0]}"
                            matches.append(match_str)
                            # print(i[["Close", "ma50", "ma10"]])
                            # print(data["ma10"].iloc[indx-5:indx])
                            # print("Buy Signal")
    def find_match2():
        for idx,i in symbol_df.iterrows():
            if (pd.isna(i["ma50"]) is not True) and idx.year==current_year:
                indx=symbol_df["ma50"].index.get_loc(idx)
                indxc = symbol_df["Close"].index.get_loc(idx)
                if i.isna().any()!=True:
                    if math.isclose(float(i["ma50"].iloc[0]),float(i["ma10"].iloc[0]),rel_tol=0.001) and symbol_df["ma10"].iloc[indx-5:indx].diff().gt(0).any():
                        # if (float(symbol_df["Close"][symbol].iloc[indxc:indxc+5].mean()) > float(symbol_df["ma10"].iloc[indx]))==True:
                            match_str=f"Date:{str(i.name)} Close:{i["Close"][symbol]} ma50:{i["ma50"].iloc[0]} ma10:{i["ma10"].iloc[0]}"
                            matches.append(match_str)
                            # print(i[["Close", "ma50", "ma10"]])
                            # print(data["ma10"].iloc[indx-5:indx])
                            # print("Buy Signal")
    find_match()
    # if matches==[]:
    #     find_match2()
    #     breakpoint()
    return matches

def get_multiple_symbols(list_of_symbols):
    today=datetime.date.today()
    todays_date_formatted=today.strftime("%Y-%m-%d")
    one_year_ago=today-datetime.timedelta(days=365)
    one_year_ago_formatted=one_year_ago.strftime("%Y-%m-%d")
    multi_data=yf.download(list_of_symbols,start=one_year_ago_formatted, end=todays_date_formatted)
    return multi_data

test_list=["ABX.TO","RY.TO"]

def run_cross_finder(symbol_list):
    price_datas=get_multiple_symbols(symbol_list)
    for ticker in symbol_list:
        try:
            matches_= new_get_symbol_matches(ticker,price_datas)
            print(ticker)
            print(matches_[-1])
        except:
            print(f"No matches found in {ticker}")
        # print(*matches_,sep='\n')
def run_rsi_calc(symbol_list):
    ta
    price_datas=get_multiple_symbols(symbol_list)
    rsi_data=[]
    for ticker in symbol_list:
        try:
            # print(ticker)
            rsi_val=get_RSI(ticker,price_datas)
            rsi_data.append(rsi_val)
            # print(rsi_val)
        except:
            print(f"No matches found in {ticker}")
        # print(*matches_,sep='\n')
        # print(*rsi_data, sep='\n')
    rsi_data.sort(key=lambda rsi_obj: rsi_obj.rsi)
    for i in rsi_data:
        i.print()

def run_MACD_cross_finder(symbol_list):
    price_datas=get_multiple_symbols(symbol_list)
    for ticker in symbol_list:
        try:
            matches_= get_MACD_crosses(ticker,price_datas)
            print(ticker)
            print(matches_[-1])
        except:
            print(f"No matches found in {ticker}")
        # print(*matches_,sep='\n')
# You can then use this list in your Python code, for example:
# print(ticker_symbols)
# run_cross_finder(cdrs)f
# run_rsi_calc(list_ofnasdaq_companies)
# list_ofSnP500_companies.remove('BRK.B')
# list_ofSnP500_companies.remove('BRK.B')
# list_ofSnP500_companies.remove('BF.B')
# run_cross_finder(["PYPL"])
run_rsi_calc(["FICO"])
breakpoint()
# run_cross_finder()
# test_var.macd_diff()
# ta.trend.MACD(symbol_df["Close"][symbol], window_fast=12, window_slow=26).macd_diff()
