import random
import sys
from pyfiglet import Figlet


def main(args):
    figlet = Figlet()
    if len(args) == 1:
        f = get_random_font(figlet)
        figlet.setFont(font=f)
    elif len(args) == 3:
        if args[1] not in ["-f", "--font"] or args[2] not in figlet.getFonts():
            exit_program()
        else:
            figlet.setFont(font=args[2])
    elif len(args) >= 2:
        exit_program()

    text = input("Input: ")
    print(f"Output: {figlet.renderText(text)}")


def exit_program():
    print("Invalid usage")
    sys.exit()


def get_random_font(figlet):
    return random.choice(figlet.getFonts())


if __name__ == "__main__":
    main(sys.argv)