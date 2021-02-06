import pytest
from . import *
from calculating.priority import priority

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