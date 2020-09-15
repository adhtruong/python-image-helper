import os
from itertools import product
from math import cos, pi, sin
from typing import Iterable

from image_helper import BLACK, WHITE, Canvas, Point, Polygon

RESOLUTION = 1_000

N = 12


def get_rectangles(n: int) -> Iterable[Polygon]:
    for i, j in product(range(n), repeat=2):
        if (i + j) % 2 == 1:
            continue

        yield Polygon(
            ((i + i_offset) / n, (j + j_offset) / n) for i_offset, j_offset in ((0, 0), (0, 1), (1, 1), (1, 0))
        )


def main():
    canvas = Canvas(RESOLUTION)

    canvas.set_background(WHITE)

    canvas.set_black()
    for rectangle in get_rectangles(N):
        canvas.draw_polygon(rectangle)
        canvas.fill()

    dir_path = os.path.dirname(os.path.realpath(__file__))
    canvas.write_to_png(f"{dir_path}/output/squares.png")


if __name__ == "__main__":
    main()
