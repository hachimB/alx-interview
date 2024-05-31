#!/usr/bin/python3
"""Rotate 2D Matrix"""


def rotate_2d_matrix(matrix):
    """Rotate 2D Matrix"""
    matrix[:] = [list(row) for row in zip(*matrix)][::-1]
