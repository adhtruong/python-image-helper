from math import pi
from typing import Iterable

from cairo import FORMAT_ARGB32, Context, ImageSurface

from .constants import BLACK, WHITE, LineCap, LineJoin
from .models import Circle, Colour, Point, PointType, Polygon


class Canvas:
    def __init__(self, width: int, height: int = None, *, normalise: bool = True):
        if height is None:
            height = width
        self._width = width
        self._height = height
        self._surface = ImageSurface(FORMAT_ARGB32, width, height)
        self._context = Context(self._surface)
        self._normalise = normalise
        if self._normalise:
            self.scale(self._width, self._height)

    @property
    def width(self) -> int:
        return self._width if not self._normalise else 1

    @property
    def height(self) -> int:
        return self._height if not self._normalise else 1

    @property
    def context(self) -> Context:
        return self._context

    def save(self) -> None:
        self._context.save()

    def restore(self) -> None:
        self._context.restore()

    # Transformation
    def rotate(self, angle: float) -> None:
        self._context.rotate(angle)

    def translate(self, x: float, y: float) -> None:
        self._context.translate(x, y)

    def scale(self, width: int, height: int) -> None:
        self._context.scale(width, height)

    def set_line_width(self, width: float) -> None:
        self._context.set_line_width(width)

    # Colour functionality
    def set_colour(self, colour: Colour) -> None:
        self._context.set_source_rgba(colour.red, colour.blue, colour.green, colour.alpha)

    def set_grey(self, colour_value: float, alpha: float = 1) -> None:
        colour = Colour(*(colour_value,) * 3, alpha)
        self.set_colour(colour)

    def set_black(self) -> None:
        self.set_colour(BLACK)

    def set_white(self) -> None:
        self.set_colour(WHITE)

    def set_background(self, colour: Colour) -> None:
        self._context.rectangle(0, 0, self.width, self.height)
        self.set_colour(colour)
        self._context.fill()

    def set_line_cap(self, line_cap: LineCap) -> None:
        self._context.set_line_cap(line_cap.value)

    def set_line_join(self, line_join: LineJoin) -> None:
        self._context.set_line_join(line_join.value)

    # Render methods
    def fill(self, preserve: bool = False) -> None:
        if not preserve:
            self._context.fill()
        else:
            self._context.fill_preserve()

    def stroke(self, preserve: bool = False) -> None:
        if not preserve:
            self._context.stroke()
        else:
            self._context.stroke_preserve()

    def clip(self) -> None:
        self._context.clip()

    def _draw_path(self, path: Iterable[Point], close_path: bool) -> None:
        self._context.new_sub_path()
        for p in path:
            self._context.line_to(*p)
        if close_path:
            self._context.close_path()

    def draw_path(self, path: Iterable[PointType], close_path: bool = False) -> None:
        points = (p if isinstance(p, Point) else Point(*p) for p in path)
        self._draw_path(points, close_path)
        self.stroke()

    def draw_polygon(self, polygon: Polygon) -> None:
        self._draw_path(polygon.points, close_path=True)

    def draw_circle(self, circle: Circle, fill: bool = False, stroke: bool = True) -> None:
        self._context.new_sub_path()
        self._context.arc(*circle.centre, circle.radius, 0, 2 * pi)

    def write_to_png(self, file_name: str) -> None:
        self._surface.write_to_png(file_name)
