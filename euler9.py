# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
#
# a2 + b2 = c2
# For example, 32 + 42 = 9 + 16 = 25 = 52.
#
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.

#Solving for a and b we got a + b -0.002ab = 1000.
#we plug numbers and get a and b


def find():
    limit = 2000;
    for a in range(1, limit):
        for b in range (1, limit):
            if(a + b -0.002*a*b == 1000):
                #we got our numbers
                #print("a ={} \t b = {}".format(a, b))
                print("{} \t {}".format(a, b))


if __name__ == '__main__':
    find()