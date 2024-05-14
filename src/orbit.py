from v_eff import Veff


class Orbit():

    def __init__(self, L, E, Veff):
        self.L = L
        self.E = E
        self.Veff = Veff(L)
        self.roots = self.Veff.REGISTRY[E]
        self.circ = None  # checks if it is a circle


