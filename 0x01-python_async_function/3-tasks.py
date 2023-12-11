#!/usr/bin/env python3
"""
Define a function that returns an asyncio task
instead of being a coroutine itself
"""

import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """Return an asyncio task that executes wait_random(max_delay)"""
    return asyncio.create_task(wait_random(max_delay))
