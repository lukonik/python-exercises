def swap(str1: str):
    return "".join(
        ([letter.lower() if letter.isupper() else letter.upper() for letter in str1])
    )


str1 = "PyThOn"

print(swap(str1))
