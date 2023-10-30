from manim import *

class NewtonsSecondLaw(Scene):
    def construct(self):
        # Create an object (e.g., a box)
        box = Square(fill_color=YELLOW, fill_opacity=1, color=YELLOW).move_to(LEFT * 2)

        # Create an arrow to represent force
        force_arrow = Arrow(LEFT, RIGHT, color=RED).next_to(box, RIGHT)

        # Add the objects to the scene
        self.play(Create(box), Create(force_arrow))

        # Label the objects
        label_box = Tex("Object", color=YELLOW).next_to(box, UP)
        label_force = Tex("Force", color=RED).next_to(force_arrow, UP)

        # Add labels to the scene
        self.play(Create(label_box), Create(label_force))

        # Create mass label
        label_mass = Tex("Mass (m)", color=WHITE).move_to(UP * 3)
        self.play(Create(label_mass))

        # Create acceleration label
        label_acceleration = Tex("Acceleration (a)", color=WHITE).move_to(DOWN * 3)
        self.play(Create(label_acceleration))

        # Apply force to the object
        self.play(box.animate.move_to(RIGHT * 2))  # Use animate for smoother motion

        # Add equation
        equation = MathTex(r"F = ma", color=WHITE).move_to(UP * 2)
        self.play(Create(equation))

        # Add values to the equation
        value_F = MathTex(r"F = 10\, \text{N}", color=WHITE).move_to(UP * 1)
        value_m = MathTex(r"m = 2\, \text{kg}", color=WHITE).move_to(DOWN * 0.5)
        self.play(Create(value_F), Create(value_m))

        # Calculate acceleration
        value_a = MathTex(r"a = \frac{F}{m} = \frac{10\, \text{N}}{2\, \text{kg}} = 5\, \frac{\text{m}}{\text{s}^2}", color=WHITE).move_to(DOWN * 2)
        self.play(Create(value_a))

        # Show motion with calculated acceleration
        self.wait(1)
