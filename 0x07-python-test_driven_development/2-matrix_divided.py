#!/usr/bin/python3
"""Matrix division module.
This module divides matrix elements by a specified divisor.
"""


def matrix_divided(matrix, div):
    """Divides all elements of a matrix.
    Args:
        matrix (list of list, int, float): Matrix.
        div (int, float): Divisor.
    Raises:
        TypeError: if matrix arg is not a list of lists of integers or floats,
                    if rows of matrix are not of same size,
                    if div arg is not a number.
        ZeroDivisionError: if div arg is 0
    Returns:
        A new matrix whose elements have been divided by div.
    """
    if (not isinstance(matrix, list) or
            not all(isinstance(row, list) for row in matrix) or
            not all(isinstance(num, (int, float)) for row in matrix
                    for num in row)):
        err = "matrix must be a matrix (list of lists) of integers floats"
        raise TypeError(err)
    if len(set(len(row) for row in matrix)) != 1:
        raise TypeError("Each row of the matrix must have the same size")
    if type(div) not in [int, float]:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    new_matrix = []
    for row in matrix:
        temp_matrix = []
        for num in row:
            temp_matrix.append(round(num/div, 2))
        new_matrix.append(temp_matrix)
    return new_matrix
