# -*- coding: utf-8 -*-
"""
Created on Wed Jul 29 17:31:47 2015

@author: justin.malinchak
"""

# -*- coding: utf-8 -*-
"""
Created on Wed Jul 29 17:18:11 2015

@author: justin.malinchak
"""

class output:
##    def set_Permutations(self,Permutations):
##        self._Permutations = Permutations
##    def get_Permutations(self):
##        return self._Permutations
##    Permutations = property(get_Permutations, set_Permutations)


    def set_RiskOverReturnDataframe(self,RiskOverReturnDataframe):
        self._RiskOverReturnDataframe = RiskOverReturnDataframe
    def get_RiskOverReturnDataframe(self):
        return self._RiskOverReturnDataframe
    RiskOverReturnDataframe = property(get_RiskOverReturnDataframe, set_RiskOverReturnDataframe)

    def set_EfficientFrontierObject(self,EfficientFrontierObject):
        self._EfficientFrontierObject = EfficientFrontierObject
    def get_EfficientFrontierObject(self):
        return self._EfficientFrontierObject
    EfficientFrontierObject = property(get_EfficientFrontierObject, set_EfficientFrontierObject)

    def myfunc(self,x, pos=0): 
        return '%1.1f%%'%(100*x)
  
    
    def __init__(self,
                     symbols 
                     ,  startdate = '2005-01-01'
                     ,  enddate = ''#'2013-12-31'
                     ,  permutations = 10
                     ,  annualized_or_cumulative = 'cumulative'
                     ):
                         
        print('Initialized class outputefficientfrontier')
        import efficientfrontier as ef   
        
        o = ef.perform(symbols,startdate,enddate,permutations,annualized_or_cumulative) # '^GSPC','^OEX','^MID','^RUT','^DJI'
        self.EfficientFrontierObject = o
        print 'Count of Permutations PLUS equal weighted',len(self.EfficientFrontierObject.PermutationsDataframe)
        self.PrintOutput()
        self.PrintSail()
        
    def PrintOutput(self,):
        # Print Output -------------------------------------------------------------------    
        import numpy
        import config
        import mytools
        import datetime
        import os
        mycachefolder = config.mycachefolder
        mytools.general().make_sure_path_exists(mycachefolder)    
        date14 = str(datetime.datetime.now().strftime("%Y%m%d%H%M%S"))
        
        o = self.EfficientFrontierObject
        print 'covariancematrix'
        cov = o.CovarianceMatrix
        cachedfilepathname = mycachefolder
        cachedfilepathname = os.path.join(cachedfilepathname,date14 + ' covariance.csv')
        cov.to_csv(cachedfilepathname,columns=(list(cov.columns.values)))
        
        print 'correlationmatrix'
        cor = o.CorrelationMatrix
        cachedfilepathname = mycachefolder
        cachedfilepathname = os.path.join(cachedfilepathname,date14 + ' correlation.csv')
        cor.to_csv(cachedfilepathname,columns=(list(cor.columns.values)))

        print 'close prices'
        prc = o.AlignedClosePriceHistoryDataframe
        cachedfilepathname = mycachefolder
        cachedfilepathname = os.path.join(cachedfilepathname,date14 + ' closeprices.csv')
        prc.to_csv(cachedfilepathname,columns=(list(prc.columns.values)))
        #print prc

        print 'adjclose prices'
        prc = o.AlignedAdjClosePriceHistoryDataframe
        cachedfilepathname = mycachefolder
        cachedfilepathname = os.path.join(cachedfilepathname,date14 + ' adjcloseprices.csv')
        prc.to_csv(cachedfilepathname,columns=(list(prc.columns.values)))
        #print prc


        print 'aggregatedreturns'
        #ret = o.AlignedReturnsDataframe
        agret = o.ReturnsClass.AggregatedTotalReturnsDataframe
        #ret['change_pct100'] = df['change_pct'].apply(lambda x: x*100.0)
        cachedfilepathname = mycachefolder
        cachedfilepathname = os.path.join(cachedfilepathname,date14 + ' aggregatedtotalreturns.csv')
        agret.to_csv(cachedfilepathname,columns=(list(agret.columns.values)))

        print 'totaldailyreturns'
        #ret = o.AlignedReturnsDataframe
        ret = o.ReturnsClass.TotalReturnsDataframe
        #ret['change_pct100'] = df['change_pct'].apply(lambda x: x*100.0)
        cachedfilepathname = mycachefolder
        cachedfilepathname = os.path.join(cachedfilepathname,date14 + ' Totalreturns.csv')
        ret.to_csv(cachedfilepathname,columns=(list(ret.columns.values)))

        print 'totalreturnsaligned'
        retalign = o.AlignedTotalReturnsDataframe
        #ret = o.ReturnsClass.ReturnsDataframe
        #ret['change_pct100'] = df['change_pct'].apply(lambda x: x*100.0)
        cachedfilepathname = mycachefolder
        cachedfilepathname = os.path.join(cachedfilepathname,date14 + ' totalreturnsalign.csv')
        retalign.to_csv(cachedfilepathname,columns=(list(retalign.columns.values)))


        print 'length of prc', len(prc)

        #print '---- AnnualizedReturnDataframe-----'
        #print o.ReturnsClass.AggregatedReturnsDataframe

        #df_perms = o.permutationstodataframe(permutations)
        #o.PermutationsDataframe = df_perms
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

    def PrintSail(self,):
