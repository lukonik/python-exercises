vowels = set(["a", "e", "i", "o", "u"])

str1 = "Hello World"

total = 0

for i in str1:
    if i in vowels:
        total += 1

print(total)