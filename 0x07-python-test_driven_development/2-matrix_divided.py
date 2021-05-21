#!/usr/bin/python3
"""
    matrix_divided(matrix, div)
    will divide the inter matrix
    returns the divided matrix
"""


def matrix_divided(matrix, div):
    """
        divide matrix
    """

    if type(div) not in [int, float]:
        raise TypeError('div must be a number')

    if div == 0:
        raise ZeroDivisionError("division by zero")

    if type(matrix) is not list:
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats"
            )
    new_matrix = []
    l = -1
    for index, row in enumerate(matrix):
        if type(row) is not list:
            raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats"
                )
        l = len(row) if index == 0 else l
        if len(row) != l:
            raise TypeError("Each row of the matrix must have the same size")
        new_matrix.append([])
        for row_index, value in enumerate(row):
            if type(value) not in [int, float]:
                raise TypeError(
                    "matrix must be a matrix (list of lists)" +
                    " of integers/floats"
                    )
            new_matrix[index].append(round(matrix[index][row_index] / div, 2))

    return new_matrix
