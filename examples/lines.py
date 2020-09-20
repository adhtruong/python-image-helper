import os

from image_helper import WHITE, Canvas, LineCap, Point

RESOLUTION = 1_000


def main():
    canvas = Canvas(RESOLUTION)

    canvas.set_background(WHITE)

    canvas.set_black()
    canvas.set_line_width(0.1)

    canvas.set_line_cap(LineCap.ROUND)
    canvas.draw_path([Point(1 / 4, 1 / 4), Point(1 / 4, 3 / 4)])
    canvas.stroke()

    canvas.set_line_cap(LineCap.BUTT)
    canvas.draw_path([Point(1 / 2, 1 / 4), Point(1 / 2, 3 / 4)])
    canvas.stroke()

    canvas.set_line_cap(LineCap.SQUARE)
    canvas.draw_path([Point(3 / 4, 1 / 4), Point(3 / 4, 3 / 4)])
    canvas.stroke()

    dir_path = os.path.dirname(os.path.realpath(__file__))
    canvas.write_to_png(f"{dir_path}/output/lines.png")


if __name__ == "__main__":
    main()
