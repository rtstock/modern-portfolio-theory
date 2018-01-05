# -*- coding: utf-8 -*-
"""
Created on Tue Jul 21 14:40:39 2015

@author: justin.malinchak
"""


import datetime
import pandas as pd
import numpy as np
def validate_date(date_text):
    try:
        datetime.datetime.strptime(date_text, '%Y-%m-%d')
        return True
    except ValueError:
        #raise ValueError("Incorrect data format, should be YYYY-MM-DD")
        return False
        

def is_number(s):
    try:
        if np.isnan(s) == True:
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

    def set_HistoryOfAdjClosePricesDataframe(self,HistoryOfAdjClosePricesDataframe):
        self._HistoryOfAdjClosePricesDataframe = HistoryOfAdjClosePricesDataframe
    def get_HistoryOfAdjClosePricesDataframe(self):
        return self._HistoryOfAdjClosePricesDataframe
    HistoryOfAdjClosePricesDataframe = property(get_HistoryOfAdjClosePricesDataframe, set_HistoryOfAdjClosePricesDataframe)

    def set_HistoryOfClosePricesDataframe(self,HistoryOfClosePricesDataframe):
        self._HistoryOfClosePricesDataframe = HistoryOfClosePricesDataframe
    def get_HistoryOfClosePricesDataframe(self):
        return self._HistoryOfClosePricesDataframe
    HistoryOfClosePricesDataframe = property(get_HistoryOfClosePricesDataframe, set_HistoryOfClosePricesDataframe)
    
    def set_TotalReturnsDataframe(self,TotalReturnsDataframe):
        self._TotalReturnsDataframe = TotalReturnsDataframe
    def get_TotalReturnsDataframe(self):
        return self._TotalReturnsDataframe
    TotalReturnsDataframe = property(get_TotalReturnsDataframe, set_TotalReturnsDataframe)
    
    def set_PriceChangeReturnsDataframe(self,PriceChangeReturnsDataframe):
        self._PriceChangeReturnsDataframe = PriceChangeReturnsDataframe
    def get_PriceChangeReturnsDataframe(self):
        return self._PriceChangeReturnsDataframe
    PriceChangeReturnsDataframe = property(get_PriceChangeReturnsDataframe, set_PriceChangeReturnsDataframe)
##
##    def set_TotalReturnsDataframeTimes100(self,TotalReturnsDataframeTimes100):
##        self._TotalReturnsDataframeTimes100 = TotalReturnsDataframeTimes100
##    def get_TotalReturnsDataframeTimes100(self):
##        return self._TotalReturnsDataframeTimes100
##    TotalReturnsDataframeTimes100 = property(get_TotalReturnsDataframeTimes100, set_TotalReturnsDataframeTimes100)
    
    def set_AggregatedTotalReturnsDataframe(self,AggregatedTotalReturnsDataframe):
        self._AggregatedTotalReturnsDataframe = AggregatedTotalReturnsDataframe
    def get_AggregatedTotalReturnsDataframe(self):
        return self._AggregatedTotalReturnsDataframe
    AggregatedTotalReturnsDataframe = property(get_AggregatedTotalReturnsDataframe, set_AggregatedTotalReturnsDataframe)
    
    def set_AggregatedPriceChangeReturnsDataframe(self,AggregatedPriceChangeReturnsDataframe):
        self._AggregatedPriceChangeReturnsDataframe = AggregatedPriceChangeReturnsDataframe
    def get_AggregatedPriceChangeReturnsDataframe(self):
        return self._AggregatedPriceChangeReturnsDataframe
    AggregatedPriceChangeReturnsDataframe = property(get_AggregatedPriceChangeReturnsDataframe, set_AggregatedPriceChangeReturnsDataframe)
    
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
        df_good,df_missing = pp1.pull().stockhistoryasdataframe(symbols,startdate,enddate)
        list_of_good_symbols = np.unique(df_good[['Ticker']])
        print 'count of symbols returned from pullprices', len(list_of_good_symbols)
        print 'list_of_good_symbols', list_of_good_symbols
        if len(df_missing) > 0:
            list_of_missing_symbols =  np.unique(df_missing[['Ticker']])
            print 'list_of_missing_symbols', list_of_missing_symbols
        self.SymbolsList = list_of_good_symbols

        df_pivotadjclose = df_good.pivot(index='Date', columns='Ticker', values='Adj Close')
        df_pivotclose = df_good.pivot(index='Date', columns='Ticker', values='Close')
        #print df_pivotadjclose
        self.HistoryOfAdjClosePricesDataframe = df_pivotadjclose
        print '--- self.HistoryOfAdjClosePricesDataframe ----'
        print self.HistoryOfAdjClosePricesDataframe
        self.HistoryOfClosePricesDataframe = df_pivotclose

        #self.TotalReturnsDataframe = self.dailyreturns('Total')        
        #self.PriceChangeReturnsDataframe = self.dailyreturns('PriceChange')
        self.LogDailyReturnsDataframe = self.dailylogreturns('PriceChange')
        self.AggregatedTotalReturnsDataframe = self.aggregatedreturns('Total')
        self.AggregatedPriceChangeReturnsDataframe = self.aggregatedreturns('PriceChange')
                                          
