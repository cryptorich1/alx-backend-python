#!/usr/bin/env python3

from async_generator_file import async_generator

async def async_comprehension():
    random_numbers = [num async for num in async_generator()]
    return random_numbers[:10]
