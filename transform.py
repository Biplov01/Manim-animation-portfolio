from manim import *

class SpringMassSystem(Scene):
    def construct(self):
        # Create the mass and spring objects
        mass = Dot(color=RED)
        spring = Line(ORIGIN, mass.get_center(), color=GREEN)
        
        # Set the spring constant and mass value
        k = 3
        m = 1
        
        # Set the overdamping coefficient
        beta = 0.5
        
        # Define the equation of motion for the mass
        def equation_of_motion(v, x):
            return -(k/m) * x - beta * v
        
        # Define the initial conditions
        initial_velocity = 1
        initial_position = 1
        
        # Simulate the motion of the mass using Euler's method
        dt = 0.01
        t = 0
        x = initial_position
        v = initial_velocity
        mass_trajectory = [(t, x)]
        for _ in range(1000):
            v += equation_of_motion(v, x) * dt
            x += v * dt
            t += dt
            mass_trajectory.append((t, x))
        
        # Convert the trajectory to a path
        trajectory_path = VMobject()
        trajectory_path.set_points_smoothly([3*RIGHT*pos for t, pos in mass_trajectory])
        
        # Create the graph
        axes = Axes(
            x_range=[0, 10, 1],
            y_range=[-2, 2, 1],
            axis_config={"color": BLUE},
        )
        graph = axes.plot(lambda t: initial_position*np.exp(-beta*t)*np.cos(np.sqrt(k/m)*t), color=YELLOW)
        
        # Add the mass, spring, trajectory, and graph to the scene
        self.add(mass, spring)
        self.play(MoveAlongPath(mass, trajectory_path), run_time=10)
        self.play(Create(axes), Create(graph), run_time=2)
