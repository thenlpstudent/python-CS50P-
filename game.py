import random
import sys


def main():
    n = get_level()
    random_num = random.randint(1, n)

    while True:
        guess = get_guess()
        if guess > random_num:
            print("Too Large!")
        elif guess < random_num:
            print("Too Small!")
        else:
            print("Just right!")
            sys.exit()


def get_guess():
    while True:
        try:
            guess = int(input("Guess: "))
            if guess > 0:
                return guess
        except ValueError:
            continue


def get_level():
    while True:
        try:
            n = int(input("Level: "))
            if n > 0:
                return n
        except ValueError:
            continue


if __name__ == "__main__":
    main()
