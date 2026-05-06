def merge_dicts(dict1: dict, dict2: dict):
    return dict1 | dict2


dict1 = {"name": "Alice", "age": 25}
dict2 = {"city": "New York", "job": "Engineer"}

print(merge_dicts(dict1, dict2))
