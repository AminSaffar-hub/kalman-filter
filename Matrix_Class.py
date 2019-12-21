# -*- coding: utf-8 -*-
"""
Created on Tue Dec 17 21:08:39 2019

@author: Amin Saffar
"""
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
            I.matrix[i][i] = 1.0
        return I
class Matrix :
    def __init__(self,matrix):
        self.matrix = matrix
    def determinant(self):
        if (len(self.matrix) == 1):
            return(self.matrix[0])
        if (len(self.matrix) == 2):
            determinant = self.matrix[0][0]*self.matrix[1][1]-self.matrix[0][1]*self.matrix[1][0]
            return(determinant)
        elif (len(self.matrix) == 3):
            determinant1 = self.matrix[0][0]*(self.matrix[2][2]*self.matrix[1][1]-self.matrix[1][2]*self.matrix[2][1])
            determinant2 = self.matrix[1][0]*(self.matrix[2][2]*self.matrix[0][1]-self.matrix[0][2]*self.matrix[2][1])
            determinant3 = self.matrix[2][0]*(self.matrix[1][2]*self.matrix[0][1]-self.matrix[1][1]*self.matrix[0][2])
            determinant = determinant1-determinant2+determinant3
            return(determinant)
        else:
            raise ValueError("this functions cant treat such matrices")
    def trace(self):
        sum = 0
        for i in range(0,len(self.matrix)):
            sum += self.matrix[i][i]
        return(sum)
    def inverse1D(self):
        inverse = []
        inverse.append([1/self.matrix[0][0]])
        return Matrix(inverse)
    def inverse2D(self):
        inverse = []
        #print(inverse)
        determinant = self.matrix[0][0]*self.matrix[1][1] - self.matrix[0][1]*self.matrix[1][0]
        if (determinant == 0):
            raise ValueError('The denominator of a fraction cannot be zero')
        else:
            row = []
            row.append(self.matrix[1][1]*(1/determinant))
            row.append(-self.matrix[0][1]*(1/determinant))
            inverse.append(row)
            row = []
            row.append(-self.matrix[1][0]*(1/determinant))
            row.append(self.matrix[0][0]*(1/determinant))
            inverse.append(row)
        return Matrix(inverse)
    def inverse3D(self):
        inverse = []
        row1 = []
        row2 = []
        row3 = []
        mt=[]
        #print(inverse)
        determinant = self.determinant()
        if (determinant == 0):
            raise ValueError('The denominator of a fraction cannot be zero')
        else:
          mt = self.transpose().matrix
          row1.append(Matrix([[mt[1][1],mt[1][2]],[mt[2][1],mt[2][2]]]).determinant()/determinant)
          row1.append(-Matrix([[mt[1][0],mt[1][2]],[mt[2][0],mt[2][2]]]).determinant()/determinant)
          row1.append(Matrix([[mt[1][0],mt[1][1]],[mt[2][0],mt[2][1]]]).determinant()/determinant)
          row2.append(-Matrix([[mt[0][1],mt[0][2]],[mt[2][1],mt[2][2]]]).determinant()/determinant)
          row2.append(Matrix([[mt[0][0],mt[0][2]],[mt[2][0],mt[2][2]]]).determinant()/determinant)
          row2.append(-Matrix([[mt[0][0],mt[0][1]],[mt[2][0],mt[2][1]]]).determinant()/determinant)
          row3.append(Matrix([[mt[0][1],mt[0][2]],[mt[1][1],mt[1][2]]]).determinant()/determinant)
          row3.append(-Matrix([[mt[0][0],mt[0][2]],[mt[1][0],mt[1][2]]]).determinant()/determinant)
          row3.append(Matrix([[mt[0][0],mt[0][1]],[mt[1][0],mt[1][1]]]).determinant()/determinant)
          inverse.append(row1)
          inverse.append(row2)
          inverse.append(row3)
        return Matrix(inverse)
    def inverse(self):
        if len(self.matrix) != len(self.matrix[0]):
            raise ValueError('The matrix must be square')
        if len(self.matrix) == 1 :
            return(self.inverse1D())
        elif len(self.matrix) == 2 :
            return(self.inverse2D())
        elif len(self.matrix) == 3:
            return(self.inverse3D())
        else :
            raise ValueError('this functionality is not implemented')
    def transpose(self):
        matrix_transpose = []
        for each_column in range(len(self.matrix[0])):
            new_row = []
            for each_row in range(len(self.matrix)):
                new_row.append(self.matrix[each_row][each_column])
            matrix_transpose.append(new_row)
        #print(matrix_transpose)
        return Matrix(matrix_transpose)
    def get_row(self, row):
        return self.matrix[row]

    def get_column(self, column_number):
        column = []
        for each_row in range(len(self.matrix)):
            #print('get_column row index:{} col index:{}'.format(each_row,column_number))
            column.append(self.matrix[each_row][column_number])
        return column

    def dot_product(self,vector_one, vector_two):
        sum = 0
        for each_element in range(len(vector_one)):
            sum += vector_one[each_element]*vector_two[each_element]
        return sum
    
## here we overload the finction add ,sub , mul , print 
    def __mul__(self,other):
        """
        Called when you use the * operator.
        """
        product = []
        T = other.transpose()
        matrix_T = T.matrix
        for each_row_A in range(len(self.matrix)):
            new_row = []
            for each_row_B_T in range(len(matrix_T)):
                vector_one = self.matrix[each_row_A]
                vector_two = matrix_T[each_row_B_T]
                new_row.append(self.dot_product(vector_one,vector_two))
            product.append(new_row)
        return Matrix(product)
    def __add__(self,other):
        """
        Called when you use the + operator.
        """
        addition = []
        col = len(self.matrix[0])
        row = len(self.matrix)
        for i in range(0,row):
            row =[]
            for j in range(0,col):
                row.append(self.matrix[i][j]+other.matrix[i][j])
            addition.append(row)
        return Matrix(addition)
    def __sub__(self,other):
        """
        Called when you use the - operator.
        """
        sub = []
        col = len(self.matrix[0])
        row = len(self.matrix)
        for i in range(0,row):
            row=[]
            for j in range(0,col):
                row.append(self.matrix[i][j]-other.matrix[i][j])
            sub.append(row)
        return Matrix(sub)
    def __rmul__(self, other):
        """
        Called when the thing on the left of the * is not a matrix.
        """
        product = []
    
        if(len(other) == 1):
                for i in range(len(self.matrix)):
                    row = []
                    for j in range(len(self.matrix[0])):
                        row.append(other[0]*self.matrix[i][j])
                    product.append(row)
        else:
                B = Matrix(other)
                product = (B*A)
        return Matrix(product)
    def __repr__(self):
        """
        Defines the behavior of calling print on an instance of this class.
        """
        s = ""
        for row in self.matrix:
            s += " ".join(["{} ".format(x) for x in row])
            s += "\n"
        return s
    def __getitem__(self,idx):
        """
        Defines the behavior of using square brackets [] on instances
        of this class.
        """
        return self.matrix[idx]   
     
A = Matrix([ 
    [2,1], 
    [4,1]])
E = Matrix([[1,0],[0,3]])
print(A.inverse()*E)