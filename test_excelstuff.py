import psutil
excelPids = []
for proc in psutil.process_iter():
  if proc.name == "EXCEL.EXE": excelPids.append(proc.pid)

import win32gui
windows = []
win32gui.EnumWindows(lambda hwnd, resultList: resultList.append(win32gui.GetWindowText(hwnd)),windows)
#print windows
#enumerates all the windows open from the top down
x = [i for i in windows if "Excel" in i].pop(0)
import openpyxl as pyxl
import itertools
wb = pyxl.load_workbook(x)
print len(wb.worksheets)
##print x
###this one is closest to the top
##import win32com
##xl = win32com.client.Dispatch("Excel.Application")
##print 'xxxx'.xl.ActiveWorkbook.FullName
