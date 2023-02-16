import pandas as pd

df = pd.read_excel("Data/HistoricalPrices.xlsx")

def getDates():
    return df.iloc[:, 0]

def getDatesBetween(startDate, endDate):
    dates = df.iloc[:, 0]

    check1 = False
    nextX = 0
    #need to add a functionality that searches for the closest date if a given date isn't valid
    for x in range(len(dates)):
        if (str(dates[x]) == startDate + " 00:00:00"):
            check1 = True
            nextX = x

    if check1:
        for x in range(len(dates) - nextX):
            if (str(dates[x + nextX]) == endDate + " 00:00:00"):
                return dates[nextX : nextX + x]

    return dates


def getStockData(val1):
    return df.iloc[:, val1]

def getStockDataBetween(startDate, endDate, val1):
    values = df.iloc[:, val1]
    dates = df.iloc[:, 0]

    check1 = False
    nextX = 0
    #need to add a functionality that searches for the closest date if a given date isn't valid
    for x in range(len(dates)):
        if (str(dates[x]) == startDate + " 00:00:00"):
            check1 = True
            nextX = x

    if check1:
        for x in range(len(dates) - nextX):
            if (str(dates[x + nextX]) == endDate + " 00:00:00"):
                return values[nextX : nextX + x]

    return values
