import os
from itertools import product

from cairo_helper import WHITE, Canvas, Circle, Point

RESOLUTION = 1_000

N = 7


def main() -> None:
    circles = []
    for i, j in product(range(1, N + 1), repeat=2):
        circle = Circle(Point(i / (N + 1), j / (N + 1)), 1 / (3 * (N + 1)))
        circles.append(circle)

    canvas = Canvas(RESOLUTION, RESOLUTION)
    canvas.set_background(WHITE)
    canvas.set_black()
    canvas.set_line_width(0.01)
    for circle in circles:
        canvas.draw_circle(circle)
        canvas.stroke()

    dir_path = os.path.dirname(os.path.realpath(__file__))
    canvas.write_to_png(f"{dir_path}/output/circles.png")


if __name__ == "__main__":
    main()
