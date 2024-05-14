from orbit import Orbit

class OrbitFactory:
    @staticmethod
    def create_orbit(L, E, Veff):
        orbit = Orbit(L, E, Veff)
        if E > Veff.Eu:
            raise ValueError("problem")

        return orbit
    
    