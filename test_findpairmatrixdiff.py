#C:\Batches\GitStuff\$work\correlation_sample.csv
def importcsv():
    print 'x'
def findpairstdev():
    s1 = 'JPM'
    s2 = 'BAC'
    import pandas as pd
    myfile = 'C:\Batches\GitStuff\$work\closeprices_sample.csv'
    df = pd.read_csv(myfile)
    df2 = df["Date"]
    df.set_index("Date", drop=True, inplace=True)
    columns = list(df.columns.values)
    #print df
    #print df2
    
    df_shares1 = 10000.0 / df.iloc[[0]]
    
    df_shares2 = df_shares1.append([df_shares1]*(len(df)-1),ignore_index=True)
    df_shares3 = pd.concat([df2, df_shares2], axis=1)
    df_shares3.set_index("Date", drop=True, inplace=True)
    #print df_shares3
    #stop
    #index_full = list(df.index)
    #print df_shares2
    #print index_full
    #df_shares3 = df_shares2.set_index(index_full)
    
    #print df_shares3
    #stop
    #import numpy as np
    #print df
    #print df_shares1
    
    df_dollarized = df.multiply(df_shares3, axis=1)
    print df_dollarized
    dict_of_difference_matrixes = {}
    for column in columns:
        df_diff = df_dollarized[columns].sub(df_dollarized[column], axis=0)
        dict_of_difference_matrixes[column] = df_diff
        print 'finished', column
    print dict_of_difference_matrixes['AAPL']
##    stop
##    for k,v in dict_of_difference_matrixes.items():
##        print v
##        print k
##        stop
##    mylist = []
##    alreadydonelist = []
##    b = True
##    mean1 = df[s1].mean()
##    mean2 = df[s1].mean()
##    quantity1 = 10000.0 / df[s1].iloc[0]
##    quantity2 = 10000.0 / df[s2].iloc[0]
##    #print df[s2].iloc[0]
##    #print df[s1]
##    dollarized1 = df[s1].apply(lambda x: x*quantity1)
##    dollarized2 = df[s2].apply(lambda x: x*quantity2)
##    print dollarized1
##    print dollarized2
##    dollarized0 = pd.concat([dollarized1, dollarized2], axis=1, join_axes=[dollarized1.index])
##    dollarized0['diff'] = dollarized0[s1] - dollarized0[s2]
##    #dollarized0['rollingstd'] = dollarized0['diff'].rolling_std()
##    print dollarized0
##    print 'max',dollarized0['diff'].max()
##    print 'min',dollarized0['diff'].min()
##    print 'mean',dollarized0['diff'].mean()
##    print 'std',dollarized0['diff'].std()
    
##    while b == True:
##        maxvalue = df.values.max()
##        
##        if not maxvalue == 1:
##            for column in columns:
##                row = df[column].idxmax()
##                if df.loc[row,column] == maxvalue:
##                    list1 = [row,column]
##                    listsorted = sorted(list1)
##                    listsortedstring = listsorted[0]+listsorted[1]
##                    #print 'listsortedstring',listsortedstring
##                    if not listsortedstring in alreadydonelist:
##                        dict1 = {'pair':listsorted, 'value':df.loc[row][column]}
##                        alreadydonelist.append(listsortedstring)
##                        mylist.append(dict1)
##                    #dict1 = {'row':row,'column':column, 'value':df.loc[row][column]}
##                    #print dict1
##                    
##        if len(mylist) >= 1000:
##            b = False
##        df[df==maxvalue] = -10000
##        print x
##        for column in columns:
##            #df.loc[df['Value'].idxmax()]
##            row = df[column].idxmax()
##            maxval = df[column].max()
##            print row,column, maxval, df.loc[row][column]
##            if not maxval == 1:
##                mylist.append({'row':row,'column':column, 'value':df.loc[row][column]})
##            df.loc[row,column] = float(-10000)
##
####            for i, row in df.iterrows():
####                if row[column] == maxval:
####                    mylist.append({
####                    df.loc[row,column] = float(-10000)
         
    return mylist
    
    #print mydict
    
pairs = findpairstdev()
for p in pairs:
    print p
