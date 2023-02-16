import requests
import datetime
import time

api_key = "your-api-key"

def reallongterm():
    time = datetime.datetime.now()

    str = time.strftime("%Y") + "-" + time.strftime("%m") + "-" + time.strftime("%d")

    url = f'https://data.nasdaq.com/api/v3/datasets/USTREASURY/REALLONGTERM?start_date={time}&end_date={time}&api_key={api_key}'

    response = requests.get(url)

    data = response.json()
    value = data['dataset']['data'][0][1]

    return value


