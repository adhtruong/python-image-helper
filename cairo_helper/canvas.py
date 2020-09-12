from math import pi
from typing import List

from cairo import FORMAT_ARGB32, Context, ImageSurface

from .constants import BLACK, WHITE
from .models import Circle, Colour, Point


class Canvas:
    def __init__(self, width: int, height: int, normalise: bool = True):
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

    def scale(self, width: int, height: int) -> None:
        self._context.scale(width, height)

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

    def draw_path(self, path: List[Point], close_path: bool = False) -> None:
        self._context.new_sub_path()
        for p in path:
            self._context.line_to(*p)
        if close_path:
            self._context.close_path()
        self._context.stroke()

    def draw_circle(self, circle: Circle) -> None:
        self._context.new_sub_path()
        self._context.arc(*circle.centre, circle.radius, 0, 2 * pi)
        self._context.fill()

    def write_to_png(self, file_name: str) -> None:
        self._surface.write_to_png(file_name)