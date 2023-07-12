#!/usr/bin/env python3

import time
from wait_n_file import wait_n

def measure_time(n: int, max_delay: int) -> float:
  start_time = time.time()
  delays = wait_n(n, max_delay)
  end_time = time.time()
  total_time = end_time - start_time
  average_time = total_time / n
  return average_time
