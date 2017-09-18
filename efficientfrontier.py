# -*- coding: utf-8 -*-
"""
Created on Tue Jul 28 16:16:39 2015

@author: justin.malinchak
"""

## Before allowing negatives
#def constrained_sum_sample_pos(n, total):
#    """Return a randomly chosen list of n positive integers summing to total.
#    Each such list is equally likely to occur."""
#    import random
#    dividers = sorted(random.sample(xrange(1, total), n - 1))
#    return [a - b for a, b in zip(dividers + [total], [0] + dividers)]

## after allowing negatives
#def constrained_sum_sample_pos(n, total):
#    """Return a randomly chosen list of n positive integers summing to total.
#    Each such list is equally likely to occur."""
#    import random    
#    dividers = random.sample(xrange(-100, total), n - 1)
#    return [a - b for a, b in zip(dividers + [total], [0] + dividers)]
 


#def constrained_sum_sample_pos(n, minimum,maximum):
#    """Return a randomly chosen list of n positive integers summing to total.
#    Each such list is equally likely to occur."""
#    import random    
#    if minimum < 0:
#        dividers = random.sample(xrange(minimum, maximum), n - 1)
#    else:
#        dividers = sorted(random.sample(xrange(minimum, maximum), n - 1))
#    return [a - b for a, b in zip(dividers + [maximum], [0] + dividers)]

# Before allowing negatives
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

##    def set_AggregatedReturnsDataframe(self,AggregatedReturnsDataframe):
##        self._AggregatedReturnsDataframe = AggregatedReturnsDataframe
##    def get_AggregatedReturnsDataframe(self):
##        return self._AggregatedReturnsDataframe
##    AggregatedReturnsDataframe = property(get_AggregatedReturnsDataframe, set_AggregatedReturnsDataframe)
##
##    def set_CumulativeReturnsDataframe(self,CumulativeReturnsDataframe):
##        self._CumulativeReturnsDataframe = CumulativeReturnsDataframe
##    def get_CumulativeReturnsDataframe(self):
##        return self._CumulativeReturnsDataframe
##    CumulativeReturnsDataframe = property(get_CumulativeReturnsDataframe, set_CumulativeReturnsDataframe)


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

    #AlignedAdjClosePriceHistoryDataframe
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


    def set_BottomConstraint(self,BottomConstraint):
        self._BottomConstraint = BottomConstraint
    def get_BottomConstraint(self):
        return self._BottomConstraint
    BottomConstraint = property(get_BottomConstraint, set_BottomConstraint)

    def set_TopConstraint(self,TopConstraint):
        self._TopConstraint = TopConstraint
    def get_TopConstraint(self):
        return self._TopConstraint
    TopConstraint = property(get_TopConstraint, set_TopConstraint)

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
        #from random import shuffle
        #shuffle(symbols_list)
        self.SymbolsList = symbols
        print 'Doing efficient frontier for',self.SymbolsList
        self.StartDateString = startdate
        self.EndDateString = enddate
        self.AnnualizedOrCumulative = annualized_or_cumulative
        self._compilehistoricaldataframes()
        
        #self.ReturnsClass = oReturns
        
        #self.BottomConstraint = bottomconstraint
        #self.TopConstraint = topconstraint
        print 'Running CovarianceMatrix'
        self.CorrelationMatrix = self.correlationmatrix()
        self.CovarianceMatrix = self.covariancematrix()
        print 'Running Permutations'
        df_perms = self.permutationstodataframe(permutations)
        self.PermutationsDataframe = df_perms
