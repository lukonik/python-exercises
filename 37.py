lst1 = ["Hello ", "Take "]
lst2 = ["Dear", "Sir"]


combined = [v1 + v2 for v1 in lst1 for v2 in lst2]


print(combined)