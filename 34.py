
str1 = "The quick brown fox jumps over the lazy dog"
splitted = str1.split()
max_word = max(splitted,key=lambda x:len(x))

print(max_word)