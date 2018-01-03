#coding:UTF-8
import time

#获取当前时间
time_now = int(time.time())

#转换成localtime
time_local = time.localtime(time_now)

#转换成新的时间格式
dt = time.strftime("%Y-%m-%d %H:%M:%S", time_local)

print(dt)
print(time_now)
