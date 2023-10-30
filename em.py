from manim import *

class ChangingMagneticField(Scene):
    def construct(self):
        # Create a coil of wire (loop)
        loop = Circle(radius=1, color=BLUE, fill_opacity=0.3)
        loop.move_to(ORIGIN)

        # Create a magnetic field arrow
        magnetic_field = Vector(UP, color=GREEN)

        # Create a current arrow (initially zero)
        current_arrow = Vector(ORIGIN, color=RED)

        # Create labels
        loop_label = MathTex("\\text{Coil}").next_to(loop, DOWN)
        field_label = MathTex("\\text{Magnetic Field}").next_to(magnetic_field, UP)
        current_label = MathTex("\\text{Induced Current}").next_to(current_arrow, DOWN)

        # Add the components to the scene
        self.play(Create(loop), Create(magnetic_field), Write(loop_label), Write(field_label))

        # Animate the changing magnetic field
        self.play(
            magnetic_field.animate.rotate(PI/2),
            run_time=2
        )

        # Animate the induced current
        self.play(
            Create(current_arrow),
            Write(current_label),
            magnetic_field.animate.rotate(PI/2),
            run_time=2
        )

        self.wait(2)
