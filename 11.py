from typing import Sequence
def unique(data:Sequence[int]):
    return list(set(data))


print(unique([1, 2, 2, 3, 4, 4, 4, 5]))