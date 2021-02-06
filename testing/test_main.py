import pytest
from main import str_parse
from main import final
from main import main_c

def test_main():
    inp = '((2-3))'
    res = -1
    assert main_c(inp) == res
