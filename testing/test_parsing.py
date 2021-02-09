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

def test_parsing2():
    inp = '(35-(44-(58*2^6)+13-14)/2)'
    out = ['(', 35.0, '-', '(', 44.0, '-', '(', 58.0, '*', 2.0, '^', 6.0, ')', '+', 13.0, '-', 14.0, ')', '/', 2.0, ')']