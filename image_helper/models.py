from __future__ import annotations

import math
from dataclasses import dataclass
from typing import List, Tuple, TypeVar


@dataclass(frozen=True)
class Colour:
    red: float
    blue: float
    green: float
    alpha: float = 1

    def __post_init__(self):
        for attr in ("red", "blue", "green", "alpha"):
            value = getattr(self, attr)
            if value < 0 or value > 1:
                raise ValueError("Values must be within [0,1]")


@dataclass(frozen=True)
class Point:
    x: float
    y: float

    @staticmethod
    def from_polar(distance: float, angle: float) -> Point:
        if not distance:
            return Point(0, 0)

        return Point(distance * math.cos(angle), distance * math.sin(angle))

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


@dataclass
class Circle:
    centre: Point
    radius: float

    def intersects(self, other: Circle) -> bool:
        distance = self.centre.dist(other.centre)
        return distance < self.radius + other.radius


PointType = TypeVar("PointInput", Point, Tuple[float, float])


@dataclass(init=False)
class Polygon:
    points: List[Point]

    def __init__(self, *points: PointType) -> None:
        self.points = [p if isinstance(p, Point) else Point(*p) for p in points]

    def get_centre(self) -> Point:
        sum_point = sum(self.points, Point(0, 0))
        return Point(sum_point.x / len(self.points), sum_point.y / len(self.points))

    def __repr__(self):  # pragma: no cover
        return "Polygon[{}]".format(", ".join(f"(x={p.x}, y={p.y})" for p in self))

    def __iter__(self):
        return iter(self.points)
