from pizza import *


def test_check_file():
    assert check_file("regular.csv") == "regular.csv"


def test_parse_args():
    assert parse_args(["pizza.py", "regular.csv"]) == "regular.csv"

# need to use the monad design pattern to test errors
