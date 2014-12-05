import pandas.io.data as web
import pandas as pd
import datetime
import matplotlib.pyplot as plt
get_ipython().magic(u'matplotlib inline')
start = datetime.datetime(2010, 1, 1)
end = datetime.datetime(2014, 1, 27)


'''get the data online'''
tickers = ['AMZN', 'BP', 'C', 'COF']
#for ticker in tickers:
portfolio_stock_price = web.get_data_yahoo(tickers, start, end)['Adj Close']
portfolio_stock_price.head()


#box plot
df = portfolio_stock_amount(portfolio_stock_price,trade_amount)



normal = normalized_data(df)
normal.plot(kind='line')
plt.ylabel('Normalized Close Price')


perdf = percentage_change(df)
#perdf.plot(kind='line',figsize=(19,8))



