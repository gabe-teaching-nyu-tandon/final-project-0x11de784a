import pytest
import src.trajectory_factory
import src.orbit_factory
import src.v_eff
import src.orbit

def test_prop_radial_period():
	assert isinstance(src.trajectory_factory.TrajectoryFactory.prop_radial_period([1,2,3],-0.5),float)

def test_prop_angular_period():
	assert isinstance(src.trajectory_factory.TrajectoryFactory.prop_angular_period([1,2,3],-0.5,0.5),float)

def test_interpolate():
	assert isinstance(src.trajectory_factory.TrajectoryFactory.interpolate([1,2,3],0.5,0.5),scipy.integrate.OdeSolution

def test_construction():
	orbit = src.orbit_factory.create_orbit(1,0.5,4)
	assert isinstance(src.trajectory_factory.TrajectoryFactory(orbit),src.trajectory.ContinuousTrajectory)

