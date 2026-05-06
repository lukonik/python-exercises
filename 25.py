def leap_year(year: int):
    if year % 100 == 0 and year % 400 != 0:
        return False
    return year % 4 == 0

print(leap_year(2024))