import scipy
import math
import src.trajectory
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

	@staticmethod
	def schwarzschild_odes(tau, y, L, E): # system of ODE's to be numerically integrated
		r, u, phi = y
		dr_dtau = u
		du_dtau = -((1 - 2 / r) * (L**2 / r**3 - 1 / r**2) + 1 / r**2 * (E**2 - 1))
		dphi_dtau = L / r**2
    		return (dr_dtau, du_dtau, dphi_dtau)

	@staticmethod
	def interpolant(rmin,L,E,rad_period) -> scipy.integrate.OdeSolution: # constructs periodic interpolant of r and phi
		sol = scipy.solve_ivp(TrajectoryFactory.schwartzchild_odes,(0,rad_period),(rmin,L**2 / rmin**2,0),dense_output=True)
		return sol.sol

	def __call__(self,orbit) -> src.trajectory.ContinuousTrajectory: # constructs Continuous Trajectory object upon call to class
		rad_period = TrajectoryFactory.prop_radial_period(orbit.Veff.REGISTRY[orbit.E],orbit.E)
		ang_period = TrajectoryFactory.prop_angular_period(orbit.Veff.REGISTRY[orbit.E],orbit.L,orbit.E)
		int = TrajectoryFactory.interpolant(orbit.Veff.REGISTRY[orbit.E][1],orbit.L,orbit.E,rad_period)
		return src.trajectory.ContinuousTrajectory(rad_period,ang_period,interpolant)
