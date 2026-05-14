s1 = "waterbottle"
s2 = "erbottlewat"


def is_rotation(s1: str, s2: str):
    s1_sort = sorted(s1)
    s2_sort = sorted(s2)

    if len(s1_sort) != len(s2_sort):
        return False

    for index, _ in enumerate(s1_sort):
        if s1_sort[index] != s2_sort[index]:
            return False
    return True

print(f"Is rotation: {is_rotation(s1, s2)}")
