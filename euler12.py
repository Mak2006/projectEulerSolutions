# Euler problem 12

### Algo
# we create a method to generate the first seq of traigular num
# we use sn = n*(n+1)/2 as the method.
# asda
#

import eulerlib.mathlib as ml


def countdivisors(seq):
    ignore = 0;  # ignroe so many numbers from the stack
    highest_num_of_divisor_found = 0
    for i in range(ignore, len(seq)):
        #ml.dprint("count fac", i)
        num = seq[i]
        fac = ml.getdivisors(num)
        #ml.dprint("There are {} factors which are {} for the num {}".format( len(fac), fac, num))
        num_of_factors = len(fac)
        if num_of_factors > highest_num_of_divisor_found:
            highest_num_of_divisor_found = num_of_factors
            print("max num of divisor found till now is " +str( highest_num_of_divisor_found) + " for num " + str(num))
        # if num_of_factors > 500:
        #     return num

        ml.iamalive(i, 10000);


if __name__ == '__main__':
    ml.DEBUG = True
    seq = ml.generate_n_trianglular_num(100000)
    res = countdivisors(seq)
    print("first Tn with factors > 500 is {}".format(res))

    # k = 40054
    # seq = ml.getdivisors(k)
    # print(seq)