from abc import ABC
import math

class Trajectory(ABC): # abstract base class to allow for future implementation of discrete and Fourier calculated trajectories
	def __call__(self,tau):
		return self._y(tau)

	@abstractmethod
	def _y(self,tau):
		pass

class ContinuousTrajectory(Trajectory): # trajectory generated from scipy interpolant
	def __init__(self,orbit,rad_period,ang_period,interpolant)
	self.orbit = orbit
	self.interpolant = interpolant
	self.rad_period = rad_period
	self.ang_period = ang_period

	def _y(self,tau): # uses periodic interpolant to return r and phi values
		tmp = self.interpolant(tau % self.rad_period)
		return (tmp[0],tmp[2] + 2 * math.pi / ang_period * tau)
