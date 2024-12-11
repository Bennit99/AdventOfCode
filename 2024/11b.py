import time
from functools import lru_cache
from aocd import data, submit

start_time = time.time()
result = 0
stones = [int(stone) for stone in data.split(' ')]

n_blinks = 75

@lru_cache(maxsize=None)
def rec(n_blinks, stone) -> int:
    if n_blinks == 0:
        return 1
    n_blinks -= 1
    if stone == 0:
        return rec(n_blinks, 1)
    else:
        num_digits = len(str(stone))
        if num_digits % 2 == 0:
            divisor = 10 ** (num_digits // 2)
            return rec(n_blinks, stone // divisor) + rec(n_blinks, stone % divisor)
        else:
            return rec(n_blinks, stone * 2024)

for stone in stones:
    result += rec(n_blinks, stone)

# Get cache statistics
cache_stats = rec.cache_info()
print(f"Cache hits: {cache_stats.hits}")        # 70710
print(f"Cache misses: {cache_stats.misses}")    # 132143

print(f"Time taken: {round(time.time() - start_time, 4)} seconds") # 100 ms
submit(result)