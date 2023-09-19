#!/usr/bin/env python3
""" Task 03 """

from asyncio.tasks import Task
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> Task:
    """ Return a Task object """
    return asyncio.create_task(wait_random(max_delay))
