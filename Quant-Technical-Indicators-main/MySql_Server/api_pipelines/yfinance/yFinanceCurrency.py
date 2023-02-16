from bs4 import BeautifulSoup
import requests
import datetime
import time
import yfinance as yf
import pandas as pd

def getNewCurrencyData(cnx):
    pairs = ["EURUSD=X", "JPY=X", "GBPUSD=X", "AUDUSD=X"]
    while True:
        time.sleep(1)
        try:
            values = []

            for x in pairs:
                ticker_data = yf.Ticker(x)
                info = ticker_data.info
                historical_data = ticker_data.history(period="5m", interval="1m")
                values.append(historical_data.iloc[-1][1])
                
            mycursor = cnx.cursor()
            now = datetime.datetime.now()
            for x in range(len(values)):
                sql = "INSERT INTO currency_data (currency, price, currentTime) VALUES (%s, %s, %s)"
                val = (pairs[x], values[x], now)

                mycursor.execute(sql, val)
                cnx.commit()
        except:
            print("yfinance currency failed")

        time.sleep(60)

    """
    page = requests.get('https://finance.yahoo.com/currencies/')

    soup = BeautifulSoup(page.content, 'html.parser')
    while True:
        try:
            time.sleep(1)

            elements = soup.find_all(class_='Va(m) Ta(end) Pstart(20px) Fw(600) Fz(s)')

            values = []
            x = 3
            for element in elements:
                if x % 3 == 0:
                    values.append(float((element.text).replace(",", "")))
                x += 1

            names = []
            elements = soup.find_all(class_='Va(m) Ta(start) Px(10px) Fz(s)')

            for element in elements:
                names.append(element.text)

            mycursor = cnx.cursor()
            now = datetime.datetime.now()

            for x in range(len(values)):
                sql = "INSERT INTO currency_data (currency, price, currentTime) VALUES (%s, %s, %s)"
                val = (names[x], values[x], now)

                mycursor.execute(sql, val)
                cnx.commit()
        except:
            print("yfinance failed")
        time.sleep(20)
    """
