from __future__ import annotations

import math
from dataclasses import dataclass


@dataclass(frozen=True)
class Colour:
    red: float
    blue: float
    green: float
    alpha: float = 1

    def __post_init(self):
        for attr in ("red", "blue", "green", "alpha"):
            value = getattr(self, attr)
            if value < 0 or value > 1:
                raise ValueError(f"Values must be within [0,1]")


@dataclass(frozen=True)
class Point:
    x: float
    y: float

    def distance_squared(self, x: float, y: float) -> float:
        return (self.x - x) ** 2 + (self.y - y) ** 2

    def dist(self, other: Point) -> float:
        return math.sqrt(self.distance_squared(other.x, other.y))

    def __sub__(self, other: Point) -> Point:
        return Point(self.x - other.x, self.y - other.y)

    def __add__(self, other: Point) -> Point:
        return Point(self.x + other.x, self.y + other.y)

    def __iter__(self):
        return iter((self.x, self.y))


@dataclass
class Line:
    start: Point
    end: Point

    def __add__(self, point: Point) -> Line:
        return Line(self.start + point, self.end + point)

    def __sub__(self, point: Point) -> Line:
        return Line(self.start - point, self.end - point)


@dataclass
class Circle:
    centre: Point
    radius: float

    def intersects(self, other: Circle) -> bool:
        distance = self.centre.dist(other.centre)
        return distance < self.radius + other.radius


@dataclass
class Polygon:
    points: List[Point]

    def get_centre(self) -> Point:
        sum_point = sum(self.points, Point(0, 0))
        return Point(sum_point.x / len(self.points), sum_point.y / len(self.points))

    def __iter__(self):
        return iter(self.points)