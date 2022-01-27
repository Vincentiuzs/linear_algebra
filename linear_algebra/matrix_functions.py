from matrix import Matrix

def transpose(matrix):
    if isinstance(matrix, Matrix):
        return matrix.transpose()
    return None

def constant(k, nrows, ncols):
    array = [[k for j in range(ncols)] for i in range(nrows)]
    return Matrix(array)

def zeros(nrows, ncols):
    return constant(0, nrows, ncols)

def ones(nrows, ncols):
    return constant(1, nrows, ncols)

def diagonal(matrix):

    if isinstance(matrix, Matrix):
        if matrix.is_square():
            n = matrix.p
            array = zeros(n, n).matrix

            for i in range(n):
                array[i][i] = matrix[i, i]

            return Matrix(array)

def diag(*elements):

    n = len(elements)
    array = zeros(n, n).matrix
    for i in range(n):
        array[i][i] = elements[i]
    
    return Matrix(array)

def identity(n):
    return diag(*[1 for i in range(n)])

def inverse(matrix):
    pass

print (identity(12))

