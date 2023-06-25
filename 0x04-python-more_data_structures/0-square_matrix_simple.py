#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    if not matrix:
        return
    squared_matrix = matrix[:]
    squared_matrix = [[pow(col, 2) for col in row] for row in squared_matrix]
    return squared_matrix
