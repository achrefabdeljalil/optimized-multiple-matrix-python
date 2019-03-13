# optimized-multiple-matrix-python
This repository solve the problem of multiple of two matrix with optimized solution
## method of library 
  -- The form of Matrix must be : EXEMPLE matrix = [list,list,list] = [[1,2,3],[9,7,3],[8,5,0]] 
  - multiple_matrix(matrix1,matrix2) :
      This method multiple two matrix 
  - multiple_line_columns(line , matrix2) 
      This method multiple a line from the first matrix to all the column of second matrix and its used by the precedent methode
  - change_matrix_direction(matrix) :
      This method change the direction of matrix and return matrix_Transposed
  - display_matrix(matrix) :
  - getColumn (matrix , indexColumn) :
      This method return a column from matrix with type 'List'
  - getLine (matrix  ,indexLine) :
      This method return a line from matrix with type 'List'
  - create_random_matrix(size_matrix) :
      This method get size matrix and return a matrix with length(size) with a random value
## how to use module 
  + First step 
      put the file "matrixLibrary.py" in the same directory of your project 
  + Second step 
      add this line in the head of your project file 
      
      ```
      from matrixLibrary import 'name of methode that you want to use it' 
      ```
      EXEMPLE :
      
      ```
      from matrixLibrary import display_matrix
      ```