##    def calc_beta_test02():
##        df = self.AggregatedTotalReturnsDataframe
##        df['mean'] = df.mean(axis=1)
##        np_array = df.values
##        print np_array
##        m = df['mean'] # market returns are column zero from numpy array
##        for s in self.SymbolsList:        
##            x = df[s] # stock returns are column one from numpy array
##            covariance = np.cov(x,m) # Calculate covariance between stock and market
##            beta = covariance[0,1]/covariance[1,1]
##        return beta
##
##
##    def calc_beta_test01(df):
##        np_array = df.values
##        m = np_array[:,0] # market returns are column zero from numpy array
##        s = np_array[:,1] # stock returns are column one from numpy array
##        covariance = np.cov(s,m) # Calculate covariance between stock and market
##        beta = covariance[0,1]/covariance[1,1]
##        return beta
    def dailylogreturns(self,totalorpricechange='PriceChange'):

        symbols = self.SymbolsList 
        import datetime
        today_date = datetime.date.today()
        #import pullpricesusingpandas as pp
        if totalorpricechange == 'PriceChange':
            df_00 = self.HistoryOfClosePricesDataframe
        else:
            df_00 = self.HistoryOfAdjClosePricesDataframe
        print '--- df_00 ---  pullreturns.dailyreturns()'
        print df_00
        
        df_01 = pd.DataFrame(index=df_00.index.copy())
        for s in self.SymbolsList:
            #df_01[s] = df_00[s].pct_change()
            df_01[s] = np.log(1.0 + df_00[s].pct_change())
        print df_01
        stop
        #df['pct_change'] = df.price.pct_change()
        #df['log_return'] = np.log(1 + df.pct_change)
    def dailyreturns(self,totalorpricechange='PriceChange'):

        symbols = self.SymbolsList 
        import datetime
        today_date = datetime.date.today()
        #import pullpricesusingpandas as pp
        if totalorpricechange == 'PriceChange':
            df_00 = self.HistoryOfClosePricesDataframe
        else:
            df_00 = self.HistoryOfAdjClosePricesDataframe
        print '--- df_00 ---  pullreturns.dailyreturns()'
        print df_00
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
        
        return df_dailyreturns #,df_dailyreturnstimes100


