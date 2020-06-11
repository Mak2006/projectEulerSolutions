# this is a combinatorial problem
# this is equal to 40!/20!20!
from math import factorial

import eulerlib.mathlib as ml
if __name__ == '__main__':
    f40 = factorial(40)
    f20 = factorial(20)
    print(f40/(f20*f20))