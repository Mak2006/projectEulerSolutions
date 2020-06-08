import pandas as pd
import numpy as np

def  factorize(target):
    fac = pd.Series([2]) # these are the factors

    #target = 600851475143
    #target = 40 say

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
    #lf = largest factor available till now  = the answer for our question.
    lf = fac[0] # we start with the first number

    while lf != target:
        #divide target by lf # lf * t = target
        quo = target//lf
        rem = target%lf
        if rem == 0:
            if quo == target: # means lf = 1
                lf = lf + 1
            else:
                #current lf is again a factor
                #so remove target, append lf and t to factors
                leng = len(fac)
                #fac = fac.drop(leng - 1)
                fac[leng - 1] = lf
                fac[leng] = quo
                #print(fac)
                target = quo
        else:
            lf = lf + 1 # hope this is our next factor
        print(lf)
    return fac

if __name__ == '__main__':
    # 600851475143 is the given numeber and it sis quit ebig to be factorized without
    # improvisation,hence moving on to a more optimised method
    s = factorize(851475143)
    print(s);
