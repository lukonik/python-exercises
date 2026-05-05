def function(value: str):
    return value[::2]


only_even = function("pynative")

for char in only_even:
    print(char)