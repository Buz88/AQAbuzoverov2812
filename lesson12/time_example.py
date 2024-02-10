import time
'''
def get_range():
    time.sleep(3) #for w8 nezaminno dlia debug, prosto dlia logiki ne treba
    return [item for item in range(10000000)]


start = time.time()
get_range()
end = time.time()

print(f'execution time: {end - start}')
print(time.time())
t = (2024,2,8,8,3,20,1,35,0)
t = time.mktime(t)
print(time.strftime('%b %d %Y %H:%M:%S', time.gmtime(t)))
'''
import datetime as dt
'''
print(dt.date(year=2024, month=2, day=8))
print(dt.datetime.now())
print(dt.datetime.now(dt.UTC))
today = dt.datetime.now()
print(today.date())
print(today.day)
print(today.second)


t1 = dt.date(2024,2,8)
t2 = dt.date(2025,10,8)
t3 = t2-t1
print(t3)
t4 = t2+t3
print(t4)
t5 = dt.datetime(2024,5,23,12,5,6)
t6 = dt.datetime(2024,5,21,12,50,35)
t7=t5-t6
print(t7)
t8 = dt.timedelta(weeks=1,days=3,hours=6,minutes=15,seconds=55)
t9 = dt.timedelta(10)
print(t8+t9)

t10 = dt.datetime.now().timestamp()
print(t10)
t11 = dt.datetime(2021,4,30).timestamp()
print(t11)
t12 = t10 + 3600*24
t13 = dt.datetime.fromtimestamp(t12)
print(t13)
'''
time_format_string = '%Y-%m-%d %A %I:%M:%S %p'
t14 = dt.datetime.now().strftime(time_format_string)
print(t14)
t15 = dt.datetime.strptime(t14,time_format_string)
print(t15)
a = t15.astimezone()
print(a)
t15.replace()
print(t15)






