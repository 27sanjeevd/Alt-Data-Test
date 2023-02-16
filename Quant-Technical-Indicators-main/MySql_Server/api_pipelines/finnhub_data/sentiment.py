import finnhub
import datetime
import time
finnhub_client = finnhub.Client(api_key="your-api-key")

stock = ['AAPL', 'MSFT', 'AMZN', 'GOOG', 'UNH']

def getScores(cnx):
    while True:
        time.sleep(3)
        try:
            mycursor = cnx.cursor()
            now = datetime.datetime.now()
            for x in stock:
                val = returnScores(x)
                reddit = val[0]
                twitter = val[1]

                sql = "INSERT INTO stock_sentiment (company, reddit, twitter, date) VALUES (%s, %s, %s, %s)"
                val = (x, reddit, twitter, now)

                mycursor.execute(sql, val)
                cnx.commit()
        except:
            print("sentiment failed")

        time.sleep(900)
        

def returnScores(stock):
    data = finnhub_client.stock_social_sentiment(stock)
    return data['reddit'][0]['score'], data['twitter'][0]['score']
