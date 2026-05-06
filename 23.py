def is_palindrome(value: int):
    str_value = str(value)
    reverse_str = str_value[::-1]
    is_palindrome = str_value == reverse_str
    return is_palindrome


print(is_palindrome(1221))