#        print df_perms
##        for index, row in df_perms.iterrows():
##            print '-----'
##            print index,row
##            print '-----'
##            print 'random weights:'
##            randomweightseries = row['value']['randomweightseries']
##            #print index,randomweightseries
##            for idx in randomweightseries.iteritems():
##                print '  ',idx[0],idx[1]
##            
##            print 'portfolioreturn=',row['value']['portfolioreturn']
##            print 'portfoliostandarddeviation=',row['value']['portfoliostandarddeviation'] 
        #-------------------------------------------------------------------



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
        
        # Total here ----------------------------------------------------------------------
        df_largestofreturns_total = pd.DataFrame(index=index, columns=columns)
        df_largestofreturns_total = df_largestofreturns_total.fillna(0) # with 0s rather than NaNs
        #print df_largestofreturns
        
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

        # Price Change here----------------------------------------------------------------------
        df_largestofreturns_pricechange = pd.DataFrame(index=index, columns=columns)
        df_largestofreturns_pricechange = df_largestofreturns_pricechange.fillna(0) # with 0s rather than NaNs
        #print df_largestofreturns
        
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



    def covariancematrix(self
#            , period='monthly'
#            , UseLogReturns = 'pctchange'
                 ):

        #'^GSmr   ^OEX    ^VIX    ^OEX    ^MID   ^RUT   ^DJI
        
#        import numpy as np
#        import pandas as pd

        #df_alignedtotalreturns = self.MonthlyReturnsDataframe #monthlyreturns(list_of_symbols)
        #df_alignedtotalreturns = self.compilereturnsdataframe(period)
        #df_alignedtotalreturns = self.compilereturnsdataframe(period,UseLogReturns)
        df_alignedpricechangereturns = self.AlignedPriceChangeReturnsDataframe
        df_alignedpricechangereturns = df_alignedpricechangereturns.dropna() #eeee
        
        
        covmatrix_array = np.cov(df_alignedpricechangereturns,None,0)
        #good np.savetxt("cov.csv", covmatrix_array, delimiter=",", fmt='%s')
        
        rows = np.array(list(df_alignedpricechangereturns))[: np.newaxis]
        #str_data = np.char.mod("%10.6f", df_alignedpricechangereturns)
        
        #print str_data
        #print rows
        #print list(df_alignedpricechangereturns)
        
        
        df_covariancematrix = pd.DataFrame(covmatrix_array, index=rows, columns=list(df_alignedpricechangereturns))
#        if period == 'daily':
#            for i in range(len(df_covariancematrix)):
#                print df_covariancematrix.iloc[i] 
        #print df_covariancematrix         
        return df_covariancematrix
#        print '----------------------------------------------------'
#        print '                 covariance matrix'
#        print '----------------------------------------------------'
        
#        df_covariancematrix.to_csv('cov1.csv',columns=(list(df_alignedtotalreturns)))
        


    def correlationmatrix(self
#            , period='monthly'
#            , UseLogReturns = 'pctchange'
                 ):

        #'^GSmr   ^OEX    ^VIX    ^OEX    ^MID   ^RUT   ^DJI
        
#        import numpy as np
#        import pandas as pd

#        print '----------------------------------------------------'
#        print '                 monthly returns'
#        print '----------------------------------------------------'

        #df_alignedtotalreturns = self.MonthlyReturnsDataframe #self.monthlyreturns(list_of_symbols)
        #df_alignedtotalreturns = self.compilereturnsdataframe(period,UseLogReturns)
        df_alignedtotalreturns = self.AlignedTotalReturnsDataframe
        df_alignedtotalreturns = df_alignedtotalreturns.dropna()
        #print '------------------- df_alignedtotalreturns -------------------'
        #print df_alignedtotalreturns
        #print '------------------- df_alignedtotalreturns -------------------'
        rows = np.array(list(df_alignedtotalreturns))[: np.newaxis]

        #print rows
        
        corrmatrix_array = np.corrcoef(df_alignedtotalreturns.T.values.tolist())
        #print corrmatrix_array
        
        dfcorrelationmatrix = pd.DataFrame(corrmatrix_array, index=rows, columns=list(df_alignedtotalreturns))
