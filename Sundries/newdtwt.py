from numpy import tri
from manimlib.imports import *
from manim_sandbox.utils.imports import *
import random
import math
import os
import pyclbr


class Part1(GraphScene):
    def construct(self):
        axes = Axes(
            x_min=-1.6,
            x_max=1.6,
            y_min=-1.6,
            y_max=1.6,
            axis_config={
                "tick_frequency": 1,
                "unit_size": 3,
            },
        )
        dot = [Dot()] * 15
        num = [TexMobject()] * 15
        arrow = [Arrow()] * 15
        ang = [0.0] * 15
        pos = [Dot()] * 15
        fst = [0, 6, 7, 8, 1, 10, 5, 4, 1, 5, 7]
        col = [
            "", "#EF5350", "#2196F3", "#009688", "#FFA000", "#00C8F3",
            "#00FBA5", "#536DFE", "#7C4DFF", "#F9F9F9", "#9D9D9D"
        ]
        circ = Circle(radius=3, color=WHITE, fill_opacity=0, plot_depth=-1)

        for i in range(1, 11):
            ang[i] = -36 * (i - 1)
            pos[i] = Dot().move_to((fst[i] - 1) * 36 * LEFT + 30 * UP)
            dot[i] = Dot(
                color=col[i],
                radius=0.125,
                plot_depth=5,
            ).move_to(
                axes.c2p(math.cos(ang[i] * DEGREES),
                         math.sin(ang[i] * DEGREES)))
            num[i] = TexMobject(
                str(i),
                plot_depth=10,
            ).scale(0.8).move_to(
                axes.c2p(
                    math.cos(ang[i] * DEGREES) * 1.15,
                    math.sin(ang[i] * DEGREES) * 1.15))
            arrow[i] = Arrow(
                ORIGIN,
                ORIGIN,
                color=col[i],
                plot_depth=1,
            )

        arrow[1].add_updater(lambda t: t.put_start_and_end_on(
            axes.c2p(math.cos(ang[1] * DEGREES), math.sin(ang[1] * DEGREES)),
            axes.c2p(math.cos(pos[1].get_center()[0] * DEGREES),
                     math.sin(pos[1].get_center()[0] * DEGREES))))
        arrow[2].add_updater(lambda t: t.put_start_and_end_on(
            axes.c2p(math.cos(ang[2] * DEGREES), math.sin(ang[2] * DEGREES)),
            axes.c2p(math.cos(pos[2].get_center()[0] * DEGREES),
                     math.sin(pos[2].get_center()[0] * DEGREES))))
        arrow[3].add_updater(lambda t: t.put_start_and_end_on(
            axes.c2p(math.cos(ang[3] * DEGREES), math.sin(ang[3] * DEGREES)),
            axes.c2p(math.cos(pos[3].get_center()[0] * DEGREES),
                     math.sin(pos[3].get_center()[0] * DEGREES))))
        arrow[4].add_updater(lambda t: t.put_start_and_end_on(
            axes.c2p(math.cos(ang[4] * DEGREES), math.sin(ang[4] * DEGREES)),
            axes.c2p(math.cos(pos[4].get_center()[0] * DEGREES),
                     math.sin(pos[4].get_center()[0] * DEGREES))))
        arrow[5].add_updater(lambda t: t.put_start_and_end_on(
            axes.c2p(math.cos(ang[5] * DEGREES), math.sin(ang[5] * DEGREES)),
            axes.c2p(math.cos(pos[5].get_center()[0] * DEGREES),
                     math.sin(pos[5].get_center()[0] * DEGREES))))
        arrow[6].add_updater(lambda t: t.put_start_and_end_on(
            axes.c2p(math.cos(ang[6] * DEGREES), math.sin(ang[6] * DEGREES)),
            axes.c2p(math.cos(pos[6].get_center()[0] * DEGREES),
                     math.sin(pos[6].get_center()[0] * DEGREES))))
        arrow[7].add_updater(lambda t: t.put_start_and_end_on(
            axes.c2p(math.cos(ang[7] * DEGREES), math.sin(ang[7] * DEGREES)),
            axes.c2p(math.cos(pos[7].get_center()[0] * DEGREES),
                     math.sin(pos[7].get_center()[0] * DEGREES))))
        arrow[8].add_updater(lambda t: t.put_start_and_end_on(
            axes.c2p(math.cos(ang[8] * DEGREES), math.sin(ang[8] * DEGREES)),
            axes.c2p(math.cos(pos[8].get_center()[0] * DEGREES),
                     math.sin(pos[8].get_center()[0] * DEGREES))))
        arrow[9].add_updater(lambda t: t.put_start_and_end_on(
            axes.c2p(math.cos(ang[9] * DEGREES), math.sin(ang[9] * DEGREES)),
            axes.c2p(math.cos(pos[9].get_center()[0] * DEGREES),
                     math.sin(pos[9].get_center()[0] * DEGREES))))
        arrow[10].add_updater(lambda t: t.put_start_and_end_on(
            axes.c2p(math.cos(ang[10] * DEGREES), math.sin(ang[10] * DEGREES)),
            axes.c2p(math.cos(pos[10].get_center()[0] * DEGREES),
                     math.sin(pos[10].get_center()[0] * DEGREES))))

        self.play(
            FadeIn(circ),
            FadeIn(dot[1]),
            FadeIn(dot[2]),
            FadeIn(dot[3]),
            FadeIn(dot[4]),
            FadeIn(dot[5]),
            FadeIn(dot[6]),
            FadeIn(dot[7]),
            FadeIn(dot[8]),
            FadeIn(dot[9]),
            FadeIn(dot[10]),
            FadeIn(num[1]),
            FadeIn(num[2]),
            FadeIn(num[3]),
            FadeIn(num[4]),
            FadeIn(num[5]),
            FadeIn(num[6]),
            FadeIn(num[7]),
            FadeIn(num[8]),
            FadeIn(num[9]),
            FadeIn(num[10]),
            FadeIn(arrow[1]),
            FadeIn(arrow[2]),
            FadeIn(arrow[3]),
            FadeIn(arrow[4]),
            FadeIn(arrow[5]),
            FadeIn(arrow[6]),
            FadeIn(arrow[7]),
            FadeIn(arrow[8]),
            FadeIn(arrow[9]),
            FadeIn(arrow[10]),
        )
        self.wait(1.5)
        self.play(pos[1].move_to, ang[9] * RIGHT + 30 * UP)
        self.wait(1.5)
        self.play(pos[9].move_to, ang[3] * RIGHT + 30 * UP)
        self.wait(1.5)
        self.play(pos[3].move_to, ang[9] * RIGHT + 30 * UP)
        self.wait(1.5)
        self.play(pos[9].move_to, ang[1] * RIGHT + 30 * UP)
        self.wait(1.5)
        self.play(pos[1].move_to, ang[2] * RIGHT + 30 * UP)
        self.wait(1.5)


# python -m manim dtwt.py Part1 -p

# 8BDFFC