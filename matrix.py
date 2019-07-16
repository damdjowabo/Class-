import math
from math import sqrt
import numbers

def zeroes(height, width):
        """
        Creates a matrix of zeroes.
        """
        g = [[0.0 for _ in range(width)] for __ in range(height)]
        return Matrix(g)

def identity(n):
        """
        Creates a n x n identity matrix.
        """
        I = zeroes(n, n)
        for i in range(n):
            I.g[i][i] = 1.0
        return I

class Matrix(object):

    # Constructor
    def __init__(self, grid):
        self.g = grid
        self.h = len(grid)
        self.w = len(grid[0])

    #
    # Primary matrix math methods . Here we have to define some primary matrix methos
    #############################
 
    def determinant(self):
        """
        Calculates the determinant of a 1x1 or 2x2 matrix.
        """
        if not self.is_square():
            raise(ValueError, "Cannot calculate determinant of non-square matrix.")
        if self.h > 2:
            raise(NotImplementedError, "Calculating determinant not implemented for matrices largerer than 2x2.")
        
        else:
            if self.h == 1:
                det = self.g[0][0] 
            else:
                det = self.g[0][0] * self.g[1][1] - (self.g[1][0] * self.g[0][1] )
        # TODO - your code here
         
        m1 = Matrix(det)
        return m1
    
    def trace(self):
        """
        Calculates the trace of a matrix (sum of diagonal entries).
        """
        if not self.is_square():
            raise(ValueError, "Cannot calculate the trace of a non-square matrix.")
        else:
            trace = 0
            if self.h == 1:
                trace = self.g[0][0] 
            else:
                for i in range (self.h):
                    for j in range (self.w):
                        if i == j:
                            trace += self.g[i][j]                            
         
            m1 = trace
            return m1  
        # TODO - your code here

    def inverse(self):
        """
        Calculates the inverse of a 1x1 or 2x2 Matrix.
        """
        inverse = []
        
        if not self.is_square():
            raise(ValueError, "Non-square Matrix does not have an inverse.")
        if self.h > 2:
            raise(NotImplementedError, "inversion not implemented for matrices larger than 2x2.")
        else :
            if self.h == 1:
                inverse.append([1 / self.g[0][0]])
            elif self.h==2:
                if self.g[0][0] * self.g[1][1] == self.g[0][1] * self.g[1][0]:
                    raise ValueError('The matrix is not invertible.')
                else:
                    factor = 1 / (self.g[0][0] * self.g[1][1] - self.g[0][1] * self.g[1][0])
                    inverse = [[self.g[1][1], -self.g[0][1]],[-self.g[1][0], self.g[0][0]]]
                    for i in range(self.h):
                        for j in range(self.w):
                            inverse[i][j] = factor * inverse[i][j]
        
                    
        m1 = Matrix(inverse)
        return m1               
        # TODO - your code here

    def T(self):
        """
        Returns a transposed copy of this Matrix.
        """
        # TODO - your code here
        matrix_transpose = []
        for c in range(self.w):
            new_row = []
            for r in range(self.h):
                new_row.append(self.g[r][c])
            matrix_transpose.append(new_row)
        
        m1 = Matrix(matrix_transpose)
        return m1       


    def is_square(self):
        return self.h == self.w

    #
    # Begin Operator Overloading
    ############################
    def __getitem__(self,idx):
        """
        Defines the behavior of using square brackets [] on instances
        of this class.

        Example:

        > my_matrix = Matrix([ [1, 2], [3, 4] ])
        > my_matrix[0]
          [1, 2]

        > my_matrix[0][0]
          1
        """
        return self.g[idx]

    def __repr__(self):
        """
        Defines the behavior of calling print on an instance of this class.
        """
        s = ""
        for row in self.g:
            s += " ".join(["{} ".format(x) for x in row])
            s += "\n"
        return s

    def __add__(self,other):
        """
        Defines the behavior of the + operator
        """
        if self.h != other.h or self.w != other.w:
            raise(ValueError, "Matrices can only be added if the dimensions are the same") 
        #   
        # TODO - your code here
        #
        matrixSum = []
        row = []
        for r in range(self.h):
            row = []
            for c in range(self.w):
                row.append(self.g[r][c] + other[r][c])
            matrixSum.append(row)
            
         
        m1 = Matrix(matrixSum)
        return m1
    
    def __neg__(self):
        """
        Defines the behavior of - operator (NOT subtraction)

        Example:

        > my_matrix = Matrix([ [1, 2], [3, 4] ])
        > negative  = -my_matrix
        > print(negative)
          -1.0  -2.0
          -3.0  -4.0
        """
        #   
        # TODO - your code here
        #
        negative = []
        for i in range(self.h):
            row = []
            for j in range(self.w):
                row.append(-self.g[i][j])
            negative.append(row)
          
        m1 = Matrix(negative)
        return m1
            

    def __sub__(self, other):
        """
        Defines the behavior of - operator (as subtraction)
        """
        #   
        # TODO - your code here
        #
        matrixSub = []
        row = []
        for r in range(self.h):
            row = []
            for c in range(self.w):
                row.append(self.g[r][c] - other[r][c])
            matrixSub.append(row)
            
        
         
        m1 = Matrix(matrixSub)
        return m1
    
    def __mul__(self, other):
        """
        Defines the behavior of * operator (matrix multiplication)
        """
        #   
        # TODO - your code here
        #
        def dot_product(vectorA, vectorB):
            result = 0
            for i in range(self.w):
                result += vectorA[i] * vectorB[i]
            return result
        
        def transpose(matrixinp):
            matrix_transpose = []
            for c in range(other.w):
                new_row = []
                for r in range(other.h):
                    new_row.append(matrixinp[r][c])
                matrix_transpose.append(new_row)
            return matrix_transpose

        product = []
        
        transposeB = Matrix(transpose(other))
        # This funtion below have to be comment to run succesfull this part of scrips 
#        if (self.w == other.h and self.h != other.w) or (self.w == other.h and self.h == other.w):
#            transposeB = transpose(other)
#        else:
#            transposeB = other
        for r1 in range(self.h):
            new_row = []
            for r2 in range(transposeB.h):
                dp = dot_product(self.g[r1], transposeB[r2])
                new_row.append(dp)
            product.append(new_row)
        
    
        
        m1 = Matrix(product)
        return m1    

    def __rmul__(self, other):
        """
        Called when the thing on the left of the * is not a matrix.

        Example:

        > identity = Matrix([ [1,0], [0,1] ])
        > doubled  = 2 * identity
        > print(doubled)
          2.0  0.0
          0.0  2.0
        """
        if isinstance(other, numbers.Number):
            pass
            #   
            # TODO - your code here
            #
            rmult = []
            for i in range (self.h):
                row = []
                for j in range(self.w):
                    row.append(other*self.g[i][j])
                rmult.append(row)
            m1 = Matrix(rmult)
            return m1
        
         
        

            
