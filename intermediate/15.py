def symm_diff(a: list[int], b: list[int]):
    set_a = set(a)
    set_b = set(b)
    return set_a.symmetric_difference(set_b)


list1 = [101, 102, 103]
list2 = [103, 104, 105]

print(symm_diff(list1, list2))
