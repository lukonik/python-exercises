s1 = "ABC"
s2 = "xyz"

result = [value1 + value2 for value1, value2 in zip(s1, s2)]

print("".join(result))
