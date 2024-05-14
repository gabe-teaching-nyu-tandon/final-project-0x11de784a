from src.v_eff import Veff

class VeffFactory:
    """
    A factory class for creating instances of the Veff class for different angular momentum (L).

    Attributes:
        REGISTRY (dict): A dictionary to store instances of Veff for different L values.

    Methods:
        create(L: float) -> Veff:
            Creates and returns an instance of the Veff class for the given angular momentum L.
            If an instance for the given L already exists, returns the existing object.
    """

    def __init__(self):
        self.REGISTRY = {}  # Registry to store Veff objects for different L values

    def create(self, L: float) -> Veff:
        # Check if a Veff instance for the given L already exists in the registry
        if L in self.REGISTRY:
            return self.REGISTRY[L]

        # If not, create a new Veff instance for the given L
        veff_instance = Veff(L)
        
        #Update the registry
        self.REGISTRY[L] = veff_instance

        return veff_instance
