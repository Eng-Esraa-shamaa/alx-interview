#!/usr/bin/python3
"""
function that returns a list of lists of integers
representing the Pascal’s triangle of n
"""


def pascal_triangle(n):
    """
    return list of lists of integers
    """
    listt = [];
    if (n <= 0):
        return [];
    for i in range(n):
        listt.append([])
        listt[i].append(1)
        if (i > 0):
            for j in range(1, i):
                listt[i].append(listt[i - 1][j - 1] + listt[i - 1][j])
            listt[i].append(1)
    return listt
