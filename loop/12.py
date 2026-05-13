text = "Loops are Fun!"

vowels = set(["a", "e", "i", "o", "u"])

total = 0
another = 0
for letter in text:
    if not letter.isalpha():
        continue
    if letter in vowels:
        total += 1
    else:
        another += 1

print(total)
print(another)
