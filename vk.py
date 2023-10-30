from manim import *

class DrawImage(Scene):
    def construct(self):
        # Create notebook
        notebook = Rectangle(width=6, height=4, fill_color=WHITE, fill_opacity=1)
        notebook.move_to(ORIGIN)

        # Create pencil
        pencil = ImageMobject("D:\\bplv final codes\\manim\\png-clipart-mechanical-pencil-drawing-pencil-pencil-orange-thumbnail-removebg-preview (1).png")
        pencil.scale(0.5)
        pencil.move_to(notebook.get_top() + 2 * DOWN + 1 * RIGHT)

        # Load the image to be drawn
        image = ImageMobject("D:\\bplv final codes\\manim\\vk.jpeg")
        image.scale(2)
        image.move_to(notebook.get_center())

        # Generate paths for tracing the image (Example paths)
        paths = [
            Line(LEFT, RIGHT),
            Line(UP, DOWN)
        ]

        # Animation to draw the image
        self.play(FadeIn(notebook), FadeIn(pencil), run_time=0.5)

        def pencil_trace(t):
            point = pencil.get_center()
            return point + t * RIGHT

        for path in paths:
            trace_path = ParametricFunction(pencil_trace, t_range=[0, 1])
            self.play(MoveAlongPath(pencil, trace_path), run_time=1)  # Faster pencil movement
            self.add(image.copy())  # Add a traced version of the image
            self.remove(image)  # Remove the traced image

        # Make the traced image stay
        self.remove(pencil)
        self.wait(28)  # 30 seconds video duration (including previous animations)

        # Add the final image to stay on screen
        self.add(image)
        self.wait(30)  # Additional 30 seconds

class DrawAnotherImage(Scene):
    def construct(self):
        # Load the new image to be drawn
        image = ImageMobject("D:\\bplv final codes\\manim\\vk1.jpeg")  # Changed to vk1.jpeg
        image.scale(2)
        image.move_to(ORIGIN)

        # Generate paths for tracing the image (Example paths)
        paths = [
            Line(LEFT, RIGHT),
            Line(UP, DOWN)
        ]

        # Animation to draw the image
        for path in paths:
            self.play(Create(image))
            self.wait(0.5)  # Short pause before drawing starts

            trace_path = path.copy()
            trace_path.set_color(WHITE)
            self.play(MoveAlongPath(image, trace_path), run_time=2)

            self.wait(1)  # Pause after drawing finishes

        # Make the traced image stay
        self.wait(28)  # 30 seconds video duration (including previous animations)
