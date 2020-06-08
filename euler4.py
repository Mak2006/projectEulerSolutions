# find the largest palindrome made out of the product of two n digit number

# Problem cited 3 , and our challeng is to solve for any digits.

# brute force to begin with. will result in n squared complexity

##
# Algo
# take the largest numebr of n digits
# find the next lowest palindrome (this would be ok )
# find the factors and check if they are of k digit (this would be hard, as factorization is hard)
#   1. find all the factors
#   2. multiple them in combinations?
#   3. do something more etc (not sure)
# Algo 2
# initial idea - go from n2 n x n numbers , two for loops and check if the number is palindrome
# for i = 100 to 999
#   for j = 100 to 999
#     candidate = i*j
#     check if can is palindrome
#     save it
# get the last#
# ,


def ispalindrome(num):
    snum = str(num)
    ispalin = False
    if (len(snum) == 0):
        return True
    else:
        if int(snum[0]) == int(snum[len(snum) - 1]):
            # remove the numbers
            snum = snum[1: len(snum) - 1]
            ispalin = ispalindrome(snum)
        else:
            ispalin = False;

    return ispalin


def find():
    pds = []
    for i in range(100, 1000):
        for j in range(100, 1000):
            num = i * j;
            if (ispalindrome(num)):
                pds.append(num)
    return (pds[len(pds)])


if __name__ == '__main__':
    # get n
    # n = int(input())
    # find()

    # Testing palindrome
    # print(ispalindrome(101));
    # print(ispalindrome(10));
    # print(ispalindrome(0));
    # print(ispalindrome(10001));
    # print(ispalindrome(151));
    # print(ispalindrome(1013));
