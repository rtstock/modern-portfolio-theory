class addsimulation:
    
    def set_OutputEfficientFrontierObject(self,OutputEfficientFrontierObject):
        self._OutputEfficientFrontierObject = OutputEfficientFrontierObject
    def get_OutputEfficientFrontierObject(self):
        return self._OutputEfficientFrontierObject
    OutputEfficientFrontierObject = property(get_OutputEfficientFrontierObject, set_OutputEfficientFrontierObject)
    
    #PathnameToSimulationWorkbook
    def set_PathnameToSimulationWorkbook(self,PathnameToSimulationWorkbook):
        self._PathnameToSimulationWorkbook = PathnameToSimulationWorkbook
    def get_PathnameToSimulationWorkbook(self):
        return self._PathnameToSimulationWorkbook
    PathnameToSimulationWorkbook = property(get_PathnameToSimulationWorkbook, set_PathnameToSimulationWorkbook)
        
    def __init__(self,symbols,startdate,enddate,permutations,annualized_or_cumulative):
        import compileworkbook as cwbk
        o = cwbk.compileclass(symbols,startdate,enddate,permutations,annualized_or_cumulative)
        path_to_workbook = o.PathnameToCompiledWorkbook
        #path_to_workbook = 'C:\\Batches\\GitStuff\\modern-portfolio-theory\\cache\\20170921102057 compiled.xlsx'
        from os.path import basename
        import os
        rootpath = os.path.dirname(os.path.abspath(path_to_workbook))
        filename = basename(path_to_workbook)
        fileroot = filename.split(' ')[0]
        newfilename = fileroot + ' simulated.xlsx'
        new_path_to_workbook = os.path.join(rootpath, newfilename)
        from openpyxl import load_workbook
        from openpyxl.chart import (
            ScatterChart,
            Reference,
            Series,
        )
        
        wb = load_workbook(filename = path_to_workbook)
        current_wks_name = 'permutations'
        print '-----',current_wks_name,'------------'
        wks = wb[current_wks_name]
        col_portfoliostandarddeviation = 0
        col_portfolioreturn = 0
        row_max = 0
        for row_cells in wks.iter_rows(min_row=1, max_row=1):
            for cell in row_cells:
                print cell.col_idx, cell.column, cell.row, cell.value
                if cell.value == 'portfoliostandarddeviation':
                    col_portfoliostandarddeviation = cell.col_idx
                if cell.value == 'portfolioreturn':
                    col_portfolioreturn = cell.col_idx
        for col_cells in wks.iter_rows(min_col=1, max_col=1):
            for cell in col_cells:
                #print cell.col_idx, cell.column, cell.row, cell.value
                row_max = cell.row
        
        chart = ScatterChart()
        chart.title = "Scatter Chart"
        chart.style = 5
        chart.charttype = -4169 

        chart.x_axis.title = 'Risk'
        chart.y_axis.title = 'Return'

        xvalues = Reference(wks, min_col=col_portfoliostandarddeviation, min_row=2, max_row=row_max)
        yvalues = Reference(wks, min_col=col_portfolioreturn, min_row=1, max_row=row_max)
        series = Series(yvalues, xvalues, title_from_data=True)
        chart.series.append(series)
        wks.add_chart(chart, "N10")
        
        
        current_wks_name = 'aggregatedpricechangereturns'
        print '-----',current_wks_name,'------------' 
        wks = wb[current_wks_name]
        col_portfoliostandarddeviation = 0
        col_portfolioreturn = 0
        row_max = 0
        col_max = 0
        for row_cells in wks.iter_rows(min_row=1, max_row=1):
            for cell in row_cells:
                print cell.col_idx, cell.column, cell.row, cell.value
                if cell.value == 'symbol':
                    col_symbol = cell.col_idx
                if cell.value == 'cumulative_return':
                    col_cumulative_return = cell.col_idx
                if cell.value == 'random_return':
                    col_random_return = cell.col_idx
                col_max = cell.col_idx
        for col_cells in wks.iter_rows(min_col=1, max_col=1,min_row=2):
            for cell in col_cells:
                #print cell.col_idx, cell.column, cell.row, cell.value
                row_max = cell.row

        wb.create_sheet('simulation')
        wks_simulation = wb['simulation']

        wb.save(new_path_to_workbook)
        self.PathnameToSimulationWorkbook = new_path_to_workbook
##        try:
##            wb.create_sheet('simulation')
##            wks_simulation = wb['simulation']
##            wb.save('C:\\Batches\\GitStuff\\modern-portfolio-theory\\cache\\20170921102057 simulated.xlsx')
##            simulation_row_offset = 7
##            print 'simulation_row_offset',simulation_row_offset
##            for row_cells in wks.iter_rows(min_row=1, max_row=row_max):
##                for c in row_cells:
##                    wks_simulation.cell(row=c.row, column=c.column).value = c.value
##                    print 'got here 1',c,wks_simulation.cell(row=c.row, column=c.column).value
##            for col_cells in wks.iter_rows(min_col=col_symbol, max_col=col_symbol,min_row=1):
##                for c in col_cells:
##                    wks_simulation.cell(row=c.row, column=col_max+2).value = wks.cell(row=c.row, column=col_symbol).value
##                    wks_simulation.cell(row=c.row, column=col_max+3).value = wks.cell(row=c.row, column=col_random_return).value
##                    print 'got here 2',c,wks_simulation.cell(row=c.row, column=col_max+3).value
##                    if c.row == 1:
##                        print 'got here 3',c
##                        wks_simulation.cell(row=c.row, column=col_max+2).value = 'Symbol'
##                        wks_simulation.cell(row=c.row, column=col_max+3).value = 'Forecast Return'
##                        wks_simulation.cell(row=c.row, column=col_max+4).value = 'Top Constraint'
##                        wks_simulation.cell(row=c.row, column=col_max+5).value = 'Bottom Constraint'
##                        wks_simulation.cell(row=c.row, column=col_max+6).value = 'Simulated Weights'
##                        wks_simulation.cell(row=c.row, column=col_max+7).value = 'Equal Weights'
##        except:
##            pass
##        print 'got here 4'
##        wb.save('C:\\Batches\\GitStuff\\modern-portfolio-theory\\cache\\20170921102057 simulatedxx.xlsx')
        

if __name__=='__main__':

    o = addsimulation(
##spy
##iwm
##mdy
##'spy',
##'iwm',
##'mdy'

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
