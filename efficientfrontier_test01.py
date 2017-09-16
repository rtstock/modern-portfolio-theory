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

    def set_AggregatedReturnsDataframe(self,AggregatedReturnsDataframe):
        self._AggregatedReturnsDataframe = AggregatedReturnsDataframe
    def get_AggregatedReturnsDataframe(self):
        return self._AggregatedReturnsDataframe
    AggregatedReturnsDataframe = property(get_AggregatedReturnsDataframe, set_AggregatedReturnsDataframe)
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

    def set_AlignedReturnsDataframe(self,AlignedReturnsDataframe):
        self._AlignedReturnsDataframe = AlignedReturnsDataframe
    def get_AlignedReturnsDataframe(self):
        return self._AlignedReturnsDataframe
    AlignedReturnsDataframe = property(get_AlignedReturnsDataframe, set_AlignedReturnsDataframe)

    #AlignedPriceHistoryDataframe
    def set_AlignedPriceHistoryDataframe(self,AlignedPriceHistoryDataframe):
        self._AlignedPriceHistoryDataframe = AlignedPriceHistoryDataframe
    def get_AlignedPriceHistoryDataframe(self):
        return self._AlignedPriceHistoryDataframe
    AlignedPriceHistoryDataframe = property(get_AlignedPriceHistoryDataframe, set_AlignedPriceHistoryDataframe)

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
        #print oReturns.AggregatedReturnsDataframe()
        #self.ReturnsClass = oReturns
        
        #self.BottomConstraint = bottomconstraint
        #self.TopConstraint = topconstraint
        print 'Running CovarianceMatrix'
        self.CovarianceMatrix = self.covariancematrix()
        self.CorrelationMatrix = self.correlationmatrix()
        #if showresults == 1:
        #    print('showresults=' + str(showresults) + ' builddataframeofrefdateminusd2tod1stockpricechanges')
        
        #self.build(list_of_symbols,showresults)
    


        #-------------------------------------------------------------------    
        import numpy
        import config
        import mytools
        import datetime
        import os
        mycachefolder = config.mycachefolder
        mytools.general().make_sure_path_exists(mycachefolder)    
        date14 = str(datetime.datetime.now().strftime("%Y%m%d%H%M%S"))

        print 'covariancematrix'
        cov = self.CovarianceMatrix
        cachedfilepathname = mycachefolder
        cachedfilepathname = os.path.join(cachedfilepathname,date14 + ' covariance.csv')
        cov.to_csv(cachedfilepathname,columns=(list(cov.columns.values)))
        
        print 'correlationmatrix'
        cor = self.CorrelationMatrix
        cachedfilepathname = mycachefolder
        cachedfilepathname = os.path.join(cachedfilepathname,date14 + ' correlation.csv')
        cor.to_csv(cachedfilepathname,columns=(list(cor.columns.values)))

        print 'prices'
        prc = self.AlignedPriceHistoryDataframe
        cachedfilepathname = mycachefolder
        cachedfilepathname = os.path.join(cachedfilepathname,date14 + ' prices.csv')
        prc.to_csv(cachedfilepathname,columns=(list(prc.columns.values)))
        #print prc

        print 'returns'
        #ret = self.AlignedReturnsDataframe
        ret = self.ReturnsClass.ReturnsDataframe
        #ret['change_pct100'] = df['change_pct'].apply(lambda x: x*100.0)
        cachedfilepathname = mycachefolder
        cachedfilepathname = os.path.join(cachedfilepathname,date14 + ' returns.csv')
        ret.to_csv(cachedfilepathname,columns=(list(ret.columns.values)))

        print 'length of prc', len(prc)

        #print '---- AnnualizedReturnDataframe-----'
        #print self.ReturnsClass.AggregatedReturnsDataframe

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

        #'^GSmr   ^OEX    ^VIX    ^OEX    ^MID   ^RUT   ^DJI
