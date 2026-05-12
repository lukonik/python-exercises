names = ["Alice", "Bob", "Charlie"]
scores = [85, 92, 78]


print(f"{'Name':<10} Score")
print("-" * 20)

for name, value in zip(names, scores):
    print(f"{name:<10} {value}")
