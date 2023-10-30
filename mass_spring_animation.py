from manim import *

class PythagoreanTheorem(Scene):
    def construct(self):
        # Create a right triangle
        a = 3
        b = 4
        c = (a**2 + b**2)**0.5

        triangle = Polygon(
            np.array([0, 0, 0]),
            np.array([a, 0, 0]),
            np.array([0, b, 0]),
            color=BLUE
        )

        # Create labels for sides
        a_label = MathTex("a", color=WHITE).next_to(triangle, DOWN)
        b_label = MathTex("b", color=WHITE).next_to(triangle, LEFT)
        c_label = MathTex("c", color=WHITE).next_to(triangle.get_center() + UP + RIGHT)

        # Create squares to represent areas
        square_a = Square(side_length=a, color=ORANGE, fill_opacity=0.5).next_to(triangle, LEFT)
        square_b = Square(side_length=b, color=GREEN, fill_opacity=0.5).next_to(triangle, DOWN)

        # Label the squares
        square_a_label = MathTex("a^2", color=WHITE).next_to(square_a, DOWN)
        square_b_label = MathTex("b^2", color=WHITE).next_to(square_b, LEFT)

        # Position the squares
        square_a.move_to(np.array([-1, 2, 0]))
        square_b.move_to(np.array([2, -1, 0]))

        # Show the right triangle, squares, and labels
        self.play(Create(triangle))
        self.play(Create(square_a), Create(square_b))
        self.play(Write(a_label), Write(b_label))

        # Animate the squares labels
        self.play(TransformFromCopy(square_a, square_a_label), TransformFromCopy(square_b, square_b_label))

        # Draw the hypotenuse and label it
        hypotenuse = Line(triangle.get_vertices()[1], triangle.get_vertices()[2], color=RED)
        self.play(Create(hypotenuse), Write(c_label))

        # Prove the theorem (a^2 + b^2 = c^2)
        equation = MathTex("a^2 + b^2", "=", "c^2", color=WHITE).next_to(triangle, RIGHT)
        self.play(Write(equation))

        self.wait(2)
