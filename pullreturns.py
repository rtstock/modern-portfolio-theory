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
    def set_SymbolsList(self,SymbolsList):
        self._SymbolsList = SymbolsList
    def get_SymbolsList(self):
        return self._SymbolsList
    SymbolsList = property(get_SymbolsList, set_SymbolsList)

    def set_StartDateString(self,StartDateString):
        self._StartDateString = StartDateString
    def get_StartDateString(self):
        return self._StartDateString
    StartDateString = property(get_StartDateString, set_StartDateString)

    def set_EndDateString(self,EndDateString):
        self._EndDateString = EndDateString
    def get_EndDateString(self):
        return self._EndDateString
    EndDateString = property(get_EndDateString, set_EndDateString)

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

    def set_ReturnsDataframeTimes100(self,ReturnsDataframeTimes100):
        self._ReturnsDataframeTimes100 = ReturnsDataframeTimes100
    def get_ReturnsDataframeTimes100(self):
        return self._ReturnsDataframeTimes100
    ReturnsDataframeTimes100 = property(get_ReturnsDataframeTimes100, set_ReturnsDataframeTimes100)
    
    def set_AnnualizedReturnsDataframe(self,AnnualizedReturnsDataframe):
        self._AnnualizedReturnsDataframe = AnnualizedReturnsDataframe
    def get_AnnualizedReturnsDataframe(self):
        return self._AnnualizedReturnsDataframe
    AnnualizedReturnsDataframe = property(get_AnnualizedReturnsDataframe, set_AnnualizedReturnsDataframe)
    
    def __init__(self
                    , symbols
                    , startdate = '2004-12-31'
                    , enddate = '2005-12-31'
                ):
        
        print('Initialized class pullreturns.perform')
        
        self.SymbolsList = symbols
        self.StartDateString = startdate
        self.EndDateString = enddate
        
        import datetime
        import numpy as np
        
        yesterday_date = datetime.date.fromordinal(datetime.date.today().toordinal()-1)
        import pullprices as pp1
        df_good,df_missing = pp1.stockhistoryasdataframe(symbols,startdate,enddate)
        list_of_good_symbols = np.unique(df_good[['Ticker']])
        print 'list_of_good_symbols', list_of_good_symbols
        self.SymbolsList = list_of_good_symbols
        df_pivot = df_good.pivot(index='Date', columns='Ticker', values='Adj Close')
        #print df_pivot
        self.StockHistoryDataframe = df_pivot
        #import pullpricesusingpandas as pp
        #self.StockHistoryDataframe = pp.stockhistory(symbols,startdate,enddate)
        self.ReturnsDataframe,self.ReturnsDataframeTimes100 = self.dailyreturns()
        self.AnnualizedReturnsDataframe = self.annualizedreturns()
                                          



    def dailyreturns(self,):

        symbols = self.SymbolsList 
        import datetime
        today_date = datetime.date.today()
        #import pullpricesusingpandas as pp
        df_00 = self.StockHistoryDataframe
        
        import pandas as pd
        dates1 = pd.date_range('1910-01-01', str(today_date), freq='D')
        
        dummy_date = datetime.datetime.strptime("1801-01-01", "%Y-%m-%d")
        prev_date = dummy_date
        prev_value = float('Nan')
        
        rows_dailyreturns = []        
        rows_dailyreturnstimes100 = []
        rows_dailyreturns.append(['prev_date','curr_date','ticker','prev_value','curr_value','change_pct'])
        rows_dailyreturnstimes100.append(['prev_date','curr_date','ticker','prev_value','curr_value','change_pct'])
        
        d_of_prevs = {}
        prevclose = []
        for dt in dates1:
            if str(dt.date()) in df_00.index:
                myobj = df_00.loc[str(dt.date())]
                
                curr_date = dt.date()
                for s in symbols:
                    if s in d_of_prevs:
                        if len(d_of_prevs[s]) > 0:
                            t,c,d = d_of_prevs[s]
                            #print t,c,d
                            if is_number(myobj[s]):
                                curr_value = myobj[s]
                                prev_value = c
                                if is_number(curr_value) and is_number(prev_value):
                                    change_pct = (float(curr_value) - float(prev_value))/float(prev_value)
                                else:
                                    change_pct =  float('NaN')
                                #print str(d),str(curr_date), s, prev_value, curr_value, change_pct
                                rows_dailyreturns.append([str(d),str(curr_date), t, prev_value, curr_value, change_pct])
                                rows_dailyreturnstimes100.append([str(d),str(curr_date), t, prev_value, curr_value, change_pct * 100.0])

                
                for s in symbols:
                    #print 'xxx',myobj[s]                
                    if not s in d_of_prevs:
                        d_of_prevs[s] = []
                    if is_number(myobj[s]):
                        d_of_prevs[s] = [s,myobj[s],curr_date]
        headers = rows_dailyreturns.pop(0)
        df_dailyreturns = pd.DataFrame(rows_dailyreturns, columns = headers)

        headers = rows_dailyreturnstimes100.pop(0)
        df_dailyreturnstimes100 = pd.DataFrame(rows_dailyreturnstimes100, columns = headers)
        
        return df_dailyreturns,df_dailyreturnstimes100


    def annualizedreturns(self):
        ar = self._annualizeddailyreturns()
        
        #if uselogreturns == False:
        #    ar = self._annualizeddailyreturn()  
        #else:
        #    ar = self._annualizeddailyreturnusinglogreturns()
        return ar
    

    def _annualizeddailyreturns(self,):
        ls_final = []
        ls_final.append(['symbol','start_date','end_date','annualized_return', 'cumulative_return','last_adjprice','last_adjprice'])
        for s in self.SymbolsList:
            print 'Doing annualized return for',s
            dfr = self.ReturnsDataframe.copy()
            df_dailyreturns = dfr[(dfr.ticker == s)]
            df_dailyreturns = df_dailyreturns.dropna()
            df_dailyreturns.sort_index(inplace = True)
            #print df_dailyreturns
            # =PRODUCT(F85:F155)^(1/($B85/12))-1
            # [(1.13)*(0.98)*(1.15)*(1.08)]^(12/42)-1
            #df_dailyreturns = self.dailyreturns()
            #df_dailyreturns = df_dailyreturns.dropna()
            
            first_valid_index = df_dailyreturns.first_valid_index()
            #print 'first_valid_index', first_valid_index
            firstdate = df_dailyreturns.loc[first_valid_index]['curr_date']
            first_adjprice = df_dailyreturns.loc[first_valid_index]['curr_value']
            
            last_valid_index = df_dailyreturns.last_valid_index()
            #print 'last_valid_index',last_valid_index
            lastdate = df_dailyreturns.loc[last_valid_index]['curr_date']
            last_adjprice = df_dailyreturns.loc[last_valid_index]['curr_value']
            #df_dailyreturns.loc[df_dailyreturns.index,'change_pct']= df_dailyreturns.loc[df_dailyreturns.index, 'change_pct'] + float(1.0)
            df_dailyreturns.loc[df_dailyreturns.index,'change_pct_unitized'] = df_dailyreturns.loc[df_dailyreturns.index, 'change_pct'] + float(1.0)
            ls_dailyreturns = df_dailyreturns['change_pct_unitized'].values.tolist()
            #print 'lastdate',lastdate
            #print '------------------- df_dailyreturns ----------------------'
            #print df_dailyreturns
            listmultiplied = reduce(lambda x, y: x*y, ls_dailyreturns)
            #print 'listmultiplied',listmultiplied

            #years between
            import datetime
            time1 = datetime.datetime.strptime(str(firstdate) + ' 00:00:00.00', "%Y-%m-%d %H:%M:%S.%f")
            time2 = datetime.datetime.strptime(str(lastdate) + ' 23:59:59.999999', "%Y-%m-%d %H:%M:%S.%f") #datetime.datetime.now()
            #print 'times',time1,time2
            elapsedTime = time2 - time1
            yrs = float(divmod(elapsedTime.total_seconds(), 60.0)[0]/60.0/24.0/365.0)
            #print 'years',yrs
            
            adr = listmultiplied ** (float(1)/(yrs)) - 1.0
            df_dailyreturns.loc[df_dailyreturns.index,'cumulative_return']  = (1 + df_dailyreturns.change_pct).cumprod() - 1
            #print df_dailyreturns
            cumr = df_dailyreturns.loc[last_valid_index]['cumulative_return']
            ls_final.append([s,firstdate,lastdate,adr,cumr,first_adjprice,last_adjprice])
        headers = ls_final.pop(0)
        import pandas as pd
        df_final = pd.DataFrame(ls_final, columns = headers)
        return df_final


    def _annualizeddailyreturnusinglogreturns_old(self,):
        # =PRODUCT(F85:F155)^(1/($B85/12))-1
        # [(1.13)*(0.98)*(1.15)*(1.08)]^(12/42)-1
        df_dailyreturns = self.dailyreturns()
        df_dailyreturns = df_dailyreturns.dropna()
        
        df_dailyreturns.sort_index(inplace = True)
        firstdate = df_dailyreturns.loc[0]['b_periodend']
        #print firstdate
        lastdate = df_dailyreturns.loc[len(df_dailyreturns)-1]['b_periodend']
        #print lastdate
        #print df_dailyreturns
        df_dailyreturns.loc[df_dailyreturns.index,'e_logreturnunitized']= df_dailyreturns.loc[df_dailyreturns.index, 'e_logreturn'] + float(1.0)
        ls_dailyreturns = df_dailyreturns['e_logreturnunitized'].values.tolist()
        listmultiplied = reduce(lambda x, y: x*y, ls_dailyreturns)
        #print listmultiplied

        #years between
        import datetime
        time1 = datetime.datetime.strptime(str(firstdate) + ' 16:00', "%Y-%m-%d %H:%M")
        time2 = datetime.datetime.strptime(str(lastdate) + ' 16:00', "%Y-%m-%d %H:%M")#datetime.datetime.now() 
        elapsedTime = time2 - time1
        yrs = float(divmod(elapsedTime.total_seconds(), 60.0)[0]/60.0/24.0/365.0)
        #print 'yrs',yrs

        adr = listmultiplied ** (float(1)/(yrs)) - 1.0
        return adr



    def standarddeviationofmonthlyreturns(self,):
        df_monthlyreturnsusingyahoosymbols = df_monthlyreturnsusingyahoosymbols = self.MonthlyReturnsDataframe
        std_float = float(df_monthlyreturnsusingyahoosymbols['e_pctchange'].std())
        return std_float
    
