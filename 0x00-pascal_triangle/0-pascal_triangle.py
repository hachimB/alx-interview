#!/usr/bin/python3
"""Module Documentation"""
from math import factorial


def pascal_triangle(n):
    """Function Documentation"""
    my_list = []
    if n <= 0:
        return my_list
    for i in range(n):
        row = [factorial(i) // (factorial(j) * factorial(i - j)
                                )for j in range(i + 1)]
        my_list.append(row)
    return my_list
