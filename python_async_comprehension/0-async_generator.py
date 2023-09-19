#!/usr/bin/env python3
""" Task 00 """
import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator:
    """ A async generator of 10 random numbers between 0/10 """
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
