def is_palindrome(text: str):
    cleaned_text = "".join([char.lower() for char in text if char.isalnum()])
    return (cleaned_text[::]) == (cleaned_text[::-1])


print(is_palindrome("A man, a plan, a canal: Panama"))
