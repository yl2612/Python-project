'''
Created on 2014.12.4

@author: apple
'''
import re
import pandas.io.data as web
import datetime
from mypackage.Exceptions import *

def ParseStockName(stock_name):
    """
    Check whether the input is a valid stock name.
    """
    if isinstance(stock_name, str):
        #Check whether input of list has a valid form
        try:
            df =web.DataReader(stock_name,'yahoo')
        except:
            raise StockNameInputException()
        else:
            return stock_name
    else:
        raise StockNameInputException()

def ParseDate(datestring):
    """
    Check whether the input is a valid date.
    """
    if isinstance(datestring, str):
        #Check whether input of list has a valid form
        try:
            valid_date = datetime.datetime.strptime(datestring, '%Y/%m/%d')
            return valid_date
        except ValueError:
            raise DateInputException()
    else:
        raise DateInputException()

if __name__ == '__main__':
    pass