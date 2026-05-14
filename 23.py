def remove_special(str1: str):
    return "".join([letter for letter in str1 if letter.isalnum() or letter.isspace()])


print(remove_special("/*Jon is @developer & musician!!"))
