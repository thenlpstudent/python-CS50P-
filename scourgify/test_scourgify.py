from scourgify import *
from ErrorType import *


def test_check_file():
    error = create_error("Not a valid CSV file!")
    assert check_file(create_result("test.txt")) == error
    assert check_file(create_result("test.csv")) == create_result("test.csv")
    assert check_file(create_result(None)) == error


def test_parse_args():
    too_many_args_err = create_error("Too many arguments")
    too_few_args_err = create_error("Too few arguments")
    valid_input = create_result(["scourgify.py", "test.csv"])
    invalid_input_toomany = create_result(["scourgify.py", "test.csv", "abc.txt"])
    invalid_input_few = create_result(["scourgify.py"])

    assert parse_args(invalid_input_toomany) == too_many_args_err
    assert parse_args(invalid_input_few) == too_few_args_err
    assert parse_args(valid_input) == create_result("test.csv")


def test_transform_func():
    row = create_result(["Potter, Harry", "Gryffindor"])
    assert transform_row(row) == create_result(["Harry", "Potter", "Gryffindor"])


def test_read_csv_file_not_found():
    filename = create_result("invalid.csv")
    err = create_error("CSV file invalid.csv was not found!")

    assert read_csv(filename) == err
