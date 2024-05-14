import numpy as np
from scipy.optimize import fsolve
from typing import List

class Veff:
    """
    This class represents the effective potential in orbital mechanics.

    Attributes:
        L (float): The angular momentum of the orbit.

    Properties:
        Veff_values (ndarray[(r, Veff)]): An array of Veff values calculated for a range of r values.
        Eu (float): Unstable energy. The energy at the peak of the effective potential.
        Es (float): Stable energy. The energy at the saddle point of the effective potential.

    Methods:
        calc_Veff_at_r(r: float) -> float
            Calculates the Veff value at a single r value.
        calc_turning points(E: float) -> List[float] 
            Calculates the turining points of the effective potential energy equation for a given energy E.

    REGISTRY (dict): 
        A dictionary to store the calculated turning points for different values of E.
        The keys are the values of E, and the values are lists of turning points corresponding to each E.
    """

    def __init__(self, L: float):
        self.L = L
        self.REGISTRY = {}
        self._Veff_values = None
        self._Eu = None
        self._Es = None

    @property
    def Veff_values(self):
        #Calculate Veff_values for a set range of radius using the effective potential equation.
        if not isinstance(self._Veff_values, np.ndarray):
            r_values = np.linspace(0.1, 10**4, 2**20)  # Example range of r values
            veff = 0.5 - (1 / r_values) + ((self.L ** 2) / (2* r_values**2)) - ((self.L**2) / (r_values**3))
            self._Veff_values = np.column_stack((r_values, veff))
        return self._Veff_values

    @property
    def Eu(self):
        #Calculate the unstable effective energy, which is the local maxima of Veff_values, then E_eff = E^2/2 so E = sqrt(2*E_eff)
        if self.L > (12**(1/2)) or self.L ==(12**(1/2)): #Is L above L_{ISCO}
            if not self._Eu:
                #calculate where the derivative of Veff is changing sign from + to -, local maxima
                diff_Veff = np.diff(self._Veff_values[:, 1])
                max_indices = np.where((np.sign(diff_Veff[:-1]) > 0) & (np.sign(diff_Veff[1:]) < 0))[0] + 1
                max_Veff = self._Veff_values[max_indices, 1][0]
                self._Eu = (2 * max_Veff) ** (1/2)
        elif self.L < (12**(1/2)): #If L below L_{ISCO}, then Eu = Es
            self._Eu = self.Es
        return self._Eu

    @property
    def Es(self):
        #Calculate the stable effective energy, which the local minima of Veff_values, then E_eff = E^2/2 so E = sqrt(2*E_eff)
        if self.L > (12**(1/2)) or self.L == (12**(1/2)): #Is L above L_{ISCO}
            if not self._Es:
                #calculate where the derivative of Veff is changing sign from - to +, local minima
                diff_Veff = np.diff(self._Veff_values[:, 1])
                min_indices = np.where((np.sign(diff_Veff[:-1]) < 0) & (np.sign(diff_Veff[1:]) > 0))[0] + 1
                min_Veff = self._Veff_values[min_indices, 1][0]
                self._Es = (2 * min_Veff) ** (1/2)
        elif self.L < (12**(1/2)): #If L below L_{ISCO}
            if not self._Es:
                #calculate the second derivative of Veff.
                veff_values = self.Veff_values[:, 1]
                second_derivative = np.diff(np.diff(veff_values))
                min_indices = np.where(second_derivative > 0)[0] + 1  # Add 1 to get the correct index
                if min_indices.size > 0:  # Check if min_indices is not empty
                    min_Veff = veff_values[min_indices][0]  # Take the first minimum found
                    self._Es = (2 * min_Veff) ** 0.5
                else:
                    # If no local minima are found, set Es to None or handle accordingly
                    self._Es = None        
        return self._Es
    
    #calculate Veff at any given r
    def calc_veff_at_r(self, r: float) -> float:
        return 0.5 - (1 / r) + ((self.L ** 2) / (2*r**2)) - ((self.L**2) / (r**3))

    
    #find the intersection points between the Veff values and the Eeff value. 
    def calc_turning_points(self, E: float) -> List[float]:
        Eu = self.Eu
        Es = self.Es

        if E is None:
            raise ValueError("Energy given is not of type float.")
        
        #check if roots for this E are already in REGISTRY
        if E in self.REGISTRY:
            return self.REGISTRY[E]
        #else, lets calculate the roots for the new E
        
        #check if the values even produce an intersection
        if self.L < 4 and (E == 1 or E>1):
          return []

        #the equation st Eeff = Veff -> Eeff - Veff = 0
        def equation_to_solve(r):
            return (E**2)/2 - 0.5 + (1/r) - (self.L**2)/(2*r**2) + (self.L**2)/(r**3)

        roots = []
        initial_guesses = np.linspace(0.1, 10**4, 2**10)

        #using scipy.fsolve to find the points of intersection
        for guess in initial_guesses:
           root = round(fsolve(equation_to_solve, guess)[0], 10)
           if root not in roots: #check if root already in list
              roots.append(root)

           if Es == None and Eu == None and len(roots)==1: #L low, no maxima/minima
              break
          
           if len(roots) == 3: #can at most have 3 distinct roots 
              break
           #extra conditions for different values of L and E
           if len(roots) == 2 and (1 < E < Eu) and (self.L > 4 or self.L == 4):
              break
           if len(roots) == 1 and (Eu < E < 1) and (self.L < 4):
              break
           if len(roots) == 2 and E == 1 and (self.L > 4 or self.L == 4):
              break
           if len(roots) == 1 and E == Eu:
              roots.append(roots[0]) #These are double roots so lets repreent them twice
              break
           if len(roots) == 2 and E == Es:
              maxroot = max(roots)
              roots.append(maxroot) #double root
              break
           if len(roots) == 1 and E < Es:
               break

        #update registry
        self.REGISTRY[E] = sorted(roots)   
        return sorted(roots)
