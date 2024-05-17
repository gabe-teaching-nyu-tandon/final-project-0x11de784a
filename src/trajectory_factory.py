import scipy
import math
class TrajectoryFactory:

	@staticmethod
	def period_integral(integrand,a,b) -> float: # integral from rmin to rmax, used repeatedly for different period calculations
		return scipy.integrate.quad(integrand,a,b,weight='alg',wvar=(-0.5,-0.5))[0]

	@staticmethod
	def prop_radial_period(r_list,E) -> float: # proper radial period of orbit
		integrand = lambda r: math.sqrt(r**3 / (r - r_list[0]))
		return 2 / math.sqrt(1 - E**2) * TrajectoryFactory.period_integral(integrand,r_list[1],r_list[2])

	@staticmethod
	def prop_angular_period(r_list,L,E) -> float: # proper angular period of orbit
		integrand = lambda r: (L / (r**2)) * math.sqrt(r**3 / (r - r_list[0]))
		return 2 / math.sqrt(1 - E**2) * TrajectoryFactory.period_integral(integrand,r_list[1],r_list[2])

	@staticmethod
	def obs_radial_period(r_list,E) -> float: # observer radial period of orbit
		integrand = lambda r: (E * r / (r - 2 )) * math.sqrt(r**3 / (r - r_list[0]))
		return 2 / math.sqrt(1 -E**2) * TrajectoryFactory.period_integral(integrand,r_list[1],r_list[2])

print(TrajectoryFactory.prop_radial_period([1,2,3],0.5))
