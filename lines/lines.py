import sys
from pathlib import Path


def main(args):
    file_name = get_file_name(args)
    check_file_format(file_name)

    try:
        count = 0
        with open(file_name) as code_file:
            for line_no, line in enumerate(code_file):
                count += process_line(line)
                if (process_line(line) == 1):
                    print(line_no, line)
        print(count)
    except FileNotFoundError:
        exit_program("File does not exist")


def get_file_name(args):
    if len(args) <= 1:
        exit_program("Too few command-line arguments")
    if len(args) > 2:
        exit_program("Too many command-line arguments")
    return args[1]


def check_file_format(fname):
    if Path(fname).suffix != ".py":
        exit_program("Not a Python file")


def process_line(line):
    line = line.strip()
    try:
        return 0 if line == "" or line[0] == "#" else 1
    except Exception:
        return 0


def exit_program(message):
    print(message)
    sys.exit()


if __name__ == "__main__":
    main(sys.argv)
