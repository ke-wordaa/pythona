import time
while True:
    lo_time = time.localtime()
    hour =  lo_time.tm_hour
    minn = lo_time.tm_min
    se = lo_time.tm_sec
    print(hour,"點",minn,"分",se,"秒")
    time.sleep(1)
