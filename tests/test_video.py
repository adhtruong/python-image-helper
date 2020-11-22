import os

import pytest

from image_helper import WHITE, Canvas, Point, render_canvases


def _render_method(frame: int) -> Canvas:
    canvas = Canvas(10)

    canvas.set_background(WHITE)

    canvas.set_black()
    canvas.set_line_width(0.1)
    canvas.draw_path((Point(0, 0), Point(frame / 30, frame / 30)))
    canvas.stroke()

    return canvas


def test_video() -> None:
    dir_path = os.path.dirname(os.path.realpath(__file__))
    render_canvases(_render_method, 30, 15, f"{dir_path}/run/output.mp4")


def test_invalid_frame_rate() -> None:
    with pytest.raises(ValueError):
        render_canvases(_render_method, 0, 15, "output.mp4")

    with pytest.raises(ValueError):
        render_canvases(_render_method, 15, 0, "output.mp4")