#        if self.Period == 'daily':
#            import pullreturnsdaily as pr
#        else:
#            import pullreturnsmonthly as pr
        
        #dict_of_df_pricehistory = {}
        dict_of_df_returns = {}
        # Build the annualized returns series
        mysymbolslist = self.SymbolsList # list_of_symbols #['^GSPC','^DJI','^MID','^OEX','AAPL','LEO']
        ser_annual = pd.Series()
        import pullreturns as pr
        print 'ok got here'
        o = pr.perform(
                        symbols = mysymbolslist
                        , startdate = self.StartDateString
                        , enddate = self.EndDateString
                    )
        #print 'ok got here'
        df_alignedpricehistory = o.StockHistoryDataframe
        #print df_alignedpricehistory
        df_returns = o.ReturnsDataframe
        #print df_returns
        df_annualizedreturns = o.AggregatedReturnsDataframe
        #print df_annualizedreturns
        
        #print df_prices
        #stop
        #print df_returns
        #print '------------------ ok'
        for symbol in mysymbolslist:
            
            #df_prices_ticker = df_prices[(df_prices.ticker == symbol)]
            df_returns_ticker = df_returns[(df_returns.ticker == symbol)]
            df_returns_ticker.set_index(['curr_date'], inplace=True)
            #df_prices_ticker = df_prices[symbol]
            #df_returns_ticker = df_returns[symbol]
            
            
            #print '------------------ symbol'
            #print df_returns_ticker
            #dict_of_df_pricehistory[symbol] = df_prices_ticker
            dict_of_df_returns[symbol] = df_returns_ticker
            #rrrrrrr
            #ser_annual = ser_annual.set_value(symbol, annualizedreturn)
        #print 'xxxxxaaa'
        #print dict_of_df_returns
        
        
        


        index = ['X']
        columns = ['A','B','C']
        
        # ----------------------------------------------------------------------
        df_largestofreturns = pd.DataFrame(index=index, columns=columns)
        df_largestofreturns = df_largestofreturns.fillna(0) # with 0s rather than NaNs
        #print df_largestofreturns
        
        keyoflargestreturnsdf = ''
        for k,v in dict_of_df_returns.items():
            if len(v) > len(df_largestofreturns):
                df_largestofreturns = v
                keyoflargestreturnsdf = k

        df_alignedreturns = df_largestofreturns[['change_pct']]
        df_alignedreturns.columns = [keyoflargestreturnsdf]
        df_alignedreturns.sort_index
             
        for k,v in dict_of_df_returns.items():
            if not k == keyoflargestreturnsdf:
                df_new = v[['change_pct']] #ttttttt
                #print df_new
                df_new.columns = [k]
                #print df_new
                df_new.sort_index
                #print df_new
                #print df_alignedreturns 
                #df_alignedreturns[k] = df_new
                result = pd.concat([df_alignedreturns, df_new], axis=1, join='inner')
                
                df_alignedreturns = result
                #print df_alignedreturns
        
        self.ReturnsClass = o
        self.AlignedReturnsDataframe = df_alignedreturns
        self.AlignedPriceHistoryDataframe = df_alignedpricehistory
        self.AggregatedReturnsDataframe = o.AggregatedReturnsDataframe
        self.SymbolsList = o.SymbolsList
##        # ----------------------------------------------------------------------
##        df_largestofpricehistory = pd.DataFrame(index=index, columns=columns)
##        df_largestofpricehistory = df_largestofpricehistory.fillna(0) # with 0s rather than NaNs
##        keyoflargestpricehistorydf = ''
##        for k,v in dict_of_df_pricehistory.items():
##            if len(v) > len(df_largestofpricehistory):
##                df_largestofpricehistory = v
##                keyoflargestpricehistorydf = k
##
##        df_alignedpricehistory = df_largestofpricehistory[['e_adjclose']]
##        df_alignedpricehistory.columns = [keyoflargestpricehistorydf]
##        df_alignedpricehistory.sort_index
##             
##        for k,v in dict_of_df_pricehistory.items():
##            if not k == keyoflargestpricehistorydf:
##                df_new = v[['e_adjclose']]
##                df_new.columns = [k]
##                df_new.sort_index
##                df_alignedpricehistory[k] = df_new[k]
##        
##        self.PriceHistoryDataframe = df_alignedpricehistory
##        # ----------------------------------------------------------------------




    def covariancematrix(self
#            , period='monthly'
#            , UseLogReturns = 'pctchange'
                 ):

        #'^GSmr   ^OEX    ^VIX    ^OEX    ^MID   ^RUT   ^DJI
        
