from bs4 import BeautifulSoup
import requests
import datetime
import time
import yfinance as yf
import pandas as pd

def getNewFuturesData(cnx):
    pairs = ["NQ=F", "RTY=F", "ZB=F", "ZN=F", "ZF=F", "ZT=F", 
            "GC=F", "MGC=F", "SI=F", "SIL=F", "HG=F", "CL=F", 
            "HO=F", "NG=F", "RB=F", "BZ=F"]
    while True:
        time.sleep(2)
        try:
            mycursor = cnx.cursor()
            now = datetime.datetime.now()

            for x in pairs:
                ticker_data = yf.Ticker(x)
                info = ticker_data.info
                historical_data = ticker_data.history(period="30m", interval="1m")
                value = float(historical_data.iloc[-1][1])

                sql = "INSERT INTO futures_data (currency, price, currentTime) VALUES (%s, %s, %s)"
                val = (x, value, now)

                mycursor.execute(sql, val)
                cnx.commit()
                
        except:
            print("yfinance futures failed")

        time.sleep(60)
