lst_1 = ["Py", "is", "awes"]
lst_2 = ["thon", " ", "ome"]


lst_3 = [v1 + v2 for (v1, v2) in zip(lst_1, lst_2)]

print(lst_3)