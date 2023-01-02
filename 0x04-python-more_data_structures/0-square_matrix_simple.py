#!/usr/bin/python3


def square_matrix_simple(matrix=[]):
    n_matrix = matrix.copy()
    for row in range(len(matrix)):
        n_matrix[row] = list(map(lambda sqr: sqr**2, matrix[row]))
    
    return (n_matrix)
