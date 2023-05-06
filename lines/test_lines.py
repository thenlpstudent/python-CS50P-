import pytest
from lines import *

def test_process_line():
    assert process_line(" # this is a comment") == 0
    assert process_line("#this is a comment") == 0
    assert process_line(" print('helloworld') ") == 1
    assert process_line("") == 0