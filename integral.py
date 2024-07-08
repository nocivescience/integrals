from manim import *
class IntegralsScene(Scene):
    conf={
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
                # "numbers_to_include": np.arange(-1, 1, .2),
                'color': RED,    
            },
        )
        self.play(Create(axes))
        funcion = axes.plot(self.conf['funcion'], color=WHITE)
        self.add(funcion)
        self.wait()