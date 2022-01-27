from matrix import Matrix
from matrix_functions import identity as I

def row_swap(row1, row2, n):
    I_matrix = I(n).matrix

    temp = I_matrix[row1]
    I_matrix[row1] = I_matrix[row2]
    I_matrix[row2] = temp

    return Matrix(I_matrix)

def scalar_mul(row, alpha, n):
    I_matrix = I(n).matrix
    I_matrix[row] = list(map(lambda x: alpha * x, I_matrix[row]))
    return Matrix(I_matrix)

def row_sum(row1, row2, alpha, n):
    I_matrix = I(n).matrix
    I_matrix[row1][row2] = alpha
    return Matrix(I_matrix)

print(row_sum(0,1, 2, 4))
