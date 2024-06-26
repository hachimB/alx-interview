#!/usr/bin/python3
"""Module documentation"""


def minOperations(n):
    """minOperations"""
    operations = 0
    i = 2
    while i * i <= n:
        while n % i:
            i += 1
        while n % i == 0:
            n //= i
            operations += i
    if n > 1:
        operations += n
    return operations
