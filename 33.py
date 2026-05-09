import time
from functools import lru_cache


@lru_cache(maxsize=None)
def fibonacci(number: int):
    if number < 2:
        return number
    return fibonacci(number - 1) + fibonacci(number - 2)


start_time = time.perf_counter()
print(fibonacci(number=100))
end_time = time.perf_counter()

total_time = end_time - start_time

print(f"Time: {total_time}")
