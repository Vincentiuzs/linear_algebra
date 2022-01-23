from linear_algebra.matrix import Matrix

class ArgumentedMatrix:

    def __init__(self, matrix1, matrix2):

        if len(list(map(lambda x: isinstance(x, Matrix), [matrix1, matrix2]))):
            pass

        else:
            raise Exception("both arguments of ArgumentedMatrix must be of type Matrix")
