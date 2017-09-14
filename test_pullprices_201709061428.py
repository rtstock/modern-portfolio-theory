def stockhistory(symbolslist,fromdate,todate):
    from pandas_datareader import data
    import pandas as pd


    # Define the instruments to download. We would like to see Apple, Microsoft and the S&P500 index.
    tickers = symbolslist #['AAPL', 'MSFT', 'SPY']

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
    return close

if __name__=='__main__':
    #options(sys.argv[1],sys.argv[2],sys.argv[3])
    df = stockhistory(['AAPL', 'MSFT', 'SPY'],'2017-01-01','2017-09-30')
    print df
