def write_and_read():
    with open("text.txt", "w") as file:
        file.writelines(["First line \n ", "Second Line \n", "Third Line \n"])

    with open("text.txt", "r",newline="\n") as file:
        return file.readlines()


print(write_and_read())