

#driver test
import pytest
import yaml

from src.orbit import Orbit
from src.v_eff import Veff

from src.viz import Visualizer

import driver


# test YAML data as a string
yaml_data = """
L: 4.5
E: 0.979795
C: 4
"""


@pytest.fixture
def loaded_yaml_data():
    return yaml.safe_load(yaml_data)

# Test to check YAML data is correct
def test_model_name(loaded_yaml_data):
    
    # Assert the model name is as expected
    assert isinstance(loaded_yaml_data, dict)

    assert loaded_yaml_data['L'] == 4.5, "L doesnt match"
    assert loaded_yaml_data['E'] == 0.979795, "E doesnt match"


# testing driver code functions

def test_orbit_create(loaded_yaml_data):
    o = driver.create_orbit(loaded_yaml_data)
    assert isinstance(o, Orbit) 
    
def test_veff_create(loaded_yaml_data):
    veff = driver.create_veff(loaded_yaml_data)
    assert isinstance(veff, Veff)


def test_visualize_veff(loaded_yaml_data):
    veff = driver.create_veff(loaded_yaml_data)
    veff_viz = driver.visualize(driver.create_orbit(loaded_yaml_data), None, veff, loaded_yaml_data, True)

    assert isinstance(veff_viz, Visualizer)

