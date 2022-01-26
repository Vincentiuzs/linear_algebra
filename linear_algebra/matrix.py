from collections import Counter


class Matrix:
    """A (p \u00D7 q) matrix."""

    def __init__(self, array):

        # Check if the array is a valid matrix and
        # raise errors/exceptions if invalid
        self._isValid(array)

        self.matrix = array

        # size of the matrix: p x q
        self.p, self.q = self._size()
        self.size = self._size()

    def _isValid(self, array):
        """

        Args:
          array:

        Returns:


        """
        assert(len(array) > 0)

        # check if array is of type list
        if isinstance(array, list):

            # variable to check if array is 2d list
            array_is_2d = False

            # check if elements of array are all lists
            if sum(list(map(lambda x: isinstance(x, list), array))) == len(array):

                # check if elements of array (lists) have same length
                lengths = Counter(list(map(len, array)))
                if lengths.most_common(1)[0][1] != len(array):
                    raise Exception('rows of the matrix have different lengths')
                else:
                    array_is_2d = True
            
            if not array_is_2d:
                raise Exception('matrix can only be created from a 2D list')
            
            # lambda function to generate all matrix entries in single list
            extract_elements = lambda x, y=False: [i for i in x] if not y \
                                        else [i for row in x for i in row]
            
            # check if all elements are real or complex numbers
            array_all_elements = extract_elements(array, array_is_2d)
            
            is_valid_type = lambda x: isinstance(x, int) or isinstance(x, complex) or isinstance(x, float)
            
            # function to check if all entries are valid types
            if sum(list(map(is_valid_type, array_all_elements))) == len(array_all_elements):
                return True
            else:
                raise TypeError('elements must be of type: int, complex or float')
        
        # raise a type error since the class only uses a list
        else:
            raise TypeError(f'the matrix must be a list not {type(array)}')
        
    def _size(self):
        """Returns size of the matrix"""
        array = self.matrix
        if isinstance(array, list):
            
            # check if elements of array are all lists
            if sum(list(map(lambda x: isinstance(x, list), array))) == len(array):
                return len(array), len(array[0])
            
            # check if elements of array are numbers i.e., row vector
            elif sum(list(map(lambda x: isinstance(x, int), array))) == len(array) or \
                 sum(list(map(lambda x: isinstance(x, float), array))) == len(array):
                return 1, len(array)       
    
    def __repr__(self) -> 'str':
        '''Return string representation for a particular Matrix'''
        # number of sapces to reserve for row name
        rsv_spaces_index = len(str(self.p)) + 3
        
        # function to calculate the longest number in each column
        longest_number = lambda x: [[len(str(x[i][j])) for i in range(self.p)] \
                                    for j in range(self.q)]
        
        # number of spaces to reserve in each column
        rsv_spaces_cols1 = list(map(max, longest_number(self.matrix)))
        rsv_spaces_cols2 = [len(str(j)) + 3 for j in range(self.q)]
        
        # find the maximums between rsv_spaces_cols# lists
        rsv_spaces_cols = [max(i, j) for i, j in zip(rsv_spaces_cols1, rsv_spaces_cols2)]
        
        # row representing colnames
        colname = lambda x: f'[,{x}]'
        mat_str_lst = [f"{' ':<{rsv_spaces_index}}"] + [f' {colname(j):>{rsv_spaces_cols[j]}}' for j in range(self.q)]
        mat_str = " ".join(mat_str_lst)
        
        # returns real part of number if imaginary part is 0
        for i in range(self.p):
            index = f'[{i},]'
            mat_str += " ".join([f'\n{index:>{rsv_spaces_index}}'] +[f' {self.matrix[i][j]:{rsv_spaces_cols[j]}}'\
                                                                     for j in range(self.q)])

        return str(mat_str)
    
    def __eq__(self, other):
        
        if isinstance(other, Matrix):
            # check if rows elements of two matrices are equal
            rows_equal = lambda x, y: [i == j for i, j in zip(x, y)]
            
            # list of bool where rows/elements are equals
            equals = rows_equal(self.matrix, other.matrix)
            
            # add booleans in the least and check if sm is equal to length of the list
            return sum(equals) == len(equals)

        return False
    
    def __add__(self, other):
        '''Return self+other'''
        return self.add(other)
    
    def __mul__(self, other):
        '''Return self*other'''
        return self.mul(other)
    
    def __rmul__(self, other):
        '''return other*self'''
        if not isinstance(other, Matrix):
            return self * other
   
    def __sub__(self, other):
        '''Return self-other'''
        return self.sub(other)
    
    def __getitem__(self, key):
        
        if isinstance(key, tuple):
            rowkey = key[0]
            colkey = key[1]

            if isinstance(rowkey, int) and isinstance(colkey, int):
                # chooses a specific element
                return self.getrows()[rowkey][colkey]            

            elif isinstance(rowkey, int) and isinstance(colkey, slice):
                # choose a row elemenets
                return Matrix([self.getrows()[rowkey][colkey]])

            elif isinstance(rowkey, slice) and isinstance(colkey, int):
                # choose a  column elements
                return Matrix([self.getcols()[colkey][rowkey]]).transpose()

            elif isinstance(rowkey, slice) and isinstance(colkey, slice):
                # choose a submatrix
                submatrix = []
                
                def new_slice(aslice, isrowkey=True):
                    start = aslice.start 
                    stop = aslice.stop
                    step = aslice.step

                    if aslice.start is None:
                        start = 0
                    if aslice.stop is None:
                        if isrowkey:
                            stop = self.p
                        else:
                            stop = self.q
                    if aslice.step is None:
                        step = 1

                    return slice(start, stop, step)

                rowkey = new_slice(rowkey)
                colkey = new_slice(colkey, isrowkey=False)

                j = 0
                for i in range(rowkey.start, rowkey.stop, rowkey.step):
                    submatrix.append([])
                    
                    for k in range(colkey.start, colkey.stop, colkey.step):
                        submatrix[j].append(self.matrix[i][k])

                    j += 1

                return Matrix(submatrix)

    def __setitem__(self, key, value):
        pass


    def getrows(self):

        return self.matrix

    def getcols(self):

        return self.transpose().matrix


    def add(self, other):
        """

        Args:
          other: 

        Returns:

        
        """
        
        if isinstance(other, Matrix):

            # check if matrices have same size so that they can be added
            if self.size == other.size:
                
                # adds corresponding elements given two rows each from different matrix
                add_row_elements = lambda x, y: [i + j for i, j in zip(x,y)]
                
                # add corresponding elements given two matrices
                add_all_elements = lambda x, y: [add_row_elements(i, j) for i, j in zip(x,y)]

                return Matrix(add_all_elements(self.matrix, other.matrix))

            else:
                raise Exception('matrices have different sizes')   
        else:
            raise TypeError(f'Matrix object can only be added to other Matrix, not {type(other)}')

    def sub(self, other):
        """

        Args:
          other: 

        Returns:

        
        """
        return self + other * -1
    
    def mul(self, other):
        """

        Args:
          other: 

        Returns:

        
        """
        # checks if is other is a number (either real or complex) for scalar 
        is_number = lambda x: isinstance(x, float) or isinstance(x, complex) or isinstance(x, int)
        
        if is_number(other):
            prod = []
            for i in range(self.p):
                prod.append([])
                for j in range(self.q):
                    # multiply each entry by other
                    prod[i].append(self.matrix[i][j] * other)
          
            return Matrix(prod)
        
        elif isinstance(other, Matrix):
            # check if number of column of this matrix equals number of rows in other matrix
            if self.q == other.p:
                a = self.matrix; b = other.matrix
                # c[i][j] = a[i][0]*b[1][0] + ... + a[i][self.p-1]*b[self.p-1][j]
                c = [[sum([a[i][k]* b[k][j] for k in range(self.q)]) \
                      for i in range(self.p)] for j in range(other.q)]
                return Matrix(c)
            else:
                raise Exception('matrices are non-comformable')
            
        else:
            raise TypeError(f'Matrix can only be mutiplied by Matrix, int, complex or float not {type(other)}')
            
    
    def transpose(self):
        """ """
        # make rows to be columns, and columns be rows
        transpose = [[row[j] for row in self.matrix] for j in range(self.q)]
        
        return Matrix(transpose)
    
    def is_square(self):
        return self.p == self.q

    def is_symmetric(self):
        return is_square() and self == self.transpose() 

def matrix(*elements, nrows, ncols):
    """Returns a Matrix object"""

    elements = list(elements)

    start = 0; end = ncols
    matrix = [];

    for i in range(nrows):
        matrix.append(elements[start: end])
        start += ncols
        end += ncols

    return Matrix(matrix)

def vector(*elements, row=True):
    
    if row:
        return matrix(*elements, nrows=1, ncols=len(elements))
    return matrix(*elements, nrows=len(elements), ncols=1)


#print(matrix(1,2,3,4,5,6,ncols=3,nrows=2))
