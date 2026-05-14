from itertools import count

str1 = "P@#yn26at^&i5ve"

all_digits = len([item for item in str1 if item.isdigit()])
all_alpha = len([item for item in str1 if item.isalpha()])
all_letters = len([item for item in str1 if item.isascii()])


print(f"Digits: {all_digits}, Alpha: {all_alpha}, Letters: {all_letters}")