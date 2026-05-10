import time
from threading import Thread


def download_file(url: str):
    print("Start downloading " + url)
    time.sleep(2)
    print("End download")


threads = [
    Thread(target=download_file, args=("A")),
    Thread(target=download_file, args=("B")),
    Thread(target=download_file, args=("C")),
    Thread(target=download_file, args=("D")),
    Thread(target=download_file, args=("E")),
    Thread(target=download_file, args=("F")),
]


for thread in threads:
    thread.start()


for thread in threads:
    thread.join()

print("FINISHED")