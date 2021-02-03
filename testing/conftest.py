import pytest
from . import *
from calculating.calc_main import Calc
from calculating.calc_wo_brackets import calculating_w_out_br


@pytest.fixture
def supply_calc():
    return Calc()

@pytest.fixture
def supply_calculating():
    return calculating_w_out_br()
