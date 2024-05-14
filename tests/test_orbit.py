from orbit import Orbit
from orbit_factory import OrbitFactory


def test_orbit_factory():
    L = 3.0
    E = 1.5
    rmin = 2.0
    rmax = 10.0
    Veff = 2.0 # in actual code this will be a function, but we will use a number for testing purposes

    created_orbit = OrbitFactory.create(L, E, rmin, rmax, Veff)

    assert isinstance(created_orbit, Orbit)



