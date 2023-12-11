def square_matrix_simple(matrix=[]):
    outer_matrix = []
    for row in matrix:
        new_list = []
        for i in row:
            new_list.append(i ** 2)
        outer_matrix.append(new_list)
    return (outer_matrix)
