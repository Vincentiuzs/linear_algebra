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


def matrixToArray(A):
    if isinstance(A, Matrix):
        return A.matrix
    if isinstance(B, ArgumentedMatrix):
        return A.left.matrix

def all_pivots_to_right(A):
    array = matrixToArray(A)

    # copy contents to another variable: avoid passing by reference
    temp = array.copy()
    
    pivots = []

    for i in range(len(matrix_array)):
        for j in range(len(matrix_array[0])):
            pivot = temp[i].pop(0)
            if temp == [] or pivot != 0:
                pivots.append(j)
                break

    for i in range(len(pivots)):
        if i == 0:
            pass
        else:
            if pivots[i] <= pivots[i-1]:
                return False, i, pivots[i]
            return True, None, None

def row_echelon(A):
    """Returns the row echolon form of a matrix."""
    A = order(A)
    
    
    find_matrix = lambda x: x.matrix if isinstance(x, Matrix) else x.left.matrix
    matrix_array = find_matrix(A)
    
    true, row, col = are_pivots_to_right(A)
    print(matrix_array)
    while not true:
        # R1:  4 8 -8
        # R2: -3 2 0       quotient=-3/4 
        # =============================
        # R2 = R2 - (-3/4) * R1
        # R1: 4 2 3
        # R2: 0 8 -6
        r1_pivot = matrix_array[row][col] 
        r2_pivot = matrix_array[row-1][col]
        
        print(matrix_array)
        quotient = r1_pivot / r2_pivot

        if (r1_pivot > 0 and r2_pivot > 0) or (r1_pivot < 0 and r2_pivot < 0) or r2_pivot < 0:
            quotient = -1 * quotient
        else: # r1_pivot < 0:
            quotient = abs(quotient)

        new_row = [r1_i + quotient * r2_i for r1_i, r2_i in zip(matrix_array[row], matrix_array[row-1])]
        matrix_array[row] = new_row

        if isinstance(A, ArgumentedMatrix):
            left = A.left.matrix
            left[row] = [r1_i - quotient * r2_i for r1_i, r2_i in zip(left[row], left[row-1])]
            A = order(ArgumentedMatrix(Matrix(matrix_array),Matrix(left)))
        else:
            A = order(Matrix(matrix_array))

        true, row, col = are_pivots_to_right(A)
        matrix_array = find_matrix(A)

    return A
def reduced_row_echelon(A):
    """Returns the reduced row echelon form of a matrix."""

    pass


def main():
    A = Matrix([[1,3,1,3],[0,4,2,0],[1,0,2,3]])
    B = Matrix([[1],[-3],[0]])

    C = ArgumentedMatrix(A,B)

    print(C)
    print()
    #print(order(A))
    #print(order(B))

    #print("",A,B,sep="\n\n",end="\n\n")

    print(row_echelon(C))

if __name__ == "__main__":
    main()

