#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for x in range(len(matrix)):
        for y in range(len(matrix[0])):
            print('{:d}'.format(matrix[x][y]), end='')
            if y + 1 < len(matrix[0]):
                print(' ', end='')
        print()
