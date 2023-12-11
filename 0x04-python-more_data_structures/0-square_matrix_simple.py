def square_matrix_simple(matrix=[]):
    new_matrix = []
    for row in matrix:
        for i in row:
            new_matrix.append(i ** 2)
    return (new_matrix)
