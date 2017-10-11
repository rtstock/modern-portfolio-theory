import datetime
import numpy as np
from pandas_datareader import data, wb
import pandas as pd
class pull:
    
    #startdatetime = datetime.datetime(2015, 1, 1)
    #enddatetime = datetime.datetime(2017, 9, 30)
    def __init__(self,
                 list_of_symbols,startdate, enddate):
        startdatetime = datetime.datetime.strptime(startdate,"%Y-%m-%d")
        enddatetime = datetime.datetime.strptime(enddate,"%Y-%m-%d")
        df = self.getcloseprices(list_of_symbols,startdatetime,enddatetime)
    def getcloseprices(self,list_of_symbols,startdatetime,enddatetime):

        prices1 = data.DataReader(list_of_symbols, "yahoo", startdatetime, enddatetime)
        
        df_a = pd.DataFrame(index=prices1.index)
        #df_a[s1] = prices1["Close"]
        df = df_a.dropna(axis=0, how='any')
        print df
        return df

if __name__=='__main__':
    #pairlist = []
    list_of_symbols = ['AAP','AAPL','CA','CHD']
    o = pull(list_of_symbols=list_of_symbols,startdate='2015-01-01',enddate='2017-09-30')