#        print '----------------------------------------------------'
#        print '                 correlation matrix'
#        print '----------------------------------------------------'
        
        #print dfcorrelationmatrix
        #dfcorrelationmatrix.to_csv('corr1.csv',columns=(list(df_alignedtotalreturns)))
        
        return dfcorrelationmatrix
        #print '222',sqrt(float(9))

    def equalweightseries(self,

                     ):
        
        index = self.SymbolsList
        ser_seed = pd.Series(float(1)/float(len(index)), index=index)
        
        return ser_seed


    def randomweightseries(self, 
                     ):
        #mysymbolslist = self.SymbolsList #['WMT','BAC','JPM','AAPL','GOOG']

        #int_list = constrained_sum_sample_pos(len(self.SymbolsList),100) 
        #print 'wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww'
        int_list = constrained_sum_sample_pos(len(self.SymbolsList),100) 
        
        fractions_list = [float(x)/float(100) for x in int_list]
        #sums them all to test
        #t = reduce(lambda x,y:x+y,s)
        
        fractions_series = pd.Series(fractions_list, index=self.SymbolsList)
        return fractions_series

#    def portfolioreturnrandomweights(self,):
#        return sumproduct(self.randomweightseries(),self.AggregatedTotalReturnsDataframe)
#
#    def portfolioreturnequalweights(self,):
#        return sumproduct(self.equalweightseries(),self.AggregatedTotalReturnsDataframe)

#    def portfoliostandarddeviationrandomweights(self,):
#        #df = pd.DataFrame({'a' : [4,1,3], 'b' : [5,2,4]},index=[1,2,3])
#        df = self.CovarianceMatrix
#        #s = pd.Series([0.6,0.4],index=['a','b'])
#        s = self.randomweightseries()
#        s1 = df.dot(s)
#        s2 = s1.dot(s.T)
#        return s2
#
#
#    def portfoliostandarddeviationequalweights(self,):
#        #df = pd.DataFrame({'a' : [4,1,3], 'b' : [5,2,4]},index=[1,2,3])
#        df = self.CovarianceMatrix
#        #s = pd.Series([0.6,0.4],index=['a','b'])
#        s = self.equalweightseries()
#        s1 = df.dot(s)
#        s2 = s1.dot(s.T)
#        return s2

    def portfolioriskreturnrandomweight(self,oftype='random'):  #uuuuuuu
        #df = pd.DataFrame({'a' : [4,1,3], 'b' : [5,2,4]},index=[1,2,3])
        #s = pd.Series([0.6,0.4],index=['a','b'])
        if oftype == 'equal':
            rws = self.equalweightseries()
        else:
            rws = self.randomweightseries()
        #print 'randomweightseries'
        #print rws
        #print self.AggregatedTotalReturnsDataframe
        if self.AnnualizedOrCumulative == 'cumulative':
            aggregatedreturn_list = self.ReturnsClass.AggregatedTotalReturnsDataframe['cumulative_return'].tolist()
        else:
            aggregatedreturn_list = self.ReturnsClass.AggregatedTotalReturnsDataframe['annualized_return'].tolist()
        #print 'aggregatedreturn_list'
        #print aggregatedreturn_list
        portfolioreturn = sumproduct(rws,aggregatedreturn_list)
        #print 'portfolioreturn'
        #print portfolioreturn
        df = self.covariancematrix()

        #old way
##        s1 = df.dot(rws)
##        portfoliovariance = s1.dot(rws.T)
##        portfoliostandarddeviation = mth.sqrt(portfoliovariance)

        import numpy as np
        portfoliostandarddeviation = np.sqrt(np.dot(rws.T,np.dot(df, rws)))
        
        data = [rws,portfolioreturn,portfoliostandarddeviation]
        index = ['randomweightseries','portfolioreturn','portfoliostandarddeviation']
        returnseries = pd.Series(data, index=index)
        #print 'returnseries',data
        #print 'portfolioriskreturnrandomweight'
        #print returnseries
        return returnseries

