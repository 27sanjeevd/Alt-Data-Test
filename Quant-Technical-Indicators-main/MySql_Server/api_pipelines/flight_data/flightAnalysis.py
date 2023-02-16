import mysql.connector
import matplotlib.pyplot as plt
import datetime

cnx = mysql.connector.connect(
    user="user",
    password="password",
    host="host",
    database="database"
)

mycursor = cnx.cursor()

mycursor.execute("SELECT country FROM flights")
countries1 = mycursor.fetchall()

mycursor.execute("SELECT amount FROM flights")
amount1 = mycursor.fetchall()

mycursor.execute("SELECT time FROM flights")
time1 = mycursor.fetchall()

data = {}

for x in range(len(countries1)):
    if countries1[x][0] not in data:
        data[countries1[x][0]] = {}
    data[countries1[x][0]][time1[x][0]] = amount1[x][0]


for x in data.keys():
    if x != "United States":
        a1 = []
        b1 = []

        for y in data[x].keys():
            a1.append(y)
            b1.append(data[x][y])

        plt.plot(a1, b1)

plt.show()
