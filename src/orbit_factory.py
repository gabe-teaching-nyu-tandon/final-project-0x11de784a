from orbit import Orbit

class OrbitFactory:
    @staticmethod
    def create_orbit(L, E, Veff):
        orbit = Orbit(L, E, Veff)

        return orbit
    
    