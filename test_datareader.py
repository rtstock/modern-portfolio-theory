import pandas_datareader as web
import datetime

co = web.DataReader("AAPL", "yahoo", datetime.date.today() - datetime.timedelta(days=10), datetime.date.today())

print co.head()
