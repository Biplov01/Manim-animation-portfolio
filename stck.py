from manim import *

class ThrowBall(Scene):
    def construct(self):
        # Create ground
        ground = Rectangle(width=config.frame_width, height=1, fill_color=YELLOW, fill_opacity=1)
        ground.shift(DOWN * 3)

        # Create stick figure
        body = Line(ORIGIN, DOWN * 2)
        body.set_stroke(width=0.5)  # Make the body thinner

        # Create hands
        left_hand = Line(ORIGIN + LEFT * 0.5, ORIGIN + LEFT * 1.5)
        right_hand = Line(ORIGIN + RIGHT * 0.5, ORIGIN + RIGHT * 1.5)
        hands = VGroup(left_hand, right_hand)
        hands.next_to(body, UP)

        # Connect head with body properly
        head = Circle(radius=0.5)
        head.next_to(body.get_start(), UP)  

        stick_figure = VGroup(body, hands, head)

        # Create ball
        ball = Dot(radius=0.2, color=BLUE)
        ball.next_to(stick_figure, RIGHT)

        # Create equation
        equation = MathTex("y = v_0 \\sin(\\theta) t - \\frac{1}{2} g t^2")
        equation.to_edge(UP)

        # Add everything to the scene
        self.add(ground, stick_figure, ball, equation)

        # Animate the ball
        self.play(
            ApplyMethod(
                ball.move_to,
                np.array([5, 3, 0]),  # Adjust as needed
                path_arc=45 * DEGREES,  # Angle of projection
                run_time=15,
            )
        )
