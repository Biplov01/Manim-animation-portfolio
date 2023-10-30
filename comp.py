from manim import *

class YoungModulus(Scene):
    def construct(self):
        # Add a very large horizontal line
        large_line = Line(LEFT, RIGHT, color=WHITE)
        large_line.match_height(FRAME_HEIGHT).to_edge(DOWN, buff=0)

        # Set up the helical spring
        spring = always_redraw(lambda: ParametricFunction(
            lambda t: [t, 0.5 * np.sin(3*t), 0],
            t_range=[-4, 4],
            color=YELLOW
        ))

        # Set up the mass (square-shaped)
        mass = Square(
            side_length=1,
            color=RED,
            fill_opacity=1,
            stroke_width=0
        )

        # Add a label for the mass
        mass_label = Tex("20 kg").next_to(mass, DOWN)

        # Attach the mass to the end of the spring
        mass.move_to(spring.get_end())
        mass.add_updater(lambda m: m.move_to(spring.get_end()))
        mass_label.add_updater(lambda l: l.next_to(mass, DOWN))

        # Set up a ValueTracker to control compression/expansion
        compression_tracker = ValueTracker(1)

        spring.add_updater(lambda s: s.become(
            ParametricFunction(
                lambda t: [t, 0.5 * compression_tracker.get_value() * np.sin(3*t), 0],
                t_range=[-4, 4],
                color=YELLOW
            )
        ))

        # Add a horizontal line passing through spring
        small_line = Line(LEFT, RIGHT, color=WHITE)
        small_line.match_height(spring).move_to(spring)

        self.play(Create(large_line))
        self.play(FadeIn(mass, mass_label, spring))
        self.play(spring.animate.to_edge(RIGHT), compression_tracker.animate.set_value(0.5))
        self.play(Create(small_line))
        self.wait(2)
        self.play(compression_tracker.animate.set_value(1.5))
        self.wait(2)
