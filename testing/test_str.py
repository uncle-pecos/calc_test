import pytest
from . import *
from calculating.str_check import checking

def test_str():
    inp = '1+2'
    out = '1+2'
    assert checking(inp) == out

def test_str1():
    inp = '()'
    out = False
    assert checking(inp) == out

def test_str2():
    inp = ''
    out = False
    assert checking(inp) == out

def test_str3():
    inp = '(1)'
    out = '(1)'
    assert checking(inp) == out