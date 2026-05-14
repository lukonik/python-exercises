def remove_duplicates(str1: str):
    data = dict(((letter, letter) for letter in str1))
    return "".join(data.keys())


str1 = "google"

print(remove_duplicates(str1))
