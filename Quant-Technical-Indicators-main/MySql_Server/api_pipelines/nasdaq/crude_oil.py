import requests
import datetime
import time

api_key = "your-api-key"

def inputOil(cnx):
    time = datetime.datetime.now()
    str = time.strftime("%Y") + "-" + time.strftime("%m") + "-" + time.strftime("%d")

    url = f'https://data.nasdaq.com/api/v3/datasets/OPEC/ORB?start_date={str}&end_date={str}&api_key={api_key}'

    response = requests.get(url)

    data = response.json()
    price = data['dataset']['data'][0][1]

    mycursor = cnx.cursor()
    sql = "INSERT INTO oil (date, price) VALUES (%s, %s)"
    val = (str, price)

    mycursor.execute(sql, val)
    cnx.commit()


def getOil(cnx):

    inputOil(cnx)
    time.sleep(86400)
