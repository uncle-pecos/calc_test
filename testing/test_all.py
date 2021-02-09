import pytest
from . import *
from calculating.brackets_del import brackets
from calculating.calc_wo_brackets import calculating_w_out_br
from calculating.string_parsing import str_parse
from calculating.str_check import checking
from calculating.finalizing import final
from calculating.priority import priority
from calculating.return_res import return_res



def test_test_br():
    arr = ['(', 15.0, '-', '(', 5.0, '+', 4.0, ')', ')']
    out = [5.0, '+', 4.0]
    assert brackets(arr) == out

@pytest.mark.parametrize("a, b, ans", [(1, 2, 3)])
def test_plus(supply_calc, a, b, ans):
    assert supply_calc.plus(a, b) == ans, "addition is bad"


@pytest.mark.parametrize("a, b, ans", [(1, 2, -1)])
def test_minus(supply_calc, a, b, ans):
    assert supply_calc.minus(a, b) == ans, "minus isbad"


@pytest.mark.parametrize("a, b, ans", [(4, 3, 12), (4, 0, 0), (0, 0, 0)])
def test_mult(supply_calc, a, b, ans):
    assert supply_calc.mult(a, b) == ans, "multi is bad"


@pytest.mark.parametrize("a, b, ans", [(120, 6, 20), (1, 0, 'zero division'), (0, 0, 'zero division' )])
def test_divis(supply_calc, a, b, ans):
    assert supply_calc.divis(a, b) == ans, "division is bad"

@pytest.mark.parametrize("a, b, ans", [(2, 4, 16), (0, 900, 0), (98, 1, 98), (98, 0, 1), (0, 0, 1)])
def test_sterp(supply_calc, a, b, ans):
    assert supply_calc.step(a, b) == ans, "multi step is bad"

def test_calculating():
    t_arr = [3.0, '+', 4.0]
    result = 7
    assert calculating_w_out_br(t_arr) == result

def test_calculating1():
    t_arr = [0, '-', 0]
    result = 0
    assert calculating_w_out_br(t_arr) == result

def test_calculating2():
    t_arr = [0, '-', 0, '^', 0]
    result = -1
    assert calculating_w_out_br(t_arr) == result

def test_calculating3():
    t_arr = [0, '/', 0]
    result = 'zero division'
    assert calculating_w_out_br(t_arr) == result 

def test_final():
    arr = ['(', 5.0, '+', '(', 0, '-', 2.0, ')', ')']
    res = 3
    assert final(arr) == res

def test_final1():
    arr = ['(', 5.0, '+', '(', 0, '-', 2.0, ')', ')', ')']
    res = 'input data error (brackets mismatch)'
    assert final(arr) == res

def test_final2():
    arr = ['(', 35.0, '-', '(', 44.0, '-', '(', 58.0, '*', 2.0, '^', 6.0, ')', '+', 13.0, '-', 14.0, ')', '/', 2.0, ')']
    res = 1869.5
    assert final(arr) == res

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

def test_priority():
    znak = '+'
    out = 2
    assert priority(znak) == out

def test_priority1():
    znak = '^'
    out = 0
    assert priority(znak) == out  

def test_priority2():
    znak = '/'
    out = 1
    assert priority(znak) == out 

def test_return():
    znak = '+'
    a = 0
    b = 1
    res = 1
    assert return_res(znak, a, b) == res

def test_return1():
    znak = '+'
    a = 2
    b = 3
    res = 5
    assert return_res(znak, a, b) == res

def test_return2():
    znak = '-'
    a = 2
    b = 3
    res = -1
    assert return_res(znak, a, b) == res

def test_return3():
    znak = '*'
    a = 2
    b = 3
    res = 6
    assert return_res(znak, a, b) == res

def test_return4():
    znak = '*'
    a = 2
    b = 0
    res = 0
    assert return_res(znak, a, b) == res

def test_return5():
    znak = '/'
    a = 150
    b = 3
    res = 50
    assert return_res(znak, a, b) == res

def test_return6():
    znak = '/'
    a = 2
    b = 0
    res = 'zero division'
    assert return_res(znak, a, b) == res

def test_return7():
    znak = '^'
    a = 2
    b = 0
    res = 1
    assert return_res(znak, a, b) == res

def test_return8():
    znak = '^'
    a = 12
    b = 2
    res = 144
    assert return_res(znak, a, b) == res

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