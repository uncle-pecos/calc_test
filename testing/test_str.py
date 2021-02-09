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

def test_str4():
    inp = ')1('
    out = False
    assert checking(inp) == out

def test_str5():
    inp = '11111111111111111111111111111111111111111111111111111111111111111111111111111111.0+1.001'
    out = '11111111111111111111111111111111111111111111111111111111111111111111111111111111.0+1.001'
    assert checking(inp) == out

def test_str6():
    inp = '--1'
    out = False
    assert checking(inp) == out

def test_str7():
    inp = '(35-(44-(58*2^6)+13-14)/2)'
    out = '(35-(44-(58*2^6)+13-14)/2)'
    assert checking(inp) == out