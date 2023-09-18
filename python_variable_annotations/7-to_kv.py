#!/usr/bin/env python3
from typing import Union, Tuple
""" Task 7"""


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Return a tuple
    """
    return (k, v ** 2)
