import string

str1 = "/*Jon is @developer & musician!!"

punctuation = string.punctuation


for i in punctuation:
    str1 = str1.replace(i, "#")

print(str1)
