from datetime import datetime, timedelta
from math import log
import matplotlib.pyplot as plt
epoch = datetime(1970, 1, 1)

def epoch_seconds(date):
    td = date - epoch
    return td.days * 86400 + td.seconds + (float(td.microseconds) / 1000000)

def get_w(z):
    if (z>0):
        return 1
    elif (z==0) :
        return 0
    elif (z<0):
        return -1
def get_m(z):
    if (abs(z)>=1):
        return abs(z)
    elif (abs(z)<1):
        return 1
    
def get_ts(date):
    return epoch_seconds(date) - 1134028003

def get_z(u,d):
    return u - d
    
def hot(ts,w,m):
    order = log(m, 10)
    return round(order + (w * ts)/45000, 7)
    
    
ts_now = get_ts(datetime.now())
ts_1_hour_ago = get_ts(datetime.now() - timedelta(minutes=60))

z = get_z(100,2)
m = get_m(z)
w = get_y(z)
score_now = hot(ts_now,w,m)
score_1_hour_ago = hot (ts_1_hour_ago,w,m)
print(score_now)

plt.hist(x=[ts_now,ts_1_hour_ago],y=[score_now,score_1_hour_ago])
