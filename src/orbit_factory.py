from orbit import Orbit
from v_eff import Veff

class OrbitFactory:
    @staticmethod
    def create_orbit(L, E, category):
        if category == "category 1":
            veff = Veff(L)
            if E in veff.REGISTRY:
                rmin, rmax = veff.REGISTRY[E]
            else:
                rmin, rmax = veff.calc_turning_points(E)
        elif category == "category 2":
            pass
        elif category == "category 3":
            pass
        elif category == "category 4":
            pass

        orbit = Orbit(L, E, rmin, rmax, veff)

        return orbit
    
    