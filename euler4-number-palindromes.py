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

# Looks like it will take good time, have to find a numerical function.
# well it ran sort of ok for 3 digits, this has room for optimization
def ispalindrome(num):
    snum = str(num)
    ispalin = False
    if (len(snum) == 0):
        return True
    else:
        if int(snum[0]) == int(snum[len(snum) - 1]):
            snum = snum[1: len(snum) - 1]
            ispalin = ispalindrome(snum)
        else:
            ispalin = False;

    return ispalin


# stiching the n
def find(n):
    pds = 0
    r = 10 ** (n - 1)  # gives the lowest number of n digits
    for i in range(r, r * 10):
        for j in range(r, r * 10):
            num = i * j;
            if (pds < num):
                # so we are now only checking greater numbers.
                if (ispalindrome(num)):
                    print("i {} j {} num{} ".format(i,j,num))
                    # print(".", end='')  # a pointer so that we know the prog has not hanged
                    # pds.append(num) # gues we don not need to retain the palindrome
                    # in that way we do not need to sort as well.
                    pds = num;  # retain the latest large number

    return pds


if __name__ == '__main__':
    # get n where n is the numbre of digits.
    print("We are after 2 numbers each of n digits which will give a palindrome")
    print("Enter the number of digits n")
    n = int(input())
    palins = find(n);
    print(palins)

    # Testing palindrome
    # print(ispalindrome(101));
    # print(ispalindrome(10));
    # print(ispalindrome(0));
    # print(ispalindrome(10001));
    # print(ispalindrome(151));
    # print(ispalindrome(1013));
