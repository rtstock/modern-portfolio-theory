
import xlwings as xw
xw.Range('A1').value = 'something'
def rand_numbers():
    wb = xw.Book() 
    sht = wb.sheets['Sheet1']
    
    sht.range('M6').value = 'Hello from python'
    
