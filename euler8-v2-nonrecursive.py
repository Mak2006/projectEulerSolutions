# The four adjacent digits in the 1000-digit number that have the greatest product are 9 × 9 × 8 × 9 = 5832.
#
# 73167176531330624919225119674426574742355349194934
# 96983520312774506326239578318016984801869478851843
# 85861560789112949495459501737958331952853208805511
# 12540698747158523863050715693290963295227443043557
# 66896648950445244523161731856403098711121722383113
# 62229893423380308135336276614282806444486645238749
# 30358907296290491560440772390713810515859307960866
# 70172427121883998797908792274921901699720888093776
# 65727333001053367881220235421809751254540594752243
# 52584907711670556013604839586446706324415722155397
# 53697817977846174064955149290862569321978468622482
# 83972241375657056057490261407972968652414535100474
# 82166370484403199890008895243450658541227588666881
# 16427171479924442928230863465674813919123162824586
# 17866458359124566529476545682848912883142607690042
# 24219022671055626321111109370544217506941658960408
# 07198403850962455444362981230987879927244284909188
# 84580156166097919133875499200524063689912560717606
# 05886116467109405077541002256983155200055935729725
# 71636269561882670428252483600823257530420752963450
#
# Find the thirteen adjacent digits in the 1000-digit number that have the greatest product. What is the value of this product?

# Algo 1
# The number is given, this is a good candidate for map reduce,
# where in we chunk the given 1000 numbe in 13 digits and compute the product of all and then compare.
# However, this does not use maths so we do algo 2

## Algo 2 '
# here we make use of th fact that all are single digits
# instead of multiplying , we add, if the add sum is greated, the mul will be greater.

# so we take the first 13 seq and cal the sum.  = s1
# get the next 13 seq and cal the sum = s2
# if s2 > s1, we retain s2 and the seq is our seq. we do this untill the seq is exhausted.

def break_num(num, length):
    pass


def mul(seq):
    res = 1
    for i in range(0, len(seq)):
        res = res * int(seq[i])
        print("i {} res {} ".format(i, res))
    return res


def add(seq):
    res = 0
    for i in range(0, len(seq)):
        res = res + int(seq[i])
    return res


# compares seq and nextseq and return true if the digits sum of seq is > then that of nextseq
def compare(seq, nextseq):
    # just get the sum of the numebrs within the sequence and compare
    # 12313 , 33441 1+2+3+1+3 vs 3 + 3+4 +4 +1
    # say True or False.
    sa = mul(seq)
    sna = mul(nextseq)
    if (sa >= sna):
        return True
    else:
        return False


# Returns the needed seq
def findseq(seq, num, length):
    # seq is the existing list which holds the best answer we have.
    # num is the number
    # length is the chunks to be be broken into.
    # chunks = break_num(num, length) do noth think it will be a good idea to store the chunks

    # and we use recursion
    # we introduce a seq variable which holds the last useful seq.
    # we change the invoke in main and pass an empty []
    # we assume the next sequence to be taken starts from the first char of num
    while len(num) >= length:
        nextseq = num[0:length]
        print("next seq " + str(nextseq))
        cres = compare(seq, nextseq)
        if (not cres):
            # we got a better seq
            seq = nextseq
        #reduce num
        num = num[1:len(num)]

    return seq
    # if (len(num) >= length):
    #     nextseq = num[0:length ]  # get the first sequen of length chars
    # else:
    #     # no more chunks exists and seq is the required seq
    #     return seq

    # at this time more exists
    # print("next seq " + str(nextseq))

    # now we require a comparator
    # returns true if seq > nextseq as per the compare function.
    # cres = compare(seq, nextseq)
    # if (cres):
    #     # this is the reduction step.
    #     # knock of the first digit and call recurse
    #     num = num[1:len(num)]
    #
    # else:
    #     seq = nextseq  # as nextseq is greater
    #
    # # go on to compare with more seq
    # seq = findseq(seq, num, length)
    #
    # return seq


if __name__ == '__main__':
    # We probably have to take this num as a string
    num = "7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450"
    #num = "1234135940"  # test num
    seq = []  # this is the seq that is of interest
    # for now we do not knwo what it is
    seq = findseq(seq, num, 13)  # num is the target num and 3 is the chunk size
    print("Seq is " + str(seq))
    # Now do what we want to do
    res = mul(seq)
    print("Required value " + str(res))
