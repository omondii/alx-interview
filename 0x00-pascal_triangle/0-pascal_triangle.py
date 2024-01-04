#!/usr/bin/python3
"""
Create a function def pascal_triangle(n): that returns a list of lists of
integers representing the Pascal’s triangle of n:
"""
def pascal_triangle(n):
    """ Use nested loop to generate the triangle """
    triangle = []
    for i in range(n):
        row = []
        val = 1
        for j in range(i + 1):
            row.append(val)
            val = val * (i - j) // (j + 1)
        triangle.append(row)
    return triangle