# [3]
# [7,4]
# [2,4,6]
# [8,5,9,3]
import eulerlib.mathlib as ml
def getdata():
    # we used text pad to format the data as a array
    a = [
        [3],
        [7, 4],
        [2, 4, 6]
     #   [8, 5, 9, 3]
    ]
    return a

if __name__ == '__main__':

    ml.DEBUG = True
    data = getdata()
    row = len(data)
    col = len(data[row - 1])

    #ml.dprint(row, col, data[col -1], len(data[col - 1]), data[col - 1][1])