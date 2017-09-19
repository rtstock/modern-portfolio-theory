class execute:
    def __init__(self,symbols,startdate,enddate,permutations,annualized_or_cumulative):
        import outputefficientfrontier as oef
        o = oef.output(symbols,startdate,enddate,permutations,annualized_or_cumulative)
        d = o.DictionaryOfOutputFiles
        for k,v in d.items():
            print k, v

if __name__=='__main__':

    mysymbols = ['AAPL','MSFT','XOM','JNJ','GE']
    o = execute(
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
