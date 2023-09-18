#!/usr/bin/env python3
"""
A type-annotated function sum_list which takes a
list input_list of floats as argument and returns
their sum as a float.
"""


def sum_list(input_list: list[float]) -> float:
    """ Return te sum of input_list as a float """
    result = float(0)

    for item in input_list:
        result += item

    return result
