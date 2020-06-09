# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
#
# a2 + b2 = c2
# For example, 32 + 42 = 9 + 16 = 25 = 52.
#
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.

#Solving for a and b we got a*b -1*1000*(a+b) + 500000
#we plug numbers and get a and b


def find():
    limit = 1000;

    for a in range(1, limit):
        for b in range (1, limit):
            if (a*b -1*1000*(a+b) + 500000) == 0 : # b -0.002*a*b == 1000):
                #we got our numbers
                #print("a ={} \t b = {}".format(a, b))
                print("a={} \t b={} \t c={} \t abc={}".format(a, b, (1000 - a -b), a*b*(1000-a-b)))


if __name__ == '__main__':
    k = 3710728753390210279879799822083759024651013574025037107287533902102798797998220837590246510135740250
    m = 37107287533902102798797998220837590246510135740250
    print(18*k + m)
    find()