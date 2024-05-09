import numpy as np
import pytest

from src.v_eff import Veff

def test_import():
    pass

@pytest.fixture
def veff():
    return Veff(L=4.5)

def test_veff_init(veff):
    assert veff.L == 4.5
    assert veff._Eu is None
    assert veff._Es is None
    assert veff._Veff_values is None

@pytest.fixture
def veff_set():
    veff_set = Veff(4.5)
    veff_set.Veff_values
    return veff_set

def test_veff_Eu_setter(veff_set):
    Eu = veff_set.Eu
    assert Eu == pytest.approx((2*0.57)**(1/2), abs = 0.01)

def test_veff_Es_setter(veff_set):
    Es = veff_set.Es
    assert Es == pytest.approx((2*0.47)**(1/2), abs = 0.01)

#def test_Veff_values(veff_set):

def test_veff_calc_turning_points(veff_set):
    E = 0.979795
    expected_tp = [2.66319, 10.2518, 37.0828]
    turning_points = veff_set.calc_turning_points(E)
    assert np.allclose(turning_points, expected_tp)
