#!/usr/bin/env python3

import asyncio

async def task_wait_random(max_delay: int) -> float:
    delay = await wait_random(max_delay)
    return delay

async def task_wait_n(n: int, max_delay: int) -> List[float]:
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    delays = await asyncio.gather(*tasks)
    return sorted(delays)
