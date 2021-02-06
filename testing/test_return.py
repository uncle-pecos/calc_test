import pytest
from . import *
from calculating.return_res import return_res

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