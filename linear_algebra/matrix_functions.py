from linear_algebra.matrix import Matrix

def transpose(matrix):

    if isinstance(matrix, Matrix):
        return matrix.transpose()

    return None


