#!/usr/bin/env python3

import asyncio
from async_comprehension_file import async_comprehension

async def measure_runtime():
    start_time = asyncio.get_event_loop().time()

    await asyncio.gather(
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
        async_comprehension()
    )

    end_time = asyncio.get_event_loop().time()
    total_runtime = end_time - start_time

    return total_runtime
