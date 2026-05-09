names = ["Alice", "Bob", "Charlie"]
scores = [85, 92, 78]

for index, (name, score) in enumerate(
    sorted(zip(names, scores), key=lambda x: x[1], reverse=True)
):
    print(f"Rank: {index + 1}: {name} scores: {score}")
