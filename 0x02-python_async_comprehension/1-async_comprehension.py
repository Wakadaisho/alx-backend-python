#!/usr/bin/env python3
"""
Module that loops through an async generator yield
"""

from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    Loop through async generator
    """
    return [n async for n in async_generator()]
