import secrets


def random_password_generator(length: int):
    return secrets.token_urlsafe(length)


print(random_password_generator(16))
