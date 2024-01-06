#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        new_matrix = ' '.join(map(str, row))
        print("{}".format(new_matrix))
