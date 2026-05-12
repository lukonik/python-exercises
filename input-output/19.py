fruit_list = ["Apple", "Banana", "Cherry", "Date"]

with open("19.txt","w") as file:
    file.writelines([f"{fruit}\n" for fruit in fruit_list])