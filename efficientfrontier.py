# -*- coding: utf-8 -*-
"""
Created on Tue Jul 28 16:16:39 2015

@author: justin.malinchak
"""


def constrained_sum_sample_pos(n, total):
    """Return a randomly chosen list of n positive integers summing to total.
    Each such list is equally likely to occur."""
    import random
    dividers = sorted(random.sample(xrange(1, total), n - 1))
    return [a - b for a, b in zip(dividers + [total], [0] + dividers)]

def constrained_sum_sample_nonneg(n, total):
    """Return a randomly chosen list of n nonnegative integers summing to total.
    Each such list is equally likely to occur."""

    return [x - 1 for x in constrained_sum_sample_pos(n, total + n)]

def unconstrained_sample_posneg(l, h , total, divisor=1):
    """Return a randomly chosen list of n positive integers not summing to a specific total.
    Each such list is equally likely to occur."""
    import random
    l1 = l * 100.0
    h1 = h * 100.0
    lst = []
    for i in range(0,total):
        lst.append(random.randrange(l1,h1,5)/100.0/divisor)
    return lst


import operator
def sumproduct(*lists):
    return sum(reduce(operator.mul, data) for data in zip(*lists))

import numpy as np
import pandas as pd
import math as mth
class perform:

#    #DataFrameResult
    def set_ReturnsClass(self,ReturnsClass):
        self._ReturnsClass = ReturnsClass
    def get_ReturnsClass(self):
        return self._ReturnsClass
    ReturnsClass = property(get_ReturnsClass, set_ReturnsClass)

    def setCovarianceMatrix(self,CovarianceMatrix):
        self.CovarianceMatrix = CovarianceMatrix
    def getCovarianceMatrix(self):
        return self._CovarianceMatrix
    CovarianceMatrix = property(getCovarianceMatrix, setCovarianceMatrix)

    def setCorrelationMatrix(self,CorrelationMatrix):
        self.CorrelationMatrix = CorrelationMatrix
    def getCorrelationMatrix(self):
        return self._CorrelationMatrix
    CorrelationMatrix = property(getCorrelationMatrix, setCorrelationMatrix)

    def setPermutationsDataframe(self,PermutationsDataframe):
        self.PermutationsDataframe = PermutationsDataframe
    def getPermutationsDataframe(self):
        return self._PermutationsDataframe
    PermutationsDataframe = property(getPermutationsDataframe, setPermutationsDataframe)


    def set_SymbolsList(self,SymbolsList):
        self._SymbolsList = SymbolsList
    def get_SymbolsList(self):
        return self._SymbolsList
    SymbolsList = property(get_SymbolsList, set_SymbolsList)

    def set_AlignedTotalReturnsDataframe(self,AlignedTotalReturnsDataframe):
        self._AlignedTotalReturnsDataframe = AlignedTotalReturnsDataframe
    def get_AlignedTotalReturnsDataframe(self):
        return self._AlignedTotalReturnsDataframe
    AlignedTotalReturnsDataframe = property(get_AlignedTotalReturnsDataframe, set_AlignedTotalReturnsDataframe)

    def set_AlignedPriceChangeReturnsDataframe(self,AlignedPriceChangeReturnsDataframe):
        self._AlignedPriceChangeReturnsDataframe = AlignedPriceChangeReturnsDataframe
    def get_AlignedPriceChangeReturnsDataframe(self):
        return self._AlignedPriceChangeReturnsDataframe
    AlignedPriceChangeReturnsDataframe = property(get_AlignedPriceChangeReturnsDataframe, set_AlignedPriceChangeReturnsDataframe)

    def set_AlignedAdjClosePriceHistoryDataframe(self,AlignedAdjClosePriceHistoryDataframe):
        self._AlignedAdjClosePriceHistoryDataframe = AlignedAdjClosePriceHistoryDataframe
    def get_AlignedAdjClosePriceHistoryDataframe(self):
        return self._AlignedAdjClosePriceHistoryDataframe
    AlignedAdjClosePriceHistoryDataframe = property(get_AlignedAdjClosePriceHistoryDataframe, set_AlignedAdjClosePriceHistoryDataframe)

    #AlignedClosePriceHistoryDataframe
    def set_AlignedClosePriceHistoryDataframe(self,AlignedClosePriceHistoryDataframe):
        self._AlignedClosePriceHistoryDataframe = AlignedClosePriceHistoryDataframe
    def get_AlignedClosePriceHistoryDataframe(self):
        return self._AlignedClosePriceHistoryDataframe
    AlignedClosePriceHistoryDataframe = property(get_AlignedClosePriceHistoryDataframe, set_AlignedClosePriceHistoryDataframe)


