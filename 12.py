global_var = 10


def change_global():
    global global_var
    global_var = 20


print(f"Initial {global_var}")
change_global()
print(f"Modified: {global_var}")