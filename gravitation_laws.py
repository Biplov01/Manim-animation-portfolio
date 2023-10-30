from manim import *

class GravitationalForce(Scene):
    def construct(self):
        # Create objects
        object1 = Circle(fill_color=BLUE, fill_opacity=1, color=BLUE, radius=0.3, stroke_width=0)
        object2 = Circle(fill_color=GREEN, fill_opacity=1, color=GREEN, radius=0.3, stroke_width=0)

        # Position objects
        object1.move_to(LEFT * 2)
        object2.move_to(RIGHT * 2)

        # Create Earth and another planet
        earth = Circle(fill_color=WHITE, fill_opacity=1, color=BLUE, radius=0.5, stroke_width=0)
        earth_label = Tex("Earth", color=BLUE, font_size=18, stroke_width=0.5, fill_color=WHITE).next_to(earth, DOWN)
        planet = Circle(fill_color=YELLOW, fill_opacity=1, color=YELLOW, radius=0.3, stroke_width=0)
        planet.move_to(3*UP + 2*RIGHT)
        planet_label = Tex("Planet", color=YELLOW, font_size=18, stroke_width=0.5, fill_color=WHITE).next_to(planet, UP)

        # Create an arrow to represent gravitational force with a label
        force_arrow = Arrow(UP, DOWN, color=RED)
        force_arrow.next_to(object1.get_center(), UP)
        force_label = MathTex("\\vec{F} = G\\frac{m_1m_2}{r^2}", color=RED).next_to(force_arrow.get_center(), UP)

        # Add the objects and force arrow to the scene
        self.play(Create(object1), Create(object2))
        self.play(Create(earth), Create(earth_label), Create(planet), Create(planet_label))
        self.play(Create(force_arrow), Write(force_label))

        # Label the objects
        label_object1 = Tex("Object 1", color=BLUE, font_size=18, stroke_width=0.5, fill_color=WHITE).next_to(object1.get_center(), UP)
        label_object2 = Tex("Object 2", color=GREEN, font_size=18, stroke_width=0.5, fill_color=WHITE).next_to(object2.get_center(), UP)

        # Add labels to the scene
        self.play(Create(label_object1), Create(label_object2))

        # Add text to explain the law of gravitation
        explanation_text = Text(
            "According to Newton's law of universal gravitation...",
            color=WHITE,
            font_size=18,
            t2c={'Newton': YELLOW}
        )
        
        explanation_text.to_edge(DOWN)

        # Show explanation text
        self.play(Create(explanation_text))

        # Apply gravitational force to the objects
        gravity1 = ApplyMethod(object1.shift, DOWN * 3)
        gravity2 = ApplyMethod(object2.shift, UP * 3)
        
        self.play(gravity1 & gravity2)

