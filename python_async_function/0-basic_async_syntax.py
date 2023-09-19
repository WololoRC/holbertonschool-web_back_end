#!/usr/bin/env python3
""" Task 0 """
import random
import asyncio


async def wait_random(max_delay: int | float = 10) -> float:
    """
    Wait 'n' seconds and return a number within 0 and max_delay
    - max_delat : int | float
        max delay for random.uniform() to get the 'n' secons to wait.

    Return: The 'n' seconds awaited.
    """
    wait_this = random.uniform(0, max_delay)
    await asyncio.sleep(wait_this)
    return wait_this
