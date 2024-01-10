#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    matrix_copy = []
    for i in matrix:
        square_el = [j**2 for j in i]
        matrix_copy.append(square_el)
    return (matrix_copy)
