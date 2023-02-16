import finnhub
import datetime
finnhub_client = finnhub.Client(api_key="your-api-key")

stock = ['AAPL', 'MSFT', 'AMZN', 'GOOG', 'UNH']

def getSenate():

    now = datetime.datetime.now()
    now_time = now.strftime("%Y") + "-" + now.strftime("%m") + "-" + now.strftime("%d")
    month_ago = now - datetime.timedelta(weeks=10)
    month_time = month_ago.strftime("%Y") + "-" + month_ago.strftime("%m") + "-" + month_ago.strftime("%d")

    amount = []

    for x in stock:
        val = returnSenate(x, month_time, now_time)

        amount.append(val)

    return amount

    

def returnSenate(stock, old, new1):

    data = finnhub_client.stock_lobbying(stock, _from=old, to=new1)
    return len(data['data'])
