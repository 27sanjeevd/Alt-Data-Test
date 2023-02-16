from forex_python.converter import CurrencyRates
import datetime
import mysql.connector

cr = CurrencyRates()
t = datetime.datetime(2001, 10, 18)


cnx = mysql.connector.connect(
    user="user",
    password="password",
    host="host",
    database="database"
)

def addCurrency(cnx, date):
    mycursor = cnx.cursor()
    data = cr.get_rates("USD", date)

    sql = "INSERT INTO currency_data (EUR, JPY, BGN, CAD, IDR, MXN, currentTime) VALUES (%s, %s, %s, %s, %s, %s, %s)"
    val = (data["EUR"], data["JPY"], data["BGN"], data["CAD"], data["IDR"], data["MXN"], date)

    mycursor.execute(sql, val)

    cnx.commit()

def addHistoricCurr():
    time = datetime.datetime(2010, 10, 18)
    time1 = datetime.datetime(2022, 12, 12)
    while time != time1:
        addCurrency(cnx, time)
        time += datetime.timedelta(days=1)
        

if __name__=='__main__':
    addHistoricCurr()
