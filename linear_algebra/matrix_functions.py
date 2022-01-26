from linear_algebra.matrix import Matrix

def transpose(matrix):
    if isinstance(matrix, Matrix):
        return matrix.transpose()
    return None

def constant(k, nrows, ncols):
    array = [[k for j in range(ncols)] for i in range(nrows)]]
    return Matrix(array)

def zeros(nrows, ncols):
    return constant(0, nrows, ncols)

def ones(nrows, ncols):
    return constant(1, nrows, ncols)

def diag(matrix):

    if isinstance(matrix, Matrix):
        if matrix.is_square():
            n = matrix.p
            array = zeros(n, n)

            for i in range(n):
                array[i][i] == 1

            return Matrix(array)
            
def inverse(matrix):
    pass
