from builtins import int

import eulerlib.mathlib as ml


def get_longest_collatz(max_limit):
    seq = []
    largestseq = []
    maxlength = 0
    for i in range(1, max_limit):
        seq, length = ml.generate_collatz_seq(i)
        if (maxlength < length):
            maxlength = length
            largestseq = seq
            print("Max length breach num ={} lenght = {}".format(i, maxlength))
    return largestseq, maxlength

if __name__ == '__main__':
    ml.DEBUG = False
    num = 1000
    # seq = ml.generate_collatz_seq(num)
    # ml.dprint(seq)

    #max limig
    max_limit = 999999
    longestseq, length = get_longest_collatz(max_limit)
    print("Ans" , length)