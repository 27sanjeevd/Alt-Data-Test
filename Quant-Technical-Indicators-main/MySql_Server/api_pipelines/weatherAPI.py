import requests
import datetime
import time

api_key = ""


def inputCityWeather(cnx, city):
    try:
        url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'
        
        response = requests.get(url)

        data = response.json()

        weather_name = data.get("weather")[0].get("main")
        weather_desc = data.get("weather")[0].get("description")
        avg_temp = data.get("main").get("temp")
        max_temp = data.get("main").get("temp_max")
        min_temp = data.get("main").get("temp_min")
        feels_like = data.get("main").get("feels_like")
        humidity = data.get("main").get("humidity")
        visibility = data.get("visibility")
        wind_speed = data.get("wind").get("speed")
        wind_deg = data.get("wind").get("deg")
        rain = data.get("rain")
        if rain is not None:
            rain = rain.get("1h")
        else:
            rain = -1
        snow = data.get("snow")
        if snow is not None:
            snow = snow.get("1h")
        else:
            snow = -1
        name = city
        time = datetime.datetime.now()

        mycursor = cnx.cursor()
        sql = "INSERT INTO weather (weather_name, weather_desc, avg_temp, max_temp, min_temp, feels_like, humidity, visibility, wind_speed, wind_deg, rain, snow, name, time) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        val = (weather_name, weather_desc, avg_temp, max_temp, min_temp, feels_like, humidity, visibility, wind_speed, wind_deg, rain, snow, name, time)

        mycursor.execute(sql, val)
        cnx.commit()
    except:
        print(str(city) + " failed")


def getCityWeather(cnx):
    names = ["chicago", "boston", "san francisco", "new york city", "washington dc"]
    while True:
        for x in names:
            inputCityWeather(cnx, x)

        time.sleep(3600)
