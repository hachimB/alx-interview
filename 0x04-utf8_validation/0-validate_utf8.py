#!/usr/bin/python3
"""Module documentation"""


def validUTF8(data):
    """ValidUTF8"""
    for i in data:
        binary = bin(i)
        if binary[2] == '0' or binary[2:5] == '110'\
                or binary[2:6] == '1110' or binary[2:7] == '11110':
            return True
        else:
            return False
