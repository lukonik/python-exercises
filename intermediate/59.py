file_name = "59.text"


def add_task(task: str):
    with open(file_name, "a") as file:
        file.write(task)


def view_list():
    try:
        with open(file_name, "r") as file:
            print("Task is")
            for line in file:
                print(line)
    except FileNotFoundError:
        print("Tasks are empty for now")


def clear_list():
    try:
        with open(file_name, "w") as file:
            file.write("")
    except FileNotFoundError:
        print("Tasks doesn't exists")


while promp := input("TODO LIST: commands: [clear,view,add:task]: "):
    if promp == "clear":
        clear_list()
    elif promp == "view":
        view_list()
    elif "add" in promp:
        add_task(promp.split(":")[1])


print("Goodbye!")
