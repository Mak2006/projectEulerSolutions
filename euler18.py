# [3]
# [7,4]
# [2,4,6]
# [8,5,9,3]

# The algo, we reduce the array with adding the lower layer to the layer above.
# at each point on the row - 1 we check which candidate below gives the largest path and retain that.
# repeat this untill we have a row left and it is hte value.

import eulerlib.mathlib as ml
def getdata():
    # we used text pad to format the data as a array
    a = [
        [3],
        [7, 4],
        [2, 4, 6],
        [8, 5, 9, 3]
    ]

    # edited in text pad and removed leading zeroes
    b = [
        [75],
        [95, 64],
        [17, 47, 82],
        [18, 35, 87, 10],
        [20, 4, 82, 47, 65],
        [19, 1, 23, 75, 3, 34],
        [88, 2, 77, 73, 7, 63, 67],
        [99, 65, 4, 28, 6, 16, 70, 92],
        [41, 41, 26, 56, 83, 40, 80, 70, 33],
        [41, 48, 72, 33, 47, 32, 37, 16, 94, 29],
        [53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14],
        [70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57],
        [91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48],
        [63, 66, 4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31],
        [4, 62, 98, 27, 23, 9, 70, 98, 73, 93, 38, 53, 60, 4, 23]
    ]

    return b



#
def get_max_path(data):
    rowmax = len(data)
    colmax = len(data[rowmax - 1])
    ml.dprint("get_max_path", rowmax, colmax)

    # [3]
    # [7,4]
    # [2,4,6]
    # [8,5,9,3]

    # crow = current row
    for c_row in range(rowmax -2, -1, -1 ): # start from the last - 1 row

        #for each number in this row, check the row below and the same index, index + 1, which is greater.
        row = data[c_row]
        rowbelow = data[c_row+1]
        ml.dprint("processing row, row below", row, rowbelow)
        # iterate over the elements of thw row
        rlen = len(row)
        for c_col in range(0, rlen):
            rowval = row[c_col]
            ml.dprint("item ", rowval)
            leftchoice = rowval + rowbelow[c_col]
            rightchoice = rowval + rowbelow[c_col + 1]
            if(leftchoice >= rightchoice):
                row[c_col] = leftchoice
            else:
                row[c_col] = rightchoice

        # Now a row is done,
        ml.dprint(" row i {} and the val is", c_row, row)
    return row[0]

if __name__ == '__main__':

    ml.DEBUG = True
    data = getdata()
    row = len(data)
    col = len(data[row - 1])

    #ml.dprint(row, col, data[col -1], len(data[col - 1]), data[col - 1][1])

    maxpath = get_max_path(data)
    ml.dprint("Maximum path is ", maxpath)