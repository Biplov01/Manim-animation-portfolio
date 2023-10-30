from manim import *

class NewtonsLaws(Scene):
    def construct(self):
        # First Law
        first_law_text = Text("Newton's First Law of Motion", font_size=48)
        first_law_text.to_edge(UP)

        object_1 = Circle(color=BLUE, fill_opacity=0.8, radius=0.5)
        object_1.next_to(first_law_text, DOWN)

        force_arrow = Arrow(ORIGIN, UP, color=RED)
        force_arrow.next_to(object_1, DOWN)

        # Second Law
        second_law_text = Text("Newton's Second Law of Motion", font_size=48)
        second_law_text.next_to(first_law_text, DOWN, buff=2)

        object_2 = Circle(color=BLUE, fill_opacity=0.8, radius=0.5)
        object_2.next_to(second_law_text, DOWN, buff=1)
        object_3 = Circle(color=BLUE, fill_opacity=0.8, radius=0.3)
        object_3.next_to(object_2, RIGHT, buff=1)

        force_arrow_2 = Arrow(ORIGIN, UP, color=RED)
        force_arrow_2.next_to(object_2, DOWN)
        acceleration_arrow = Arrow(ORIGIN, RIGHT, color=YELLOW)
        acceleration_arrow.next_to(object_3, RIGHT)

        # Third Law
        third_law_text = Text("Newton's Third Law of Motion", font_size=48)
        third_law_text.next_to(second_law_text, DOWN, buff=2)

        object_4 = Circle(color=BLUE, fill_opacity=0.8, radius=0.5)
        object_5 = Circle(color=BLUE, fill_opacity=0.8, radius=0.5)
        object_4.next_to(third_law_text, DOWN, buff=1)
        object_5.next_to(object_4, RIGHT, buff=1)

        force_arrow_3 = Arrow(ORIGIN, RIGHT, color=RED)
        force_arrow_4 = Arrow(ORIGIN, LEFT, color=RED)
        force_arrow_3.next_to(object_4, DOWN)
        force_arrow_4.next_to(object_5, DOWN)

        self.play(Write(first_law_text))
        self.play(Create(object_1), Create(force_arrow))
        self.wait(2)
        self.play(Write(second_law_text))
        self.play(Create(object_2), Create(object_3), Create(force_arrow_2), Create(acceleration_arrow))
        self.wait(2)
        self.play(Write(third_law_text))
        self.play(Create(object_4), Create(object_5), Create(force_arrow_3), Create(force_arrow_4))
        self.wait(2)
