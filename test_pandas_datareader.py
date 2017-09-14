from pandas_datareader import data, wb
from datetime import datetime
start = datetime(2016, 12, 31)
end = datetime.now()
INPX = data.DataReader('AAPL', 'yahoo', start, end)
print INPX
