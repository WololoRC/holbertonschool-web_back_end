#!/usr/bin/env python3
""" Task 1 """

import asyncio
from typing import List
wait_random = __import__("0-basic_async_syntax").wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Execute a list of corutines and return his values in a list.
    -----------------------------------------------------------
    Args:
    max_delay : int
        Delay for 'wait_random' function.
    n : int
        'n' times to run the corutine

    Returns:
        A list of float values as a result of each task
    """
    tasks = [wait_random(max_delay) for i in range(n)]
    delay_list = await asyncio.gather(*tasks)
    return sorted(delay_list)
