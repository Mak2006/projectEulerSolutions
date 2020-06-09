import eulerlib.mathlib as ml

# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
#
# Find the sum of all the primes below two million.
#
#I think 2 mil is 2 000 000

if __name__ == '__main__':
    # k = ml.factorize(1200)
    # print(k)

    import cProfile
    import profile

    #cProfile.run('ml.getprimes_lessthan(2000)')
    #profile.run('ml.getprimes_lessthan(2000); print')
    #time =
    k = 2000000
    import time

    start_time = time.time()
    #primelist = ml.getprimes_lessthan(k)
    primelist, sum = ml.getprimes_lessthan_array(k)
    end_time = time.time()
    tot_time = end_time - start_time

    print("# speed = {} / prime for k {} numbers, total time {} sec".format(tot_time/k, k, tot_time))
    print(primelist)
    print("sum is {}".format(sum))
    #print(primelist.sum())