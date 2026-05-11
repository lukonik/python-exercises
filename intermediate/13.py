def sort_employes(employes: list[dict]):
    return sorted(employes, key=lambda e: e["salary"], reverse=False)


employees = [
    {"name": "A", "salary": 50},
    {"name": "B", "salary": 70},
    {"name": "C", "salary": 60},
]
print(sort_employes(employees))
