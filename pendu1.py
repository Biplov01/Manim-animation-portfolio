from manim import *

class PendulumWithGraph(Scene):
    def construct(self):
        times = ValueTracker(0)
        theta_max = PI/6
        l = 3
        w = np.sqrt(15/3)
        T = 2*PI/w

        refpoint = 2*UP

        theta = DecimalNumber().set_color(BLACK).move_to(15*RIGHT)
        theta.add_updater(lambda m: m.set_value(theta_max * np.sin(w*times.get_value())))
        self.add(theta)

        def get_line1(x,y):
            line = Line(start=ORIGIN+refpoint, end=x*RIGHT+y*UP+refpoint, color=BLUE)
            return line

        line = always_redraw(lambda: get_line1(l*np.sin(theta.get_value()), -l*np.cos(theta.get_value())))
        self.add(line)

        verticalline = DashedLine(start=line.get_start(), end=line.get_start()+3*DOWN+0.001*LEFT) # Add a small angle
        self.add(verticalline)

        def angle_arc(theta):
            if theta > 0:
                angle = Angle(line, verticalline, quadrant=(1, 1), other_angle=True, color=YELLOW, fill_opacity=0)
            else:
                angle = Angle(line, verticalline, quadrant=(1, 1), other_angle=False, color=YELLOW, fill_opacity=0)
            return angle

        angle = always_redraw(lambda: angle_arc(theta.get_value()))
        self.add(angle)

        arctext = MathTex(r"\theta").scale(0.5).add_updater(lambda m: m.next_to(angle, DOWN))
        self.add(arctext)

        def get_ball(x, y):
            dot = Dot(fill_color=BLUE, fill_opacity=1).move_to(x*RIGHT+y*UP+refpoint).scale(l)
            return dot

        ball = always_redraw(lambda: get_ball(l*np.sin(theta.get_value()), -l*np.cos(theta.get_value())))

        # **Make the green plot appear inside the graph x-axis**

        # Get the xmin and xmax values of the graph axes
        xmin, xmax = axes.get_x_range()

        # Create a new axes object with the xmin and xmax values adjusted so that the plot fits inside the graph
        graph_axes = Axes(
            x_range=[xmin, xmax, 1],
            y_range=[-1, 1, 0.5],
            axis_config={"color": WHITE},
            x_axis_config={"numbers_to_include": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]},
            y_axis_config={"numbers_to_include": [-1, -0.5, 0, 0.5, 1]},
        ).to_corner(UL)

        # Create the green plot on the new axes object
        graph = always_redraw(
            lambda: ParametricFunction(
                lambda t: (t, theta_max * np.sin(w*t), 0),
                t_range=[max(0, times.get_value() - 5), times.get_value()],
                color=GREEN
            ).shift(2*DOWN)
        )

        # Add the new axes object and the green plot to the scene
        self.add(graph_axes, graph)

        # Run the simulation for 10 seconds
        self.play(times.animate.set_value(3*T), rate_func=linear, run_time=3*T)

# Render the scene
if __name__ == "__main__":
    script = f"{Path(__file__).resolve()}"
    os.system(f"manim {script} PendulumWithGraph -pqh")
