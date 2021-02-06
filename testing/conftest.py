import pytest
from . import *
from calculating.calc_main import Calc


@pytest.fixture
def supply_calc():
    return Calc()

