#!/usr/bin/python3
""" divide each number of a list of lists """


def matrix_divided(matrix, div):
    """ divide each number of a list of lists """
    if not matrix or type(matrix) is not list or len(matrix) == 0:
        raise TypeError ("matrix must be a matrix (list of lists) of integers/floats")
    if isinstance(matrix[0], list) is False:
        aise TypeError("matrix must be a matrix (list of lists) of integers/"
                                               "floats")
