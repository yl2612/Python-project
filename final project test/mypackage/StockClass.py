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

    def __init__(self, company,start,end):
        '''
        Constructor
        '''
        self.company = company
        self.starttime = start
        self.endtime = end
        self.dataframe = web.DataReader(company,'yahoo',start,end)
        self.closeprice = self.dataframe['Adj Close']
    
    def change_price_precent(self):
        company_firstday = self.closeprice[0]
        self.dataframe['company_%chg'] = (self.closeprice - company_firstday)/company_firstday
        change_price_precent = self.dataframe['company_%chg']
        return change_price_precent
    
    def plot_closeprice_comparision(self):
        fig = plt.figure()
        self.closeprice.plot(color = 'b',label = self.company)
        market = Market(self.starttime,self.endtime)
        market.closeprice.plot(color = 'r',label = 'market price')
        plt.legend()
        plt.savefig('{} and market close price comparision'.format(self.company))
    
    def plot_changeprice_comparision(self):
        fig = plt.figure()
        self.change_price_precent().plot(color = 'b',label = self.company)
        market = Market(self.starttime,self.endtime)
        market.change_price_precent().plot(color = 'r',label = 'market')
        plt.legend()
        plt.savefig('{} and market price change comparision'.format(self.company))
        
        