import finnhub
import datetime
import time
finnhub_client = finnhub.Client(api_key="your-api-key")

stock = ['AAPL', 'MSFT', 'AMZN', 'GOOG', 'UNH']

def getSpending(cnx):
    while True:
        try:
            time.sleep(2)
            now = datetime.datetime.now()
            now_time = now.strftime("%Y") + "-" + now.strftime("%m") + "-" + now.strftime("%d")
            month_ago = now - datetime.timedelta(weeks=10)
            month_time = month_ago.strftime("%Y") + "-" + month_ago.strftime("%m") + "-" + month_ago.strftime("%d")


            for x in stock:
                amt = returnSpending(x, month_time, now_time)

                mycursor = cnx.cursor()
                
                sql = "INSERT INTO gov_spending (company, amount, time) VALUES (%s, %s, %s)"
                val = (x, amt, now)

                mycursor.execute(sql, val)
                cnx.commit()
        except:
            print("spending failed")
        time.sleep(86400)


    

def returnSpending(stock, old, new1):
    val = 0
    data = finnhub_client.stock_usa_spending(stock, _from=old, to=new1)

    for x in data['data']:
        val += x['totalValue']
    return val
