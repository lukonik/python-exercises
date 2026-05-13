s1 = "Abc"
s2 = "Xyz"

result = ""

s1_len = len(s1)
s2_len = len(s2)
max_len = max(s1_len, s2_len)

s2 = s2[::-1]

for i in range(0, max_len):
    if i < s1_len:
        result += s1[i]
    if i < s2_len:
        result += s2[i]

print(result)