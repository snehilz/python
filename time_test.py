import schedule
import time
from datetime import datetime

def printtime():
    print(f"filename_{date}")

schedule.every(10).seconds.do(printtime)
while True:
    schedule.run_pending()
    time.sleep(1)

