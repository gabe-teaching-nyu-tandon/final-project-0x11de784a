import numpy as np
from scipy.optimize import fsolve
from scipy.signal import find_peaks

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
        calc_turning points(E): Calculates the turining points of the effective potential energy equation for a given energy E.
    """

    def __init__(self, L):
        self.L = L
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
        if self.L > (12**(1/2)) or self.L ==(12**(1/2)):
            if not self._Eu:
                diff_Veff = np.diff(self._Veff_values[:, 1])
                max_indices = np.where((np.sign(diff_Veff[:-1]) > 0) & (np.sign(diff_Veff[1:]) < 0))[0] + 1
                max_Veff = self._Veff_values[max_indices, 1][0]
                self._Eu = (2 * max_Veff) ** (1/2)
        else:
            self._Eu = self.Es
        return self._Eu

    @property
    def Es(self):
        #Calculate the stable effective energy, which the local minima of Veff_values, then E_eff = E^2/2 so E = sqrt(2*E_eff)
        if self.L > (12**(1/2)) or self.L == (12**(1/2)):
            if not self._Es:
                diff_Veff = np.diff(self._Veff_values[:, 1])
                min_indices = np.where((np.sign(diff_Veff[:-1]) < 0) & (np.sign(diff_Veff[1:]) > 0))[0] + 1
                min_Veff = self._Veff_values[min_indices, 1][0]
                self._Es = (2 * min_Veff) ** (1/2)
        else:
            if not self._Es:
                veff_values = self.Veff_values[:, 1]
                second_derivative = np.diff(np.diff(veff_values))
                min_indices = np.where(second_derivative > 0)[0] + 1  # Add 1 to get the correct index
                min_Veff = veff_values[min_indices][0]  # Take the first maximum found
                self._Es = (2 * min_Veff) ** 0.5
        return self._Es

    def calc_turning_points(self, E):
        if self.L < 4 and (E == 1 or E>1):
          return []

        def equation_to_solve(r):
            return (E**2)/2 - 0.5 + (1/r) - (self.L**2)/(2*r**2) + (self.L**2)/(r**3)

        roots = []
        initial_guesses = np.linspace(0.1, 10**4, 2**10)

        for guess in initial_guesses:
           root = round(fsolve(equation_to_solve, guess)[0], 10)
           if root not in roots:
              roots.append(root)

           if len(roots) == 3:
              break
           if len(roots) == 2 and (1<E<self.Eu) and (self.L > 4 or self.L == 4):
              break
           if len(roots) == 1 and (self.Eu < E < 1) and (self.L < 4):
              break
           if len(roots) == 2 and E == 1 and (self.L > 4 or self.L == 4):
              break
           if len(roots) == 1 and E == self.Eu:
              roots.append(roots[0])
              break
           if len(roots) == 2 and E == self.Es:
              maxroot = max(roots)
              roots.append(maxroot)
              break
           if len(roots) == 1 and E < self.Es:
               break

        return sorted(roots)
    
