def merge_dicts(dict1: dict, dict2: dict):
    merged = {}
    for key in dict1.keys() | dict2.keys():
        if key in dict1 and key in dict2:
            merged[key] = (dict1[key], dict2[key])
        else:
            merged[key] = dict1[key] if key in dict1 else dict2[key]
    return merged


d1 = {"a": 1, "b": 2}
d2 = {"b": 3, "c": 4}


print(merge_dicts(d1, d2))
