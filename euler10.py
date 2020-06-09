import eulerlib.mathlib as ml

if __name__ == '__main__':
    k = ml.factorize(1200)
    print(k)

    primelist = ml.getprime(1000)
    print(primelist.sum())