##    def set_BottomConstraint(self,BottomConstraint):
##        self._BottomConstraint = BottomConstraint
##    def get_BottomConstraint(self):
##        return self._BottomConstraint
##    BottomConstraint = property(get_BottomConstraint, set_BottomConstraint)
##
##    def set_TopConstraint(self,TopConstraint):
##        self._TopConstraint = TopConstraint
##    def get_TopConstraint(self):
##        return self._TopConstraint
##    TopConstraint = property(get_TopConstraint, set_TopConstraint)

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

    #AnnualizedOrCumulative
    def set_AnnualizedOrCumulative(self,AnnualizedOrCumulative):
        self._AnnualizedOrCumulative = AnnualizedOrCumulative
    def get_AnnualizedOrCumulative(self):
        return self._AnnualizedOrCumulative
    AnnualizedOrCumulative = property(get_AnnualizedOrCumulative, set_AnnualizedOrCumulative)


    def __init__(self,
                     symbols = ['AAPL','MSFT'] 
                     ,  startdate = '2017-01-01'
                     ,  enddate ='' #2014-01-01
                     ,  permutations = 10
                     ,  annualized_or_cumulative = 'annualized'
                     ,  showresults = 0
                 ):
        
        print('Initialized class efficientfrontier')

        self.SymbolsList = symbols
        print 'Doing efficient frontier for',len(self.SymbolsList), 'symbols'
        print 'Doing efficient frontier for',self.SymbolsList
        self.StartDateString = startdate
        self.EndDateString = enddate
        self.AnnualizedOrCumulative = annualized_or_cumulative
        self._compilehistoricaldataframes()
        newsymbolslist = self.ReturnsClass.SymbolsList
        print 'Actual number of good symbols found',len(newsymbolslist), 'symbols'
        self.SymbolsList = newsymbolslist
        print 'Running CovarianceMatrix'
        self.CorrelationMatrix = self.correlationmatrix()
        self.CovarianceMatrix = self.covariancematrix()
        print 'Running Permutations'
        df_perms = self.permutationstodataframe(permutations)
        self.PermutationsDataframe = df_perms



    def _compilehistoricaldataframes(self
                 , showresults = 0):
        
        mysymbolslist = self.SymbolsList 
        ser_annual = pd.Series()
        
        import pullreturns as pr
        o = pr.perform(
                        symbols = mysymbolslist
                        , startdate = self.StartDateString
                        , enddate = self.EndDateString
        )
    
        df_alignedadjclosepricehistory = o.HistoryOfAdjClosePricesDataframe
        df_totalreturns = o.TotalReturnsDataframe
        df_aggregatedtotalreturns = o.AggregatedTotalReturnsDataframe
        dict_of_df_totalreturns = {}

        df_alignedclosepricehistory = o.HistoryOfClosePricesDataframe
        df_pricechangereturns = o.PriceChangeReturnsDataframe
        df_aggregatedpricechangereturns = o.AggregatedPriceChangeReturnsDataframe
        dict_of_df_pricechangereturns = {}
        
        for symbol in mysymbolslist:
 
            df_totalreturns_ticker = df_totalreturns[(df_totalreturns.ticker == symbol)]
            df_totalreturns_ticker.set_index(['curr_date'], inplace=True)
            dict_of_df_totalreturns[symbol] = df_totalreturns_ticker
        
            df_pricechangereturns_ticker = df_pricechangereturns[(df_pricechangereturns.ticker == symbol)]
            df_pricechangereturns_ticker.set_index(['curr_date'], inplace=True)
            dict_of_df_pricechangereturns[symbol] = df_pricechangereturns_ticker
        

        index = ['X']
        columns = ['A','B','C']
        
        df_largestofreturns_total = pd.DataFrame(index=index, columns=columns)
        df_largestofreturns_total = df_largestofreturns_total.fillna(0) # with 0s rather than NaNs
        
        keyoflargestreturnsdf_total = ''
        for k,v in dict_of_df_totalreturns.items():
            if len(v) > len(df_largestofreturns_total):
                df_largestofreturns_total = v
                keyoflargestreturnsdf_total = k

        df_alignedtotalreturns = df_largestofreturns_total[['change_pct']]
        df_alignedtotalreturns.columns = [keyoflargestreturnsdf_total]
        df_alignedtotalreturns.sort_index

        for k,v in dict_of_df_totalreturns.items():
            if not k == keyoflargestreturnsdf_total:
                df_new = v[['change_pct']] 
                df_new.columns = [k]
                df_new.sort_index
                result = pd.concat([df_alignedtotalreturns, df_new], axis=1, join='inner')
                df_alignedtotalreturns = result

        df_largestofreturns_pricechange = pd.DataFrame(index=index, columns=columns)
        df_largestofreturns_pricechange = df_largestofreturns_pricechange.fillna(0) # with 0s rather than NaNs
        
        keyoflargestreturnsdf_pricechange = ''
        for k,v in dict_of_df_totalreturns.items():
            if len(v) > len(df_largestofreturns_pricechange):
                df_largestofreturns_pricechange = v
                keyoflargestreturnsdf_pricechange = k
                
        df_alignedpricechangereturns = df_largestofreturns_pricechange[['change_pct']]
        df_alignedpricechangereturns.columns = [keyoflargestreturnsdf_pricechange]
        df_alignedpricechangereturns.sort_index
             
        for k,v in dict_of_df_pricechangereturns.items():
            if not k == keyoflargestreturnsdf_pricechange:
                df_new = v[['change_pct']] 
                df_new.columns = [k]
                df_new.sort_index
                result = pd.concat([df_alignedpricechangereturns, df_new], axis=1, join='inner')
                df_alignedpricechangereturns = result
                
        
        self.AlignedTotalReturnsDataframe = df_alignedtotalreturns
        self.AlignedAdjClosePriceHistoryDataframe = df_alignedadjclosepricehistory

        self.AlignedPriceChangeReturnsDataframe = df_alignedpricechangereturns
        self.AlignedClosePriceHistoryDataframe = df_alignedclosepricehistory

        self.ReturnsClass = o
        self.SymbolsList = o.SymbolsList
        print 'After processing _compilehistoricaldataframes:  len(self.SymbolsList)',len(self.SymbolsList)
    

    def covariancematrix(self
                 ):

        df_alignedpricechangereturns = self.AlignedPriceChangeReturnsDataframe
        df_alignedpricechangereturns = df_alignedpricechangereturns.dropna() #eeee
        
        
        covmatrix_array = np.cov(df_alignedpricechangereturns,None,0)
        rows = np.array(list(df_alignedpricechangereturns))[: np.newaxis]
        
        df_covariancematrix = pd.DataFrame(covmatrix_array, index=rows, columns=list(df_alignedpricechangereturns))
        return df_covariancematrix
    


    def correlationmatrix(self
                 ):

        df_alignedpricechangereturns = self.AlignedPriceChangeReturnsDataframe
        df_alignedpricechangereturns = df_alignedpricechangereturns.dropna()
        rows = np.array(list(df_alignedpricechangereturns))[: np.newaxis]
        corrmatrix_array = np.corrcoef(df_alignedpricechangereturns.T.values.tolist())
        
        dfcorrelationmatrix = pd.DataFrame(corrmatrix_array, index=rows, columns=list(df_alignedpricechangereturns))
        
        return dfcorrelationmatrix

    def equalweightseries(self,

                     ):
        
        index = self.SymbolsList
        ser_seed = pd.Series(float(1)/float(len(index)), index=index)
        
        return ser_seed


    def randomweightseries(self, 
                     ):
        int_list = constrained_sum_sample_pos(len(self.SymbolsList),200) 
        
        fractions_list = [float(x)/float(100) for x in int_list]
        
        fractions_series = pd.Series(fractions_list, index=self.SymbolsList)
        return fractions_series

    def randomweightserieswithnegatives(self,
                                        ):
        #print 'rws len(self.SymbolsList)', len(self.SymbolsList)
        int_list = unconstrained_sample_posneg(-5,5,len(self.SymbolsList),1)
        #print 'rws len(int_list)', len(int_list)
        fractions_list = [float(x)/float(100) for x in int_list]
        #print 'rws len(fractions_list)', len(fractions_list)
        fractions_series = pd.Series(fractions_list, index=self.SymbolsList)
        #print 'rws len(fractions_series)', len(fractions_series)
        return fractions_series


    def portfolioriskreturnrandomweight(self,oftype='random'):
        if oftype == 'equal':
            rws = self.equalweightseries()
        else:
            rws = self.randomweightserieswithnegatives()
            
        if self.AnnualizedOrCumulative == 'cumulative':
            aggregatedreturn_list = self.ReturnsClass.AggregatedTotalReturnsDataframe['cumulative_return'].tolist()
        else:
            aggregatedreturn_list = self.ReturnsClass.AggregatedTotalReturnsDataframe['annualized_return'].tolist()
        portfolioreturn = sumproduct(rws,aggregatedreturn_list)
        df = self.covariancematrix()

        import numpy as np
        portfoliostandarddeviation = np.sqrt(np.dot(rws.T,np.dot(df, rws)))
        
        data = [rws,portfolioreturn,portfoliostandarddeviation]
        index = ['randomweightseries','portfolioreturn','portfoliostandarddeviation']
        returnseries = pd.Series(data, index=index)
        return returnseries

    def permutationstodataframe(self,howmany):    
        dict_permutations = {}        
        for i in range(howmany):
            permutation_series = self.portfolioriskreturnrandomweight(oftype='random')
            dict_permutations[len(dict_permutations)] = permutation_series #randomweightseries,portfolioreturn,portfoliostandarddeviation

        permutation_series = self.portfolioriskreturnrandomweight(oftype='equal')
        dict_permutations[len(dict_permutations)] = permutation_series 
        df = pd.DataFrame(dict_permutations.items(), columns=['key','value']) # 'portfolioreturn','portfoliostandarddeviation','weight'
        df = df.set_index('key',drop=True)
        return df

