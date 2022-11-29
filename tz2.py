from manim import *
from numpy import *
from pathlib import Path


class VectorArrow(MovingCameraScene):
  def construct(self):
    quote = Tex("Mathematics is the only perfect...")
    quote.set_color(YELLOW_A)
    quote.to_edge(UP)
    quote2 = Tex("Doing calculations, you get into a mess ... realize it")
    quote2.set_color(YELLOW_B)
    author = Tex("-Albert Einstein")
    author.scale(0.75)
    author.next_to(quote.get_corner(DOWN + RIGHT), DOWN)

    self.add(quote)
    self.add(author)
    self.wait(2)
    self.play(Transform(quote, quote2), ApplyMethod(author.move_to, quote2.get_corner(DOWN + RIGHT) + DOWN + 2 * LEFT))
    self.play(ApplyMethod(author.match_color, quote2), Transform(author, author.scale(1)))
    self.play(FadeOut(quote))
    self.play(FadeOut(author))
    math = MathTex("5^2+x^{4+5}gx5", "=", "\sin\left(a^2d\right)=d\sqrt{d5}")

    uwu1 = SurroundingRectangle(math[0], buff=.1)
    uwu2 = SurroundingRectangle(math[2], buff=.1)

    code = ''' # Write math
        math = MathTex("5^2+x^{4+5}gx5", "=", "\sin\left(a^2d\right)=d\sqrt{d5}")

        self.play(Write(math))

        uwu1 = SurroundingRectangle(math[0], buff=.1)
        uwu2 = SurroundingRectangle(math[2], buff=.1)

        self.play(Create(uwu1)) 
        self.wait()
        self.play(ReplacementTransform(uwu1, uwu2))
        self.wait()
'''

    rendered_code = Code(code=code, tab_width=4, background="window",
                         language="Python", font="Monospace")
    self.add(rendered_code)
    self.play(FadeOut(rendered_code), run_time=5.2)
    self.play(Write(math))

    self.play(Create(uwu1))

    self.wait()

    self.play(ReplacementTransform(uwu1, uwu2))

    self.wait()