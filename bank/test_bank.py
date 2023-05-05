import pytest
from bank import *


def test_value_with_hello():
    assert value("hello") == 0


def test_value_with_upper_case_hello():
    assert value("HELLO") == 0


def test_value_with_title_case_hello():
    assert value("Hello") == 0


def test_value_wth_H_letter():
    assert value("hey") == 20


def test_trail_str():
    assert value("   hello   ") == 0
    assert value("    hey  ") == 20
    assert value("   helo  ") == 20


def test_value_sentence():
    assert value("  hello man what's up?") == 0


def test_value_with_whatsup():
    assert value("what's up") == 100


def test_format_func():
    assert format_value(100) == "$100"
    assert format_value(20) == "$20"
    assert format_value(0) == "$0"


def test_value_None_word():
    with pytest.raises(ValueError) as val_err:
        value(None)
    assert str(val_err.value) == "greeting cannot be none!"


def test_value_empty_word():
    with pytest.raises(ValueError) as val_err:
        value("")
    assert str(val_err.value) == "greeting cannot be an empty string!"