##    def aggregatedreturns(self):
##        ar = self._aggregateddailyreturns()
##        
##        #if uselogreturns == False:
##        #    ar = self._annualizeddailyreturn()  
##        #else:
##        #    ar = self._annualizeddailyreturnusinglogreturns()
##        return ar
    

    def aggregatedreturns(self,totalorpricechange='PriceChange'):
        import numpy as np
        import random
        import datetime
        ls_final = []
        ls_final.append(['symbol','start_date','end_date','annualized_return', 'cumulative_return','random_return','start_price','end_price','stdev','stdev_np','mean_np'])
        i = 0
        for s in self.SymbolsList:
            i += 1
            print 'Doing aggregated return for',totalorpricechange,i,s
            if totalorpricechange == 'PriceChange':
                dfr = self.PriceChangeReturnsDataframe.copy()
            else:
                dfr = self.TotalReturnsDataframe.copy()
            #333333
            #print '----- dfr ------', 'pullreturns'
            #print dfr
            df_dailyreturns = dfr[(dfr.ticker == s)]
            df_dailyreturns = df_dailyreturns.dropna()
            df_dailyreturns.sort_index(inplace = True)
            #print '----- df_dailyreturns ------', 'pullreturns'
            #print df_dailyreturns
            # =PRODUCT(F85:F155)^(1/($B85/12))-1
            # [(1.13)*(0.98)*(1.15)*(1.08)]^(12/42)-1
            #df_dailyreturns = self.dailyreturns()
            #df_dailyreturns = df_dailyreturns.dropna()
            
            first_valid_index = df_dailyreturns.first_valid_index()
            #print 'first_valid_index', first_valid_index
            firstdate = df_dailyreturns.loc[first_valid_index]['curr_date']
            start_price = df_dailyreturns.loc[first_valid_index]['curr_value']
            
            last_valid_index = df_dailyreturns.last_valid_index()
            #print 'last_valid_index',last_valid_index
            lastdate = df_dailyreturns.loc[last_valid_index]['curr_date']
            end_price = df_dailyreturns.loc[last_valid_index]['curr_value']
            #df_dailyreturns.loc[df_dailyreturns.index,'change_pct']= df_dailyreturns.loc[df_dailyreturns.index, 'change_pct'] + float(1.0)

            stdev = float(df_dailyreturns.loc[df_dailyreturns.index, 'change_pct'].std())
            
            stdev_np = np.std(df_dailyreturns.loc[df_dailyreturns.index, 'change_pct'], ddof=1)
            mean_np = np.mean(df_dailyreturns.loc[df_dailyreturns.index, 'change_pct'])
            #print 'stdev', s,std_float
            df_dailyreturns.loc[df_dailyreturns.index,'change_pct_unitized'] = df_dailyreturns.loc[df_dailyreturns.index, 'change_pct'] + float(1.0)
            ls_dailyreturns = df_dailyreturns['change_pct_unitized'].values.tolist()
            #print 'lastdate',lastdate
            #print '------------------- df_dailyreturns ----------------------'
            #print df_dailyreturns
            listmultiplied = reduce(lambda x, y: x*y, ls_dailyreturns)
            #print 'listmultiplied',listmultiplied

            #years between

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
            
            randret = random.randint(0, 200)  # 0 or 1(both incl.)
            randr = adr * randret/100.0

            ls_final.append([s,firstdate,lastdate,adr,cumr,randr,start_price,end_price,stdev,stdev_np,mean_np])
        headers = ls_final.pop(0)
        import pandas as pd
        df_final = pd.DataFrame(ls_final, columns = headers)
        print 'pullreturns - finished def aggregatedreturns with ', len(df_final)
        return df_final


