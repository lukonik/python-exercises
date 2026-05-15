data = ["apple", "pie", "banana", "kiwi", "pear"]
k = 5


filtered = [value for value in data if len(value) >= k]

print(filtered)
