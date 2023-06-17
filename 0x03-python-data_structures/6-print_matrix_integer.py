#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            if col != len(matrix[row]) - 1:
                print("{}".format(matrix[row][col]), end=' ')
            else:
                print("{}".format(matrix[row][col]), end='')
        print()
