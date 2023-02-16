import finnhub
import datetime
import time
finnhub_client = finnhub.Client(api_key="your-api-key")

stock = ['AAPL', 'MSFT', 'AMZN', 'GOOG', 'UNH']

def returnPatents(stock, now):
    now_time = now.strftime("%Y") + "-" + now.strftime("%m") + "-" + now.strftime("%d")
    month_ago = now - datetime.timedelta(weeks=4)
    month_time = month_ago.strftime("%Y") + "-" + month_ago.strftime("%m") + "-" + month_ago.strftime("%d")

    data = finnhub_client.stock_uspto_patent(stock, _from=month_time, to=now_time)

    return len(data['data'])


    

def getPatents(cnx):
    while True:
        try:
            time.sleep(1)
            amount = []
            now = datetime.datetime.now()
            for x in stock:
                amt = returnPatents(x, now)

                mycursor = cnx.cursor()
                    
                sql = "INSERT INTO patents (company, amount, time) VALUES (%s, %s, %s)"
                val = (x, amt, now)

                mycursor.execute(sql, val)
                cnx.commit()
        except:
            print("patents failed")
        time.sleep(86400)
