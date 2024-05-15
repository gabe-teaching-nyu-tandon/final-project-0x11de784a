from orbit import Orbit
from orbit_factory import OrbitFactory


def test_orbit_factory():
    L = 3.0
    E = 1.5
    category = 1

    created_orbit = OrbitFactory.create(L, E, category)

    assert isinstance(created_orbit, Orbit)



