
class Orbit():
    '''Abstract base class describing Orbit interface
    '''

    # All Orbit subclasses should will share __init__()
    def __init__(self, L, E, rmin, rmax, Veff):
        '''
        Parameters
        ----------

        L: angular momentum
        E: energy
        rmin: minimum r value
        rmax: maximum r value
        Veff: from Veff class

        '''
        self.L = L
        self.E = E
        self.rmin = rmin
        self.rmax = rmax
        self.Veff = Veff


