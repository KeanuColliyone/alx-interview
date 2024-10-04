#!/usr/bin/python3
def pascal_triangle(n):
    """Returns a list of lists of integers representing Pascal's triangle of n."""
    if n <= 0:
        return []

    # Initialize the triangle with an empty list
    triangle = []

    # Build Pascal's triangle row by row
    for i in range(n):
        # Start with a row of 1s
        row = [1] * (i + 1)

        # Update the inner elements of the row (except for the first and last)
        for j in range(1, i):
            row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]

        # Append the completed row to the triangle
        triangle.append(row)

    return triangle
