from manim import *

class IntegralsScene(Scene):
    conf = {
        'funcion': lambda x: np.sin(x),
    }

    def construct(self):
        axes = Axes(
            x_range=[-7, 7, 1],
            y_range=[-1, 1, 1],
            x_axis_config={
                "numbers_to_include": range(-6, 8, 2),
                'color': GREEN,    
            },
            y_axis_config={
                'color': RED,    
            },
        )
        self.play(Create(axes))
        funcion = axes.plot(self.conf['funcion'], color=WHITE)
        self.add(funcion)

        start_dx = 1
        end_dx = 0.1
        num_steps = 10
        dx_values = np.linspace(start_dx, end_dx, num_steps)

        for dx in dx_values:
            rects = axes.get_riemann_rectangles(
                graph=funcion,
                x_range=[-7, 7],
                dx=dx,
                stroke_width=0.1,
                fill_opacity=0.5,
                stroke_color=BLUE,
            )
            self.play(Create(rects), run_time=0.5)
            self.wait(0.5)
            self.remove(rects)

        self.wait()

