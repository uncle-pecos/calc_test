import pytest
from main import str_parse
from main import final
from main import main

def test_main():
    inp = '((2-3))'
    res = -1
    assert main(inp) == res
def test_main1():
    inp = '  (  -1)'
    res = -1
    assert main(inp)    
