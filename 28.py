data = {"banana": 3, "apple": 5, "cherry": 1, "date": 4}


sort = {key: data[key] for key in sorted(data.keys())}

print(sort)