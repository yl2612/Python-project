'''
Created on 2014.12.4

@author: apple
'''

class StockNameInputException(Exception):
    """
    Raise when the input is not a stock name in the yahoo financial data.
    """
    def __str__(self):
        return "The input is invalid. It must be a stock name in the yahoo financial data."
    
class DateInputException(Exception):
    """
    Raise when the input is not date form.
    """
    def __str__(self):
        return "The input is invalid. It must contain year, month, and day, separated by '/', such as 2011/1/1."
    