from orbit import Orbit
from v_eff import Veff
from v_eff_factory import VeffFactory

class OrbitFactory:
    '''
     A factory class for creating Orbit objects based on specified parameters and categories.
    '''
    @staticmethod
    def create_orbit(L: float, E: float, category: int) -> Orbit:
        '''
        Creates an Orbit object based on the angular momentum, energy, and category.

        Parameters:
        L (float): Angular momentum of the orbiting body.
        E (float): Energy of the orbiting body.
        category (int): Category determining the type of orbit to create.

        Returns:
        Orbit: An Orbit object with the specified parameters.

        Raises:
        ValueError: If the category is not recognized or if the required roots are not found.
        '''
        if category == 1:
            pass
        elif category == 2:
            pass
        elif category == 3:
            pass
        elif category == 4:
            veff_factory = VeffFactory()
            veff = veff_factory.create(L)
            roots = veff.calc_turning_points(E)
            if len(roots) == 2:
                rmin, rmax = roots
            elif len(roots) == 3:
                rmin, rmax = roots[1:]
            else:
                raise ValueError("Invalid number of turning points found for category 4.")
        else:
            raise ValueError("Unrecognized category.")

        orbit = Orbit(L, E, rmin, rmax, veff)

        return orbit
    
    