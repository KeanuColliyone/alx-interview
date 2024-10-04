#!/usr/bin/python3
"""
Module to return Pascal's Triangle
"""

def pascal_triangle(n):
    """
    Returns a list of lists representing Pascal's triangle of n
    """
    if n <= 0:
        return []

    triangle = [[1]]  # Start with the first row

    for i in range(1, n):
        prev_row = triangle[-1]  # Get the previous row
        new_row = [1]  # Start the new row with 1
        # Compute the values for the new row
        for j in range(1, i):
            new_row.append(prev_row[j - 1] + prev_row[j])
        new_row.append(1)  # End the new row with 1
        triangle.append(new_row)  # Append the new row to the triangle

    return triangle
