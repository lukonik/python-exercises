def is_unique_char(str1: str):
    return len(set(str1)) == len(str1)


str1 = "python"
str2 = "alphabet"

print("Is unique " + str(is_unique_char(str1)))

print("Is unique " + str(is_unique_char(str2)))
