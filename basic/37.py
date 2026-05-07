import time
def countdown(timer: int):
    while timer >= 0:
        if timer == 0:
            print("Blast off")
            break
        print(timer, end=" ",flush=True)
        timer -= 1
        time.sleep(1)


countdown(5)
