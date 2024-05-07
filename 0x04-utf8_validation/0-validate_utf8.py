#!/usr/bin/python3
"""Module documentation"""


def validUTF8(data):
    """ValidUTF8"""
    bytes_to_check = 0
    for i in data:
        if i < 0 or i > 255:
             return False
        if bytes_to_check == 0:
            # Use bitwise shift to count the number of leading 1s
            if (i & 0b10000000) == 0:
                bytes_to_check = 0
            elif (i & 0b11100000) == 0b11000000:
                bytes_to_check = 1
            elif (i & 0b11110000) == 0b11100000:
                bytes_to_check = 2
            elif (i & 0b11111000) == 0b11110000:
                bytes_to_check = 3
            else:
                return False
        else:
            # Use bitwise shift to check if the byte starts with '10'
            if (i & 0b11000000) != 0b10000000:
                return False
            bytes_to_check -= 1
    return True
