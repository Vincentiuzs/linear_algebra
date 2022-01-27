from matrix import Matrix
from argumented_matrix import (ArgumentedMatrix, unmerge)
from elementary_row_operations import(row_swap, scalar_mul, row_sum)
from functools import reduce
from operator import mul

def find_pivot_pos(A):
    
    positions = []

    for i in range(A.p):
        for j in range(A.q):
            if A.matrix[i][j] != 0:
                positions.append(j)
                break
            elif j == A.q - 1:
                positions.append(j)
            else:
                pass
    return positions

def is_ordered(A):

    pos = find_pivot_pos(A)

    for i in range(1, len(pos)):
        if pos[i] < pos[i-1]:
            return False

    return True

def order(A, det=1):

    pos = find_pivot_pos(A)
    current_row = 0
    positions = iter(sorted(pos))

    while not is_ordered(A):
        low = next(positions)
        if pos[current_row] >= low:
            A = row_swap(current_row, pos.index(low), A.p) * A
            det *= -1
            positions = iter(sorted(find_pivot_pos(A)))
        current_row += 1

    return A, det

def all_pivots_to_right(A):
    array = A.matrix

    # create a generator
    temp  = ((row[i] for i in range(len(row))) for row in array)

    pivots = []
    for i in range(A.p):
        row = next(temp)
        for j in range(A.q):
            pivot = next(row)
            if pivot != 0 or j == A.q - 1:
                pivots.append(j)
                break

    for i in range(A.p):
        if i == 0: 
            pass
        else:
            if pivots[i] <= pivots[i-1]:
                return False, i, pivots[i]

    return True, None, None

def row_echelon_with_det(A):
    A_is_aug = False
    left_ncols = None

    if isinstance(A, ArgumentedMatrix):
        A_is_aug = True
        left_ncols = A.left.q
        A = A.merge()

    if not isinstance(A, Matrix):
        raise TypeError(f'argument must be type Matrix or ArgumentedMatrix not type{A}')

    B, det = order(A)    
    true, row, col  = all_pivots_to_right(B)

    while not true:
        array = B.matrix

        r1_pivot = array[row][col]
        r2_pivot = array[row-1][col]
        
        quotient = r1_pivot / r2_pivot

        if (r1_pivot > 0 and r2_pivot > 0) or (r1_pivot < 0 and r2_pivot < 0) or r2_pivot < 0:
            quotient = -1 * quotient
        else: # r1_pivot < 0:
            quotient = abs(quotient)

        B, det = order(row_sum(row, row-1, quotient, B.p) * B, det)
        true, row, col = all_pivots_to_right(B)
    
    if A_is_aug:
        return unmerge(B, left_ncols), det
    return B, det

def row_echelon(A):
    return row_echelon_with_det(A)[0]

def determinant(A):
    B, det = row_echelon_with_det(A)
    if B.is_square():
        detB = det * reduce(mul, [B[i,i] for i in range(B.p)])
        return detB

def find_pivots(A):
    array = A.matrix

    pivots = []
    for i in range(A.p):
        for j in range(A.q):
            if array[i][j] == 0 and j != A.q - 1:
                pass
            else:
                pivots.append(array[i][j])
                break

    return pivots

def reduced_row_echelon_with_det(A):
    B, det = row_echelon_with_det(A)
    B_is_aug = False
    left_ncols = None

    if isinstance(B, ArgumentedMatrix):
        B_is_aug = True
        left_ncols = B.left.q
        B = B.merge()

    pivots = find_pivots(B)
    
    for i in range(len(pivots) - 1, -1, -1):
        if pivots[i] == 0 or pivots[i] == 1:
            pass
        else:
            B = scalar_mul(i, 1/pivots[i], B.p) * B
            det *= 1/pivots[i]
            pivots = find_pivots(B)
        if i == len(pivots) - 1:
            pass
        else:
            for j in range(i, len(pivots) - 1):
                pos = B.matrix[j+1].index(pivots[j+1])
                B = row_sum(i, j+1, -1 * B.matrix[i][pos], B.p) * B
                pivots = find_pivots(B)
    
    if B_is_aug:
        return unmerge(B, left_ncols), det
    return B, det

def reduced_row_echelon(A):
    return reduced_row_echelon_with_det(A)[0]




A = Matrix([[1,-7,3],[4,-5,0],[7,8,-9]])
b = Matrix([[1],[3],[4]])
C = ArgumentedMatrix(A,b)

print(reduced_row_echelon(A))
print(reduced_row_echelon(C))
