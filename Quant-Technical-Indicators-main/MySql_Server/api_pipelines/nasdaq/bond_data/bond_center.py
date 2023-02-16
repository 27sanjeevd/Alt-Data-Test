from billrates import billrates
from longtermrates import longtermrates
from reallongterm import reallongterm
from realyield import realyield
from yield1 import yield1

import requests
import time
import datetime

def inputBondData(cnx):
    now = datetime.datetime.now()
    realAverage = reallongterm()
    real5, real7, real10, real20, real30 = realyield()
    disc4, coup4, disc8, coup8, disc13, coup13, disc26, coup26, disc52, coup52 = billrates()
    yieldmo1, yieldmo2, yieldmo3, yieldmo6, yieldyr1, yieldyr2, yieldyr3, yieldyr5, yieldyr7 = yield1()
    long10, long20 = longtermrates()




def getBondData(cnx):
    while True:
        time.sleep(86400)