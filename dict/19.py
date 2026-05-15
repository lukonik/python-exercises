scores = {"Alice": 82, "Bob": 45, "Carol": 91, "Dave": 58, "Eve": 73}

updated = {key: value for (key, value) in scores.items() if value > 60}

print(updated)