#--------------------------------------------------------
        import config
        import mytools
        import datetime
        import os
        mycachefolder = config.mycachefolder
        df_perms = self.EfficientFrontierObject.PermutationsDataframe

        list_of_dicts = []
        for index, row in df_perms.iterrows():
            #print '-----'
            #print 'permutaton:',index
            #print 'weights tested:'
            randomweightseries = row['value']['randomweightseries']
            #print index,randomweightseries
            dict_rows = {}
            for idx in randomweightseries.iteritems():
                dict_rows[str(idx[0])] = str(idx[1])
            dict_rows['portfolioreturn'] = row['value']['portfolioreturn']
            #print 'portfolioreturn=',row['value']['portfolioreturn']
            dict_rows['portfoliostandarddeviation'] = row['value']['portfoliostandarddeviation'] 
            #print 'portfoliostandarddeviation=', row['value']['portfoliostandarddeviation'] 
            list_of_dicts.append(dict_rows)

        import pandas as pd
        df_final = pd.DataFrame(list_of_dicts)
        mytools.general().make_sure_path_exists(mycachefolder)    
        date14 = str(datetime.datetime.now().strftime("%Y%m%d%H%M%S"))
        cachedfilepathname = mycachefolder
        cachedfilepathname = os.path.join(cachedfilepathname,date14 + ' permutations.csv')
        df_final['returnoverrisk'] = df_final.portfolioreturn / df_final.portfoliostandarddeviation
        df_final.to_csv(cachedfilepathname,columns=(list(df_final.columns.values)))
        print 'find your permutations output here:',cachedfilepathname

        print self.drawsail(0.90)
    
