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
    classdocs
    '''

    def __init__(self, stock,start,end):
        '''
        Constructor
        '''
        self.stock = stock
        self.starttime = start
        self.endtime = end
        self.dataframe = web.DataReader(stock,'yahoo',start,end)
        self.closeprice = self.dataframe['Adj Close']
        self.period_ret = (self.closeprice[-1]-self.closeprice[0])/self.closeprice[0]
    
    def change_price_precent(self):
        stock_firstday = self.closeprice[0]
        self.dataframe['stock_%chg'] = (self.closeprice - stock_firstday)/stock_firstday
        change_price_precent = self.dataframe['stock_%chg']
        return change_price_precent
    
    def plot_closeprice_comparision(self):
        fig = plt.figure()
        self.closeprice.plot(color = 'b',label = self.stock)
        market = Market(self.starttime,self.endtime)
        market.closeprice.plot(color = 'r',label = 'market price')
        plt.legend()
        plt.savefig('{} and market close price comparision'.format(self.stock))
    
    def plot_changeprice_comparision(self):
        fig = plt.figure()
        self.change_price_precent().plot(color = 'b',label = self.stock)
        market = Market(self.starttime,self.endtime)
        market.change_price_precent().plot(color = 'r',label = 'market')
        plt.legend()
        plt.savefig('{} and market price change comparision'.format(self.stock))
        
    def closeprice_describe(self):
        return self.closeprice.describe()
    
            