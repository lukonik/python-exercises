from typing import List


def parity_merging(list_1: List[int], list_2: List[int]):
    odds_from_first = [value for value in list_1 if value % 2 != 0]
    evens_from_second = [value for value in list_2 if value % 2 == 0]
    return odds_from_first + evens_from_second


list1 = [10, 20, 25, 30, 35]
list2 = [40, 45, 60, 75, 90]

print(parity_merging(list1, list2))
