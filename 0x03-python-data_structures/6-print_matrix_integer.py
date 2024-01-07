#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for j in row[:-1]:
            print("{}".format(j), end=' ')
        if row:
            print("{}".format(row[-1]))
        else:
            print()
