import pytest
from . import *
from calculating.brackets_del import brackets
from calculating.calc_wo_brackets import calculating_w_out_br
from calculating.string_parsing import str_parse
from calculating.str_check import checking

def test_check_parse():
    inp = '(258.0+25/3)'
    res = ['(', 258.0, '+', 25.0, '/', 3.0, ')']
    assert str_parse(checking(inp)) == res

def test_check_parse1():
    inp = '(258.0+(25/3))'
    res = ['(', 258.0, '+', '(', 25.0, '/', 3.0, ')', ')']
    assert str_parse(checking(inp)) == res

def test_del_calc():
    inp = ['(', 258.0, '+', '(', 25.0, '*', 3.0, ')', ')']
    res = 75
    assert calculating_w_out_br(brackets(inp))

def test_del_calc1():
    inp = ['(', 258.0, '+', 11, ')']
    res = 269
    assert calculating_w_out_br(brackets(inp))

def test_del_calc2():
    inp = ['(', 999999.0, '^', 999999.0, '+', 1.0 , ')']
    res = 'Result too large'
    assert calculating_w_out_br(brackets(inp))