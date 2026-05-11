import os


def process_files():
    for _,_,file_names in os.walk("49"):
        for file_name in file_names:
            joined = os.path.join("49",file_name)
            print(os.path.abspath(joined))

process_files()
