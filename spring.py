from manim import *

class BarGraph(Scene):
    def construct(self):
        # Define data
        data = {
            "Category A": 4,
            "Category B": 7,
            "Category C": 2,
            "Category D": 5,
            "Category E": 9
        }

        # Create labels for categories
        category_labels = [Tex(text) for text in data.keys()]
        for i, label in enumerate(category_labels):
            label.next_to(ORIGIN, DOWN).shift((i - 2) * RIGHT * 1.5)

        # Create bars based on data
        bars = VGroup(
            *[Rectangle(width=0.5, height=value, fill_opacity=0.7, fill_color=BLUE) for value in data.values()]
        )
        for i, bar in enumerate(bars):
            bar.next_to(category_labels[i], UP, buff=0.2)

        # Add labels to bars
        value_labels = [Tex(str(value)) for value in data.values()]
        for i, value_label in enumerate(value_labels):
            value_label.next_to(bars[i], UP, buff=0.2)

        # Create axis labels
        x_label = Tex("Categories").next_to(ORIGIN, DOWN).shift((len(data) - 1) * RIGHT * 0.75)
        y_label = Tex("Values").next_to(ORIGIN, LEFT).shift(3.5 * UP)

        # Create y-axis
        y_axis = Line(3.5 * DOWN, 3.5 * UP, color=WHITE)

        # Group all elements together
        graph = VGroup(x_label, y_label, y_axis, *category_labels, *bars, *value_labels)

        # Animate the graph
        self.play(Create(graph))

        # Add animations for better visualization
        for bar, value_label in zip(bars, value_labels):
            self.play(Transform(bar, bar.copy().set_fill(BLUE_E, 0.7)), Transform(value_label, value_label.copy().scale(1.2)))

        self.wait(2)
