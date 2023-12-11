#!/usr/bin/env python3
"""
Module contains fuction that waits for a
random delay between 0 and max_delay n times
"""

import asyncio
from typing import List


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Wait for a random delay between 0 and max_delay n times
    Args:
        n (int): number of times to wait
        max_delay (int): max wait time per round
    Returns:
        list: list of all the delays
    """
    delays = [wait_random(max_delay) for _ in range(n)]

    return [await delay for delay in asyncio.as_completed(delays)]
