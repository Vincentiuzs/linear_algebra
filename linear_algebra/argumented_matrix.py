from matrix import Matrix

class ArgumentedMatrix:

    def __init__(self, matrix1, matrix2):

        # check if both matrices are instances of Matrix
        if sum(list(map(lambda x: isinstance(x, Matrix), [matrix1, matrix2]))) == 2:
            
            # check if both matrices havce the same dimensions
            if matrix1.p == matrix2.p:
                self.left  = matrix1
                self.right = matrix2
            else: 
                raise Exception("both arguments of ArgumentedMatrix must have equal number of rows")

        else:
            raise Exception("both arguments of ArgumentedMatrix must be of type Matrix")

    def __repr__(self):

        # function to calculate the longest number in each column
        longest_number = lambda x: [[len(str(x[i,j])) for i in range(x.p)] \
                                    for j in range(x.q)]
    
        # number of spaces to reserve in each column
        left_rsv_spaces  = list(map(max, longest_number(self.left)))
        right_rsv_spaces = list(map(max, longest_number(self.right)))
        
        argmat_string = ""

        for i in range(self.left.p):     # or self.right.p
            for j in range(self.left.q + self.right.q):
                if j < self.left.q - 1:
                    argmat_string += f'{self.left[i, j]:> {left_rsv_spaces[j] + 1}} '
                elif j == self.left.q - 1:
                    argmat_string += f'{self.left[i, j]:> {left_rsv_spaces[j] + 1}} |'
                else:
                    argmat_string += f' {self.right[i, j - self.left.q]:> {right_rsv_spaces[j - self.left.q] + 1}}'
            argmat_string += "\n"

        return argmat_string.strip('\n')

    def merge(self):
        """Returns a ArgumentedMatrix as a Matrix object"""
        rows = []
        for i in range(self.left.p):
            rows.append(self.left.matrix[i] + self.right.matrix[i])
        return Matrix(rows)

def arg_matrix(A, b):
    """Returns ArgumentedMatrix object"""
    return ArgumentedMatrix(A,b)

def unmerge(A, left_ncols):
    """Returns ArgumentedMatrix object"""
    if isinstance(A, Matrix):
        left = []
        right = []
        for i in range(A.p):
            left.append(A.matrix[i][:left_ncols])
            right.append(A.matrix[i][left_ncols:])

        return ArgumentedMatrix(Matrix(left),Matrix(right))

