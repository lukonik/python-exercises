def n_removal(str1: str, n: int):
    return str(str1[:n] + str1[n + 1 :])


str1 = "Python"

print(n_removal(str1, 2))
