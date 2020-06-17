
import eulerlib.mathlib as ml

if __name__ == '__main__':
    ml.DEBUG = True

    fib = ml.getFibonaci(10) # some arbit limit

    # require a new function.


    numdigits = 0
    a = 1
    b = 1
    i = 0
    while numdigits != 1000:
        c = a + b
        a = b
        b = c
        print(c)
        #fib.append(nxt) no need to store
        numdigits = len(str(abs(c)))
        i = i + 1
    ml.dprint(numdigits, i, c)

    print("index is " +str(i + 2)) # as i did not count the first two num
