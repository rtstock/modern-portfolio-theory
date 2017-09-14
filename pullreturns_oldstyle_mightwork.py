# -*- coding: utf-8 -*-
"""
Created on Tue Jul 21 14:40:39 2015

@author: justin.malinchak
"""


import datetime
def validate_date(date_text):
    try:
        datetime.datetime.strptime(date_text, '%Y-%m-%d')
        return True
    except ValueError:
        #raise ValueError("Incorrect data format, should be YYYY-MM-DD")
        return False
        
import numpy
def is_number(s):
    try:
        if numpy.isnan(s) == True:
            return False
        float(s)
        return True
    except ValueError:
        return False
        
def test_builddataframe():
    import pandas as pd
    import numpy as np
    
    df = pd.DataFrame({'a':np.random.randn(5),
                        'b':np.random.randn(5),
                        'c':np.random.randn(5),
                        'd':np.random.randn(5)})
    cols_to_keep = ['a', 'c', 'd']
    dummies = ['d']
    not_dummies = [x for x in cols_to_keep if x not in dummies]
    data = df[not_dummies]
    print(data)

class perform:
    def set_Symbols(self,Symbols):
        self._Symbols = Symbols
    def get_Symbols(self):
        return self._Symbols
    Symbols = property(get_Symbols, set_Symbols)

    def set_StartDateString(self,StartDateString):
        self._StartDateString = StartDateString
    def get_StartDateString(self):
        return self._StartDateString
    StartDateString = property(get_StartDateString, set_StartDateString)

    def set_Period(self,Period):
        self._Period = Period
    def get_Period(self):
        return self._Period
    Period = property(get_Period, set_Period)

    def set_StockHistoryDataframe(self,StockHistoryDataframe):
        self._StockHistoryDataframe = StockHistoryDataframe
    def get_StockHistoryDataframe(self):
        return self._StockHistoryDataframe
    StockHistoryDataframe = property(get_StockHistoryDataframe, set_StockHistoryDataframe)

    def set_ReturnsDataframe(self,ReturnsDataframe):
        self._ReturnsDataframe = ReturnsDataframe
    def get_ReturnsDataframe(self):
        return self._ReturnsDataframe
    ReturnsDataframe = property(get_ReturnsDataframe, set_ReturnsDataframe)

    
    def __init__(self
                    , symbols
                    , startdate_string='2004-12-31'
                    , period = 'daily' #or monthly
                    , source = 'Yahoo'
                    #, enddate_string='xxx'
                ):
        print('Initialized class pullreturns.perform')
        
        self.Symbols = symbols
        self.StartDateString = startdate_string
        self.Period = period
        
        import datetime

        yesterday_date = datetime.date.fromordinal(datetime.date.today().toordinal()-1)

        import pullprices as pp

        if period == 'daily':
            self.StockHistoryDataframe = pp.stockhistory(symbols,startdate_string,str(yesterday_date))
            self.ReturnsDataframe = self.dailyreturns()
            


    def dailyreturns(self,):

        symbols = self.Symbols 
        import datetime
        today_date = datetime.date.today()
        import pullprices as pp
        df_00 = self.StockHistoryDataframe
        
        import pandas as pd
        dates1 = pd.date_range('1910-01-01', str(today_date), freq='D')
        
        dummy_date = datetime.datetime.strptime("1801-01-01", "%Y-%m-%d")
        prev_date = dummy_date
        prev_value = float('Nan')
        
        rows_dailyreturns = []        

        rows_dailyreturns.append(['prev_date','curr_date','ticker','prev_value','curr_value','change_pct'])
        
        d_of_prevs = {}
        prevclose = []
        for dt in dates1:
            print str(dt.date())
            
            if str(dt.date()) in df_00.index:
                myobj = df_00.loc[str(dt.date())]
                
                curr_date = dt.date()
                for s in symbols:
                    if s in d_of_prevs:
                        if len(d_of_prevs[s]) > 0:
                            t,c,d = d_of_prevs[s]
                            print t,c,d
                            if is_number(myobj[s]):
                                curr_value = myobj[s]
                                prev_value = c
                                if is_number(curr_value) and is_number(prev_value):
                                    change_pct = (float(curr_value) - float(prev_value))/float(prev_value)
                                else:
                                    change_pct =  float('NaN')
                                #print str(d),str(curr_date), s, prev_value, curr_value, change_pct
                                rows_dailyreturns.append([str(d),str(curr_date), t, prev_value, curr_value, change_pct])

                
                for s in symbols:
                    print 'xxx',myobj[s]                
                    if not s in d_of_prevs:
                        d_of_prevs[s] = []
                    if is_number(myobj[s]):
                        d_of_prevs[s] = [s,myobj[s],curr_date]

##        return rows_dailyreturns
##                curr_value = myobj['Adj Close']
##                if prev_date != dummy_date:
##                    if is_number(curr_value) and is_number(prev_value):
##                        change_pct = (float(curr_value) - float(prev_value))/float(prev_value)
##                    else:
##                        change_pct =  float('NaN')
##                    
##                    rows_dailyreturns.append([symbols,curr_date,change_pct,curr_value])
##
##                    
##                prev_date = dt.date()
##                prev_value = myobj['Adj Close']
##        
##        
        headers = rows_dailyreturns.pop(0)
        df_dailyreturns = pd.DataFrame(rows_dailyreturns,columns=headers)
        print df_dailyreturns
        return df_dailyreturns
##        #print df_00
##        
##        stock_dataframe = pp.stock_dataframe(symbols)
##        myobj = df_00.loc[str(prev_date)]
##        prev_ending = myobj['Adj Close']
##        curr_price = stock_dataframe['last'][0]
##        if is_number(curr_price) and is_number(prev_ending):
##            curr_pctchange = (float(curr_price) - float(prev_ending)) / float(prev_ending)
##        else:
##            curr_pctchange = float('NaN')
##        
##        #df_curr = pd.DataFrame([symbols,today_date,curr_pctchange], columns=['a_symbols','b_periodend','e_pctchange'])
##        #newrow = np.array([symbols,today_date,curr_pctchange])
##        #columns=['a_symbols','b_periodend','e_pctchange','d_end']
##        
##        #import numpy as np
##        
##        mydict = {}
##        mydict[0] = {'a_symbols':symbols,'b_periodend':str(today_date),'e_pctchange':curr_pctchange,'d_end':curr_price}
##        df_curr = pd.DataFrame(mydict).T
##        #print df_curr.T
##        
##        
##        df_dailyreturnstotoday = df_dailyreturnsfinite.append(df_curr, ignore_index=True)
##        #print df_dailyreturns
##        #print str(today_date)[:7]
##        return df_dailyreturnstotoday

    def standarddeviationofmonthlyreturns(self,):
        df_monthlyreturnsusingyahoosymbols = df_monthlyreturnsusingyahoosymbols = self.MonthlyReturnsDataframe
        std_float = float(df_monthlyreturnsusingyahoosymbols['e_pctchange'].std())
        return std_float
    
if __name__=='__main__':
    symbols = ['AAPL', 'MSFT', 'SPY', 'IBM', 'T', 'AMD','INTC','ACN', 'VZ', 'ORCL','DIS','BA','AMGN','MCD','CELG','LLY','COST','BIIB','MDLZ','TJX']
    startdate = '2017-07-31'
    o = perform(symbols,startdate,'daily')
    print '------ DailyReturnsDataframe ------'
    print o.ReturnsDataframe()