if __name__=='__main__':

    
    o = perform(
                symbols = ['MAR', 'MON', 'NOV', 'A', 'AAL', 'AAP', 'AAPL', 'ABBV', 'ABC', 'ABT', 'ACN', 'ADBE', 'ADI', 'ADM', 'ADP', 'ADS', 'ADSK', 'AEE', 'AEP', 'AES', 'AET', 'AFL', 'AGN', 'AIG', 'AIV', 'AIZ', 'AJG', 'AKAM', 'ALB', 'ALGN', 'ALK', 'ALL', 'ALLE', 'ALXN', 'AMAT', 'AMD', 'AME', 'AMG', 'AMGN', 'AMP', 'AMT', 'AMZN', 'ANDV', 'ANSS', 'ANTM', 'AON', 'AOS', 'APA', 'APC', 'APD', 'APH', 'ARE', 'ARNC', 'ATVI', 'AVB', 'AVGO', 'AVY', 'AWK', 'AXP', 'AYI', 'AZO', 'BA', 'BAC', 'BAX', 'BBT', 'BBY', 'BCR', 'BDX', 'BEN', 'BF.B', 'BHF', 'BHGE', 'BIIB', 'BK', 'BLK', 'BLL', 'BMY', 'BRK.B', 'BSX', 'BWA', 'BXP', 'C', 'CA', 'CAG', 'CAH', 'CAT', 'CB', 'CBG', 'CBOE', 'CBS', 'CCI', 'CCL', 'CDNS', 'CELG', 'CERN', 'CF', 'CFG', 'CHD', 'CHK', 'CHRW', 'CHTR', 'CI', 'CINF', 'CL', 'CLX', 'CMA', 'CMCSA', 'CME', 'CMG', 'CMI', 'CMS', 'CNC', 'CNP', 'COF', 'COG', 'COH', 'COL', 'COO', 'COP', 'COST', 'COTY', 'CPB', 'CRM', 'CSCO', 'CSRA', 'CSX', 'CTAS', 'CTL', 'CTSH', 'CTXS', 'CVS', 'CVX', 'CXO', 'D', 'DAL', 'DE', 'DFS', 'DG', 'DGX', 'DHI', 'DHR', 'DIS', 'DISCA', 'DISCK', 'DISH', 'DLPH', 'DLR', 'DLTR', 'DOV', 'DPS', 'DRE', 'DRI', 'DTE', 'DUK', 'DVA', 'DVN', 'DWDP', 'DXC', 'EA', 'EBAY', 'ECL', 'ED', 'EFX', 'EIX', 'EL', 'EMN', 'EMR', 'EOG', 'EQIX', 'EQR', 'EQT', 'ES', 'ESRX', 'ESS', 'ETFC', 'ETN', 'ETR', 'EVHC', 'EW', 'EXC', 'EXPD', 'EXPE', 'EXR', 'F', 'FAST', 'FB', 'FBHS', 'FCX', 'FDX', 'FE', 'FFIV', 'FIS', 'FISV', 'FITB', 'FL', 'FLIR', 'FLR', 'FLS', 'FMC', 'FOX', 'FOXA', 'FRT', 'FTI', 'FTV', 'GD', 'GE', 'GGP', 'GILD', 'GIS', 'GLW', 'GM', 'GOOG', 'GOOGL', 'GPC', 'GPN', 'GPS', 'GRMN', 'GS', 'GT', 'GWW', 'HAL', 'HAS', 'HBAN', 'HBI', 'HCA', 'HCN', 'HCP', 'HD', 'HES', 'HIG', 'HLT', 'HOG', 'HOLX', 'HON', 'HP', 'HPE', 'HPQ', 'HRB', 'HRL', 'HRS', 'HSIC', 'HST', 'HSY', 'HUM', 'IBM', 'ICE', 'IDXX', 'IFF', 'ILMN', 'INCY', 'INFO', 'INTC', 'INTU', 'IP', 'IPG', 'IR', 'IRM', 'ISRG', 'IT', 'ITW', 'IVZ', 'JBHT', 'JCI', 'JEC', 'JNJ', 'JNPR', 'JPM', 'JWN', 'K', 'KEY', 'KHC', 'KIM', 'KLAC', 'KMB', 'KMI', 'KMX', 'KO', 'KORS', 'KR', 'KSS', 'KSU', 'L', 'LB', 'LEG', 'LEN', 'LH', 'LKQ', 'LLL', 'LLY', 'LMT', 'LNC', 'LNT', 'LOW', 'LRCX', 'LUK', 'LUV', 'LVLT', 'LYB', 'M', 'MA', 'MAA', 'MAC', 'MAS', 'MAT', 'MCD', 'MCHP', 'MCK', 'MCO', 'MDLZ', 'MDT', 'MET', 'MGM', 'MHK', 'MKC', 'MLM', 'MMC', 'MMM', 'MNST', 'MO', 'MOS', 'MPC', 'MRK', 'MRO', 'MS', 'MSFT', 'MSI', 'MTB', 'MTD', 'MU', 'MYL', 'NAVI', 'NBL', 'NDAQ', 'NEE', 'NEM', 'NFLX', 'NFX', 'NI', 'NKE', 'NLSN', 'NOC', 'NRG', 'NSC', 'NTAP', 'NTRS', 'NUE', 'NVDA', 'NWL', 'NWS', 'NWSA', 'O', 'OKE', 'OMC', 'ORCL', 'ORLY', 'OXY', 'PAYX', 'PBCT', 'PCAR', 'PCG', 'PCLN', 'PDCO', 'PEG', 'PEP', 'PFE', 'PFG', 'PG', 'PGR', 'PH', 'PHM', 'PKG', 'PKI', 'PLD', 'PM', 'PNC', 'PNR', 'PNW', 'PPG', 'PPL', 'PRGO', 'PRU', 'PSA', 'PSX', 'PVH', 'PWR', 'PX', 'PXD', 'PYPL', 'Q', 'QCOM', 'QRVO', 'RCL', 'RE', 'REG', 'REGN', 'RF', 'RHI', 'RHT', 'RJF', 'RL', 'RMD', 'ROK', 'ROP', 'ROST', 'RRC', 'RSG', 'RTN', 'SBAC', 'SBUX', 'SCG', 'SCHW', 'SEE', 'SHW', 'SIG', 'SJM', 'SLB', 'SLG', 'SNA', 'SNI', 'SNPS', 'SO', 'SPG', 'SPGI', 'SPLS', 'SRCL', 'SRE', 'STI', 'STT', 'STX', 'STZ', 'SWK', 'SWKS', 'SYF', 'SYK', 'SYMC', 'SYY', 'T', 'TAP', 'TDG', 'TEL', 'TGT', 'TIF', 'TJX', 'TMK', 'TMO', 'TRIP', 'TROW', 'TRV', 'TSCO', 'TSN', 'TSS', 'TWX', 'TXN', 'TXT', 'UA', 'UAA', 'UAL', 'UDR', 'UHS', 'ULTA', 'UNH', 'UNM', 'UNP', 'UPS', 'URI', 'USB', 'UTX', 'V', 'VAR', 'VFC', 'VIAB', 'VLO', 'VMC', 'VNO', 'VRSK', 'VRSN', 'VRTX', 'VTR', 'VZ', 'WAT', 'WBA', 'WDC', 'WEC', 'WFC', 'WHR', 'WLTW', 'WM', 'WMB', 'WMT', 'WRK', 'WU', 'WY', 'WYN', 'WYNN', 'XEC', 'XEL', 'XL', 'XLNX', 'XOM', 'XRAY', 'XRX', 'XYL', 'YUM', 'ZBH', 'ZION', 'ZTS']
                ,  startdate = '2017-07-01'
                ,  enddate = '2017-08-05'
                ,  permutations = 100
                ,  annualized_or_cumulative = 'cumulative'
                )   
    
    print 'AggregatedTotalReturnsDataframe'
    print o.ReturnsClass.AggregatedTotalReturnsDataframe
    print 'AlignedClosePriceHistoryDataframe'
    print o.AlignedClosePriceHistoryDataframe

##               symbols = [
##                            'GOOGL',
##                            'FB',
##                            'MSFT',
####                            'LRCX',
####                            'EVR',
####                            'MASI',
####                            'CELG',
####                            'AOS',
####                            'LPX',
####                            'MRK',
####                            'EVR',
####                            'JNJ',
####                            'INTC',
####                            #'GOLD',
####                            'LMT',
####                            'RTN',
####                            'BP',
####                            'T',
####                            'HSBC',
####                            'THO',
####                            'SPY'
##                            ]
