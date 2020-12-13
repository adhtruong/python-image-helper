import pytest

from image_helper import Canvas, Circle, Colour, FillRule, LineCap, LineJoin, Point


@pytest.fixture(scope="module")
def canvas() -> Canvas:
    return Canvas(100, 100)


def test_setup():
    canvas = Canvas(100, normalise=False)
    assert canvas.width == 100
    assert canvas.height == 100

    canvas = Canvas(100, normalise=True)
    assert canvas.width == 1
    assert canvas.height == 1


def test_set_background(canvas):
    canvas.set_background(Colour(0.5, 0.5, 0.5))


def test_set_colour(canvas):
    canvas.set_black()
    canvas.set_white()
    canvas.set_grey(0.5, 0)
    canvas.set_colour(Colour(0.5, 0.5, 0.5))


def test_save_and_restore(canvas):
    canvas.save()
    canvas.restore()


def test_setting_line_width(canvas):
    canvas.set_line_width(0)
    canvas.set_line_width(1)


@pytest.mark.parametrize("line_cap", list(LineCap))
def test_setting_line_cap(canvas, line_cap):
    canvas.set_line_cap(line_cap)


@pytest.mark.parametrize("line_join", list(LineJoin))
def test_setting_line_join(canvas, line_join):
    canvas.set_line_join(line_join)


@pytest.mark.parametrize("fill_rule", list(FillRule))
def test_setting_fill_rule(canvas, fill_rule: FillRule):
    canvas.set_fill_rule(fill_rule)


def test_transform(canvas):
    canvas.rotate(1)
    canvas.translate(0.5, 0.5)
    canvas.scale(0.5, 0.5)


def test_path_and_fill(canvas):
    canvas.draw_path([Point(0, 0), Point(0.5, 0.5), Point(1, 0)], close_path=True)
    canvas.fill()
    canvas.stroke()
    canvas.clip()


@pytest.mark.parametrize("fill,stroke", [(True, True), (True, False), (False, True)])
def test_circle(canvas, fill, stroke):
    canvas.draw_circle(Circle(Point(0.5, 0.5), 0.1), fill=fill, stroke=stroke)
