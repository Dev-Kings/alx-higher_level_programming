#!/usr/bin/python3
"""Matrix dot product module."""


def matrix_mul(m_a, m_b):
    """Multiplies 2 matrices.
    Args:
        m_a (list of list, int, float): Matrix a elements.
        ma_b (list of list, int, float): Matrix b elements.
    Raises:
        TypeError: if m_a or m_b is not a list,
                    if m_a or m_b is not a list of lists,
                    if one element of the list of list is not an integer or
                        float,
                    if m_a or m_b is not a rectangle.
        ValueError: if m_a or m_b is empty,
                    if m_a or m_b can't be multiplied.
        Returns:
            Dot product of matrix multiplication.
    """
    list_set = set()
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")
    for a_row in m_a:
        list_set.add(isinstance(a_row, list))
    if (False in list_set):
        raise TypeError("m_a must be a list of lists")
    for b_row in m_b:
        list_set.add(isinstance(b_row, list))
    if (False in list_set):
        raise TypeError("m_b must be a list of lists")
    for a_row in m_a:
        list_set.add(len(a_row) > 0)
    if (False in list_set):
        raise ValueError("m_a can't be empty")
    for b_row in m_b:
        list_set.add(len(b_row) > 0)
    if (False in list_set):
        raise ValueError("m_b can't be empty")
    for a_row in m_a:
        for i in a_row:
            list_set.add(type(i) in (int, float))
    if (False in list_set):
        raise TypeError("m_a should contain only integers or floats")
    for b_row in m_b:
        for lx in b_row:
            list_set.add(type(lx) in (int, float))
    if (False in list_set):
        raise TypeError("m_b should contain only integers or floats")
    row_set = set()
    for a_row in m_a:
        row_set.add(len(a_row))
    if len(row_set) != 1:
        raise TypeError("each row of m_a must be of the same size")
    row_set.clear()
    for b_row in m_b:
        row_set.add(len(b_row))
    if len(row_set) != 1:
        raise TypeError("each row of m_b must be of the same size")
    row_set.clear()

    result_mat = [[0 for h in range(len(m_b[0]))] for h in range(len(m_a))]

    try:
        for i in range(len(m_a)):
            for j in range(len(m_b[0])):
                for k in range(len(m_b)):
                    result_mat[i][j] += m_a[i][k] * m_b[k][j]
    except Exception:
        raise ValueError("m_a and m_b can't be multiplied")
    return (result_mat)
