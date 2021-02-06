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