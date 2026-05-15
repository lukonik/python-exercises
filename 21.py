scores = {"Alice": 88, "Bob": 95, "Carol": 72, "Dave": 95, "Eve": 84}

max_key = max(scores, key=scores.get)


print(max_key)