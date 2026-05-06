from typing import List


def common(list1: List, list2: List):
    return set(list1) & set(list2)


list_a = [1, 2, 3, 4, 5]
list_b = [4, 5, 6, 7, 8]

print(common(list_a, list_b))
