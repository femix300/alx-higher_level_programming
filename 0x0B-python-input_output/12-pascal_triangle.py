#!/usr/bin/python3
"""Defines a Pascal's Triangle function."""


def pascal_triangle(n):
    """
    Generate Pascal's Triangle of size n.

    Args:
        n (int): The size of the Pascal's Triangle.

    Returns:
        A representing the rows of the triangle or an empty list
        if n is <= 0
    """
    if n <= 0:
        return []

    triangle = [[1]]
    while len(triangle) != n:
        row = triangle[-1]
        new_row = [1]
        for i in range(len(row) - 1):
            new_row.append(row[i] + row[i + 1])
        new_row.append(1)
        triangle.append(new_row)

    return triangle
