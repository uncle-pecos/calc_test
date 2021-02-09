import pytest
from . import *
from calculating.finalizing import final

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