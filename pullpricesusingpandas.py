def stockhistory(symbols,fromdate,todate):
    print 'initialized pullpricesusingpandas'
    from pandas_datareader import data
    import pandas as pd


    # Define the instruments to download. We would like to see Apple, Microsoft and the S&P500 index.
    tickers = symbols #['AAPL', 'MSFT', 'SPY']

    # Define which online source one should use
    data_source = 'google'

    # We would like all available data from 01/01/2000 until 12/31/2016.
    start_date = fromdate
    end_date = todate

    # User pandas_reader.data.DataReader to load the desired data. As simple as that.
    panel_data = data.DataReader(tickers, data_source, start_date, end_date)

    # Getting just the adjusted closing prices. This will return a Pandas DataFrame
    # The index in this DataFrame is the major index of the panel_data.
    close = panel_data.ix['Close']

    # Getting all weekdays between 01/01/2000 and 12/31/2016
    all_weekdays = pd.date_range(start=start_date, end=end_date, freq='B')

    # How do we align the existing prices in adj_close with our new set of dates?
    # All we need to do is reindex close using all_weekdays as the new index
    close = close.reindex(all_weekdays)
    #print close
    print 'pullpricesusingpandas','Price records per symbol returned',len(close)
    return close

def cookieAndcrumb(tic):
    import requests
    url = "https://finance.yahoo.com/quote/{0}/history".format(tic)
    r = requests.get(url)
    txt = r.text
    cookie = r.cookies['B']
    import re
    pattern = re.compile('.*"CrumbStore":\{"crumb":"(?P<crumb>[^"]+)"\}')
    for line in txt.splitlines():
        m = pattern.match(line)
        if m is not None:
            crumb = m.groupdict()['crumb']

    return(cookie, crumb)


def getYahooData(tic, start, end):
    import datetime
    import requests
    import os
    start = datetime.datetime.strptime(start,'%Y-%m-%d')
    end = datetime.datetime.strptime(end,'%Y-%m-%d')
    print start
    print end
    cc = cookieAndcrumb(tic)
    dataDir = os.path.expanduser('~') + '/twpData'
    if not os.path.exists(dataDir):
        os.mkdir(dataDir)
    data = {'cookie': cc[0], 'crumb': cc[1]}
    dataFile = os.path.join(dataDir, 'yahoo_cookie.yml')
    import yaml
    with open(dataFile, 'w') as fid:
        yaml.dump(data, fid)
    
    inputData = (tic, int(start), int(end), cc[1])
    url = "https://query1.finance.yahoo.com/v7/finance/download/{0}?period1={1}&period2={2}&interval=1d&events=history&crumb={3}".format(*inputData)
    finalData = requests.get(url, cookies={'B': cc[0]})

    buf = io.StringIO(finalData.text)  # create a buffer
    df = pd.read_csv(buf, index_col=0)
    return df

def getGoogleData(tic,start,end):
    import pandas_datareader.data as web
    import datetime
    start = datetime.datetime(2017, 1, 1)
    end = datetime.datetime(2017, 1, 27)
    f = web.DataReader("F", 'google', start, end)
    return f.ix['2017-01-10']

if __name__=='__main__':
    #options(sys.argv[1],sys.argv[2],sys.argv[3])
    #df = stockhistory(['CSCO','AAPL', 'MSFT', 'SPY'],'2017-01-01','2017-09-30')
    #df = stockhistory(['CSCO','AAPL', 'MSFT', 'SPY'],'2017-01-01','2017-09-30')
    df = stockhistory(['APPL','MSFT','LRCX'],'2017-01-01','2017-09-30')
    
    #df = getYahooData('AAPL','2017-02-15','2017-09-30')
    #df = getGoogleData('AAPL','2017-02-15','2017-09-30')
    #print df