#    def testpermutations(self,howmany):    
#        print '---------------------------------------'
#        print 'permutations '
#        print '---------------------------------------'
#        for i in range(howmany):
#            permutation_series = self.portfolioriskreturnrandomweight()
#            print '---------------------'
#            print '---portfolio weights'
#            print '---------------------'
#            for idx in permutation_series['randomweightseries'].iteritems():
#                print idx
#            print '---portfolioreturn',permutation_series['portfolioreturn']
#            print '---portfoliostandarddeviation',permutation_series['portfoliostandarddeviation']
#        return 1

    def permutationstodataframe(self,howmany):    
#        print '---------------------------------------'
#        print 'permutations '
#        print '---------------------------------------'
        dict_permutations = {}        
        for i in range(howmany):
            #print 'qqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqq'
            #print self.portfolioriskreturnrandomweight
            permutation_series = self.portfolioriskreturnrandomweight(oftype='random')
            #for idx in permutation_series['randomweightseries'].iteritems():
            #    print idx
            #randomweightseries = permutation_series['randomweightseries']
            #portfolioreturn = permutation_series['portfolioreturn']
            
            #portfoliostandarddeviation = permutation_series['portfoliostandarddeviation']
            #print i,portfolioreturn,portfoliostandarddeviation 
            dict_permutations[len(dict_permutations)] = permutation_series #randomweightseries,portfolioreturn,portfoliostandarddeviation
        #Add equal weight series to end
        permutation_series = self.portfolioriskreturnrandomweight(oftype='equal')
        dict_permutations[len(dict_permutations)] = permutation_series 
        df = pd.DataFrame(dict_permutations.items(), columns=['key','value']) # 'portfolioreturn','portfoliostandarddeviation','weight'
        df = df.set_index('key',drop=True)
        #df = df['value']
        #df = pd.DataFrame(dict_permutations)
        #df = df.T.stack().reset_index()   
#        df = pd.DataFrame([
#            [col1,col2] for col1, d in dict_permutations.items() for col2 in d.items()
#        ])  
#        df = pd.DataFrame([
#            [col1,col2] for col1, d in dict_permutations.items() for col2 in d
#        ])
        #df.columns = 'weight','portfolioreturn','portfoliostandarddeviation'
        return df

if __name__=='__main__':
    
##    import mytools 
##    print mytools.mystrings.ConvertStringToDate('2017-09-13')
    
    o = perform(
                #symbols = ['GOOGL','APPL','MSFT','LRCX','EVR','MASI','CELG','AOS','LPX','MRK','EVR','JNJ','INTC','GOLD','LMT','RTN','BP','T','HSBC','THO']
                #symbols = ['CSCO','AAPL', 'MSFT', 'SPY']
                symbols = ['GOOGL',
                            'FB',
                            'MSFT',
                            'LRCX',
                            'EVR',
                            'MASI',
                            'CELG',
                            'AOS',
                            'LPX',
                            'MRK',
                            'EVR',
                            'JNJ',
                            'INTC',
                            #'GOLD',
                            'LMT',
                            'RTN',
                            'BP',
                            'T',
                            'HSBC',
                            'THO',
                            'SPY'
                            ]
                ,  startdate = '2017-02-25'
                ,  enddate = '2017-09-30'
                ,  permutations = 11
                ,  annualized_or_cumulative = 'cumulative'
                )
    
    print 'AggregatedTotalReturnsDataframe'
    print o.ReturnsClass.AggregatedTotalReturnsDataframe
    print 'AlignedClosePriceHistoryDataframe'
    print o.AlignedClosePriceHistoryDataframe
##    #-------------------------------------------------------------------
##    df_perms = o.PermutationsDataframe
##    print df_perms
##    for index, row in df_perms.iterrows():
##        print '-----'
##        print 'permutaton:',index
##        print 'weights tested:'
##        randomweightseries = row['value']['randomweightseries']
##        #print index,randomweightseries
##        for idx in randomweightseries.iteritems():
##            print '  ',idx[0],idx[1]
##        print 'portfolioreturn=',row['value']['portfolioreturn']
##        print 'portfoliostandarddeviation=', row['value']['portfoliostandarddeviation'] 
##            
##    #-------------------------------------------------------------------


     
  
