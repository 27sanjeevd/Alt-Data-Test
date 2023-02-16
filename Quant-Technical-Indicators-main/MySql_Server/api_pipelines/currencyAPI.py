from forex_python.converter import CurrencyRates
import requests
import json
import datetime
import time

cr = CurrencyRates()

def addCurrency(cnx):
    while True:
        try:
            mycursor = cnx.cursor()
            data = getCurrentCurrency()
            now = datetime.datetime.now()

            sql = "INSERT INTO currency_data (EUR, JPY, BGN, CAD, IDR, MXN, currentTime) VALUES (%s, %s, %s, %s, %s, %s, %s)"
            val = (data["EUR"], data["JPY"], data["BGN"], data["CAD"], data["IDR"], data["MXN"], now)

            mycursor.execute(sql, val)

            cnx.commit()
        except:
            print("currency failed")
        time.sleep(21600)

def getCurrentCurrency():
    return cr.get_rates("USD")
