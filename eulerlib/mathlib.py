import pandas as pd


# This library uses pandas series to compute various elements

# get fibonacci series below a certain limit.
def getFibonaci(limit):
    s = pd.Series([1, 2])  # has the first two
    for i in range(limit):
        length = len(s)
        # print(length)
        j = s[length - 1] + s[length - 2]
        if j > limit:
            return s
        else:
            s[length] = j
    return s


def factorize(target):
    # target = 600851475143
    # target = 40 say

    # Initial thinking
    # start = 2 # 2*m=t
    # divide the target by star, remainder stored in factors. # space is reduced by 2 to m
    # start++ = k1 is the next number
    # check if start divides the number m
    # if yes
    #     store k1 # k1*f1 = m , store k1 and f1, remove m
    # else
    #     start++
    #     if start = m, bail out.

    # pseudo algo
    # fac = a panda series, which will have the factors.
    # we start with fac set to 1 and target as the target number. So it has 2 numbers
    # fac = [lf, target]
    # # these two number also search as our search space.
    # lf = largest factor available till now  = the answer for our question.
    # lf = fac[1] # we start with the first number

    # while lf != target do
    #     divide target by lf # lf * t = target
    #     if no remainder
    #         if t == target # means lf = 1
    #             lf++
    #         else
    #             #current lf is again a factor
    #             so remove target, append lf and t to factors
    #     else
    #         lf ++ # hope this is our next factor

    # Implementation
    # these two number also search as our search space.
    fac = pd.Series([1, target])
    # lf = largest factor available till now  = the answer for our question.
    lf = fac[0]  # we start with the first number

    while lf != target:
        # divide target by lf # lf * t = target
        quo = target // lf
        rem = target % lf
        if rem == 0:
            if quo == target:  # means lf = 1
                lf = lf + 1
            else:
                # current lf is again a factor
                # so remove target, append lf and t to factors
                leng = len(fac)
                # fac = fac.drop(leng - 1)
                fac[leng - 1] = lf
                fac[leng] = quo
                # print(fac)
                target = quo
        else:
            lf = lf + 1  # hope this is our next factor
        # print(lf)
    return fac


# method returns n primes
def getprime(n):
    fac = pd.Series([2])  # we just put the frist prime.
    if n == 1:
        return fac

    num = fac[len(fac) - 1]  # the last num we got
    while len(fac) < n + 1:  # untill so many primes are found
        # get the next number k
        # if any of the numbers in fac divides k exclude k.
        # else add k to fac
        # loop over
        num = num + 1  # the next number
        divides = check(fac, num)
        if not divides:
            #print("found a prime " + str(num))
            fac[len(fac)] = num
    return fac


def check(fac, num):
    for i in range(1, len(fac)):
        if num % fac[i] == 0:
            # this is a composite
            return True
    return False  # if we have come thus far , it means none of the exisitn nums, in fac were able to divide the new number, henc it is a prime.