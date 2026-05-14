str1 = "hello world from python"


def first_capitalize(str1: str):
    return " ".join([word[0].upper() + word[1:] for word in str1.split()])


print(first_capitalize(str1))
