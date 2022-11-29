from manim import *
from numpy import *
from pathlib import Path


class FilledAngle(Scene):
  def construct(self):
    # --------------------------------------------------------------------------------------------------------
    numberplane = NumberPlane()

    l1 = Line(ORIGIN, 2 * RIGHT, ).set_color(GREEN_E).rotate(0 * DEGREES, about_point=ORIGIN)
    l2 = Line(ORIGIN, 4 * RIGHT, ).set_color(GREEN_D).rotate(30 * DEGREES, about_point=ORIGIN)
    l3 = Line(ORIGIN, 3.90 * RIGHT, ).set_color(GREEN_C).rotate(50 * DEGREES, about_point=ORIGIN)
    #  arc = Angle(ORIGIN,2 * RIGHT)
    # l2 = Line(ORIGIN, 2 * UP + LEFT).set_color(GREEN).rotate(-10 * DEGREES, about_point=ORIGIN)
    # l3 = Arrow(ORIGIN, 3 *  LEFT).set_color(GREEN).rotate(-35 * DEGREES, about_point=ORIGIN).
    # self.play(Create(l1))
    # arcBetweenPoints=ArcBetweenPoints(start=np.array([0,0,1]),end=np.array([1,0,0]))
    # -----------------------------------------------------------------------------------------------------------
    # self.play(Create(arcBetweenPoints))
    self.play(Create(numberplane), run_time=4.0)
    self.play(Create(l1), run_time=4.0)

    self.play(Create(l2), run_time=4.0)

    self.play(Create(l3), run_time=6.0)

    self.play(Create((Arc(angle=PI / 6))), run_time=1.0)

    self.play(Create((Arc(angle=PI / 3.60).set_color(YELLOW_A))), run_time=4.0)

    self.play(FadeOut(numberplane), run_time=0.2)
    self.play(FadeOut(l1), run_time=0.2)
    self.play(FadeOut(l2), run_time=0.2)
    self.play(FadeOut(l3), run_time=0.2)