if __name__=='__main__':
    #symbols = ['FB', 'MSFT', 'SPY', 'IBM', 'T', 'AMD','INTC','ACN', 'VZ', 'ORCL','DIS','BA','AMGN','MCD','CELG','LLY','COST','BIIB','MDLZ','TJX']
    symbols = ['FB', 'MSFT', 'SPY', 'IBM']
##    symbols = ['GOOGL',
##                            'FB',
##                            'MSFT',
##                            'LRCX',
##                            'EVR',
##                            'MASI',
##                            'CELG',
##                            'AOS',
##                            'LPX',
##                            'MRK',
##                            'EVR',
##                            'JNJ',
##                            'INTC',
##                            'GOLD',
##                            'LMT',
##                            'RTN',
##                            'BP',
##                            'T',
##                            'HSBC',
##                            'THO'
##                            ]
    startdate = '2016-06-30'
    enddate = '2017-06-30'
    o = perform(symbols,startdate,enddate)
##    print '------ Stock History Dataframe ------'
##    print o.StockHistoryDataframe
    #print '------ Daily Returns Dataframe ------'
    #print o.ReturnsDataframe

    print '------ Daily Returns Times 100 Dataframe ------'
    print o.ReturnsDataframeTimes100

    print '------ Annualized Returns ------'
    print o.AnnualizedReturnsDataframe

