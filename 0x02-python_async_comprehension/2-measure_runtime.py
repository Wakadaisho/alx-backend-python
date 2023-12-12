#!/usr/bin/env python3

"""
Module that times async operations
"""

import asyncio
import time


async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Measure runtime of async_comprehension
    """
    t_0 = time.time()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    t_1 = time.time()
    return t_1 - t_0
