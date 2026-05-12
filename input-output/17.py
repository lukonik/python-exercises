import getpass

username = input("Enter username: ")
password = getpass.getpass("Enter the password: ")

print(f"Login successfull for user: {username}, with password: {password}")

