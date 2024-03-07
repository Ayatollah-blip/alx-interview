#!/usr/bin/python3
"""Triangle Triangle"""


def pascal_triangle(n):
    """Triangle"""
    if n <= 0:
        return []
    my_list =[[1]]
    for i in range(1, n):
        row = [1]
        for j in range(1, i):
            element = my_list[i-1][j-1] + my_list[i-1][j]
            row.append(element)
        row.append(1)
        my_list.append(row)
    return my_list
