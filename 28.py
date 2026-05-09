from typing import Callable
import time
import functools


def timer(fun: Callable):
    @functools.wraps(fun)
    def wrapper_timer(*args, **kwargs):
        start_time = time.perf_counter()

        value = fun(*args, **kwargs)

        end_time = time.perf_counter()
        total_time = end_time - start_time

        print(f"function: {fun.__name__}, took total: {total_time:.4f}")

        return value

    return wrapper_timer


@timer
def heavy_work(data:int):
    print("Start working " ,data)
    time.sleep(2)
    print("End working")


heavy_work(5)
