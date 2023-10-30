from manim import *

class GravitationalForce(Scene):
    def construct(self):
        # Create two objects (e.g., circles)
        object1 = Circle(fill_color=BLUE, fill_opacity=1, color=BLUE, radius=0.5)
        object2 = Circle(fill_color=GREEN, fill_opacity=1, color=GREEN, radius=0.5)
        object1.move_to(LEFT * 2)
        object2.move_to(RIGHT * 2)

        # Create an arrow to represent gravitational force
        force_arrow = Arrow(UP, DOWN, color=RED)
        force_arrow.next_to(object1, UP)

        # Add the objects to the scene
        self.play(Create(object1), Create(object2))
        self.play(Create(force_arrow))

        # Label the objects
        label_object1 = Tex("Object 1", color=BLUE)
        label_object1.next_to(object1, UP)
        label_object2 = Tex("Object 2", color=GREEN)
        label_object2.next_to(object2, UP)
        label_force = Tex("Gravitational Force", color=RED)
        label_force.next_to(force_arrow, UP)

        # Add labels to the scene
        self.play(Create(label_object1), Create(label_object2), Create(label_force))

        # Add text to explain the law of gravitation
        explanation_text = Text(
            "According to Newton's law of universal gravitation,\\n"
            "every particle attracts every other particle\\n"
            "in the universe with a force that is directly\\n"
            "proportional to the product of their masses\\n"
            "and inversely proportional to the square of\\n"
            "the distance between their centers.",
            color=WHITE,
            size=0.5
        )
        explanation_text.to_edge(UP)

        # Show explanation text
        self.play(Create(explanation_text))

        # Apply gravitational force to the objects
        self.play(ApplyForce(object1, DOWN), ApplyForce(object2, UP))

        # Show motion due to gravitational force
        self.wait(1)
