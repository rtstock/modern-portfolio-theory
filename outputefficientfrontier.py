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

    def set_DictionaryOfOutputFiles(self,DictionaryOfOutputFiles):
        self._DictionaryOfOutputFiles = DictionaryOfOutputFiles
    def get_DictionaryOfOutputFiles(self):
        return self._DictionaryOfOutputFiles
    DictionaryOfOutputFiles = property(get_DictionaryOfOutputFiles, set_DictionaryOfOutputFiles)

    def myfunc(self,x, pos=0): 
        return '%1.1f%%'%(100*x)

    def __init__(self,
                     symbols_and_signs_list 
                     ,  startdate = '2005-01-01'
                     ,  enddate = ''#'2013-12-31'
                     ,  permutations = 10
                     ,  annualized_or_cumulative = 'cumulative'
                     ,  longmax = 5
                     ,  longmin = 1
                     ,  shortmax = -0.5
                     ,  shortmin = -2
                     ):
                         
        print('Initialized class outputefficientfrontier')
        import efficientfrontierlongshort as ef   
        
        o = ef.perform(symbols_and_signs_list
                     ,  startdate,enddate,permutations
                     ,  annualized_or_cumulative
                     ,  longmax
                     ,  longmin
                     ,  shortmax
                     ,  shortmin
                    ) 
        self.EfficientFrontierObject = o
        dict_output = self.printoutput()
        o.runpermutations()
        self.EfficientFrontierObject = o
        print 'Count of Permutations PLUS equal weighted',len(o.PermutationsDataframe)
        permutations_file = self.outputpermutations()
        dict_output['permutations'] = permutations_file
        #sail_file = self.drawsail(0.90)
        #dict_output['sail'] = sail_file
        
        self.DictionaryOfOutputFiles = dict_output
        print len(dict_output), 'files created'
        
    def printoutput(self,):

        import numpy
        import config
        import mytools
        import datetime
        import os

        d_returns = {}
        
        mycachefolder = config.mycachefolder
        mytools.general().make_sure_path_exists(mycachefolder)    
        date14 = str(datetime.datetime.now().strftime("%Y%m%d%H%M%S"))
        
        o = self.EfficientFrontierObject
        print 'covariancematrix'
        cov = o.CovarianceMatrix
        cachedfilepathname = mycachefolder
        cachedfilepathname = os.path.join(cachedfilepathname,date14 + ' covariance.csv')
        cov.to_csv(cachedfilepathname,columns=(list(cov.columns.values)))
        d_returns['covariancematrix'] = cachedfilepathname
        
        print 'correlationmatrix'
        cor = o.CorrelationMatrix
        cachedfilepathname = mycachefolder
        cachedfilepathname = os.path.join(cachedfilepathname,date14 + ' correlation.csv')
        cor.to_csv(cachedfilepathname,columns=(list(cor.columns.values)))
        d_returns['correlationmatrix'] = cachedfilepathname
        
        print 'close prices'
        prc = o.AlignedClosePriceHistoryDataframe
        cachedfilepathname = mycachefolder
        cachedfilepathname = os.path.join(cachedfilepathname,date14 + ' closeprices.csv')
        prc.to_csv(cachedfilepathname,columns=(list(prc.columns.values)))
        d_returns['closeprices'] = cachedfilepathname
        
        print 'adjcloseprices'
        prc = o.AlignedAdjClosePriceHistoryDataframe
        cachedfilepathname = mycachefolder
        cachedfilepathname = os.path.join(cachedfilepathname,date14 + ' adjcloseprices.csv')
        prc.to_csv(cachedfilepathname,columns=(list(prc.columns.values)))
        d_returns['adjcloseprices'] = cachedfilepathname
        
        print 'aggregatedpricechangereturns'
        agret = o.ReturnsClass.AggregatedPriceChangeReturnsDataframe
        cachedfilepathname = mycachefolder
        cachedfilepathname = os.path.join(cachedfilepathname,date14 + ' aggregatedpricechangereturns.csv')
        agret.to_csv(cachedfilepathname,columns=(list(agret.columns.values)))
        d_returns['aggregatedpricechangereturns'] = cachedfilepathname
        
        print 'aggregatedtotalreturns'
        agret = o.ReturnsClass.AggregatedTotalReturnsDataframe
        cachedfilepathname = mycachefolder
        cachedfilepathname = os.path.join(cachedfilepathname,date14 + ' aggregatedtotalreturns.csv')
        agret.to_csv(cachedfilepathname,columns=(list(agret.columns.values)))
        d_returns['aggregatedtotalreturns'] = cachedfilepathname
        
        print 'totaldailyreturns'
        ret = o.ReturnsClass.TotalReturnsDataframe
        cachedfilepathname = mycachefolder
        cachedfilepathname = os.path.join(cachedfilepathname,date14 + ' totaldailyreturns.csv')
        ret.to_csv(cachedfilepathname,columns=(list(ret.columns.values)))
        d_returns['totaldailyreturns'] = cachedfilepathname
        
        print 'totalreturnsaligned'
        retalign = o.AlignedTotalReturnsDataframe
        cachedfilepathname = mycachefolder
        cachedfilepathname = os.path.join(cachedfilepathname,date14 + ' totalreturnsalign.csv')
        retalign.to_csv(cachedfilepathname,columns=(list(retalign.columns.values)))
        d_returns['totalreturnsaligned'] = cachedfilepathname

        print 'pricechangereturns aligned'
        pcralign = o.AlignedPriceChangeReturnsDataframe
        cachedfilepathname = mycachefolder
        cachedfilepathname = os.path.join(cachedfilepathname,date14 + ' pricechangereturnsaligned.csv')
        pcralign.to_csv(cachedfilepathname,columns=(list(pcralign.columns.values)))
        d_returns['pricechangereturnsaligned'] = cachedfilepathname

        print 'length of prc', len(prc)
        return d_returns
    
    def outputpermutations(self,):
        #--------------------------------------------------------
        import config
        import mytools
        import datetime
        import os
        mycachefolder = config.mycachefolder
        df_perms = self.EfficientFrontierObject.PermutationsDataframe

        list_of_dicts = []
        for index, row in df_perms.iterrows():

            randomweightseries = row['value']['randomweightseries']
            dict_rows = {}
            for idx in randomweightseries.iteritems():
                dict_rows[str(idx[0])] = str(idx[1])
            dict_rows['portfolioreturn'] = row['value']['portfolioreturn']
            dict_rows['portfoliostandarddeviation'] = row['value']['portfoliostandarddeviation'] 
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
        return cachedfilepathname
        
        
    
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

        maxreturnoverriskseries = df.ix[df['returnoverrisk'].idxmax()]
        df['maxreturnoverrisk'] = maxreturnoverriskseries['returnoverrisk']
        print 'the max returnoverrisk is:',maxreturnoverriskseries['returnoverrisk']
        import matplotlib.pylab as plt

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
        
        

