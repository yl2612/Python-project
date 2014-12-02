'''
Created on 2014.12.1

@author: apple
'''

import numpy as np
import pandas as pd
import pandas.io.data as web
import matplotlib.pyplot as plt
from mypackage.StockClass import *
from mypackage.MarketClass import *

def main():
    start = pd.datetime(2011,11,21)
    end = pd.datetime(2012,3,21)
    stock = Stock('IBM',start,end)
    stock.plot_closeprice_comparision()
    stock.plot_changeprice_comparision()

if __name__ == '__main__':
    main()