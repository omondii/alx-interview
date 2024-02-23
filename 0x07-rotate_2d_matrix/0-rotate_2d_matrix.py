#!/usr/bin/python3
""" A func that rotates a matrix 90 degrees clockwise """


def rotate_2d_matrix(matrix):
    """
    loop through each row in the outer loop
    inner loop - Start from the current row, loop through each column
    transpose the matrix by swapping elements at position [i][j] with [j][i]
    Reverse each row of the transposed matrix
    """
    n = len(matrix)
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    for i in range(n):
        matrix[i] = matrix[i][::-1]
