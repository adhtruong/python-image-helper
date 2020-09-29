import os
from math import pi, sin
from typing import Iterable

from image_helper import WHITE, Canvas, Point, float_range

RESOLUTION = 1_000


def get_points(dt: float) -> Iterable[Point]:
    for t in float_range(0, 1, dt):
        yield Point(t, sin(2 * pi * t) / 3 + 1 / 2)


def main() -> None:
    canvas = Canvas(RESOLUTION)
    canvas.set_background(WHITE)
    canvas.set_black()
    canvas.set_line_width(0.005)

    canvas.draw_path(get_points(1 / RESOLUTION), close_path=False)

    dir_path = os.path.dirname(os.path.realpath(__file__))
    canvas.write_to_png(f"{dir_path}/output/sine_curve.png")


if __name__ == "__main__":
    main()
