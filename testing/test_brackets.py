import pytest
from . import *
from calculating.brackets_del import brackets

def test_br_del():
    arr = ['(', 15.0, '-', '(', 5.0, '+', 4.0, ')', ')']
    out = [5.0, '+', 4.0]
    assert brackets(arr) == out