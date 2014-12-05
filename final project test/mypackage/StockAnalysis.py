import pandas as pd

def describe_portfolio(df):
    '''Get descriptic statistics of the stocks'''
    return df.describe()


def stock_corr(df):
    '''Get stocks correlation'''
    return df.corr()

def stocks_return(df):
    return df.ix[-1] / df.ix[0] -1


def line_plot(df):
    df.plot(kind='line')
    plt.ylabel('Price')


def box_plot(df):
    plt.figure()
    df.boxplot()
    

#single scatterplot of two stocks
def two_stock_scatterplot(df, stock1, stock2):
    ''' Plot a scatterplot of two stock to see their correlation'''
    #daily_rets = percentage_change(df)
    plt.scatter(daily_rets.stock1, daily_rets.stock2, color = 'b', alpha = 0.8)


def scatter_matrix(df):
    '''create a scatter matrix to examine the correlation among stocks'''
    #daily_rets = percentage_change(df)
    pd.scatter_matrix(daily_rets, figsize=(15, 15))


def heat_map(df):
    '''create a heat map to see the correlation among stocks'''
    stocks_corr = stocks_corr(df)
    plt.imshow(stocks_corr, cmap='Blues', interpolation='none')
    plt.colorbar()
    plt.xticks(range(len(stocks_corr)), stocks_corr.columns)
    plt.yticks(range(len(stocks_corr)), stocks_corr.columns)


def risk_vs_return(df):
    '''create a plot to examine the risk and return tradeoff'''
    #daily_return = percentage_change(df)
    plt.scatter(daily_rets.mean(),daily_rets.std())
    plt.xlabel('Expected Return')
    plt.ylabel('Risk')
    for label, x, y in zip(daily_rets.columns, daily_rets.mean(), daily_rets.std()):
        plt.annotate(label, xy = (x, y),xytext = (10, 10),
                     textcoords = 'offset points', 
                     horizontalalignment = 'right', verticalalignment = 'down', 
                     bbox = dict(boxstyle = 'round,pad=0.2', facecolor='red', alpha = 0.2), 
                     arrowprops = dict(arrowstyle = '->', connectionstyle = 'arc3'))


#[20,50,200]
# 50 days moving average
def moving_avg(df,Num):
    '''Allow the user to choose moving average of 20,50 or 200 days, 
    plot a graph comparing the moving average price with the portfolio daily price'''
    moving_average = pd.rolling_mean(df['Sum'],Num,min_periods=Num)
    #df['Moving Average'] = moving_average
    plt.figure(figsize=(12,12))
    plt.plot(df.index,moving_average)
    plt.plot(df.index,df['Sum'])
    plt.ylabel('Price')

