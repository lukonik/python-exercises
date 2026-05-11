def crypt_by_shift(text: str, shift: int):
    return "".join([chr(ord(letter) + shift) for letter in text])


print(crypt_by_shift("Hello", 3))
