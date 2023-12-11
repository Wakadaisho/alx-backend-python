#!/usr/bin/env python3
"""
Use task_wati_random to wait on a number n of asyncio tasks
"""

import asyncio

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> list:
    """
    Use wait random to wait for a random delay
    between 0 and max_delay n times
    """
    delays = [task_wait_random(max_delay) for _ in range(n)]
    return [await delay for delay in asyncio.as_completed(delays)]
