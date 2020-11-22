import os
from math import pi, sin
from typing import Iterable

from image_helper import WHITE, Canvas, Point, float_range, render_canvases

RESOLUTION = 1_000
FRAME_RATE = 29.97
NUMBER_OF_FRAMES = int(FRAME_RATE * 3)


def get_points(dt: float, magnitude: float) -> Iterable[Point]:
    for t in float_range(0, 1, dt):
        yield Point(t, sin(2 * pi * t) * magnitude + 1 / 2)


def render_method(frame: int) -> Canvas:
    canvas = Canvas(RESOLUTION)
    canvas.set_background(WHITE)
    canvas.set_black()
    canvas.set_line_width(0.005)

    canvas.draw_path(get_points(1 / RESOLUTION, magnitude=1 / 3 * sin(frame * 2 * pi / 45)), close_path=False)
    canvas.stroke()

    return canvas


def main() -> None:
    dir_path = os.path.dirname(os.path.realpath(__file__))
    render_canvases(render_method, NUMBER_OF_FRAMES, FRAME_RATE, f"{dir_path}/output/animated_sine_curve.mp4")


if __name__ == "__main__":
    main()
