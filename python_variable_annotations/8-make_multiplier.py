#!/usr/bin/env python3
"""
Write a type-annotated function make_multiplier that takesi
a float multiplier as argument and returns a function that
multiplies a float by multiplier.
"""


from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Return a Callable who multiplies a arg for himself
    """
    return lambda multiplier: multiplier * multiplier
