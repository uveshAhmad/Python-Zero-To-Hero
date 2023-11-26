m = [[1, 2], [3, 4], [5, 6]]
for row in m:
    print(row)
rez = [[m[j][i] for j in range(len(m))] for i in range(len(m[0]))]
print("\n")
for row in rez:
    print(row)
    
    
    
    
import numpy
matrix = [[1, 2, 3], [4, 5, 6]]
print(matrix)
print("\n")
print(numpy.transpose(matrix))



def transpose_matrix(matrix):
    # Get the number of rows and columns
    rows, cols = len(matrix), len(matrix[0])

    # Create a new matrix with switched dimensions
    transposed_matrix = [[0 for _ in range(rows)] for _ in range(cols)]

    # Iterate through the original matrix and populate the transposed matrix
    for i in range(rows):
        for j in range(cols):
            transposed_matrix[j][i] = matrix[i][j]

    return transposed_matrix








# Example matrix
original_matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
# Transpose the matrix
transposed_matrix = transpose_matrix(original_matrix)
# Display the original and transposed matrices
print("Original Matrix:")
for row in original_matrix:
    print(row)
print("\nTransposed Matrix:")
for row in transposed_matrix:
    print(row)


    