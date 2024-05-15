from src.orbit import Orbit
from orbit_factory import OrbitFactory
from v_eff_factory import VeffFactory
import numpy as np


def test_creating_orbit():
    L = 3.0
    E = 1.5
    category = 4

    created_orbit = OrbitFactory.create(L, E, category)

    assert isinstance(created_orbit, Orbit)


def test_orbit_factory():
    L = 4.5
    E = 0.979795
    orbit = OrbitFactory.create(L, E, 4)

    assert np.allclose(orbit.rmin, 10.2518)
    assert np.allclose(orbit.rmax, 37.0828)

    


