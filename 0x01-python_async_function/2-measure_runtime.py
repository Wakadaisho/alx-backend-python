#!/usr/bin/env python3
"""
Measure the time taken by wait_n calls
"""

import asyncio
import time

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """Measure the total execution time for the async function wait_n"""
    t_0 = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    t_1 = time.perf_counter()

    return (t_1 - t_0) / n
