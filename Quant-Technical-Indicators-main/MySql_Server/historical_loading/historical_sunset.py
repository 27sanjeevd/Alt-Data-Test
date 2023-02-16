import requests
import json
import datetime
import time
import mysql.connector

cnx = mysql.connector.connect(
    user="root",
    password="Centralroad12!",
    host="127.0.0.1",
    database="temp_database"
)

def addHistoricSunset():
    time = datetime.datetime(2010, 10, 18)
    time1 = datetime.datetime(2022, 12, 12)
    while time != time1:
        str = time.strftime("%Y") + "/" + time.strftime("%m") + "/" + time.strftime("%d")
        addSunsetData(cnx, str)
        time += datetime.timedelta(days=1)
        

def addSunsetData(cnx, date):
    sunrise, sunset = getSunset(date)

    mycursor = cnx.cursor()
    sql = "INSERT INTO sunrise_data (chicago, boston, san_francisco, new_york, dc, time) VALUES (%s, %s, %s, %s, %s, %s)"
    val = (sunrise[0], sunset[1], sunset[2], sunset[3], sunset[4], date)

    mycursor.execute(sql, val)

    sql = "INSERT INTO sunset_data (chicago, boston, san_francisco, new_york, dc, time) VALUES (%s, %s, %s, %s, %s, %s)"
    val = (sunset[0], sunset[1], sunset[2], sunset[3], sunset[4], date)

    mycursor.execute(sql, val)

    cnx.commit()
        

def getSunset(time):
    #chicago, boston, san francisco, new york, dc
    lat = [41.881832, 42.361145, 37.773972, 40.730610, 38.89511]
    lng = [-87.623177, -71.057083, -122.431297, -73.935242, -77.03637]

    sunrise = []
    sunset = []

    for x in range(5):
        api_url = 'https://api.sunrise-sunset.org/json?lat={}&lng={}&date={}'.format(lat[x], lng[x], time)

        response = requests.get(api_url)

        if response.status_code == 200:
            sunrise_sunset_data = json.loads(response.text)

            sunrise.append(sunrise_sunset_data['results']['sunrise'])
            sunset.append(sunrise_sunset_data['results']['sunset'])
        else:
            sunrise.append("N/A")
            sunset.append("N/A")
        
    return sunrise, sunset


if __name__=='__main__':
    addHistoricSunset()