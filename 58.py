import re

email_val = re.compile(r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$")


def validate_email(email: str):
    return bool(email_val.match(email))


email1 = "python_pro@gmail.com"
email2 = "bad-email@com"

print(validate_email(email1))
print(validate_email(email2))
