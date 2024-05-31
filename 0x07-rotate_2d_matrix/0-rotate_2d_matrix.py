#!/usr/bin/python3
"""Rotate 2D Matrix"""


def rotate_2d_matrix(matrix):
    """Rotate 2D Matrix"""
    transposed_matrix = [list(row) for row in zip(* matrix)]
    for i in range(len(transposed_matrix)):
        for j in range(len(transposed_matrix[i])):
            matrix[i][j] = transposed_matrix[i][j]
