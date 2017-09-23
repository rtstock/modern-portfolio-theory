class execute:
    
    def set_OutputEfficientFrontierObject(self,OutputEfficientFrontierObject):
        self._OutputEfficientFrontierObject = OutputEfficientFrontierObject
    def get_OutputEfficientFrontierObject(self):
        return self._OutputEfficientFrontierObject
    OutputEfficientFrontierObject = property(get_OutputEfficientFrontierObject, set_OutputEfficientFrontierObject)
    
    def __init__(self,symbols,startdate,enddate,permutations,annualized_or_cumulative):
        import config
        import mytools
        import datetime
        import os
        import outputefficientfrontier as oef
        o = oef.output(symbols,startdate,enddate,permutations,annualized_or_cumulative)
        d = o.DictionaryOfOutputFiles
        for k,v in d.items():
            #print k, v
            (f_path, filename) = os.path.split(v)
            date14 = filename.split(' ')[0]
        print date14
        mycachefolder = config.mycachefolder
        mytools.general().make_sure_path_exists(mycachefolder)    
        #date14 = str(datetime.datetime.now().strftime("%Y%m%d%H%M%S"))
        cachedfilepathname = mycachefolder
        cachedfilepathname = os.path.join(cachedfilepathname,date14 + ' compiled.xlsx')

        import xlsxwriter
        import glob
        import csv
        import numbers
        workbook = xlsxwriter.Workbook(cachedfilepathname, {'strings_to_numbers': True}) 
        #for filename in glob.glob("*.csv"):
        for k,v in d.items():
            #print k, v
            (f_path, filename) = os.path.split(v)
            worksheetname = str(filename.split('.')[0])
            worksheetname = worksheetname.split(' ')[1]
            ws = workbook.add_worksheet(worksheetname)
            spamReader = csv.reader(open(v, 'rb'), delimiter=',')
            row_count = 0
            #print filename
            for row in spamReader:
                for col in range(len(row)):
                    n = row[col]
                    ws.write(row_count,col,n)
                row_count +=1

        workbook.close()
        print 'you can find your compiled file here: ',cachedfilepathname

if __name__=='__main__':

    ##mysymbols = ['AAPL','MSFT','XOM','JNJ','GE']
    o = execute(
##                symbols = ['GOOGL',
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
##                            #'GOLD',
##                            'LMT',
##                            'RTN',
##                            'BP',
##                            'T',
##                            'HSBC',
##                            'THO',
##                            'SPY'
##
        
##                symbols = ['GOOGL',
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
##                            #'GOLD',
##                            'LMT',
##                            'RTN',
##                            'BP',
##                            'T',
##                            'HSBC',
##                            'THO',
##                            'XOM',
##                            'WMT',
##                            'MRO',
##                            'ALGN',
##                            'WRK',
##                           'JPM',
##                           'WFC'
##                           
##                            ]
                symbols = [
                    'spy',
                    'shy',
                    'agg'
                    ]
                ,  startdate = '2017-02-28'
                ,  enddate = '2017-09-30'
                ,  permutations = 1000
                ,  annualized_or_cumulative = 'cumulative'
              )
