import datetime as dt

now = dt.datetime.now()
month = now.month
print(month)
print(type(now))

d_o_b = dt.datetime(year=2000, month=12, day=15, hour=4, minute=30)
print(d_o_b)