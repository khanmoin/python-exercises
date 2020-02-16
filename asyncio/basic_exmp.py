# Basic asyncio example to illustrate the usage of async and await

import asyncio
import time

async def work():
  print("Agent-1 is working")
  await asyncio.sleep(1)
  print("Agent-2 started working after 1 second of sleep")

async def main():
  '''
    calling work function 4 times
    in a non asyncio scenario this call should take 4 seconds to complete
  '''
  await asyncio.gather(work(), work(), work(), work())

if __name__ == '__main__':
  start_time = time.perf_counter()
  asyncio.run(main())
  time_elapsed = time.perf_counter() - start_time           # estimating the time
  print(f'{__file__} executed in {time_elapsed} seconds')
