from manim import *

class Pendulum(VGroup):
    def __init__(self, length, angle, **kwargs):
        super().__init__(**kwargs)

        self.origin = np.array([0, 0, 0])
        self.length = length
        self.angle = angle

        self.string = Line(self.origin, self.get_end_point(), color=WHITE)
        self.bob = Circle(radius=0.1, color=RED, fill_opacity=1).move_to(self.get_end_point())

        self.add(self.string, self.bob)

    def get_end_point(self):
        x = self.length * np.sin(np.radians(self.angle))
        y = -self.length * np.cos(np.radians(self.angle))
        return np.array([x, y, 0]) + self.origin

    def set_theta_and_update_bob_position(self, theta):
        self.angle = theta
        self.bob.move_to(self.get_end_point())
        self.string.become(Line(self.origin, self.bob.get_center(), color=WHITE))

class SHMWithPendulum(Scene):
    def construct(self):
        # Define constants for the pendulum
        length = 2.0
        angle_max = 30  # Maximum angle in degrees

        # Define constants for SHM curve
        amplitude = length * np.radians(angle_max)
        frequency = 1.0
        phase_angle = 0

        # Define time range
        t_min = 0
        t_max = 5
        num_points = 100

        # Create time axis
        time_axis = NumberLine(x_range=[t_min, t_max], color=BLUE)
        time_axis.move_to(ORIGIN)

        # Plot position vs. time (SHM curve)
        shm_curve = self.get_shm_curve(amplitude, frequency, phase_angle, t_min, t_max, num_points)

        # Create labels
        shm_formula = MathTex(
            "x(t) = A \\cdot \\sin(2\\pi f t + \\phi)",
            tex_to_color_map={"A": YELLOW, "f": YELLOW, "\\phi": YELLOW}
        ).next_to(shm_curve, UP)

        # Create the pendulum
        pendulum = Pendulum(length=length, angle=angle_max)
        pendulum.move_to([0, -length, 0])  # Position at the bottom

         # Animate the pendulum and red dot
        self.play(Create(time_axis), Write(shm_curve), Write(shm_formula))
        
         # Animate the pendulum and red dot
        self.play(
             self.shm_motion(pendulum, t_max, num_points, amplitude, frequency, phase_angle),
             run_time=t_max - t_min,
             rate_func=linear,
         )

    def get_shm_curve(self, amplitude, frequency, phase_angle, t_min, t_max, num_points):
         t_values = np.linspace(t_min, t_max, num_points)
         x_values = amplitude * np.sin(2 * PI * frequency * t_values + np.radians(phase_angle))

         curve_points = [np.array([t, x, 0]) for t, x in zip(t_values, x_values)]
         shm_curve = VMobject(color=GREEN).set_points_smoothly(curve_points)
         shm_curve.move_to(ORIGIN)

         return shm_curve

    def shm_motion(self, pendulum: Pendulum,t_max: float,num_points: int,
                   amplitude: float,frequency: float,
                   phase_angle: float) -> AnimationGroup:
         """Create an animation of a pendulum undergoing simple harmonic motion."""

         # Calculate the position of the pendulum bob at each point in time
         times = np.linspace(0,t_max,num_points)
         angles_rad = amplitude * np.sin(2 * PI * frequency * times + phase_angle)
         angles_deg = np.degrees(angles_rad)

         # Create an animation for each point in time
         animations = [
             ApplyMethod(pendulum.set_theta_and_update_bob_position,
                         theta) for theta in angles_deg]

         return AnimationGroup(*animations)
