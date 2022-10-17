import calendar
y = int(input("Enter the year:"))        # Year
m = int(input("Enter month:"))           # Month
print(calendar.month(y, m))

# DATE & TIME
import datetime
now = datetime.datetime.now()
print("Current date & time: ")
print(now.strftime("%Y-%m-%d %H:%M:%S"))

import numpy as np
y = np.datetime64('today', 'D') - np.timedelta64(1, 'D')
print("Yesterday date:", y)
today = np.datetime64('today', 'D')
print("Today date:", today)
t = np.datetime64('today', 'D') + np.timedelta64(1, 'D')
print("Tomorrow date:", t)

print("Number of days in specific month:")
print(np.datetime64('2020-03-01')-np.datetime64('2020-02-01'))
print(np.datetime64('2019-03-01')-np.datetime64('2019-02-01'))
print(np.datetime64('2018-03-01')-np.datetime64('2018-02-01'))

# Reverse words
def reverWord(i):
    iw = i.split(" ")
    iw = iw[-1::-1]
    o = ' '.join(iw)
    return o

if __name__ == '__main__':
    i = 'Khush is a python programmer'
    print(reverWord(i))
    days = int(input("Days:"))*3600*24
    hour = int(input("Hour:"))*3600
    min = int(input("Minutes:"))*60
    sec = int(input("Seconds:"))
    Time = days + hour + min + sec
    print("Total seconds:", Time)