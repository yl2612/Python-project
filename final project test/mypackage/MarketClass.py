'''
Created on 2014.12.1

@author: apple
'''
import numpy as np
import pandas as pd
import pandas.io.data as web
import matplotlib.pyplot as plt

class Market():
    '''
    classdocs
    '''
    def __init__(self, start,end):
        '''
        Constructor
        '''
        self.marketcode = '%5EGSPC'
        self.dataframe = web.DataReader(self.marketcode,'yahoo',start,end)
        self.closeprice = self.dataframe['Adj Close']
        self.dataframe['market_pct_chg'] = self.closeprice.pct_change()
    
    def change_price_precent(self):
        market_firstday = self.closeprice[0]
        self.dataframe['market_%chg'] = (self.closeprice - market_firstday)/market_firstday
        change_price_precent = self.dataframe['market_%chg']
        return change_price_precent