'''
Created on 2014.12.3

@author: apple
'''

import numpy as np
import pandas as pd
import pandas.io.data as web
import matplotlib.pyplot as plt
from mypackage.StockClass import *
from mypackage.MarketClass import *

def main():
    stock_name_list = ['IBM','AAPL','C']
    start = pd.datetime(2011,11,21)
    end = pd.datetime(2012,3,21)
    stock_class_list = {stock: Stock(stock,start,end) for stock in stock_name_list}
    pricecols = {stock:stock_class.closeprice for stock,stock_class in stock_class_list.iteritems()}
    closed_price_df = pd.DataFrame(pricecols)
    print closed_price_df.head()


if __name__ == '__main__':
    main()