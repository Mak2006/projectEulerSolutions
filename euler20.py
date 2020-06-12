

# taking code form euler 16

from math import factorial

if __name__ == '__main__':
    val = factorial(100)
    sval = str(val)
    res = 0
    for i in range(0, len(sval)):
        res = res + int(sval[i])

    print("res is " +str(res) + " the num is " + sval)