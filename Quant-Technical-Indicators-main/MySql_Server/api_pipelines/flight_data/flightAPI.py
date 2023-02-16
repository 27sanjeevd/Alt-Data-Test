from opensky_api import OpenSkyApi
import datetime
import time


def checkString(word1):
    val = True
    for x in word1:
        if not x.isalpha():
            val = False
        
    return val

def addPlaneData(cnx):
    while True:
        try:
            mycursor = cnx.cursor()
            api = OpenSkyApi()
            states = api.get_states()
            now = datetime.datetime.now()

            countries = {}
            if states is not None:
                for s in states.states:
                    if checkString(s.origin_country):
                        if s.origin_country in countries.keys():
                            countries[s.origin_country] += 1
                        else:
                            countries[s.origin_country] = 1

                for x in countries.keys():
                    sql = "INSERT INTO flights (country, amount, time) VALUES (%s, %s, %s)"
                    val = (x, countries[x], now)

                    mycursor.execute(sql, val)
                    cnx.commit()
        except:
            print("flight failed")
        time.sleep(140)



