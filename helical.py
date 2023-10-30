from manim import *

class HelicalSpringAndMass(Scene):
    def construct(self):
        # Create a helical spring
        num_coils = 10
        spring = self.generate_spring(num_coils, color=BLUE)

        # Create a mass (circle)
        mass = Circle(radius=0.25, color=ORANGE).next_to(spring, DOWN, buff=0)

        # Attach the spring to a fixed point
        fixed_point = Dot(color=RED).move_to(np.array([0, 0, 0]))

        # Connect the spring to the fixed point
        spring_line = Line(fixed_point, spring[0], color=GREEN)

        # Label the spring and mass
        spring_label = MathTex("k", color=WHITE).next_to(spring, UP)
        mass_label = MathTex("m", color=WHITE).next_to(mass, DOWN)

        self.add(fixed_point, spring, spring_line, mass, spring_label, mass_label)
        self.wait(2)

    def generate_spring(self, num_coils, **kwargs):
        radius = 0.2
        height_per_coil = 0.2
        num_points_per_coil = 100

        spring = VGroup()

        for _ in range(num_coils):
            coil = ParametricFunction(
                lambda t: np.array([
                    radius * np.cos(t),
                    radius * np.sin(t),
                    -height_per_coil * t / (2*np.pi)
                ]),
                t_range=(0, num_coils*2*np.pi),
                **kwargs
            )
            spring.add(coil)

        return spring
