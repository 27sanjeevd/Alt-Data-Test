import yfinance as yf
import pandas as pd

def getHourlyData(stock, start1, end1):
    temp = yf.Ticker(stock)
    return temp.history(start=start1, end=end1, interval="1h")
