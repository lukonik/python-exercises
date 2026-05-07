def sets_compare(a: list, b: list):
    set_a = set(a)
    set_b = set(b)
    if set_a.issuperset(set_b):
        return "a is superset to b"
    if set_a.issubset(set_b):
        return "a is subset to b"
    if set_a.isdisjoint(set_b):
        return "a is disjoint b"


print(sets_compare([1, 2, 3], [1, 2, 3, 4, 5]))
