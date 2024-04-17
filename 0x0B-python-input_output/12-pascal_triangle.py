#!/usr/bin/python3
"""
12-pascal_triangle module
"""

def pascal_triangle(n):
    """
    Returns a list of integers representing Pascal's triangle.
    Args:
        n: (integer): 
    Return:
        A list of lists of integers.
    """
    if n <= 0:
        return ([])
    pascal_list = []
    for i in range(1, n + 1):
        row_list = []
        m = 1
        for j in range(1, i + 1):
            row_list.append(m)
            m = int(m * (i - j) / j)
        pascal_list.append(row_list)
    return (pascal_list)
