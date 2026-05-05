def palindrome(value: int):
    stringified_value = str(value)
    for index, v in enumerate(stringified_value):
        if stringified_value[index] != stringified_value[-(index+1)]:
            return False

    return True

is_palindrome_1=palindrome(121)
is_palindrome_2 = palindrome(125)

print("Is palindrome: ",is_palindrome_1)
print("Is palindrome: ",is_palindrome_2)
