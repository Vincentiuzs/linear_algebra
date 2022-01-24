from matrix import Matrix, matrix

class ArgumentedMatrix:

    def __init__(self, matrix1, matrix2):

        if sum(list(map(lambda x: isinstance(x, Matrix), [matrix1, matrix2]))) == 2:
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
                    argmat_string += f'{self.left[i, j]: {left_rsv_spaces[j]}} '
                elif j == self.left.q - 1:
                    argmat_string += f'{self.left[i, j]: {left_rsv_spaces[j]}} |'
                else:
                    argmat_string += f' {self.right[i, j - self.left.q]: {right_rsv_spaces[j - self.left.q]}}'

            argmat_string += "\n"

        return argmat_string.strip('\n')


A = matrix(1,0,0,0,0,1,0,1,0,ncols=3,nrows=3)
b = matrix(1,0,0,2,4,5,3,4,4,ncols=3,nrows=3)

arg = ArgumentedMatrix(A,b)

print(arg)


