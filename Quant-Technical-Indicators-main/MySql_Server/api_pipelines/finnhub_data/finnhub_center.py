from multiprocessing import Process
import threading
import mysql.connector
from files.government_spending import getSpending

def finnhub_center(cnx):
    threads = []
    threads.append(threading.Thread(target=getSpending, args=(cnx,)))

    for x in threads:
        x.start()

    for x in threads:
        x.join()



cnx = mysql.connector.connect(
    user="user",
    password="password",
    host="host",
    database="database"
)
