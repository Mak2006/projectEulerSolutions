# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
#
# Find the sum of all the multiples of 3 or 5 below 1000.

# Solved initially using jupyter, here are the py files

import pandas as pd

def find():
    ser = pd.Series([0])
    len(ser)
    limit = 1000
    for i in range(limit):
        if  i%3==0 or i%5==0:
            index = len(ser)
            ser[index] = i
        #print(i)

    ser

    print(ser.sum())


if __name__ == '__main__':
    find()