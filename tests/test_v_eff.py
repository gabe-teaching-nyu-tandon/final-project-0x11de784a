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
    assert Eu == pytest.approx((2*0.57)**(1/2), abs = 0.01) #should be around 1.07

def test_veff_Es_setter(veff_set):
    Es = veff_set.Es
    assert Es == pytest.approx((2*0.47)**(1/2), abs = 0.01) #should be around 0.97 

#def test_Veff_values(veff_set):
#thousands of data values in Veff_values, not sure how to test

#test E such that Eu < E < 1, for expected values
def test_veff_calc_turning_points(veff_set):
    E = 0.979795
    expected_tp = [2.66319, 10.2518, 37.0828]
    turning_points = veff_set.calc_turning_points(E)
    assert np.allclose(turning_points, expected_tp)

#test calc_turning_points for correct number of roots for different scenarios of E
def test_correct_number_roots(veff_set):
    Eu = veff_set.Eu
    Es = veff_set.Es
    
    #double root at Eu
    double_root = veff_set.calc_turning_points(Eu)
    assert 2 == len(double_root)
    assert double_root[0] == double_root[1]
    
    #two roots for 1 < E < Eu
    assert 2 == len(veff_set.calc_turning_points(1.02))
    
    #two roots for E=1
    assert 2 == len(veff_set.calc_turning_points(1))
    
    #three roots for Es<E<1
    assert 3 == len(veff_set.calc_turning_points(0.99))

    #three roots for E = Es
    stable_roots = veff_set.calc_turning_points(Es)
    assert 3 == len(stable_roots)
    assert stable_roots[1] == stable_roots[2]

    #one root for E < Es
    assert 1 == len(veff_set.calc_turning_points(0.8))

#testing for different values of L = 4.5, E=1
def test_E_is_1_root(veff_set):
    expected = [2.7432530856, 7.3817469144]
    turning_points = veff_set.calc_turning_points(1)
    assert np.allclose(turning_points, expected)
    
#have tested for L > 4, now lets test roots for L < 4
@pytest.fixture
def veff_low():
    veff_low = Veff(3.9)
    veff_low.Veff_values
    return veff_low

def test_Eu_lower_L(veff_low):
    Eu = veff_low.Eu
    assert Eu < 1

def test_roots_lower_L(veff_low):
    Eu = veff_low.Eu
    Es = veff_low.Es
    expected = [3.48885, 5.28784, 41.2211]
    turning_points = veff_low.calc_turning_points(0.979795)
    assert np.allclose(turning_points, expected)
    assert 3 == len(veff_low.calc_turning_points(Es))
    assert 2 == len(veff_low.calc_turning_points(Eu))
    assert 0 == len(veff_low.calc_turning_points(1))
    