#--------------------------------------------------------
    def riskoverreturntodataframe(self,iterations):
        import pandas as pd
        df_permutations = self.EfficientFrontierObject.PermutationsDataframe
        mydf = pd.DataFrame(columns=('portfolioreturn', 'portfoliostandarddeviation','weightstring'))
        
        #Do map here to make quicker
        for index, row in df_permutations.iterrows():
            randomweightseries = row['value']['randomweightseries']
            weightstring = ''
            for idx in randomweightseries.iteritems():
                weightstring = weightstring + str(idx[0])+'='+ str(idx[1]*100)+'% '
            weightstring = weightstring[:-1]
            portfolioreturn = row['value']['portfolioreturn']
            portfoliostandarddeviation = row['value']['portfoliostandarddeviation'] 
            mydf.loc[index] = [portfolioreturn,portfoliostandarddeviation,weightstring]
        mydf['returnoverrisk'] = mydf.portfolioreturn / mydf.portfoliostandarddeviation
        self.RiskOverReturnDataframe = mydf
        return mydf

    def drawsail(self,optimalpctasdecimal = 0.90):
        numberofpermutations = len(self.EfficientFrontierObject.PermutationsDataframe)
        df = self.riskoverreturntodataframe(numberofpermutations)
        #df['returnoverrisk'] = df.portfolioreturn / df.portfoliostandarddeviation
        maxreturnoverriskseries = df.ix[df['returnoverrisk'].idxmax()]
        df['maxreturnoverrisk'] = maxreturnoverriskseries['returnoverrisk']
        print 'the max returnoverrisk is:',maxreturnoverriskseries['returnoverrisk']
        #df.apply(lambda row: min([row['A'], row['B']])-row['C'], axis=1)
        #df.plot(title='Title Here')
        import matplotlib.pylab as plt
        #import numpy as np
        #import pandas as pd
        #import numpy as np
        #df = pd.DataFrame(np.random.randn(10,2), columns=['col1','col2'])
        #df['col3'] = np.arange(len(df))**2 * 100 + 100
        #print df
        #plt.scatter(df.col1, df.col2, s=df.col3)
        #colors = np.where(df.col3 > 300, 'r', 'k')

        #fig = plt.figure()
        fig = plt.figure(figsize=(12.0, 9.0)) # in inches!
        
        cond = df.returnoverrisk > df.maxreturnoverrisk * optimalpctasdecimal
        subset_a = df[cond].dropna()
        subset_b = df[~cond].dropna()
        plt.scatter(subset_a.portfoliostandarddeviation, subset_a.portfolioreturn, s=7, c='red', label='frontier >' + str(int(optimalpctasdecimal*100))+'%',marker='s', edgecolors='none')
        plt.scatter(subset_b.portfoliostandarddeviation, subset_b.portfolioreturn, s=7, c='dodgerblue', label='suboptimal',marker='s', edgecolors='none') 
        
        from matplotlib.ticker import FuncFormatter 
        ax = plt.subplot(111)
        ax.xaxis.set_major_formatter(FuncFormatter(self.myfunc)) 
        ax.yaxis.set_major_formatter(FuncFormatter(self.myfunc)) 
        
        plt.legend(fontsize=12)    
        fig.suptitle('Optimal Weights  (' + self.EfficientFrontierObject.StartDateString +' to ' + self.EfficientFrontierObject.EndDateString +')' +
            chr(10) + 
            maxreturnoverriskseries['weightstring'] + 
            chr(10) +
            'N=' + str(numberofpermutations) + '   '
            'Annualized Return=' + str(round(maxreturnoverriskseries['portfolioreturn']*100,2)) + '%   ' +
            'StDev=' + str(round(maxreturnoverriskseries['portfoliostandarddeviation']*100,2)) + '%', fontsize=12)
        plt.xlabel('Risk (StDev)', fontsize=12)
        plt.ylabel('Return (%)', fontsize=12)
        import datetime
        today_datetime = datetime.datetime.today()
        today_datetime_string_forfilename = today_datetime.strftime('%Y%m%d%H%M%S')
        import config
        cachefilename = config.mycachefolder + '\\drawsail '+today_datetime_string_forfilename+'.jpg'
        fig.savefig(cachefilename)
        return cachefilename
        
        # To get a list of colors        
#        import matplotlib        
#        for name, hex in matplotlib.colors.cnames.iteritems():
#            print(name, hex)

        

if __name__=='__main__':

    mysymbols = ['AAPL','MSFT','XOM','JNJ','GE']
    o = output(
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
                ,  startdate = '2017-02-28'
                ,  enddate = '2017-09-30'
                ,  permutations = 1000
                ,  annualized_or_cumulative = 'cumulative'
              )

    #print o.EfficientFrontierObject.CorrelationMatrix
    #print o.EfficientFrontierObject.CovarianceMatrix
    #print o.EfficientFrontierObject.AlignedReturnsDataframe
    #print ' ---- here is just one random weight Series... ----'
    #print o.EfficientFrontierObject.portfolioriskreturnrandomweight()
##    import config
##    import mytools
##    import datetime
##    import os
##    mycachefolder = config.mycachefolder
##    df_perms = o.EfficientFrontierObject.PermutationsDataframe
##
##    list_of_dicts = []
##    for index, row in df_perms.iterrows():
##        #print '-----'
##        #print 'permutaton:',index
##        #print 'weights tested:'
##        randomweightseries = row['value']['randomweightseries']
##        #print index,randomweightseries
##        dict_rows = {}
##        for idx in randomweightseries.iteritems():
##            dict_rows[str(idx[0])] = str(idx[1])
##        dict_rows['portfolioreturn'] = row['value']['portfolioreturn']
##        #print 'portfolioreturn=',row['value']['portfolioreturn']
##        dict_rows['portfoliostandarddeviation'] = row['value']['portfoliostandarddeviation'] 
##        #print 'portfoliostandarddeviation=', row['value']['portfoliostandarddeviation'] 
##        list_of_dicts.append(dict_rows)
##        #-------------------------------------------------------------------
##    import pandas as pd
##    df_final = pd.DataFrame(list_of_dicts)
##    
##    mytools.general().make_sure_path_exists(mycachefolder)    
##    date14 = str(datetime.datetime.now().strftime("%Y%m%d%H%M%S"))
##    cachedfilepathname = mycachefolder
##    cachedfilepathname = os.path.join(cachedfilepathname,date14 + ' permutations.csv')
##
##    df_final['returnoverrisk'] = df_final.portfolioreturn / df_final.portfoliostandarddeviation
##    df_final.to_csv(cachedfilepathname,columns=(list(df_final.columns.values)))
##
##    print o.drawsail(50,0.90)
