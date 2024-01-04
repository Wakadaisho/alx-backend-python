#!/usr/bin/env python3

"""
Module containing async_generator coroutine
"""

import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    """
    Yield an random number between 0 and 10
      every 1 second for 10 seconds
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
