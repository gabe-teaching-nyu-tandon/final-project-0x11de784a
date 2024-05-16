import sys
import yaml
import numpy as np

from src.v_eff_factory import VeffFactory
from src.v_eff import Veff

from src.orbit_factory import OrbitFactory
from src.orbit import Orbit

from src.viz import Visualizer
from src.viz import VeffPlot

def read_params(yaml_file: str) -> dict:
    with open(yaml_file, 'r') as f:
        data = yaml.load(f, Loader=yaml.SafeLoader)
    return data


# create veff instance throught factory class
def create_veff(params: dict) -> Veff:
    L = params["L"]

    factory = VeffFactory()
    veff = factory.create(L)
    return veff


def create_orbit(params: dict) -> Orbit:
    L = params["L"]
    E = params["E"]
    C = params["C"]

    orbit = OrbitFactory()
    orbit = orbit.create_orbit(L, E, C)
    return orbit

def calc_trajectory(orbit: Orbit):
    pass

def visualize(orbit: Orbit, trajectory, veff: Veff, params: dict, in_pytest):
    # veff plot
    data = veff.Veff_values

    vis = Visualizer(veff_data=data, E_value=params["E"], test=in_pytest)

    # trajectory plot -> not yet defined
    return vis


def main(yaml_params: dict) -> None:
    
    veff = create_veff(parameters)
    orbit =create_orbit(parameters)
    trajectory = calc_trajectory(orbit)
    visualize(orbit, trajectory, veff, parameters)



# parse on command line
if __name__ == "__main__":
    if len(sys.argv) == 2:
        parameters = read_params(sys.argv[1])
        main(parameters)

    elif len(sys.argv) == 4:
        #manually transform into dict
        parameters = {"L":float(sys.argv[1]), "E":float(sys.argv[2]), "C":float(sys.argv[3])}
        main(parameters)

    else: 
        print(f"Failed to read YAML file takes filename or (L,E,C)")


