class runclass:
    
##    def set_OutputEfficientFrontierObject(self,OutputEfficientFrontierObject):
##        self._OutputEfficientFrontierObject = OutputEfficientFrontierObject
##    def get_OutputEfficientFrontierObject(self):
##        return self._OutputEfficientFrontierObject
##    OutputEfficientFrontierObject = property(get_OutputEfficientFrontierObject, set_OutputEfficientFrontierObject)
    #addsimulation
    def __init__(self,symbols,startdate,enddate,permutations,annualized_or_cumulative):
        #print startdate
        import addsimulationtoworkbook as addsim
        o = addsim.addsimulation(symbols,startdate,enddate,permutations,annualized_or_cumulative)
        path_to_workbook = o.PathnameToSimulationWorkbook
        

if __name__=='__main__':
    import pandas as pd
    lst0 = []
    lst0.append({'ticker':'MRK','longshort':'L','givenweight':0.2, 'forecastreturn':0.05,'topconstraint':0.05,'bottomconstraint':0.01})
    lst0.append({'ticker':'THO','longshort':'L','givenweight':0.2, 'forecastreturn':0.05,'topconstraint':0.05,'bottomconstraint':0.01})
    lst0.append({'ticker':'ALGN','longshort':'S','givenweight':0.2, 'forecastreturn':-0.05,'topconstraint':-0.005,'bottomconstraint':-0.02})
    lst0.append({'ticker':'CELG','longshort':'S','givenweight':0.2, 'forecastreturn':-0.05,'topconstraint':-0.005,'bottomconstraint':-0.02})
    lst0.append({'ticker':'MSFT','longshort':'L','givenweight':0.1, 'forecastreturn':0.05,'topconstraint':0.05,'bottomconstraint':0.01})
    lst0.append({'ticker':'FB','longshort':'L','givenweight':0.1, 'forecastreturn':0.05,'topconstraint':0.05,'bottomconstraint':0.01})
    df_symbols_and_signs = pd.DataFrame(lst0)
    df_symbols_and_signs = df_symbols_and_signs.set_index('ticker',drop=True)
    print df_symbols_and_signs
    #stop

    o = runclass(symbols = df_symbols_and_signs  
        ,  startdate = '2018-01-01'
        ,  enddate = '2018-04-12'
        ,  permutations = 1000
        ,  annualized_or_cumulative = 'cumulative'
              )
