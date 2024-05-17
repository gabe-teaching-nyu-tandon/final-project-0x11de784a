import pytest
import src.trajectory_factory

def test_prop_radial_period():
	assert isinstance(src.trajectory_factory.TrajectoryFactory.prop_radial_period([1,2,3],-0.5),float)

def test_prop_angular_period():
	assert isinstance(src.trajectory_factory.TrajectoryFactory.prop_angular_period([1,2,3],-0.5,0.5),float)
