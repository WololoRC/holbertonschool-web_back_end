#!/usr/bin/env python3
""" Task 02 """
import asyncio
import time
async_comprehension = __import__("1-async_comprehension").async_comprehension


async def measure_runtime() -> float:
    """ measure the time of execute async_comprehnsion 4 times """
    task_list = [async_comprehension() for i in range(4)]
    start = time.time()
    await asyncio.gather(*task_list)
    end = time.time()

    return end - start
