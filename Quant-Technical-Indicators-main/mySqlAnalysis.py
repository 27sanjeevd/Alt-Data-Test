import mysql.connector
import pandas as pd
import yfinance as yf

cnx = mysql.connector.connect(
    user="user",
    password="password",
    host="host",
    database="database"
)

mycursor = cnx.cursor()
mycursor.execute("SELECT country FROM flights")
country1 = mycursor.fetchall()

mycursor.execute("SELECT amount FROM flights")
amount1 = mycursor.fetchall()

mycursor.execute("SELECT time FROM flights")
time1 = mycursor.fetchall()

dict1 = {}

for x in range(len(country1)):
    if country1[x] not in dict1.keys():
        dict1[country1[x]] = {}
    dict1[country1[x]][time1[x]] = amount1[x]

time = list(dict1[list(dict1.keys())[0]].keys())
beginning = time[0][0].split(" ")[0]
end = time[-1][0].split(" ")[0]


stock = yf.Ticker("AAPL")
stock_data = stock.history(start=beginning, 
                           end=end, 
                           interval='1h')

values = []
for x in range(len(stock_data)):
    values.append(stock_data.iloc[x][1])

print(stock_data.iloc[1])
