import tabulate
import csv
import pathlib
import sys

TABLE_FMT = "grid"
CSV_SUFFIX = ".csv"


def main(args):
    filename = check_file(parse_args(args))
    headers, table = get_table_data(filename)
    print(tabulate.tabulate(table, headers=headers, tablefmt=TABLE_FMT))


def exit_program(message):
    print(f"[Error]:{message}")
    sys.exit()


def check_file(filename, suffix=CSV_SUFFIX):
    if filename and pathlib.Path(filename).suffix == suffix:
        return filename
    else:
        exit_program("Invalid file")


def parse_args(args):
    try:
        if len(args) > 2:
            sys.exit("Too many arguments")
        return args[1]
    except IndexError:
        sys.exit("Too few arguments")


def get_table_data(filename):
    try:
        with open(filename) as csv_file:
            reader = csv.reader(csv_file)
            table = []
            for row in reader:
                table.append(row)
            return "firstrow", table

    except FileNotFoundError:
        sys.exit(f"Cannot find file to open: {filename}")


if __name__ == "__main__":
    main(sys.argv)
