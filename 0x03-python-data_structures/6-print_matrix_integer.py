#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    row = len(matrix)
    for row in matrix:
        N_col = len(row) - 1
        x = 0
        for col in row:
            if N_col == x:
                print("{}".format(col))
            else:
                print("{} ".format(col), end = '')
            x += 1
