import os
from pprint import pprint
from turtle import clear
from google.cloud import storage
import schedule
import time
from datetime import datetime

file_path='d:\sanu_2021\python\python.py'

# convert the ctime in
# seconds since epoch
# to local time
c_time = os.path.getctime(file_path)
c_time1 = os.path.getmtime(file_path)
local_time = time.ctime(c_time)
localtime2=time.ctime(c_time1)
print("ctime (Local time):", local_time,localtime2)
