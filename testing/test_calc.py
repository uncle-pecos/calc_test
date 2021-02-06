import pytest


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
    try:
        supply_calc.divis(a, b)
    except:
        assert False, 'zero division'
    assert supply_calc.divis(a, b) == ans, "division is bad"

@pytest.mark.parametrize("a, b, ans", [(2, 4, 16), (0, 900, 0), (98, 1, 98), (98, 0, 1), (0, 0, 1)])
def test_sterp(supply_calc, a, b, ans):
    assert supply_calc.step(a, b) == ans, "multi step is bad"