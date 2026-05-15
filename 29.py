scores = {"Alice": 88, "Bob": 72, "Charlie": 95, "Diana": 60}
sort_by_values = sorted(scores.items(), key=lambda data: data[1])

print(dict(scores))
