def reverse_word_only(text: str):
    return str(["".join((reversed(word))) for word in text.split(" ")])


print(reverse_word_only("Python is awesome"))
