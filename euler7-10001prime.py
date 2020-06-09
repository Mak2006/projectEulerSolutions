# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
# 
# What is the 10 001st prime number?


def check(fac, num):
    for i in range (1, len(fac)):
        if num % fac[i] == 0:
            # this is a composite
            return True
    return False     # if we hace come thus far , it means none of the exisitn nums, in fac were able to divide the new number, henc it is a prime.


def getprime(n):
    fac = [2, 3, 5, 7] #we know these, the primes
    num = fac[len(fac) - 1]  # the last num we got
    while len(fac) < n + 1 : # untill so many primes are found
        #get the next number k
        # if any of the numbers in fac divides k exclude k.
        # else add k to fac
        # loop over
        num = num + 1 # the next number
        divides = check(fac, num)
        if divides == False:
            print("found a prime " + str(num))
            fac.append(num)
    return fac



if __name__ == '__main__':
    print("Enter n, program gives the nth prime")
    n = int(input())
    fac = getprime(n)
    print("All primes")
    print(fac)
    print("Largest in the set")
    print(fac[len(fac) - 1])