def join_two_strings(s1: str, s2: str):
    s1_len = len(s1) // 2
    first_half = s1[:s1_len]
    second_half = s1[s1_len:]
    return first_half + s1 + second_half


print(join_two_strings("Ault", "Kelly"))
