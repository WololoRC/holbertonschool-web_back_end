#!/usr/bin/env python3
""" Task 04 """

import asyncio
from typing import List
wait_random = __import__("3-tasks").task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Execute a list of task objects and return his values in a list. """
    tasks = [wait_random(max_delay) for i in range(n)]
    delay_list = await asyncio.gather(*tasks)
    return sorted(delay_list)
