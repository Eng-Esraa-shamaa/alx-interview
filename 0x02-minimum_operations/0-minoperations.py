#!/usr/bin/python3
"""
calculates the minimum number of operations
to achieve a given number of characters using
only “Copy All” and “Paste” operations
"""


def minOperations(n):
    """
    method to get min operations
    """
    if n < 2:
        return 0
    result = 0
    for i in range(2, int(n**0.5) + 1):
        while n % i == 0:
            result += i
            n //= i
    if n > 1:
        result += n
    return result
