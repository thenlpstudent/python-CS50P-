# This task uses monads which makes writing testable functions easier with no side effects!
# Author: Chirath Nissanka -> twitter.com/chiratnissanka aka @thenlpstudent

import csv
import pathlib
import sys
from ErrorType import *

CSV_SUFFIX = ".csv"
TRANSFORMED_FILE_NAME = "transformed.csv"


def main(args):
    arguments = create_result(args)
    file_name = pipe(arguments, parse_args)
    file_name = pipe(file_name, check_file)
    transformed_data = pipe(file_name, read_csv)
    transformed_data = pipe(transformed_data, sort_list)
    pipe(transformed_data, write_csv)
    print("Done!")


def check_file(value: ErrorType, suffix=CSV_SUFFIX):
    if value.result and pathlib.Path(value.result).suffix == suffix:
        return create_result(value.result)
    else:
        return create_error("Not a valid CSV file!")


def parse_args(value: ErrorType):
    try:
        if len(value.result) > 2:
            return create_error("Too many arguments")
        return create_result(value.result[1])
    except IndexError:
        return create_error("Too few arguments")


def read_csv(filename: ErrorType):
    try:
        with open(filename.result) as csv_file:
            reader = csv.reader(csv_file)
            transformed_rows = []
            for index, row in enumerate(reader):
                if index != 0:
                    transformed_row = pipe(create_result(row), transform_row)
                    transformed_rows.append(transformed_row.result)
            return create_result(transformed_rows)
    except FileNotFoundError:
        return create_error(f"CSV file {filename.result} was not found!")


def write_csv(transformed_data: ErrorType, filename=TRANSFORMED_FILE_NAME):
    try:
        with open(filename, "w") as csv_file:
            result = transformed_data.result
            writer = csv.writer(csv_file)
            writer.writerow(["first", "last", "house"])

            for row in result:
                writer.writerow(row)

        return transformed_data
    except Exception:
        return create_error(f"Error occurred when writing transformed csv : {filename}")


def transform_row(row: ErrorType):
    name, house = row.result
    lastname, firstname = name.split(",")
    return create_result([firstname.strip(), lastname.strip(), house])


def sort_key(row):
    return f"{row[0]} {row[1]}"


def sort_list(rows: ErrorType, key_func=sort_key):
    new_rows = []
    for row in sorted(rows.result, key=sort_key):
        new_rows.append(row)
    return create_result(new_rows)


if __name__ == "__main__":
    main(sys.argv)
