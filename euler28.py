#Number spiral diagonals

# Algo we can analyse to find the pattern. the center right diagonal is odd n square, like
# 1, 9 , 25 ...
 # simlarly we find the patter for all others

# center up right = odd natural number squared - 1, 9, 25
# center up left = center-up-right_i - (natural num - 1)
# center down left = center up left_i - (natural num - 1)
# center down right = center down left_i - (natural num - 1)

# these 4 sequences gives us all the numbers
# sum all to get the answer.
# 1 in the middle is counted 4 times
# so minus 3.
# the analysis was done in the jpg euler28analysis.jpg
#

import eulerlib.mathlib as ml


if __name__ == '__main__':
    ml.DEBUG = True
    limit = 500 # we have to run till 500 as (1001-1)/2
    su = 1
    for i in range(1, limit+1):
        su = su + 4 * (2 * i + 1) ** 2 - 12 * i

    print("Required sum " + str(su))
