import random


def random_number():
    chosen_number = random.randint(0, 100)
    i = 0
    while i <= 10:
        guess = input("Tell the value: ")
        guess_int = int(guess)

        if guess_int == chosen_number:
            print("You guessed it goot call! ")
            break

        if guess_int < chosen_number:
            print("Higher")
        else:
            print("Lower")

        i += 1
    else:
        print("No more tries sorry the value was " + str(chosen_number))


random_number()