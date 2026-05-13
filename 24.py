str1 = "I am 25 years and 10 months old"


only_integers = [letter for letter in str1 if letter.isdigit()]

print(int("".join(only_integers)))
