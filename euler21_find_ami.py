# Amicalble numbers
# looks like a candidate for mathlib
import eulerlib.mathlib as ml

if __name__ == '__main__':
    ml.DEBUG = True
    # print(ml.isamicable(220))
    ans = 0
    limit = 10000
    for i in range(1, limit + 1):

        flag, n, m = ml.isamicable(i)

        # this addition is all the pairs below 10000 and their sum
        # that is not what is asked for
        if flag:
            if n < limit and m < limit:
                ans = ans + n + m
                print("got ami i {}, ans {}, n {}, m {} ".format(i, ans, n, m))

    # Now everything was counted twice
    ans = ans/2
# 753256
        #What is asked is find all ami <10000, (unsaid is - their pair can be > 10000)
        # get their sum.
        # if flag:
        #     ans = ans + i
#542706
    print("Sum of all amicalbel is " + str(int(ans)))
