import pytest
from twttr import *


def test_shorten_lowercase():
    shorten_text = shorten("hello world")
    assert shorten_text == "hll wrld"


def test_shorten_capitalwords():
    shorten_text = shorten("HELLO WORLD")
    assert shorten_text == "HLL WRLD"


def test_shorten_mixed_words():
    shorten_text = shorten("HeLo WoOrLLeed")
    assert shorten_text == "HL WrLLd"


def test_shorten_none_input():
    with pytest.raises(ValueError):
        shorten(None)


def test_shorten_none_err_message():
    with pytest.raises(ValueError) as val_err:
        shorten(None)

    assert str(val_err.value) == "Parameter word cannot be null!"
