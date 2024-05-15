#driver test
import pytest
import yaml

from src.orbit import Orbit
from src.v_eff import Veff
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
def test_model_name():
    processed_data = yaml.safe_load(yaml_data)
    
    # Assert the model name is as expected
    assert isinstance(processed_data, dict)

    assert processed_data['L'] == 4.5, "L doesnt match"
    assert processed_data['E'] == 0.979795, "E doesnt match"


# testing driver code functions

def test_orbit(loaded_yaml_data):
    o = driver.create_orbit(loaded_yaml_data)
    assert isinstance(o, Orbit) 
    
def test_veff(loaded_yaml_data):
    veff = driver.create_veff(loaded_yaml_data)
    assert isinstance(veff, Veff)

