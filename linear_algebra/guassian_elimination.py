from matrix import Matrix, matrix
from argumented_matrix import ArgumentedMatrix
from collections import Counter

def order(A):
    """Orders rows (the upper rows have the leftmost pivot). 
    All rows (if any) with zeoros are grouped at the bottom"
    """

    def count_first_zeros(row):
        """Counts how many zeros are there before we find a nonzero number"""
        
        # initialize count at 0
        count = 0;
        
        for i in range(len(row)): # go through the row elements
            if row[i] == 0:
                # when we find zero we increment
                count += 1
            else:
                # when we find the first nonzero number we break the loop
                break
        
        return count
    
    if isinstance(A, Matrix):
        matrix_array = A.matrix
    elif isinstance(A, ArgumentedMatrix):
        # order according to the left matrix
        matrix_array = A.left.matrix
    else:
        raise Exception(f"argument must be of type Matrix or ArgumentedMatrix not {type(A)}")

    # count number of first zeros in each row
    counts = list(map(count_first_zeros, matrix_array))
    # sort according to count
    counts_with_index_sorted = sorted([(count, index) for index, count in enumerate(counts)])
    
    if isinstance(A, Matrix):
        ordered_matrix = []
        for count, index in counts_with_index_sorted:
            ordered_matrix.append(matrix_array[index])
        
        return Matrix(ordered_matrix)
    # Else
    left = []; right = []
    for count, index in counts_with_index_sorted:
        left.append(matrix_array[index])
        right.append(A.right.matrix[index])

    return ArgumentedMatrix(Matrix(left), Matrix(right))

def row_echelon(A):
    """Returns the row echolon form of a matrix."""




def reduced_row_echelon(A):
    """Returns the reduced row echelon form of a matrix."""

    pass


def main():
    A = Matrix([[0,1,3],[0,0,0],[1,0,2]])
    B = Matrix([[1],[-3],[0]])

    C = ArgumentedMatrix(A,B)

    print(order(A))
    print(order(B))

    print("",A,B,sep="\n\n",end="\n\n")

    print(order(C))

if __name__ == "__main__":
    main()

