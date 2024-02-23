#!/usr/bin/python3
""" A func that rotates a matrix 90 degrees clockwise """


def rotate_2d_matrix(matrix):
    """ Returns nothing """
    n = len(matrix)
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    for i in range(n):
        matrix[i] = matrix[i][::-1]
