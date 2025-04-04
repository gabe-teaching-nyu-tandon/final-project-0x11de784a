import numpy as np
import pytest

from src.v_eff import Veff
from src.v_eff_factory import VeffFactory

def test_import():
    pass

@pytest.fixture
def veff():
    return Veff(L=4.5)

#test initial creation of Veff object
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

#test the Eu and Es setters, these are marked as property of Veff class
def test_veff_Eu_setter(veff_set):
    Eu = veff_set.Eu
    assert Eu == pytest.approx((2*0.57)**(1/2), abs = 0.01) #should be around 1.07

def test_veff_Es_setter(veff_set):
    Es = veff_set.Es
    assert Es == pytest.approx((2*0.47)**(1/2), abs = 0.01) #should be around 0.97 

#def test_Veff_values(veff_set):
#thousands of data values in Veff_values, not sure how to test

def test_veff_at_r(veff):
    veff_r = veff.calc_veff_at_r(3)
    assert np.isclose(veff_r, 0.541667)

#test E such that Es < E < 1, for expected values
def test_veff_calc_turning_points(veff_set):
    E = 0.979795
    expected_tp = [2.66319, 10.2518, 37.0828]
    turning_points = veff_set.calc_turning_points(E)
    assert np.allclose(turning_points, expected_tp)

#test calc_turning_points for correct number of roots for different scenarios of E, for L > 4
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
    #check correct number of roots
    assert 3 == len(veff_low.calc_turning_points(Es))
    assert 2 == len(veff_low.calc_turning_points(Eu))
    assert 0 == len(veff_low.calc_turning_points(1))
    

#now test for L < sqrt(12)
@pytest.fixture
def veff_3():
    veff_3 = Veff(3.4)
    veff_3.Veff_values
    return veff_3

def test_veff_3_E_setters(veff_3):
    Eu = veff_3.Eu
    Es = veff_3.Es
    assert Eu is not None
    assert Es is not None

#test REGISTRY of E : [r_values] inside Veff(L)
def test_registry_E_r(veff_set):
    r_vals1 = veff_set.calc_turning_points(0.98)
    r_vals2 = veff_set.calc_turning_points(1)
    r_from_registry = veff_set.REGISTRY.get(0.98)
    assert r_vals1 == r_from_registry
    assert 2 == len(veff_set.REGISTRY)

def test_different_registries(veff_set, veff_low):
    r_vals1 = veff_set.calc_turning_points(1)
    r_vals2 = veff_low.calc_turning_points(1)
    assert veff_set.REGISTRY.get(1) != veff_low.REGISTRY.get(1)


#############################################################

#Ltes now test VeffFactory class
@pytest.fixture
def factory():
    return VeffFactory()

def test_vefffactory_instance(factory):
    veff = factory.create(L=4.3)
    assert isinstance(veff, Veff)

def test_vefffactory_registry(factory):
    veff = factory.create(L=4.2)
    assert factory.REGISTRY.get(4.2) == veff
