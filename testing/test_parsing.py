import pytest
from . import *
from calculating.string_parsing import str_parse

def test_parsing():
    inp = '(1+2)'
    out = ['(', 1.0, '+', 2.0, ')']
    assert str_parse(inp) == out

def test_parsing1():
    inp = '1+2'
    out = [1.0, '+', 2.0]
    assert str_parse(inp) == out