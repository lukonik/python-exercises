data = [1, [2, [3, 4], 5], 6, [7, 8]]


def flatten(data: list, flattened):
    for item in data:
        if isinstance(item, list):
            flatten(item, flattened)
        else:
            flattened.append(item)


output = []

print(flatten(data, output))

print(output)