def find_str(text: str, sub_str: str):
    return text.rfind(sub_str)


str1 = "Emma is a data scientist who knows Python. Emma works at google."

print(find_str(str1, "Emma"))
