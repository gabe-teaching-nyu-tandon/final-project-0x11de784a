from src.orbit import Orbit
from src.orbit_factory import OrbitFactory
from src.v_eff_factory import VeffFactory
import numpy as np


def test_creating_orbit():
    L = 4.5
    E = 1
    category = 4

    created_orbit = OrbitFactory.create_orbit(L, E, category)

    assert isinstance(created_orbit, Orbit)


def test_orbit_factory():
    L = 4.5
    E = 0.979795
    orbit = OrbitFactory.create_orbit(L, E, 4)

    assert np.allclose(orbit.rmin, 10.2518)
    assert np.allclose(orbit.rmax, 37.0828)

    


