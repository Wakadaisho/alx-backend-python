#!/usr/bin/env python3
"""
Module with an async funtion that waits a random number of seconds
"""

import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    """Async function that waits for a random delay between 0 and max_delay"""
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
