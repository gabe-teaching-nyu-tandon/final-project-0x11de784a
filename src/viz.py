import matplotlib.pyplot as plt
from abc import ABC


class Visualization(ABC):
    '''
    This class represents a visualization tool for orbital mechanics.
    '''
    def create_plot(self):
        '''
        Creates a plot object for visualizing the provided data.
        '''

class VeffPlot(Visualization):
    """
    This class represents a plot of the effective potential.

    Attributes:
        data (ndarray[(r, Veff)]): Array of (r, Veff) values for plotting.
    """
    def __init__(self, veff_data):
        self.data = veff_data

    def create_plot(self):
        """
        Plots the effective potential data that was calculated by Veff class.
        """
        # Plot Veff_values
        plt.plot(self.data[250:, 0], self.data[250:, 1], label='Effective Potential')
        plt.title('Effective Potential')
        plt.xlabel('Radius (r)')
        plt.ylabel('Veff Value')
        plt.legend()
        plt.xscale('log')
        plt.grid(True)
        plt.show()

        return self
