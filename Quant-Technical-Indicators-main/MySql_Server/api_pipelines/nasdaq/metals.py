import requests
import datetime
import time

api_key = "your-api-key"

def inputMetals(cnx, type):
    time = datetime.datetime.now()
    str = time.strftime("%Y") + "-" + time.strftime("%m") + "-" + time.strftime("%d")

    url = f'https://data.nasdaq.com/api/v3/datasets/LBMA/{type}?start_date={str}&end_date={str}&api_key={api_key}'

    response = requests.get(url)

    data = response.json()
    usd_am = data['dataset']['data'][0][1]
    usd_pm = data['dataset']['data'][0][2]

    mycursor = cnx.cursor()
    if type == "gold":
        sql = "INSERT INTO gold (date, usd_am, usd_pm) VALUES (%s, %s, %s)"
        val = (data['dataset']['data'][0][0], usd_am, usd_pm)
        mycursor.execute(sql, val)
        cnx.commit()
    else:
        sql = "INSERT INTO silver (date, usd_am, usd_pm) VALUES (%s, %s, %s)"
        val = (data['dataset']['data'][0][0], usd_am, usd_pm)
        mycursor.execute(sql, val)
        cnx.commit()



def getMetals(cnx):
    a1 = ["gold", "silver"]

    while True:
        for x in range(2):
            inputMetals(cnx, a1[x])

        time.sleep(86400)
