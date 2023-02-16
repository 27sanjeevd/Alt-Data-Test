from bs4 import BeautifulSoup
import requests
import datetime
import time
import yfinance as yf
import pandas as pd

def getNewBondData(cnx):
    pairs = ["^IRX", "^FVX", "^TNX", "^TYX"]
    while True:
        try:
            mycursor = cnx.cursor()
            now = datetime.datetime.now()

            for x in pairs:
                ticker_data = yf.Ticker(x)
                info = ticker_data.info
                historical_data = ticker_data.history(period="30m", interval="1m")
                value = float(historical_data.iloc[-1][1])

                sql = "INSERT INTO bond_data (currency, price, currentTime) VALUES (%s, %s, %s)"
                val = (x, value, now)

                mycursor.execute(sql, val)
                cnx.commit()
                
        except:
            print("yfinance bonds failed")

        time.sleep(60)
