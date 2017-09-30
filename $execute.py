class execute:
    
##    def set_OutputEfficientFrontierObject(self,OutputEfficientFrontierObject):
##        self._OutputEfficientFrontierObject = OutputEfficientFrontierObject
##    def get_OutputEfficientFrontierObject(self):
##        return self._OutputEfficientFrontierObject
##    OutputEfficientFrontierObject = property(get_OutputEfficientFrontierObject, set_OutputEfficientFrontierObject)
    #addsimulation
    def __init__(self,symbols,startdate,enddate,permutations,annualized_or_cumulative):
        import addsimulationtoworkbook as addsim
        o = addsim.addsimulation(symbols,startdate,enddate,permutations,annualized_or_cumulative)
        path_to_workbook = o.PathnameToSimulationWorkbook
        

if __name__=='__main__':

    o = execute(

      symbols = [                  
                'dspg',
                'bud',
                'px',
                'unp',
                'lbrdk',
                'chtr',
                'avgo',
                'stz',
                'mar',
                'mgm',
                'lsxma',
                'lyb',
                'goog',
                'sbac',
                'fb',
                'low',
                'aap',
                'pcln',
                'wlk',
                'crc',
                'adsk',
                'cmcsa',
                'dltr',
                'mpc'
          
                    ]
                ,  startdate = '2017-02-28'
                ,  enddate = '2017-09-30'
                ,  permutations = 1000
                ,  annualized_or_cumulative = 'cumulative'
              )
