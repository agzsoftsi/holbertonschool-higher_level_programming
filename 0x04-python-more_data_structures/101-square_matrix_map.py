#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    return list(map(lambda num1: list(map(lambda num2: num2**2, num1)), matrix))
