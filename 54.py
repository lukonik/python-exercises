def password_checker(password: str):
    chekcs = [
        len(password) >= 8,
        any([letter.isdigit() for letter in password]),
        any([letter.isalnum() for letter in password]),
        any([letter.isupper() for letter in password]),
        any([letter.islower() for letter in password]),
    ]

    return sum(chekcs)


print(password_checker("P@ss123"))
