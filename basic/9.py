def count_vowels(string: str):
    vowels = set(["a", "e", "i", "o", "u"])
    return len([_ for _ in string if _ in vowels])


print(count_vowels('"Learning Python is fun!"'))