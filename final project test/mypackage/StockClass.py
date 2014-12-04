'''
Created on 2014.12.1

@author: apple
'''

import numpy as np
import pandas as pd
import pandas.io.data as web
import matplotlib.pyplot as plt
from mypackage.MarketClass import *

class Stock():
    '''
    Generate a class describe the stock containing several attributes and functions.
    
    '''

    def __init__(self, stock,start,end):
        '''
        Constructor:
        
        Input:
            stock(string): the name of stock, can be read into pandas.io.data.DataReader
            start(pandas.datatime): the start time of date range from user input
            end(pandas.datatime): the end time of date range from user input
        
        Attributes:
            stock(string): the name of stock
            start(pandas.datatime): the start time of date range 
            end(pandas.datatime): the end time of date range 
            dataframe(pandas.dataframe): extract the data from the yahoo financial
            closeprice(pandas.series): the column 'Adj Close' in the dataframe
            period_ret(float) : the return between this date range
        '''
        self.stock = stock
        self.starttime = start
        self.endtime = end
        self.dataframe = web.DataReader(stock,'yahoo',start,end)
        self.closeprice = self.dataframe['Adj Close']
        self.period_ret = (self.closeprice[-1]-self.closeprice[0])/self.closeprice[0]
    
    def change_price_precent(self):
        """
        Generate the percent change of daily close price.
        """
        stock_firstday = self.closeprice[0]
        self.dataframe['stock_%chg'] = (self.closeprice - stock_firstday)/stock_firstday
        change_price_precent = self.dataframe['stock_%chg']
        return change_price_precent
    
    def plot_closeprice(self):
        
        fig = plt.figure()
        self.closeprice.plot(color = 'b',label = self.stock)
        plt.legend()
        plt.xticks(rotation=45)
        plt.title('The Close Price of {} '.format(self.stock))
        return fig
    
    
    def plot_changeprice_comparison(self):
        """
        Compare and plot the percent change of the stock close price and that of the actual market over time.
        """
        fig = plt.figure()
        self.change_price_precent().plot(color = 'b',label = self.stock)
        market = Market(self.starttime,self.endtime)
        market.change_price_precent().plot(color = 'r',label = 'market')
        plt.legend()
        plt.xticks(rotation=45)
        plt.title('The Comparison between {} and market close price '.format(self.stock))
        return fig
        
    def closeprice_describe(self):
        return self.closeprice.describe()
    
            