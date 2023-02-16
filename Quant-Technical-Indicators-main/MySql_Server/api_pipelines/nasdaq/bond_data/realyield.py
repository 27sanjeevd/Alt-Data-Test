import requests
import datetime
import time

api_key = "your-api-key"

def realyield():
    time = datetime.datetime.now()

    str = time.strftime("%Y") + "-" + time.strftime("%m") + "-" + time.strftime("%d")

    url = f'https://data.nasdaq.com/api/v3/datasets/USTREASURY/REALYIELD?start_date={time}&end_date={time}&api_key={api_key}'

    response = requests.get(url)

    data = response.json()
    return data['dataset']['data'][0][1:6]




