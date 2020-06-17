# I think it is an easy problem
#Algo for the starting date
# get check the day, if it is sunday increase the count, use datetime library
#  do this till the end date

import datetime
from dateutil.relativedelta import *

if __name__ == '__main__':
    count = 0
    startdate = datetime.datetime.strptime("1 January 1901", "%d %B %Y")
    enddate = datetime.datetime.strptime("31 December 2000", "%d %B %Y")
    print(startdate)
    print(enddate)
    while startdate < enddate:
        #check the day of week
        if 6 == datetime.datetime.weekday(startdate):
            count = count + 1
        startdate = startdate + relativedelta(months=+1)
        print(startdate)

    #counting over
    print(count)