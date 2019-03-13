"""
@author : Abdeljalil Achref 
@mail : abdeljalilachref@gmail.com

NB : if there are any question please contact me by mail
"""

#__________les Modules________

import threading
import sys
import random


#____________class_____________

class multiple_line_columns(threading.Thread):
    def __init__(self, line, matrix):
        threading.Thread.__init__(self)
        self.line = line
        self.matrix = matrix
        self.vector_result = []
    
    def line_columns_multiple(self):
        tmp_line_length = len(self.line)
        if(len(self.line)>len(self.matrix[0])):
            tmp_line_length = len(self.matrix[0])
        
        for i in range(len(self.matrix)):
            tmp = 0
            for j in range(tmp_line_length):
                tmp += self.line[j] * self.matrix[i][j]
            self.vector_result.append(tmp)
    def run(self):
        self.line_columns_multiple()


#_________change_matrix_direction___________
def change_matrix_direction(mtrx):
    tmp = []
    for i in range(len(mtrx[0])):
        column=[]
        for j in range(len(mtrx)):
            column.append(mtrx[j][i])
        tmp.append(column)
    display_matrix(tmp)
    return tmp


def display_matrix(matrix):
        for i in range(len(matrix)):
            print('   ')
            for j in range(len(matrix[0])):
                print(' ',matrix[i][j],end=' ')
                sys.stdout.flush()
        print('\n')
            
#_________get_Column__________

def getColumn(mtrx,numCol):
    column=[]
    for i in range(len(mtrx[0])):
        column.append(mtrx[i][numCol])
    return column
    
#_________get_Line____________

def getLine(mtrx,numLine):
    return mtrx[numLine]


def create_random_matrix(matrix_size):
    matrix_result=[]
    for i in range(matrix_size):
        vector_result = []
        for j in range(matrix_size):
            vector_result.append(random.randrange(0, 9, 1))
        matrix_result.append(vector_result)
    return matrix_result



# multiple of two matrix 
def multiple_matrix(matrix1,matrix2):
    matrixx = change_matrix_direction (matrix2)
    matrix_result=[]
    for i in range(len(matrix1)):
        m_l_cs = multiple_line_columns(matrix1[i], matrixx)
        m_l_cs.start()
        matrix_result.append(m_l_cs.vector_result)
    return matrix_result