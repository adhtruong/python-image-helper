from itertools import product

from cairo_helper import BLACK, WHITE, Canvas, Circle, Point

RESOLUTION = 1_000

N = 4


def main() -> None:
    circles = []
    for i, j in product(range(1, N + 1), repeat=2):
        circle = Circle(Point(i / (N + 1), j / (N + 1)), 1 / (3 * (N + 1)))
        circles.append(circle)

    canvas = Canvas(RESOLUTION, RESOLUTION)
    canvas.set_background(WHITE)
    canvas.set_colour(BLACK)
    for circle in circles:
        canvas.draw_circle(circle)

    canvas.write_to_png("run/circle.png")


if __name__ == "__main__":
    main()
