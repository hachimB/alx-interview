#!/usr/bin/python3
"""Module Documentation"""


def factorial(number):
    """Factorial Function"""
    fact = 1
    for i in range(number):
        fact *= i + 1
    return fact


def pascal_triangle(n):
    """Pascal's triangle function"""
    my_list = []
    if n <= 0:
        return my_list
    for i in range(n):
        row = [factorial(i) // (factorial(j) * factorial(i - j)
                                )for j in range(i + 1)]
        my_list.append(row)
    return my_list
