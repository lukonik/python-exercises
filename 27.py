def palindrome(s1: str):
    for i in range(0, len(s1)):
        if s1[i] != s1[i]:
            return False
    return True

str1 = "radar"
print(palindrome(str1))