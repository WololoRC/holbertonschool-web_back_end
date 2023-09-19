#!/sur/bin/env pyhton3
""" Task 00 """
import asyncio
import random
from typing import AsyncIterator


async def async_generator() -> AsyncIterator[float]:
    """ A async generator of 10 random numbers between 0/10 """
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
