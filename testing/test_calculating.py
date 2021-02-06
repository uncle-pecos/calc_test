import pytest
from . import *
from calculating.calc_wo_brackets import calculating_w_out_br

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