from manim import *

class WriteOnNotebook(Scene):
    def construct(self):
        # Create notebook
        notebook = Rectangle(width=6, height=4, fill_color=WHITE, fill_opacity=1)
        notebook.move_to(ORIGIN)

        # Create pencil
        pencil = ImageMobject("D:\\bplv final codes\\manim\\png-clipart-mechanical-pencil-drawing-pencil-pencil-orange-thumbnail-removebg-preview (1).png")  # Updated path
        pencil.scale(0.5)
        pencil.move_to(notebook.get_top() + 2 * DOWN + 1 * RIGHT)  # Adjusted position

        # Define writing animation and formulae
        formulas = [
            Tex(r"$\int_a^b f(x) dx$", font_size=20, color=BLACK),
            Tex(r"$a^2 + b^2 = c^2$", font_size=20, color=BLACK),
            Tex(r"$E=mc^2$", font_size=20, color=BLACK),
            
        ]

        for i in range(len(formulas)):
            formulas[i].move_to(notebook.get_center() + (i - 0.5) * UP)  # Position formulas on the notebook

        # Animation to write on notebook
        self.play(FadeIn(notebook), FadeIn(pencil), run_time=0.5)  # Make the pencil appear faster
        self.play(Write(formulas[0]))  # Write the first formula

        for formula in formulas[1:]:
            path_up = Line(pencil.get_bottom(), pencil.get_top() + 0.3 * UP)
            path_down = Line(pencil.get_top() + 0.3 * UP, pencil.get_bottom())
            self.play(MoveAlongPath(pencil, path_up), run_time=1/3)  # Speed up pencil movement
            self.play(Write(formula))
            self.play(MoveAlongPath(pencil, path_down), run_time=1/3)  # Speed up pencil movement

        self.wait(1)
