# reusing problem

import eulerlib.mathlib as ml

import pandas as pd


def file_read(fname):
    arr = []
    with open(fname) as f:
        for line in f:
            strlin = line.strip("\n").split(" ")
            line = [int(i) for i in strlin]
            arr.append(line)
    return arr


if __name__ == '__main__':

    ml.DEBUG = True

    # load the text data
    arr = file_read("p067_triangle.txt")
    print(arr)

    maxpath = ml.get_max_path(arr)
    ml.dprint("Maximum path is ", maxpath)
