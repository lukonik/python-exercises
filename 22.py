import os
stat=os.stat("22.text")

if not stat.st_size:
    print("file is empty")