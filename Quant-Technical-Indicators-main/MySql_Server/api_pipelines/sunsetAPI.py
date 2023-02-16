import requests
import json
import datetime
import time


def addSunsetData(cnx):
    while True:
        now = datetime.datetime.now()
        sunrise, sunset = getSunset()

        mycursor = cnx.cursor()
        sql = "INSERT INTO sunrise_data (chicago, boston, san_francisco, new_york, dc, time) VALUES (%s, %s, %s, %s, %s, %s)"
        val = (sunrise[0], sunset[1], sunset[2], sunset[3], sunset[4], now)

        mycursor.execute(sql, val)

        sql = "INSERT INTO sunset_data (chicago, boston, san_francisco, new_york, dc, time) VALUES (%s, %s, %s, %s, %s, %s)"
        val = (sunset[0], sunset[1], sunset[2], sunset[3], sunset[4], now)

        mycursor.execute(sql, val)

        cnx.commit()
        time.sleep(86400)
        
        
def getSunset():
    #chicago, boston, san francisco, new york, dc
    lat = [41.881832, 42.361145, 37.773972, 40.730610, 38.89511]
    lng = [-87.623177, -71.057083, -122.431297, -73.935242, -77.03637]

    sunrise = []
    sunset = []

    for x in range(5):
        api_url = 'https://api.sunrise-sunset.org/json?lat={}&lng={}'.format(lat[x], lng[x])

        response = requests.get(api_url)

        if response.status_code == 200:
            sunrise_sunset_data = json.loads(response.text)

            sunrise.append(sunrise_sunset_data['results']['sunrise'])
            sunset.append(sunrise_sunset_data['results']['sunset'])
        else:
            sunrise.append("N/A")
            sunset.append("N/A")
        
    return sunrise, sunset
