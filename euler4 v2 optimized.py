# find the largest palindrome made out of the product of two n digit number

# Problem cited 3 , and our challeng is to solve for any digits.

# **** Here we optimize so that we do not start checking from the bottom rather go on the top.
# other optimization possible is in palindrome chek and multiplication.
# this runs sort of fine till 7 digits
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
    r = 10 ** (n) - 1   # gives the highest number of n digits
    rlow = 10 ** (n-1)  # gives the lowese number of n digits
    for i in range(r, rlow, -1):
        for j in range(r, rlow, -1):
            num = i * j;
            if (ispalindrome(num)):
                print("i {} j {} num{} ".format(i,j,num))
                # We have got our first palindromes and it wiil be the largest.
                return num


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