if __name__=='__main__':

    symbols_and_signs_list = [
['AAL','S'],
['ADM','S'],
['AES','L'],
['AGN','S'],
['ALKS','S'],
['AMAT','L'],
['AMD','S'],
['AMGN','L'],
['APD','L'],
['ARNC','S'],
['AVT','S'],
['AXP','L'],
['AXS','S'],
['BAC','L'],
['BC','S'],
['BEN','L'],
['CA','L'],
['CAH','S'],
['CASY','S'],
['CELG','L'],
['CL','L'],
['CMCSA','S'],
['COLM','S'],
['CRI','S'],
['CSCO','L'],
['CVS','L'],
['CVX','L'],
['CXO','S'],
['DIS','S'],
['DISH','S'],
['EGN','S'],
['ETR','L'],
['F','S'],
['FCNCA','S'],
['FLS','S'],
['FSLR','S'],
['FTI','S'],
['GE','S'],
['GPC','S'],
['GPS','L'],
['GRMN','L'],
['GWR','S'],
['GWW','S'],
['HAIN','S'],
['HAS','S'],
['HD','L'],
['HHC','S'],
['HOG','S'],
['HPE','S'],
['HRL','S'],
['INTC','L'],
['JLL','S'],
['JNJ','L'],
['JWN','L'],
['KHC','S'],
['KMB','L'],
['KMI','S'],
['KSS','L'],
['LAZ','L'],
['LEG','S'],
['LLY','L'],
['LMT','L'],
['LNG','S'],
['LOW','L'],
['LPX','L'],
['LUK','S'],
['LVLT','S'],
['LYB','L'],
['M','L'],
['MAS','L'],
['MD','S'],
['MDLZ','S'],
['MDT','S'],
['MLM','S'],
['MMM','L'],
['MO','L'],
['MS','L'],
['MUR','S'],
['NFX','S'],
['NKE','S'],
['NUAN','S'],
['NWL','S'],
['NWS','S'],
['OTEX','S'],
['PAG','S'],
['PCLN','L'],
['PDCO','S'],
['PEP','L'],
['PM','L'],
['QCOM','S'],
['RPM','S'],
['RTN','L'],
['S','S'],
['SEE','S'],
['SJM','S'],
['SKX','S'],
['SLB','S'],
['SNA','S'],
['SON','S'],
['STX','L'],
['SWKS','L'],
['T','L'],
['TAP','S'],
['TGT','L'],
['TRIP','S'],
['TWTR','S'],
['UAL','S'],
['UHS','S'],
['UNP','L'],
['VIA','S'],
['VMC','S'],
['VRSK','S'],
['VSAT','S'],
['WAB','S'],
['WHR','S'],
['WPX','S'],
['WTM','S'],
['XOM','S'],
['XRAY','S'],
['Y','S']
]

    symbols = ['MAR', 'MON', 'NOV', 'A', 'AAL', 'AAP', 'AAPL', 'ABBV', 'ABC', 'ABT', 'ACN', 'ADBE', 'ADI', 'ADM', 'ADP', 'ADS', 'ADSK', 'AEE', 'AEP', 'AES', 'AET', 'AFL', 'AGN', 'AIG', 'AIV', 'AIZ', 'AJG', 'AKAM', 'ALB', 'ALGN', 'ALK', 'ALL', 'ALLE', 'ALXN', 'AMAT', 'AMD', 'AME', 'AMG', 'AMGN', 'AMP', 'AMT', 'AMZN', 'ANDV', 'ANSS', 'ANTM', 'AON', 'AOS', 'APA', 'APC', 'APD', 'APH', 'ARE', 'ARNC', 'ATVI', 'AVB', 'AVGO', 'AVY', 'AWK', 'AXP', 'AYI', 'AZO', 'BA', 'BAC', 'BAX', 'BBT', 'BBY', 'BCR', 'BDX', 'BEN', 'BF.B', 'BHF', 'BHGE', 'BIIB', 'BK', 'BLK', 'BLL', 'BMY', 'BRK.B', 'BSX', 'BWA', 'BXP', 'C', 'CA', 'CAG', 'CAH', 'CAT', 'CB', 'CBG', 'CBOE', 'CBS', 'CCI', 'CCL', 'CDNS', 'CELG', 'CERN', 'CF', 'CFG', 'CHD', 'CHK', 'CHRW', 'CHTR', 'CI', 'CINF', 'CL', 'CLX', 'CMA', 'CMCSA', 'CME', 'CMG', 'CMI', 'CMS', 'CNC', 'CNP', 'COF', 'COG', 'COH', 'COL', 'COO', 'COP', 'COST', 'COTY', 'CPB', 'CRM', 'CSCO', 'CSRA', 'CSX', 'CTAS', 'CTL', 'CTSH', 'CTXS', 'CVS', 'CVX', 'CXO', 'D', 'DAL', 'DE', 'DFS', 'DG', 'DGX', 'DHI', 'DHR', 'DIS', 'DISCA', 'DISCK', 'DISH', 'DLPH', 'DLR', 'DLTR', 'DOV', 'DPS', 'DRE', 'DRI', 'DTE', 'DUK', 'DVA', 'DVN', 'DWDP', 'DXC', 'EA', 'EBAY', 'ECL', 'ED', 'EFX', 'EIX', 'EL', 'EMN', 'EMR', 'EOG', 'EQIX', 'EQR', 'EQT', 'ES', 'ESRX', 'ESS', 'ETFC', 'ETN', 'ETR', 'EVHC', 'EW', 'EXC', 'EXPD', 'EXPE', 'EXR', 'F', 'FAST', 'FB', 'FBHS', 'FCX', 'FDX', 'FE', 'FFIV', 'FIS', 'FISV', 'FITB', 'FL', 'FLIR', 'FLR', 'FLS', 'FMC', 'FOX', 'FOXA', 'FRT', 'FTI', 'FTV', 'GD', 'GE', 'GGP', 'GILD', 'GIS', 'GLW', 'GM', 'GOOG', 'GOOGL', 'GPC', 'GPN', 'GPS', 'GRMN', 'GS', 'GT', 'GWW', 'HAL', 'HAS', 'HBAN', 'HBI', 'HCA', 'HCN', 'HCP', 'HD', 'HES', 'HIG', 'HLT', 'HOG', 'HOLX', 'HON', 'HP', 'HPE', 'HPQ', 'HRB', 'HRL', 'HRS', 'HSIC', 'HST', 'HSY', 'HUM', 'IBM', 'ICE', 'IDXX', 'IFF', 'ILMN', 'INCY', 'INFO', 'INTC', 'INTU', 'IP', 'IPG', 'IR', 'IRM', 'ISRG', 'IT', 'ITW', 'IVZ', 'JBHT', 'JCI', 'JEC', 'JNJ', 'JNPR', 'JPM', 'JWN', 'K', 'KEY', 'KHC', 'KIM', 'KLAC', 'KMB', 'KMI', 'KMX', 'KO', 'KORS', 'KR', 'KSS', 'KSU', 'L', 'LB', 'LEG', 'LEN', 'LH', 'LKQ', 'LLL', 'LLY', 'LMT', 'LNC', 'LNT', 'LOW', 'LRCX', 'LUK', 'LUV', 'LVLT', 'LYB', 'M', 'MA', 'MAA', 'MAC', 'MAS', 'MAT', 'MCD', 'MCHP', 'MCK', 'MCO', 'MDLZ', 'MDT', 'MET', 'MGM', 'MHK', 'MKC', 'MLM', 'MMC', 'MMM', 'MNST', 'MO', 'MOS', 'MPC', 'MRK', 'MRO', 'MS', 'MSFT', 'MSI', 'MTB', 'MTD', 'MU', 'MYL', 'NAVI', 'NBL', 'NDAQ', 'NEE', 'NEM', 'NFLX', 'NFX', 'NI', 'NKE', 'NLSN', 'NOC', 'NRG', 'NSC', 'NTAP', 'NTRS', 'NUE', 'NVDA', 'NWL', 'NWS', 'NWSA', 'O', 'OKE', 'OMC', 'ORCL', 'ORLY', 'OXY', 'PAYX', 'PBCT', 'PCAR', 'PCG', 'PCLN', 'PDCO', 'PEG', 'PEP', 'PFE', 'PFG', 'PG', 'PGR', 'PH', 'PHM', 'PKG', 'PKI', 'PLD', 'PM', 'PNC', 'PNR', 'PNW', 'PPG', 'PPL', 'PRGO', 'PRU', 'PSA', 'PSX', 'PVH', 'PWR', 'PX', 'PXD', 'PYPL', 'Q', 'QCOM', 'QRVO', 'RCL', 'RE', 'REG', 'REGN', 'RF', 'RHI', 'RHT', 'RJF', 'RL', 'RMD', 'ROK', 'ROP', 'ROST', 'RRC', 'RSG', 'RTN', 'SBAC', 'SBUX', 'SCG', 'SCHW', 'SEE', 'SHW', 'SIG', 'SJM', 'SLB', 'SLG', 'SNA', 'SNI', 'SNPS', 'SO', 'SPG', 'SPGI', 'SPLS', 'SRCL', 'SRE', 'STI', 'STT', 'STX', 'STZ', 'SWK', 'SWKS', 'SYF', 'SYK', 'SYMC', 'SYY', 'T', 'TAP', 'TDG', 'TEL', 'TGT', 'TIF', 'TJX', 'TMK', 'TMO', 'TRIP', 'TROW', 'TRV', 'TSCO', 'TSN', 'TSS', 'TWX', 'TXN', 'TXT', 'UA', 'UAA', 'UAL', 'UDR', 'UHS', 'ULTA', 'UNH', 'UNM', 'UNP', 'UPS', 'URI', 'USB', 'UTX', 'V', 'VAR', 'VFC', 'VIAB', 'VLO', 'VMC', 'VNO', 'VRSK', 'VRSN', 'VRTX', 'VTR', 'VZ', 'WAT', 'WBA', 'WDC', 'WEC', 'WFC', 'WHR', 'WLTW', 'WM', 'WMB', 'WMT', 'WRK', 'WU', 'WY', 'WYN', 'WYNN', 'XEC', 'XEL', 'XL', 'XLNX', 'XOM', 'XRAY', 'XRX', 'XYL', 'YUM', 'ZBH', 'ZION', 'ZTS']
    #symbols = ['XRX', 'XYL', 'YUM', 'ZBH', 'ZION', 'ZTS']
    symbols_and_signs_list = []
    for s in symbols:
        pair = [s,'L']
        symbols_and_signs_list.append(pair)
    print symbols_and_signs_list
    
    o = output(
                symbols_and_signs_list = symbols_and_signs_list
                
                ,  startdate = '2017-03-01'
                ,  enddate = '2017-09-30'
                ,  permutations = 100
                ,  annualized_or_cumulative = 'cumulative'
                ,  longmax = 5
                ,  longmin = 1
                ,  shortmax = -0.5
                ,  shortmin = -2
              )