#        import numpy as np
#        import pandas as pd

        #df_alignedreturns = self.MonthlyReturnsDataframe #monthlyreturns(list_of_symbols)
        #df_alignedreturns = self.compilereturnsdataframe(period)
        #df_alignedreturns = self.compilereturnsdataframe(period,UseLogReturns)
        df_alignedreturns = self.AlignedReturnsDataframe
        df_alignedreturns = df_alignedreturns.dropna() #eeee
        
        
        covmatrix_array = np.cov(df_alignedreturns,None,0)
        #good np.savetxt("cov.csv", covmatrix_array, delimiter=",", fmt='%s')
        
        rows = np.array(list(df_alignedreturns))[: np.newaxis]
        #str_data = np.char.mod("%10.6f", df_alignedreturns)
        
        #print str_data
        #print rows
        #print list(df_alignedreturns)
        
        
        df_covariancematrix = pd.DataFrame(covmatrix_array, index=rows, columns=list(df_alignedreturns))
#        if period == 'daily':
#            for i in range(len(df_covariancematrix)):
#                print df_covariancematrix.iloc[i] 
        #print df_covariancematrix         
        return df_covariancematrix
#        print '----------------------------------------------------'
#        print '                 covariance matrix'
#        print '----------------------------------------------------'
        
#        df_covariancematrix.to_csv('cov1.csv',columns=(list(df_alignedreturns)))
        


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

        #df_alignedreturns = self.MonthlyReturnsDataframe #self.monthlyreturns(list_of_symbols)
        #df_alignedreturns = self.compilereturnsdataframe(period,UseLogReturns)
        df_alignedreturns = self.AlignedReturnsDataframe
        df_alignedreturns = df_alignedreturns.dropna()
        #print '------------------- df_alignedreturns -------------------'
        #print df_alignedreturns
        #print '------------------- df_alignedreturns -------------------'
        rows = np.array(list(df_alignedreturns))[: np.newaxis]

        #print rows
        
        corrmatrix_array = np.corrcoef(df_alignedreturns.T.values.tolist())
        #print corrmatrix_array
        
        dfcorrelationmatrix = pd.DataFrame(corrmatrix_array, index=rows, columns=list(df_alignedreturns))
#        print '----------------------------------------------------'
#        print '                 correlation matrix'
#        print '----------------------------------------------------'
        
        #print dfcorrelationmatrix
        #dfcorrelationmatrix.to_csv('corr1.csv',columns=(list(df_alignedreturns)))
        
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
#        return sumproduct(self.randomweightseries(),self.AggregatedReturnsDataframe)
#
#    def portfolioreturnequalweights(self,):
#        return sumproduct(self.equalweightseries(),self.AggregatedReturnsDataframe)

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
        #print self.AggregatedReturnsDataframe
        if self.AnnualizedOrCumulative == 'cumulative':
            annualizedreturn_list = self.AggregatedReturnsDataframe['cumulative_return'].tolist()
        else:
            annualizedreturn_list = self.AggregatedReturnsDataframe['annualized_return'].tolist()
        #print 'annualizedreturn_list'
        #print annualizedreturn_list
        portfolioreturn = sumproduct(rws,annualizedreturn_list)
        #print 'portfolioreturn'
        #print portfolioreturn
        df = self.covariancematrix()
        s1 = df.dot(rws)
        portfoliovariance = s1.dot(rws.T)
        portfoliostandarddeviation = mth.sqrt(portfoliovariance)
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

    df_perms = o.PermutationsDataframe
    print df_perms
    for index, row in df_perms.iterrows():
        print '-----'
        print 'permutaton:',index
        print 'weights tested:'
        randomweightseries = row['value']['randomweightseries']
        #print index,randomweightseries
        for idx in randomweightseries.iteritems():
            print '  ',idx[0],idx[1]
        print 'portfolioreturn=',row['value']['portfolioreturn']
        print 'portfoliostandarddeviation=', row['value']['portfoliostandarddeviation'] 
            
        #-------------------------------------------------------------------


     
  
