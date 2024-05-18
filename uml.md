classDiagram
    VeffFactory --> Veff
    class Veff{
        + float L
        + float Es
        + float Eu
        + ndarray Veff_values
        + dict REGISTRY
        + calc_Veff_at_r(r: float) float
        + calc_turning points(E: float) List[float]
    } 
    class VeffFactory{
        dict REGISTRY
        create(L) Veff
    }

    OrbitFactory --> Orbit 
    class Orbit{
        +float L
        +float E
        +float rmin
        +float rmax
        +Veff Veff  
        +float Tr
        +float Tphi   
        +is_r_periodic() bool 
    }

    class OrbitFactory{
        create(L, E, rmin, rmax, Veff) Orbit
    } 


    class TrajectoryFactory{
        + create(Orbit) ContinuousTrajectory
    }

    TrajectoryFactory --> Trajectory

    Trajectory <|-- SampleTrajectory
    Trajectory <|-- ContinuousTrajectory

    class Trajectory{
        + calc_trajectory()
    }
    class SampleTrajectory{
        +calc_trajectory(OrbitSampler) ndarray
    }
    class ContinuousTrajectory{
        +expand(SmapleTrajectory)
    }

    ContinuousTrajectory <|-- Interpolated
    ContinuousTrajectory <|-- Fourier
    
    class Interpolated{
        + expand(SampleTrajectory) Interp 
    }
    class Fourier{
        + expand(SampleTrajectory) 
    }


    OrbitSampler <|-- PeriodicOrbitSampler
    class OrbitSampler{
        +Orbit Orbit
        +rhs(ndarray) ndarray
    }  
    class PeriodicOrbitSampler{
        + rhs() ndarray
    } 


    Visualize <|-- TrajectoryPlot
    Visualize <|-- VeffPlot
    class Visualize{
        + make_plot()
    }
    class VeffPlot{
        make_plot(Veff)
        +show_orbit(Orbit)
        +remove_orbit(Orbit)
        +show_point()
    }
    class TrajectoryPlot{
        +make_plot(ContinuousTrajectory)
    }

