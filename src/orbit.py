from src.v_eff import Veff


class Orbit():
    '''
    Class to represent an orbit object which holds the following attributes.

    Attributes:
    L (float): Angular momentum of the orbiting body.
    E (float): Energy of the orbiting body.
    rmin (float): Minimum radius of the orbit.
    rmax (float): Maximum radius of the orbit.
    Veff (Veff): Effective potential function for the orbit.
    '''

    def __init__(self, L: float, E: float, rmin: float, rmax: float, Veff: Veff):
        self.L = L
        self.E = E
        self.rmin = rmin
        self.rmax = rmax
        self.Veff = Veff