##    def _annualizeddailyreturnusinglogreturns_old(self,):
##        # =PRODUCT(F85:F155)^(1/($B85/12))-1
##        # [(1.13)*(0.98)*(1.15)*(1.08)]^(12/42)-1
##        df_dailyreturns = self.dailyreturns()
##        df_dailyreturns = df_dailyreturns.dropna()
##        
##        df_dailyreturns.sort_index(inplace = True)
##        firstdate = df_dailyreturns.loc[0]['b_periodend']
##        #print firstdate
##        lastdate = df_dailyreturns.loc[len(df_dailyreturns)-1]['b_periodend']
##        #print lastdate
##        #print df_dailyreturns
##        df_dailyreturns.loc[df_dailyreturns.index,'e_logreturnunitized']= df_dailyreturns.loc[df_dailyreturns.index, 'e_logreturn'] + float(1.0)
##        ls_dailyreturns = df_dailyreturns['e_logreturnunitized'].values.tolist()
##        listmultiplied = reduce(lambda x, y: x*y, ls_dailyreturns)
##        #print listmultiplied
##
##        #years between
##        import datetime
##        time1 = datetime.datetime.strptime(str(firstdate) + ' 16:00', "%Y-%m-%d %H:%M")
##        time2 = datetime.datetime.strptime(str(lastdate) + ' 16:00', "%Y-%m-%d %H:%M")#datetime.datetime.now() 
##        elapsedTime = time2 - time1
##        yrs = float(divmod(elapsedTime.total_seconds(), 60.0)[0]/60.0/24.0/365.0)
##        #print 'yrs',yrs
##
##        adr = listmultiplied ** (float(1)/(yrs)) - 1.0
##        return adr

    
if __name__=='__main__':
    #symbols = ['FB', 'MSFT', 'SPY', 'IBM', 'T', 'AMD','INTC','ACN', 'VZ', 'ORCL','DIS','BA','AMGN','MCD','CELG','LLY','COST','BIIB','MDLZ','TJX']
    #symbols  = ['FB', 'MSFT', 'SPY', 'IBM']   
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

    #symbols = ['LAZ', 'LMT', 'RTN', 'MAS', 'AMAT', 'INTC', 'LPX', 'GRMN', 'PCLN', 'KSS', 'JWN', 'M', 'GPS', 'LOW', 'PEP', 'CVS', 'CL', 'KMB', 'MO', 'PM', 'CVX', 'BAC', 'BEN', 'MS', 'AXP', 'CELG', 'AMGN', 'JNJ', 'LLY', 'MMM', 'UNP', 'CSCO', 'SWKS', 'CA', 'STX', 'LYB', 'APD', 'T', 'TGT', 'HD', 'ETR', 'AES', 'HOG', 'F', 'GPC', 'LEG', 'WHR', 'NWL', 'TRIP', 'HAS', 'BC', 'CMCSA', 'DIS', 'VIA', 'DISH', 'NWS', 'PAG', 'CRI', 'COLM', 'SKX', 'NKE', 'TAP', 'CASY', 'HRL', 'HAIN', 'SJM', 'ADM', 'KHC', 'MDLZ', 'FTI', 'SLB', 'NFX', 'KMI', 'CXO', 'MUR', 'WPX', 'EGN', 'XOM', 'LNG', 'FCNCA', 'LUK', 'Y', 'WTM', 'AXS', 'ALKS', 'MDT', 'XRAY', 'CAH', 'MD', 'PDCO', 'UHS', 'AGN', 'ARNC', 'UAL', 'AAL', 'GE', 'SNA', 'WAB', 'FLS', 'VRSK', 'GWR', 'GWW', 'VSAT', 'AVT', 'TWTR', 'AMD', 'QCOM', 'FSLR', 'OTEX', 'NUAN', 'HPE', 'RPM', 'MLM', 'VMC', 'SEE', 'SON', 'HHC', 'LVLT', 'LVLT', 'S', 'JLL']
    symbols = ['MAR', 'MON', 'NOV', 'A', 'AAL', 'AAP', 'AAPL', 'ABBV', 'ABC', 'ABT', 'ACN', 'ADBE', 'ADI', 'ADM', 'ADP', 'ADS', 'ADSK', 'AEE', 'AEP', 'AES', 'AET', 'AFL', 'AGN', 'AIG', 'AIV', 'AIZ', 'AJG', 'AKAM', 'ALB', 'ALGN', 'ALK', 'ALL', 'ALLE', 'ALXN', 'AMAT', 'AMD', 'AME', 'AMG', 'AMGN', 'AMP', 'AMT', 'AMZN', 'ANDV', 'ANSS', 'ANTM', 'AON', 'AOS', 'APA', 'APC', 'APD', 'APH', 'ARE', 'ARNC', 'ATVI', 'AVB', 'AVGO', 'AVY', 'AWK', 'AXP', 'AYI', 'AZO', 'BA', 'BAC', 'BAX', 'BBT', 'BBY', 'BCR', 'BDX', 'BEN', 'BF.B', 'BHF', 'BHGE', 'BIIB', 'BK', 'BLK', 'BLL', 'BMY', 'BRK.B', 'BSX', 'BWA', 'BXP', 'C', 'CA', 'CAG', 'CAH', 'CAT', 'CB', 'CBG', 'CBOE', 'CBS', 'CCI', 'CCL', 'CDNS', 'CELG', 'CERN', 'CF', 'CFG', 'CHD', 'CHK', 'CHRW', 'CHTR', 'CI', 'CINF', 'CL', 'CLX', 'CMA', 'CMCSA', 'CME', 'CMG', 'CMI', 'CMS', 'CNC', 'CNP', 'COF', 'COG', 'COH', 'COL', 'COO', 'COP', 'COST', 'COTY', 'CPB', 'CRM', 'CSCO', 'CSRA', 'CSX', 'CTAS', 'CTL', 'CTSH', 'CTXS', 'CVS', 'CVX', 'CXO', 'D', 'DAL', 'DE', 'DFS', 'DG', 'DGX', 'DHI', 'DHR', 'DIS', 'DISCA', 'DISCK', 'DISH', 'DLPH', 'DLR', 'DLTR', 'DOV', 'DPS', 'DRE', 'DRI', 'DTE', 'DUK', 'DVA', 'DVN', 'DWDP', 'DXC', 'EA', 'EBAY', 'ECL', 'ED', 'EFX', 'EIX', 'EL', 'EMN', 'EMR', 'EOG', 'EQIX', 'EQR', 'EQT', 'ES', 'ESRX', 'ESS', 'ETFC', 'ETN', 'ETR', 'EVHC', 'EW', 'EXC', 'EXPD', 'EXPE', 'EXR', 'F', 'FAST', 'FB', 'FBHS', 'FCX', 'FDX', 'FE', 'FFIV', 'FIS', 'FISV', 'FITB', 'FL', 'FLIR', 'FLR', 'FLS', 'FMC', 'FOX', 'FOXA', 'FRT', 'FTI', 'FTV', 'GD', 'GE', 'GGP', 'GILD', 'GIS', 'GLW', 'GM', 'GOOG', 'GOOGL', 'GPC', 'GPN', 'GPS', 'GRMN', 'GS', 'GT', 'GWW', 'HAL', 'HAS', 'HBAN', 'HBI', 'HCA', 'HCN', 'HCP', 'HD', 'HES', 'HIG', 'HLT', 'HOG', 'HOLX', 'HON', 'HP', 'HPE', 'HPQ', 'HRB', 'HRL', 'HRS', 'HSIC', 'HST', 'HSY', 'HUM', 'IBM', 'ICE', 'IDXX', 'IFF', 'ILMN', 'INCY', 'INFO', 'INTC', 'INTU', 'IP', 'IPG', 'IR', 'IRM', 'ISRG', 'IT', 'ITW', 'IVZ', 'JBHT', 'JCI', 'JEC', 'JNJ', 'JNPR', 'JPM', 'JWN', 'K', 'KEY', 'KHC', 'KIM', 'KLAC', 'KMB', 'KMI', 'KMX', 'KO', 'KORS', 'KR', 'KSS', 'KSU', 'L', 'LB', 'LEG', 'LEN', 'LH', 'LKQ', 'LLL', 'LLY', 'LMT', 'LNC', 'LNT', 'LOW', 'LRCX', 'LUK', 'LUV', 'LVLT', 'LYB', 'M', 'MA', 'MAA', 'MAC', 'MAS', 'MAT', 'MCD', 'MCHP', 'MCK', 'MCO', 'MDLZ', 'MDT', 'MET', 'MGM', 'MHK', 'MKC', 'MLM', 'MMC', 'MMM', 'MNST', 'MO', 'MOS', 'MPC', 'MRK', 'MRO', 'MS', 'MSFT', 'MSI', 'MTB', 'MTD', 'MU', 'MYL', 'NAVI', 'NBL', 'NDAQ', 'NEE', 'NEM', 'NFLX', 'NFX', 'NI', 'NKE', 'NLSN', 'NOC', 'NRG', 'NSC', 'NTAP', 'NTRS', 'NUE', 'NVDA', 'NWL', 'NWS', 'NWSA', 'O', 'OKE', 'OMC', 'ORCL', 'ORLY', 'OXY', 'PAYX', 'PBCT', 'PCAR', 'PCG', 'PCLN', 'PDCO', 'PEG', 'PEP', 'PFE', 'PFG', 'PG', 'PGR', 'PH', 'PHM', 'PKG', 'PKI', 'PLD', 'PM', 'PNC', 'PNR', 'PNW', 'PPG', 'PPL', 'PRGO', 'PRU', 'PSA', 'PSX', 'PVH', 'PWR', 'PX', 'PXD', 'PYPL', 'Q', 'QCOM', 'QRVO', 'RCL', 'RE', 'REG', 'REGN', 'RF', 'RHI', 'RHT', 'RJF', 'RL', 'RMD', 'ROK', 'ROP', 'ROST', 'RRC', 'RSG', 'RTN', 'SBAC', 'SBUX', 'SCG', 'SCHW', 'SEE', 'SHW', 'SIG', 'SJM', 'SLB', 'SLG', 'SNA', 'SNI', 'SNPS', 'SO', 'SPG', 'SPGI', 'SPLS', 'SRCL', 'SRE', 'STI', 'STT', 'STX', 'STZ', 'SWK', 'SWKS', 'SYF', 'SYK', 'SYMC', 'SYY', 'T', 'TAP', 'TDG', 'TEL', 'TGT', 'TIF', 'TJX', 'TMK', 'TMO', 'TRIP', 'TROW', 'TRV', 'TSCO', 'TSN', 'TSS', 'TWX', 'TXN', 'TXT', 'UA', 'UAA', 'UAL', 'UDR', 'UHS', 'ULTA', 'UNH', 'UNM', 'UNP', 'UPS', 'URI', 'USB', 'UTX', 'V', 'VAR', 'VFC', 'VIAB', 'VLO', 'VMC', 'VNO', 'VRSK', 'VRSN', 'VRTX', 'VTR', 'VZ', 'WAT', 'WBA', 'WDC', 'WEC', 'WFC', 'WHR', 'WLTW', 'WM', 'WMB', 'WMT', 'WRK', 'WU', 'WY', 'WYN', 'WYNN', 'XEC', 'XEL', 'XL', 'XLNX', 'XOM', 'XRAY', 'XRX', 'XYL', 'YUM', 'ZBH', 'ZION', 'ZTS']
    symbols = ['MAR', 'MON', 'NOV', 'A', 'AAL', 'AAP', 'AAPL',]
    startdate = '2017-07-01'
    enddate = '2017-08-05'
    o = perform(symbols,startdate,enddate)
##    print '------ Stock History Dataframe ------'
##    print o.HistoryOfAdjClosePricesDataframe
    #print '------ Daily Returns Dataframe ------'
    #print o.TotalReturnsDataframe

    print '------ AggregatedTotalReturnsDataframe Returns ------'
    print o.AggregatedTotalReturnsDataframe

    print '------ AggregatedPriceChangeReturnsDataframe Returns ------'
    print o.AggregatedPriceChangeReturnsDataframe
