from collections import Counter

str1 = "apple banana apple cherry banana apple"


count = Counter(str1.split(" "))


print(count)