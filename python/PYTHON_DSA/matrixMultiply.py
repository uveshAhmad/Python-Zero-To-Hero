def multiply_matrices(matrix1, matrix2):
    result = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    # Iterate through rows of matrix1
    for i in range(len(matrix1)):
        # Iterate through columns of matrix2
        for j in range(len(matrix2[0])):
            # Iterate through rows of matrix2
            for k in range(len(matrix2)):
                result[i][j] += matrix1[i][k] * matrix2[k][j]
    return result
# Example matrices
matrix_a = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
matrix_b = [
    [9, 8, 7],
    [6, 5, 4],
    [3, 2, 1]
]
# Multiply matrices
result_matrix = multiply_matrices(matrix_a, matrix_b)
# Display the result
for row in result_matrix:
    print(row)
    
    
    
    
    
    
    
    
    
    
import numpy as np
# take a 3x3 matrix
A = [[12, 7, 3],
    [4, 5, 6],
    [7, 8, 9]]
 
# take a 3x4 matrix
B = [[5, 8, 1, 2],
    [6, 7, 3, 0],
    [4, 5, 9, 1]]
 
# result will be 3x4
 
result= [[0,0,0,0],
        [0,0,0,0],
        [0,0,0,0]]
 
result = np.dot(A,B)
 
for r in result:
    print(r)    