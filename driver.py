import sys
import yaml
import numpy as np
from src.v_eff_factory import VeffFactory
from src.v_eff import Veff
from src.orbit_factory import OrbitFactory
from src.orbit import Orbit

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

    orbit_ = OrbitFactory()
    orbit_ = orbit_.create_orbit(L, E, C)
    return orbit_

def calc_trajectory(orbit: Orbit):
    pass

def visualize(orbit: Orbit, trajectory, veff: Veff):
    pass

def main(yaml_params: dict) -> None:
    
    create_veff(parameters)
    create_orbit(parameters)




# parse on command line
if __name__ == "__main__":
    if len(sys.argv) == 2:
        parameters = read_params(sys.argv[1])
        main(parameters)

    elif len(sys.argv) == 4:
        #manually transform into dict
        parameters = {"L":sys.argv[1], "E":sys.argv[2], "C":sys.argv[3]}
        main(parameters)

    else:
        print(f"Failed to read YAML file takes filename or (L,E,C)")
