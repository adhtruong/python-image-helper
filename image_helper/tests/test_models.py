import pytest

from image_helper import Circle, Colour, Point, Polygon


def test_colour():
    Colour(1, 1, 1)


@pytest.mark.parametrize("r,b,g", [(-1, 0, 0), (1.1, 0, 0)])
def test_invalid_colour(r, g, b):
    with pytest.raises(ValueError):
        Colour(r, g, b)


def test_point():
    assert Point(1, 1) == Point(1, 0) + Point(0, 1)
    assert Point(2, 1) - Point(1, 1) == Point(1, 0)
    assert (0, 1) == tuple(Point(0, 1))


def test_circle():
    assert Circle(Point(1, 1), 1).intersects(Circle(Point(0, 0), 1))
    assert not Circle(Point(1, 1), 0.5).intersects(Circle(Point(0, 0), 0.5))


def test_polygon():
    p = Polygon((0, 0), (1, 1))
    assert p.get_centre() == Point(0.5, 0.5)
    assert [Point(0, 0), Point(1, 1)] == list(p)
