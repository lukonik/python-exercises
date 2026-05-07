def merge_dicts(dict1: dict, dict2: dict):
    dict_3 = {}
    for key in (dict1 | dict2).keys():
        if key in dict1 and key in dict2:
            dict_3[key] = dict1[key] + dict2[key]
        else:
            dict_3[key] = dict1[key] if key in dict1 else dict2[key]
    return dict_3


dict_a = {"a": 10, "b": 20}
dict_b = {"b": 5, "c": 15}

print(merge_dicts(dict_a, dict_b))
