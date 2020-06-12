import pandas as pd
import numpy as np

# This library uses pandas series to compute various elements
global DEBUG


def dprint(*args):
    if (DEBUG):
        print(args)


def iamalive(i, processed):
    if (i % processed == 0):
        print("I am alive ", i)


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

# Gives the prime factors only.
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

# returns all the divisors of a  num, and proper divisors
def getdivisors(n):
    first = 1
    last = n
    seq = [first, last]
    firstindex = 1
    while first < (last -1)/2:
        #get the next num
        first = first + 1
        q , r = divmod(n, first)
        #dprint("first {}, last {}".format(first, last))
        if r == 0:
            seq.insert(firstindex, first)
            seq.insert(firstindex + 1, q)
            #print(seq)
            last = q
            firstindex = firstindex + 1

        # if(first > n + 100 ):
        #     return seq
    leng = len(seq)
    return seq, seq[0:leng-1]




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
            # print("found a prime " + str(num))
            fac[len(fac)] = num
    return fac


# performance
# 0.0006874 per prime for 2000

def getprimes_lessthan(n):
    fac = pd.Series([2])  # we just put the frist prime.
    if n <= 1:
        return fac

    num = fac[len(fac) - 1]  # the last num we got
    while num < n:  # till our number is < than n
        # get the next number k
        # if any of the numbers in fac divides k exclude k.
        # else add k to fac
        # loop over
        num = num + 1  # the next number
        divides = check(fac, num)
        if not divides:
            print("found a prime " + str(num))
            fac[len(fac)] = num
    return fac


# perform - much better using just [] rather than pandas
# 3.998041152954101e-06 / prime for 2000 prime
# 0.0002474347138404846 / prime for 200000
# speed = 3.5189390182495115e-06 / prime 2000
# speed = 2.500176429748535e-06 / prime for k 2000 numbers
# speed = 7.669986963272094e-05 / prime for k 100000 numbers
# speed = 0.0003510916748046875 / prime for k 500000 numbers
# the output for 2000000 did not show the time, probably buffer was cleared, the oupt ut is stored as a file. it
# was hopelessly slwo - another candidate to optimize - tooke around 25 mins to compute
def getprimes_lessthan_array(n):
    sum = 5
    fac = [2, 3]  # we just put the frist prime.
    if n <= 1:
        return fac

    num = fac[len(fac) - 1]  # the last num we got
    while num < n:  # till our number is < than n
        # get the next number k
        # if any of the numbers in fac divides k exclude k.
        # else add k to fac
        # loop over
        num = num + 2  # certainly next num is even so we can increment by 2
        divides = check(fac, num)
        if not divides:
            # print("found a prime " + str(num))
            fac.append(num)
            sum = sum + num  # keep the sum as well
        # to see am alive
        if (num % 10000 == 1):
            print(num)
    return fac, sum


def check(fac, num):
    k = len(fac)
    for i in range(1, k):  # 1 becuase we dont need check with 2
        # print("num {}, fac[i] {}".format(num, fac[i]))
        if num % fac[i] == 0:
            # this is a composite
            # print("am here")
            return True  # return on first occurance
    return False  # if we have come thus far , it means none of the exisitn nums, in fac were able to divide the new number, henc it is a prime.


# Method finds sequence of characters, numbers from input which is of interest.
# inp_seq is the input sequence of strings or numbers in which we are interested.
# length is the length of the chunk in which we are interested
# compare_op is the method we shall use to compare
# seq is a starting sequence to compare with
def findseq(start_seq, inpseq, length, compare_op):
    sequ = start_seq
    dprint("findseq inp: ", inpseq)
    while len(inpseq) >= length:
        nextseq = inpseq[0:length]
        dprint("findseq: seq and nextseq ", sequ, nextseq)
        cres = compare(sequ, nextseq, compare_op)
        if (not cres):
            # we got a better seq
            sequ = nextseq
        # reduce inp_seq
        inpseq = inpseq[1:len(inpseq)]

    return sequ


# the comparision using the compare opeation
# as yet compare does not cache the calculation between invocation.
def compare(seq, nextseq, method):
    # just get the mul of the numebrs within the sequence and compare
    # 12313 , 33441 1+2+3+1+3 vs 3 + 3+4 +4 +1
    # say True or False.
    sa = method(seq)
    sna = method(nextseq)
    dprint("compare", sa, sna)
    if (sa >= sna):
        return True
    else:
        return False


# definition of the compare operation
def compare_op_mul(seq):
    lenght = len(seq)
    res = 1.0  # using float to compare as int is overflowing
    for i in range(0, lenght):
        dprint("compare_op_mul: ", seq[i], res)
        res = res * seq[i]
    return res


def generate_n_trianglular_num(n):
    seq = []

    for i in range(0, n):
        s = (i + 1) * (i + 2) / 2  # as index is 0
        seq.append(int(s))

    dprint(seq)
    return seq


# start generating from x and include n more triagular numbers
def generate_n_trianglular_num_afterx(x, n):
    seq = []

    for i in range(x, x + n):
        s = (i + 1) * (i + 2) / 2  # as index is 0
        seq.append(int(s))

    dprint(seq)
    print("last triagular number is " + str(s))
    return seq


# generate collatz sequence
def generate_collatz_seq(n):
    # n → n / 2(n is even)
    # n → 3n + 1(n is odd)
    seq = [n]
    while n > 1:
        if(n % 2 == 0):
            n = n/2
        else:
            n = 3*n + 1
        seq.append(int(n))
    length = len(seq)

    return seq, length


#is this number amicable
#returns false or
#returns true, other amicale number

def isamicable(n):

    _, divs_of_n = getdivisors(n)

    othernum = np.sum(divs_of_n)

    _, divs_of_othernum = getdivisors(othernum)

    num2 = np.sum(divs_of_othernum)
    if(n == num2  & n != othernum ):
        dprint("Ami pair found", n,  othernum)
        return True, n, othernum
    else:
        return False, None, None