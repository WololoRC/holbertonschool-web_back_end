#!/usr/bin/env python3
""" Task 01 """
import asyncio
from typing import List

async_generator = __import__("0-async_generator").async_generator


async def async_comprehension() -> List[float]:
    """ Returns a comprehsed list from a asyn generator """
    return [item async for item in async_generator()]
