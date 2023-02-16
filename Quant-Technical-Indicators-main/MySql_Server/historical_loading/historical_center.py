from multiprocessing import Process
import threading
from historical_currency import addHistoricCurr
from historical_sunset import addHistoricSunset

if __name__=='__main__':
    threads = []
    threads.append(threading.Thread(target=addHistoricCurr))
    threads.append(threading.Thread(target=addHistoricSunset))

    for x in threads:
        x.start()

    for x in threads:
        x.join()