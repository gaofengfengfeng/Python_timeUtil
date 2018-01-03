#coding:UTF-8
import time
import sys

timestamp = sys.argv[1]
#timestamp = 1462451334

#转换成localtime
time_local = time.localtime(int(timestamp))
print(time_local)
#转换成新的时间格式(2018-01-03 16:25:35)
dt = time.strftime("%Y-%m-%d %H:%M:%S", time_local)
dt1 = time.strftime("%Y%m%d", time_local)

print dt
print dt1

