l1 = [3, 6, 9, 12, 15, 18, 21]
l2 = [4, 8, 12, 16, 20, 24, 28]

odd_l1 = [item for index, item in enumerate(l1) if index % 2 == 1]
even_l2 = [item for index, item in enumerate(l2) if index % 2 == 0]

lst = odd_l1 + even_l2

print(lst)