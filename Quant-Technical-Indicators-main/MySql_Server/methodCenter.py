import mysql.connector
from api_pipelines.currencyAPI import addCurrency
from api_pipelines.sunsetAPI import addSunsetData
from api_pipelines.flight_data.flightAPI import addPlaneData
from api_pipelines.weatherAPI import getCityWeather
from api_pipelines.nasdaq.metals import getMetals
from api_pipelines.nasdaq.crude_oil import getOil
from api_pipelines.finnhub_data.government_spending import getSpending
from api_pipelines.finnhub_data.patents import getPatents
from api_pipelines.yfinance.yFinanceCurrency import getNewCurrencyData
from api_pipelines.yfinance.futures import getNewFuturesData
from api_pipelines.yfinance.bonds import getNewBondData
from api_pipelines.finnhub_data.sentiment import getScores
import datetime
import time
from multiprocessing import Process
import threading
import sys

cnx = mysql.connector.connect(
    user="user",
    password="password",
    host="host",
    database="database"
)

if __name__=='__main__':
    threads = []
    #threads.append(threading.Thread(target=addCurrency, args=(cnx,)))    <- redundant with new yfinance script
    threads.append(threading.Thread(target=getNewCurrencyData, args=(cnx,)))
    threads.append(threading.Thread(target=getScores, args=(cnx,)))
    threads.append(threading.Thread(target=getNewFuturesData, args=(cnx,)))
    #threads.append(threading.Thread(target=getNewBondData, args=(cnx,)))
    threads.append(threading.Thread(target=addPlaneData, args=(cnx,)))
    #threads.append(threading.Thread(target=getSpending, args=(cnx,)))
    #threads.append(threading.Thread(target=getPatents, args=(cnx,)))
    threads.append(threading.Thread(target=getCityWeather, args=(cnx,)))
    threads.append(threading.Thread(target=addSunsetData, args=(cnx,)))
    #threads.append(threading.Thread(target=getMetals, args=(cnx,)))
    #threads.append(threading.Thread(target=getOil, args=(cnx,)))

    for x in threads:
        x.start()

    for x in threads:
        x.join()
