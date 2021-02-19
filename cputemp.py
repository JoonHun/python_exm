import os
import time
import datetime

def getCPUTemp():
    temp = os.popen("vcgencmd measure_temp").readline()
    return (temp.replace("temp=", "").replace("'C", ""))

while True:
    now_time = datetime.datetime.now()
    format_time = now_time.strftime("%H:%M:%S")
    now_temp = getCPUTemp()
    print("time : ", format_time, " temp : ", now_temp)
    time.sleep(1)
